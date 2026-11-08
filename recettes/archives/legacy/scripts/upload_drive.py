# -*- coding: utf-8 -*-
"""
Synchronisation et Organisation automatique de Google Drive (Dossier Recette).
Auteur : Antigravity
"""

import json
import os
import sys
import urllib.request
import urllib.parse
import uuid
from pathlib import Path

CREDENTIALS_FILE = Path("/home/toto/.google_workspace_mcp/credentials/lanoetheau56@gmail.com.json")
ATELIER_DIR = Path("Cahier_Recettes_Atelier")
RECETTE_FOLDER_ID = "17gF1hv2FQcARh8lEuiCVoaj-HS0dyHhH"
ARCHIVE_FOLDER_ID = "1lL9gb5gvh86uunjb04r6n0EsQxRL4dtb"
FOLDER_A_IMPRIMER = "1BPX3UJTUmJE9hh-uQudk1i3p2A5O_z5m"
FOLDER_FICHES_INDIV = "1GG8M8BQuF2a3m0-mIQcCJJkC8ZNbKS4K"


def get_token():
    with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
        creds = json.load(f)

    token = creds["token"]
    req = urllib.request.Request(
        "https://www.googleapis.com/drive/v3/about?fields=user",
        headers={"Authorization": f"Bearer {token}"}
    )
    try:
        with urllib.request.urlopen(req):
            return token
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print("Rafraîchissement du token d'accès Google...")
            data = urllib.parse.urlencode({
                "client_id": creds["client_id"],
                "client_secret": creds["client_secret"],
                "refresh_token": creds["refresh_token"],
                "grant_type": "refresh_token"
            }).encode("utf-8")
            req2 = urllib.request.Request(creds["token_uri"], data=data)
            with urllib.request.urlopen(req2) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                creds["token"] = res["access_token"]
                with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f_out:
                    json.dump(creds, f_out, indent=2)
                return res["access_token"]
        raise


def drive_api(endpoint, method="GET", data=None, headers=None, token=None):
    if headers is None:
        headers = {}
    headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"https://www.googleapis.com{endpoint}", data=data, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode("utf-8")
        return json.loads(content) if content else {}


def move_file(file_id, new_parent_id, old_parent_id, token):
    url = f"/drive/v3/files/{file_id}?addParents={new_parent_id}&removeParents={old_parent_id}&fields=id,parents"
    return drive_api(url, method="PATCH", token=token)


def upload_pdf(file_path, folder_id, token):
    # Vérifier si un fichier du même nom existe déjà dans le dossier pour l'écraser / mettre à jour
    query = f"name = '{file_path.name}' and '{folder_id}' in parents and trashed = false"
    search_url = f"/drive/v3/files?q={urllib.parse.quote(query)}&fields=files(id,name)"
    search_res = drive_api(search_url, token=token)
    existing_files = search_res.get("files", [])

    boundary = f"-------{uuid.uuid4().hex}"
    file_bytes = file_path.read_bytes()

    if existing_files:
        file_id = existing_files[0]["id"]
        # Mise à jour du contenu existant
        url = f"https://www.googleapis.com/upload/drive/v3/files/{file_id}?uploadType=media"
        req = urllib.request.Request(
            url,
            data=file_bytes,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/pdf",
                "Content-Length": str(len(file_bytes))
            },
            method="PATCH"
        )
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            print(f"  [MÀJ] {file_path.name} -> ID: {res['id']}")
            return res
    else:
        # Nouveau fichier
        metadata = {"name": file_path.name, "parents": [folder_id]}
        body = [
            f"--{boundary}\r\n".encode("utf-8"),
            b"Content-Type: application/json; charset=UTF-8\r\n\r\n",
            json.dumps(metadata).encode("utf-8"),
            b"\r\n",
            f"--{boundary}\r\n".encode("utf-8"),
            b"Content-Type: application/pdf\r\n\r\n",
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
            print(f"  [CRÉÉ] {file_path.name} -> ID: {res['id']}")
            return res


def main():
    print("=== DÉMARRAGE DE LA SYNCHRONISATION GOOGLE DRIVE ===")
    token = get_token()

    # 1. NETTOYAGE ET RANGEMENT DE 'TRAVAIL/RECETTE'
    print("\n1. Rangement des anciens fichiers et brouillons dans Archive...")
    items_in_recette = drive_api(
        f"/drive/v3/files?q='{RECETTE_FOLDER_ID}'+in+parents+and+trashed=false&fields=files(id,name,mimeType)",
        token=token
    ).get("files", [])

    # Dossiers qu'on garde à la racine de 'Recette'
    kept_folder_ids = {FOLDER_A_IMPRIMER, FOLDER_FICHES_INDIV, ARCHIVE_FOLDER_ID}

    for item in items_in_recette:
        if item["id"] in kept_folder_ids:
            continue
        # Déplacer tout fichier ou dossier ancien vers Archive
        print(f"  -> Déplacement de '{item['name']}' vers Archive...")
        try:
            move_file(item["id"], ARCHIVE_FOLDER_ID, RECETTE_FOLDER_ID, token)
            print(f"     [OK] Déplacé : {item['name']}")
        except Exception as e:
            print(f"     [ERREUR déplacement] {item['name']}: {e}")

    # 2. UPLOAD DES DOCUMENTS PRIORITAIRES DANS '01_A_IMPRIMER (Cahier & Affiches)'
    print("\n2. Envoi des fichiers prioritaires dans '01_A_IMPRIMER (Cahier & Affiches)'...")
    priority_files = [
        ATELIER_DIR / "Cahier_Recettes_Complet_Labo.pdf",
        ATELIER_DIR / "Affiche_Cuissons_Apres_Midi.pdf",
        ATELIER_DIR / "Affiche_Programmes_Ligne_Rondo.pdf",
    ]
    for p_file in priority_files:
        if p_file.exists():
            upload_pdf(p_file, FOLDER_A_IMPRIMER, token)

    # 3. UPLOAD DES 16 FICHES ATELIER DANS '02_FICHES_INDIVIDUELLES (16 Fiches Atelier)'
    print("\n3. Envoi des 16 fiches individuelles d'atelier dans '02_FICHES_INDIVIDUELLES'...")
    individual_pdfs = sorted(list(ATELIER_DIR.glob("[0-1][0-9]_*.pdf")))
    for ind_file in individual_pdfs:
        upload_pdf(ind_file, FOLDER_FICHES_INDIV, token)

    print("\n=== SYNCHRONISATION ET RANGEMENT GOOGLE DRIVE TERMINÉS AVEC SUCCÈS ! ===")


if __name__ == "__main__":
    main()
