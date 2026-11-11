#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Synchronisation Google Drive pour l'Index Global de Recherche du Laboratoire.
Cible : Boulangerie/Recherche/INDEX_GLOBAL_SOURCES_ET_RECHERCHE.md
Auteur : Équipe Laboratoire & Antigravity (Jalon M5)
"""

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

DEFAULT_CREDENTIALS = Path("/home/toto/.google_workspace_mcp/credentials/lanoetheau56@gmail.com.json")
DEFAULT_INDEX_PATH = Path(__file__).resolve().parent.parent / "docs" / "INDEX_GLOBAL_SOURCES_ET_RECHERCHE.md"
TARGET_FILE_ID = "15pEyrlZcYNFkXZq1ZPozJ5lvy3jf8G8b"
TARGET_FOLDER_ID = "1Gxlcude0ev17NjRAxhHInPpERbsW3MHW"  # Boulangerie/Recherche


def get_authenticated_token(creds_path: Path) -> str:
    """Récupère et rafraîchit si nécessaire le jeton d'accès OAuth Google."""
    if not creds_path.exists():
        raise FileNotFoundError(f"Fichier de credentials introuvable : {creds_path}")

    with open(creds_path, "r", encoding="utf-8") as f:
        creds = json.load(f)

    token = creds.get("token")
    if token:
        # Test de validité du token
        req = urllib.request.Request(
            "https://www.googleapis.com/drive/v3/about?fields=user",
            headers={"Authorization": f"Bearer {token}"}
        )
        try:
            with urllib.request.urlopen(req):
                return token
        except urllib.error.HTTPError as e:
            if e.code != 401:
                raise

    # Rafraîchissement du token expiré
    refresh_token = creds.get("refresh_token")
    client_id = creds.get("client_id")
    client_secret = creds.get("client_secret")
    token_uri = creds.get("token_uri", "https://oauth2.googleapis.com/token")

    if not (refresh_token and client_id and client_secret):
        raise ValueError("Credentials incomplets pour rafraîchir le jeton OAuth.")

    data = urllib.parse.urlencode({
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }).encode("utf-8")

    req_refresh = urllib.request.Request(token_uri, data=data)
    with urllib.request.urlopen(req_refresh) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        new_token = res["access_token"]
        creds["token"] = new_token
        with open(creds_path, "w", encoding="utf-8") as f_out:
            json.dump(creds, f_out, indent=2)
        return new_token


def get_remote_file_info(file_id: str, token: str) -> dict:
    """Récupère les métadonnées du fichier distant sur Google Drive."""
    url = f"https://www.googleapis.com/drive/v3/files/{file_id}?fields=id,name,size,modifiedTime,webViewLink"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def upload_index_content(file_id: str, local_path: Path, token: str) -> dict:
    """Téléverse le contenu local de l'index dans le document miroir Google Drive existant."""
    content_bytes = local_path.read_bytes()
    url = f"https://www.googleapis.com/upload/drive/v3/files/{file_id}?uploadType=media"
    req = urllib.request.Request(
        url,
        data=content_bytes,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "text/markdown; charset=utf-8",
            "Content-Length": str(len(content_bytes))
        },
        method="PATCH"
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    parser = argparse.ArgumentParser(description="Synchronisation Google Drive de l'Index Global du Laboratoire")
    parser.add_argument("--check", action="store_true", help="Vérifier le statut sans mettre à jour")
    parser.add_argument("--credentials", type=Path, default=DEFAULT_CREDENTIALS, help="Chemin du fichier de credentials JSON")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX_PATH, help="Chemin du fichier index local")
    args = parser.parse_args()

    print("=== SYNCHRONISATION GOOGLE DRIVE — LABORATOIRE DE TOURAGE ===")
    print(f"Index local : {args.index}")
    if not args.index.exists():
        print(f"ERREUR : Fichier index local introuvable à {args.index}", file=sys.stderr)
        sys.exit(1)

    local_size = args.index.stat().st_size
    print(f"Taille locale : {local_size:,} octets")

    try:
        token = get_authenticated_token(args.credentials)
        print("Authentification OAuth : VALIDE")
    except Exception as e:
        print(f"ERREUR d'authentification Google OAuth : {e}", file=sys.stderr)
        sys.exit(2)

    try:
        remote_info = get_remote_file_info(TARGET_FILE_ID, token)
        print(f"Fichier distant trouvé : {remote_info.get('name')} (ID: {remote_info.get('id')})")
        print(f"Taille distante : {int(remote_info.get('size', 0)):,} octets")
        print(f"Dernière modification distante : {remote_info.get('modifiedTime')}")
        print(f"Lien : {remote_info.get('webViewLink')}")
    except Exception as e:
        print(f"ERREUR lors de la vérification distante : {e}", file=sys.stderr)
        sys.exit(3)

    if args.check:
        if int(remote_info.get("size", 0)) == local_size:
            print("=> Statut : En synchronisation parfaite (tailles identiques).")
            sys.exit(0)
        else:
            print("=> Statut : Désynchronisé (tailles différentes). Relancer sans --check pour synchroniser.")
            sys.exit(4)

    print("\nApplication de la mise à jour sur Google Drive...")
    try:
        updated = upload_index_content(TARGET_FILE_ID, args.index, token)
        refreshed = get_remote_file_info(TARGET_FILE_ID, token)
        print(f"Mise à jour réussie : ID {refreshed.get('id')}, taille {int(refreshed.get('size', 0)):,} octets.")
        print(f"Horodatage distant : {refreshed.get('modifiedTime')}")
        print("=> Synchronisation terminée avec succès !")
    except Exception as e:
        print(f"ERREUR lors de la synchronisation : {e}", file=sys.stderr)
        sys.exit(5)


if __name__ == "__main__":
    main()
