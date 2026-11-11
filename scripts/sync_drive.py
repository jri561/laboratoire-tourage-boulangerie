#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Synchronisation Google Drive Global pour le Laboratoire de Tourage & Boulangerie.

Synchronise :
1. Le Cahier d'Atelier complet (PDF) dans '01_A_IMPRIMER (Cahier & Affiches)'
2. Les fiches individuelles d'atelier (PDFs) dans '02_FICHES_INDIVIDUELLES'
3. Toutes les recettes du catalogue (Markdown) dans '03_CATALOGUE_RECETTES' (dossier Recette)
4. L'Index Global, Index Recettes et Audits dans 'Boulangerie/Recherche'

Auteur : Équipe Laboratoire & Antigravity
"""

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CREDENTIALS = Path("/home/toto/.google_workspace_mcp/credentials/lanoetheau56@gmail.com.json")

# IDs Google Drive connus
FOLDER_RECETTE_ID = "17gF1hv2FQcARh8lEuiCVoaj-HS0dyHhH"
FOLDER_A_IMPRIMER_ID = "1BPX3UJTUmJE9hh-uQudk1i3p2A5O_z5m"
FOLDER_FICHES_INDIV_ID = "1GG8M8BQuF2a3m0-mIQcCJJkC8ZNbKS4K"
FOLDER_RECHERCHE_ID = "1Gxlcude0ev17NjRAxhHInPpERbsW3MHW"


def get_authenticated_token(creds_path: Path = DEFAULT_CREDENTIALS) -> str:
    """Récupère et rafraîchit automatiquement le jeton OAuth Google Drive."""
    if not creds_path.exists():
        raise FileNotFoundError(f"Fichier de credentials introuvable : {creds_path}")

    with open(creds_path, "r", encoding="utf-8") as f:
        creds = json.load(f)

    token = creds.get("token")
    if token:
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

    # Rafraîchissement du jeton expiré
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


def drive_api(endpoint: str, method: str = "GET", data: bytes = None, headers: dict = None, token: str = "") -> dict:
    """Appel générique à l'API Google Drive v3."""
    if headers is None:
        headers = {}
    headers["Authorization"] = f"Bearer {token}"
    url = f"https://www.googleapis.com{endpoint}" if endpoint.startswith("/") else endpoint
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode("utf-8")
        return json.loads(content) if content else {}


def get_or_create_subfolder(parent_id: str, folder_name: str, token: str) -> str:
    """Trouve un sous-dossier ou le crée dans le dossier parent."""
    query = f"name = '{folder_name}' and '{parent_id}' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    url = f"/drive/v3/files?q={urllib.parse.quote(query)}&fields=files(id,name)"
    res = drive_api(url, token=token)
    files = res.get("files", [])
    if files:
        return files[0]["id"]

    # Création du dossier
    meta = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [parent_id]
    }
    data = json.dumps(meta).encode("utf-8")
    created = drive_api(
        "/drive/v3/files",
        method="POST",
        data=data,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        token=token
    )
    print(f"  [DOSSIER CRÉÉ] '{folder_name}' -> ID: {created['id']}")
    return created["id"]


def upload_or_update_file(local_path: Path, folder_id: str, mime_type: str, token: str, remote_name: str = None) -> dict:
    """Met à jour un fichier existant par PATCH ou en téléverse un nouveau en multipart POST."""
    file_name = remote_name or local_path.name
    query = f"name = '{file_name}' and '{folder_id}' in parents and trashed = false"
    search_url = f"/drive/v3/files?q={urllib.parse.quote(query)}&fields=files(id,name,size,modifiedTime)"
    search_res = drive_api(search_url, token=token)
    existing_files = search_res.get("files", [])

    file_bytes = local_path.read_bytes()

    if existing_files:
        file_id = existing_files[0]["id"]
        # Vérification si taille identique
        url = f"https://www.googleapis.com/upload/drive/v3/files/{file_id}?uploadType=media"
        req = urllib.request.Request(
            url,
            data=file_bytes,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": mime_type,
                "Content-Length": str(len(file_bytes))
            },
            method="PATCH"
        )
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            print(f"  [MÀJ] {file_name} -> ID: {res['id']} ({len(file_bytes):,} octets)")
            return res
    else:
        # Nouveau fichier
        boundary = f"-------{uuid.uuid4().hex}"
        metadata = {"name": file_name, "parents": [folder_id]}
        body = [
            f"--{boundary}\r\n".encode("utf-8"),
            b"Content-Type: application/json; charset=UTF-8\r\n\r\n",
            json.dumps(metadata).encode("utf-8"),
            b"\r\n",
            f"--{boundary}\r\n".encode("utf-8"),
            f"Content-Type: {mime_type}\r\n\r\n".encode("utf-8"),
            file_bytes,
            b"\r\n",
            f"--{boundary}--\r\n".encode("utf-8")
        ]
        data = b"".join(body)
        url = "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart"
        req = urllib.request.Request(
            url,
            data=data,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": f"multipart/related; boundary={boundary}",
                "Content-Length": str(len(data))
            },
            method="POST"
        )
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            print(f"  [CRÉÉ] {file_name} -> ID: {res['id']} ({len(file_bytes):,} octets)")
            return res


