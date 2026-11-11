#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests unitaires pour scripts/sync_drive.py
"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.sync_drive import (
    DEFAULT_CREDENTIALS,
    FOLDER_A_IMPRIMER_ID,
    FOLDER_FICHES_INDIV_ID,
    FOLDER_RECETTE_ID,
    FOLDER_RECHERCHE_ID,
    drive_api,
    get_authenticated_token,
    get_or_create_subfolder,
    upload_or_update_file,
)


class TestSyncDrive(unittest.TestCase):

    def test_missing_credentials_raises_file_not_found(self):
        non_existent_path = Path("/tmp/non_existent_creds_999.json")
        with self.assertRaises(FileNotFoundError):
            get_authenticated_token(non_existent_path)

    def test_get_or_create_subfolder_existing(self):
        with patch("scripts.sync_drive.drive_api") as mock_api:
            mock_api.return_value = {"files": [{"id": "folder-123", "name": "03_CATALOGUE_RECETTES"}]}
            folder_id = get_or_create_subfolder("parent-abc", "03_CATALOGUE_RECETTES", "fake-token")
            self.assertEqual(folder_id, "folder-123")

    def test_get_or_create_subfolder_creates_new(self):
        with patch("scripts.sync_drive.drive_api") as mock_api:
            # 1er appel: recherche vide, 2e appel: création
            mock_api.side_effect = [
                {"files": []},
                {"id": "new-folder-456", "name": "03_CATALOGUE_RECETTES"}
            ]
            folder_id = get_or_create_subfolder("parent-abc", "03_CATALOGUE_RECETTES", "fake-token")
            self.assertEqual(folder_id, "new-folder-456")

    def test_upload_or_update_file_patch(self):
        with tempfile.NamedTemporaryFile("w+", suffix=".pdf", delete=False) as tmp:
            tmp.write("fake pdf content")
            tmp_path = Path(tmp.name)

        try:
            with patch("scripts.sync_drive.drive_api") as mock_api, \
                 patch("urllib.request.urlopen") as mock_urlopen:
                mock_api.return_value = {"files": [{"id": "file-existing-789", "name": tmp_path.name}]}
                mock_resp = MagicMock()
                mock_resp.read.return_value = json.dumps({"id": "file-existing-789"}).encode("utf-8")
                mock_urlopen.return_value.__enter__.return_value = mock_resp

                res = upload_or_update_file(tmp_path, "folder-xyz", "application/pdf", "fake-token")
                self.assertEqual(res["id"], "file-existing-789")
        finally:
            if tmp_path.exists():
                tmp_path.unlink()

    def test_live_credentials_if_present(self):
        if not DEFAULT_CREDENTIALS.exists():
            self.skipTest("Credentials non trouvés")
        token = get_authenticated_token(DEFAULT_CREDENTIALS)
        self.assertIsNotNone(token)
        self.assertTrue(len(token) > 20)


if __name__ == "__main__":
    unittest.main()
