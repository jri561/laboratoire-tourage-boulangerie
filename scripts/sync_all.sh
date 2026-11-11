#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# Script de Synchronisation Totale (PDFs + Google Drive + GitHub)
# Laboratoire Tourage & Boulangerie

set -e

REPO_DIR="/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie"
cd "$REPO_DIR"

echo "=========================================================="
echo "  SYNCHRONISATION GLOBALE — LABORATOIRE DE TOURAGE"
echo "  $(date '+%Y-%m-%d %H:%M:%S')"
echo "=========================================================="

echo ""
echo "▶ Étape 1/3 : Génération et compilation des PDFs d'atelier..."
python3 scripts/generate_cahier_atelier_pdf.py

echo ""
echo "▶ Étape 2/3 : Synchronisation miroir vers Google Drive..."
python3 scripts/sync_drive.py

echo ""
echo "▶ Étape 3/3 : Synchronisation vers GitHub..."
# Vérification des modifications locales
if [ -n "$(git status --porcelain)" ]; then
    echo "  -> Modifications détectées dans le dépôt local."
    git add .
    COMMIT_MSG="chore(sync): synchronisation globale recettes, PDFs & Drive [$(date '+%Y-%m-%d %H:%M')]"
    git commit -m "$COMMIT_MSG"
    echo "  -> Commit créé : $COMMIT_MSG"
else
    echo "  -> Aucun changement non commité."
fi

echo "  -> Envoi (git push) vers origin/main (GitHub)..."
git push origin main

echo ""
echo "=========================================================="
echo "  SYNCHRONISATION TERMINÉE AVEC SUCCÈS SUR GITHUB & DRIVE !"
echo "=========================================================="