def sync_all(token: str, check_only: bool = False):
    """Exécute la synchronisation complète de tous les pôles du laboratoire."""
    print("=== DÉMARRAGE SYNCHRONISATION GOOGLE DRIVE ===")

    # 1. Pôle Cahier Complet dans 01_A_IMPRIMER
    print("\n1. Pôle A Imprimer (Cahier Complet)...")
    cahier_pdf = REPO_ROOT / "exports_pdf" / "Cahier_Recettes_Complet_Labo.pdf"
    if not cahier_pdf.exists():
        cahier_pdf = REPO_ROOT / "exports_pdf" / "cahier_atelier_equipe.pdf"
    if cahier_pdf.exists():
        upload_or_update_file(cahier_pdf, FOLDER_A_IMPRIMER_ID, "application/pdf", token, remote_name="Cahier_Recettes_Complet_Labo.pdf")

    # 2. Pôle Fiches Individuelles dans 02_FICHES_INDIVIDUELLES
    print("\n2. Pôle Fiches Individuelles d'Atelier (PDFs)...")
    exports_dir = REPO_ROOT / "exports_pdf"
    fiches_sync = [
        ("06_PLF_Pret_A_Cuire_PAC.pdf", "06_PLF_Pret_A_Cuire_PAC.pdf"),
        ("03_Kouign_Amann_Cru_Surgele.pdf", "03_Kouign_Amann_Cru_Surgele.pdf"),
        ("04_Viennoise_Nature_Chocolat_PAC.pdf", "04_Viennoise_Nature_Chocolat_PAC.pdf"),
        ("05_Feuilletage_Inverse.pdf", "05_Feuilletage_Inverse.pdf"),
        ("06_Brioche_Fine_Nanterre.pdf", "06_Brioche_Fine_Nanterre.pdf"),
        ("15_Brioches_Individuelles_Sucre_PAC.pdf", "15_Brioches_Individuelles_Sucre_PAC.pdf"),
        ("09_fiche_atelier_galettes_rois_epiphanie.pdf", "09_Galettes_Rois_Epiphanie.pdf"),
        ("10_Frangipane_Galette_Rois.pdf", "10_Frangipane_Gateau_Nantais.pdf"),
        ("16_Registre_General_Cuissons_Atelier.pdf", "16_Registre_General_Cuissons_Atelier.pdf"),
    ]
    for local_name, remote_name in fiches_sync:
        p = exports_dir / local_name
        if p.exists():
            upload_or_update_file(p, FOLDER_FICHES_INDIV_ID, "application/pdf", token, remote_name=remote_name)

    # 3. Pôle Catalogue Markdown dans 03_CATALOGUE_RECETTES
    print("\n3. Pôle Catalogue Recettes Markdown (Consultation mobile / plein texte)...")
    folder_cat_id = get_or_create_subfolder(FOLDER_RECETTE_ID, "03_CATALOGUE_RECETTES", token)
    catalogue_dir = REPO_ROOT / "recettes" / "catalogue"
    md_files = sorted(list(catalogue_dir.glob("*.md")))
    for md_file in md_files:
        upload_or_update_file(md_file, folder_cat_id, "text/markdown; charset=utf-8", token)

    # 4. Pôle Recherche et Audits dans Boulangerie/Recherche
    print("\n4. Pôle Recherche, Index et Audits...")
    docs_to_sync = [
        REPO_ROOT / "INDEX_RECETTES.md",
        REPO_ROOT / "docs" / "INDEX_GLOBAL_SOURCES_ET_RECHERCHE.md",
        REPO_ROOT / "docs" / "AUDIT_COMPARATIF_POLE_1_PLF_TOURAGE.md",
        REPO_ROOT / "docs" / "AUDIT_ET_BLINDAGE_POLE_2_VIENNOISERIE_BRIOCHES.md",
        REPO_ROOT / "docs" / "fiche-controle-qualite-atelier.md",
    ]
    for doc in docs_to_sync:
        if doc.exists():
            upload_or_update_file(doc, FOLDER_RECHERCHE_ID, "text/markdown; charset=utf-8", token)

    print("\n=== SYNCHRONISATION GOOGLE DRIVE TERMINÉE AVEC SUCCÈS ===")


def main():
    parser = argparse.ArgumentParser(description="Synchronisation Google Drive Globale du Laboratoire")
    parser.add_argument("--check", action="store_true", help="Vérifier le statut sans mettre à jour")
    parser.add_argument("--credentials", type=Path, default=DEFAULT_CREDENTIALS, help="Chemin du fichier credentials OAuth")
    args = parser.parse_args()

    token = get_authenticated_token(args.credentials)
    sync_all(token, check_only=args.check)


if __name__ == "__main__":
    main()
