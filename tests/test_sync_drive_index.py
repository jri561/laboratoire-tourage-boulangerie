#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests unitaires et d'intégration pour scripts/sync_drive_index.py
"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Ajouter le chemin racine au sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.sync_drive_index import (
    DEFAULT_CREDENTIALS,
    DEFAULT_INDEX_PATH,
    TARGET_FILE_ID,
    get_authenticated_token,
    get_remote_file_info,
    upload_index_content,
)


class TestSyncDriveIndex(unittest.TestCase):

    def test_missing_credentials_raises_file_not_found(self):
        """Vérifie qu'une exception FileNotFoundError est levée si le fichier de credentials est inexistant."""
        non_existent_path = Path("/tmp/non_existent_creds_xyz.json")
        with self.assertRaises(FileNotFoundError):
            get_authenticated_token(non_existent_path)

    def test_token_valid_without_refresh(self):
        """Vérifie que le token est retourné directement s'il est encore valide."""
        with tempfile.NamedTemporaryFile("w+", suffix=".json", delete=False) as tmp:
            json.dump({"token": "valid-token-123"}, tmp)
            tmp_path = Path(tmp.name)

        try:
            with patch("urllib.request.urlopen") as mock_urlopen:
                mock_resp = MagicMock()
                mock_urlopen.return_value.__enter__.return_value = mock_resp
                token = get_authenticated_token(tmp_path)
                self.assertEqual(token, "valid-token-123")
        finally:
            if tmp_path.exists():
                tmp_path.unlink()

    def test_token_refreshed_on_401(self):
        """Vérifie que le jeton OAuth est rafraîchi automatiquement en cas d'erreur 401."""
        from urllib.error import HTTPError

        with tempfile.NamedTemporaryFile("w+", suffix=".json", delete=False) as tmp:
            json.dump({
                "token": "expired-token",
                "refresh_token": "valid-refresh-token",
                "client_id": "test-client-id",
                "client_secret": "test-client-secret",
                "token_uri": "https://oauth2.googleapis.com/token"
            }, tmp)
            tmp_path = Path(tmp.name)

        try:
            with patch("urllib.request.urlopen") as mock_urlopen:
                # 1er appel lève 401, 2e appel (refresh) réussit
                mock_refresh_cm = MagicMock()
                mock_refresh_cm.__enter__.return_value.read.return_value = json.dumps({"access_token": "new-refreshed-token"}).encode("utf-8")

                mock_urlopen.side_effect = [
                    HTTPError("https://www.googleapis.com/drive/v3/about", 401, "Unauthorized", {}, None),
                    mock_refresh_cm
                ]

                token = get_authenticated_token(tmp_path)
                self.assertEqual(token, "new-refreshed-token")

                # Vérifie que le fichier a bien été mis à jour sur disque
                with open(tmp_path, "r", encoding="utf-8") as f:
                    updated_data = json.load(f)
                self.assertEqual(updated_data["token"], "new-refreshed-token")
        finally:
            if tmp_path.exists():
                tmp_path.unlink()

    def test_get_remote_file_info(self):
        """Vérifie la récupération des métadonnées du fichier distant."""
        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_resp = MagicMock()
            mock_resp.read.return_value = json.dumps({
                "id": TARGET_FILE_ID,
                "name": "INDEX_GLOBAL_SOURCES_ET_RECHERCHE.md",
                "size": "90534",
                "modifiedTime": "2026-11-09T18:22:58.091Z"
            }).encode("utf-8")
            mock_urlopen.return_value.__enter__.return_value = mock_resp

            info = get_remote_file_info(TARGET_FILE_ID, "fake-token")
            self.assertEqual(info["id"], TARGET_FILE_ID)
            self.assertEqual(info["size"], "90534")
            self.assertEqual(info["name"], "INDEX_GLOBAL_SOURCES_ET_RECHERCHE.md")

    def test_upload_index_content(self):
        """Vérifie la requête PATCH de téléversement du contenu."""
        with tempfile.NamedTemporaryFile("w+", suffix=".md", delete=False) as tmp:
            tmp.write("# Test Index")
            tmp_path = Path(tmp.name)

        try:
            with patch("urllib.request.urlopen") as mock_urlopen:
                mock_resp = MagicMock()
                mock_resp.read.return_value = json.dumps({
                    "id": TARGET_FILE_ID,
                    "name": "INDEX_GLOBAL_SOURCES_ET_RECHERCHE.md"
                }).encode("utf-8")
                mock_urlopen.return_value.__enter__.return_value = mock_resp

                res = upload_index_content(TARGET_FILE_ID, tmp_path, "fake-token")
                self.assertEqual(res["id"], TARGET_FILE_ID)
        finally:
            if tmp_path.exists():
                tmp_path.unlink()

    def test_live_credentials_and_check_if_present(self):
        """Test d'intégration réel si le fichier de credentials officiel est présent."""
        if not DEFAULT_CREDENTIALS.exists():
            self.skipTest("Fichier de credentials officiel non présent sur cet environnement.")

        token = get_authenticated_token(DEFAULT_CREDENTIALS)
        self.assertIsNotNone(token)
        remote_info = get_remote_file_info(TARGET_FILE_ID, token)
        self.assertEqual(remote_info.get("name"), "INDEX_GLOBAL_SOURCES_ET_RECHERCHE.md")
        self.assertEqual(remote_info.get("id"), TARGET_FILE_ID)
        self.assertGreater(int(remote_info.get("size", 0)), 80000)


if __name__ == "__main__":
    unittest.main()
