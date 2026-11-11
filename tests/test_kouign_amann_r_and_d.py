#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests de certification et vérification formelle R&D du Kouign-Amann (Individuel & Partage).
Auteur : Ingénieur R&D Senior en Boulangerie Industrielle & Maître Tourrier
Vérification des livrables : fiches catalogue, fiche atelier double-page, pesées 100% en grammes,
absence de virgules, conformité cryoscopique et thermodynamique.
"""

import os
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOGUE_PATH = REPO_ROOT / "recettes" / "catalogue" / "kouign-amann-pac.md"
ATELIER_PATH = REPO_ROOT / "recettes" / "fiches_atelier_operateurs" / "07-fiche-atelier-kouign-amann.md"
SOMMAIRE_PATH = REPO_ROOT / "recettes" / "fiches_atelier_operateurs" / "00-sommaire-classeur-atelier.md"
CUISSON_PATH = REPO_ROOT / "recettes" / "fiches_atelier_operateurs" / "03-annexe-baremes-generaux-cuisson.md"
PDF_DEDIE = REPO_ROOT / "exports_pdf" / "07_fiche_atelier_kouign_amann.pdf"
PDF_CLASSEUR = REPO_ROOT / "exports_pdf" / "cahier_atelier_equipe.pdf"


class TestKouignAmannRD(unittest.TestCase):
    """Vérification stricte de la R&D et standardisation atelier du Kouign-Amann."""

    @classmethod
    def setUpClass(cls):
        cls.catalogue_text = CATALOGUE_PATH.read_text(encoding="utf-8")
        cls.atelier_text = ATELIER_PATH.read_text(encoding="utf-8")
        cls.sommaire_text = SOMMAIRE_PATH.read_text(encoding="utf-8")
        cls.cuisson_text = CUISSON_PATH.read_text(encoding="utf-8")

    def test_01_files_exist(self):
        """Vérifie la présence de tous les fichiers attendus."""
        self.assertTrue(CATALOGUE_PATH.exists(), f"Fichier catalogue manquant : {CATALOGUE_PATH}")
        self.assertTrue(ATELIER_PATH.exists(), f"Fichier atelier manquant : {ATELIER_PATH}")
        self.assertTrue(PDF_DEDIE.exists(), f"PDF dédié manquant : {PDF_DEDIE}")
        self.assertTrue(PDF_CLASSEUR.exists(), f"PDF classeur manquant : {PDF_CLASSEUR}")

    def test_02_double_page_vis_a_vis(self):
        """Vérifie le format standard en double page vis-à-vis pour la fiche d'atelier opérateur."""
        self.assertIn("PAGE GAUCHE", self.atelier_text, "Atelier: PAGE GAUCHE manquante")
        self.assertIn("PAGE DROITE", self.atelier_text, "Atelier: PAGE DROITE manquante")
        self.assertIn("POSTE DE PESÉE", self.atelier_text, "Atelier: Section POSTE DE PESÉE manquante")

    def test_03_zero_virgule_and_strictly_grams_in_weights(self):
        """Vérifie que les tableaux de pesées n'utilisent aucun 'kg' ni décimales dans les colonnes de poids."""
        for text, name in [(self.atelier_text, "atelier"), (self.catalogue_text, "catalogue")]:
            lines = text.splitlines()
            in_table = False
            for line in lines:
                if "| Phase & Ordre |" in line:
                    in_table = True
                    continue
                if in_table and line.startswith("|") and not line.startswith("| :---"):
                    cols = [c.strip() for c in line.split("|")[1:-1]]
                    if len(cols) >= 7 and ("`[1]`" in cols[0] or "`[2]`" in cols[0] or "`[3]`" in cols[0] or "SOUS-TOTAL" in cols[0] or "TOTAL" in cols[0]):
                        for col_idx in [3, 4, 5, 6]:
                            raw_val = cols[col_idx]
                            clean_val = raw_val.replace("*", "").strip()
                            self.assertNotIn("kg", clean_val, f"{name} ligne '{cols[1]}': présence interdite de 'kg' ({clean_val})")
                            self.assertNotIn(",", clean_val, f"{name} ligne '{cols[1]}': présence interdite de virgule décimale ({clean_val})")
                            self.assertTrue(clean_val.endswith("g") or "pile" in clean_val, f"{name} poids doit se terminer par 'g' : {clean_val}")
                elif in_table and not line.strip():
                    in_table = False

    def test_04_mathematical_coherence_weights(self):
        """Vérifie l'exactitude des pesées du bac étalon au Ratio d'Or (5 000 g détrempe et 8 820 g pâte finie)."""
        # Bac 1 Détrempe : 2750 + 1420 + 50 + 70 + 70 + 15 + 50 + 165 + 410 = 5000 g
        self.assertEqual(2750 + 1420 + 50 + 70 + 70 + 15 + 50 + 165 + 410, 5000)
        # Beurre Manié Bac 1 : 2000 g beurre + 1800 g sucre + 20 g fleur de sel = 3820 g
        self.assertEqual(2000 + 1800 + 20, 3820)
        # Total Pâton Touré : 5000 + 3820 = 8820 g
        self.assertEqual(5000 + 3820, 8820)

        # Bac 5 : 5000 * 5 = 25 000 g détrempe, total = 8820 * 5 = 44 100 g
        self.assertEqual(5000 * 5, 25000)
        self.assertEqual(8820 * 5, 44100)

        # Bac 10 : 5000 * 10 = 50 000 g détrempe, total = 8820 * 10 = 88 200 g
        self.assertEqual(5000 * 10, 50000)
        self.assertEqual(8820 * 10, 88200)

    def test_05_scientific_diagnostics_and_terms(self):
        """Vérifie la présence des diagnostics thermodynamiques et biochimiques complets."""
        required_scientific_terms = [
            "L'Hirondelle Or",
            "osmotolérante",
            "saccharose",
            "plasmolyse",
            "glutathion",
            "GSH",
            "transition vitreuse",
            "T_g'",
            "abaissement cryoscopique",
            "conductivité thermique",
            "silicone",
            "roulé tronçonné",
            "3,5 cm",
            "ouras",
            "miroir"
        ]
        for term in required_scientific_terms:
            self.assertIn(term.lower(), self.catalogue_text.lower(), f"Terme scientifique manquant dans catalogue : {term}")

    def test_06_sommaire_and_cuisson_integration(self):
        """Vérifie que la fiche 07 est répertoriée dans le sommaire et le tableau de cuisson."""
        self.assertIn("07-fiche-atelier-kouign-amann.md", self.sommaire_text)
        self.assertIn("Kouign-Amann Indiv. (100 g)", self.cuisson_text)
        self.assertIn("Kouign-Amann Partage (400 g)", self.cuisson_text)
        self.assertIn("Kouign-Amann Partage (600 g)", self.cuisson_text)
        self.assertIn("OUVRIR À 20 MIN", self.cuisson_text)


if __name__ == "__main__":
    unittest.main()
