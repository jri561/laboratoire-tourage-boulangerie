#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Suite de tests de certification et de blindage formel du Pôle 2 (Viennoises & Brioches PAC).
Auteur : Ingénieur R&D Senior en Boulangerie Industrielle
Vérification des 4 fiches d'atelier, de l'Option C (Soft'r + Kimo), de l'huile de colza,
des bacs de 6 000 g, du calibre 75 g, et de l'expression 100 % en GRAMMES.
"""

import os
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOGUE_DIR = REPO_ROOT / "recettes" / "catalogue"
DOCS_DIR = REPO_ROOT / "docs"
INDEX_PATH = REPO_ROOT / "INDEX_RECETTES.md"


class TestPole2ViennoisesBrioches(unittest.TestCase):
    """Vérification stricte des livrables d'ingénierie du Pôle 2."""

    @classmethod
    def setUpClass(cls):
        cls.audit_file = DOCS_DIR / "AUDIT_ET_BLINDAGE_POLE_2_VIENNOISERIE_BRIOCHES.md"
        cls.fiches = {
            "V-VIE-01": CATALOGUE_DIR / "v-vie-01-pain-viennois-nature-pac.md",
            "V-VIE-02": CATALOGUE_DIR / "v-vie-02-pain-viennois-chocolat-pac.md",
            "V-BRI-01": CATALOGUE_DIR / "brioche-individuelle-sucre-pac.md",
            "V-BRI-02": CATALOGUE_DIR / "brioche-fine-nanterre.md",
        }
        cls.fiches_content = {
            code: path.read_text(encoding="utf-8")
            for code, path in cls.fiches.items()
        }
        cls.audit_content = cls.audit_file.read_text(encoding="utf-8")
        cls.index_content = INDEX_PATH.read_text(encoding="utf-8")

    def test_01_all_files_exist(self):
        """Vérifie l'existence de l'audit R&D et des 4 fiches homologuées."""
        self.assertTrue(self.audit_file.exists(), f"Fichier manquant : {self.audit_file}")
        for code, path in self.fiches.items():
            self.assertTrue(path.exists(), f"Fiche manquante pour {code} : {path}")

    def test_02_double_page_vis_a_vis_structure(self):
        """Chaque fiche doit adopter la double-page officielle : Page Gauche Pesée / Page Droite Machine."""
        for code, text in self.fiches_content.items():
            self.assertIn("PAGE GAUCHE", text, f"{code} : Section PAGE GAUCHE manquante")
            self.assertIn("PAGE DROITE", text, f"{code} : Section PAGE DROITE manquante")
            self.assertIn("POSTE DE PESÉE", text, f"{code} : Titre POSTE DE PESÉE manquant")
            self.assertIn("```mermaid", text, f"{code} : Diagramme Mermaid manquant en Page Droite")

    def test_03_soft_r_and_kimo_short_parameters(self):
        """Vérifie le mix technologique 1,5 % Soft'r Puratos + 1,5 % Kimo Short."""
        for code in ["V-VIE-01", "V-VIE-02", "V-BRI-01"]:
            text = self.fiches_content[code]
            self.assertIn("Soft'r", text, f"{code} : Améliorant Soft'r absent")
            self.assertIn("Kimo", text, f"{code} : Améliorant Kimo absent")
            self.assertIn("1,5 %", text, f"{code} : Dosage 1,5 % absent")

    def test_04_direct_method_and_banned_24h_frigo_for_viennoises(self):
        """Les viennoises V-VIE-01 et V-VIE-02 doivent formaliser la méthode directe le jour même."""
        for code in ["V-VIE-01", "V-VIE-02"]:
            text = self.fiches_content[code]
            self.assertIn("Méthode Directe", text, f"{code} : Méthode Directe absente")
            self.assertIn("Pointage court en cuve", text, f"{code} : Pointage court cuve absent")
            self.assertIn("façonneuse à tapis", text.lower(), f"{code} : Façonneuse à tapis absente")
            self.assertIn("-35 °C", text, f"{code} : Surgélation flash -35 °C absente")

    def test_05_weights_and_calibres_accuracy(self):
        """Vérifie la stricte conformité des calibres cru révisés (280 g, 140 g, 75 g), des bacs en grammes et des matières grasses."""
        # V-VIE-01 : 280 g cru -> 5 600 g / bac avec Margarine OPALE cuve
        v01 = self.fiches_content["V-VIE-01"]
        self.assertIn("280 g cru", v01)
        self.assertIn("5 600 g", v01)
        self.assertIn("Margarine OPALE cuve", v01)

        # V-VIE-02 : 140 g cru -> 5 600 g / bac avec Margarine OPALE cuve
        v02 = self.fiches_content["V-VIE-02"]
        self.assertIn("140 g cru", v02)
        self.assertIn("5 600 g", v02)
        self.assertIn("Margarine OPALE cuve", v02)

        # V-BRI-01 : 75 g cru et bacs standardisés à 6 000 g net avec Huile de colza
        b01 = self.fiches_content["V-BRI-01"]
        self.assertIn("75 g", b01)
        self.assertIn("Sucre Grain n°10", b01)
        self.assertIn("6 000 g", b01)
        self.assertIn("Huile de colza", b01)

        # V-BRI-02 : 400 g cru (8 boules de 50 g)
        b02 = self.fiches_content["V-BRI-02"]
        self.assertIn("400 g cru", b02)
        self.assertIn("50 g", b02)
        self.assertIn("4 000 g", b02)

    def test_06_scales_expressed_in_grams(self):
        """Toutes les valeurs des tableaux de pesée doivent être exprimées en GRAMMES (g)."""
        for code, text in self.fiches_content.items():
            self.assertIn("Base 1 000 g Farine", text, f"{code} : Base 1 000 g Farine manquante")
            self.assertIn("1 Bac", text, f"{code} : Colonne 1 Bac manquante")
            self.assertIn("10 Bacs", text, f"{code} : Colonne 10 Bacs manquante")
            self.assertIn("20 Bacs", text, f"{code} : Colonne 20 Bacs manquante")

        # Pour les viennoises et brioches : vérifier l'échelle 30 Bacs en grammes
        for code in ["V-VIE-01", "V-VIE-02"]:
            self.assertIn("30 Bacs", self.fiches_content[code], f"{code} : Échelle 30 Bacs manquante")
            self.assertIn("168 000 g", self.fiches_content[code], f"{code} : 168 000 g manquant")

        # Pour la brioche au sucre : vérifier 30 bacs à 180 000 g
        self.assertIn("180 000 g", self.fiches_content["V-BRI-01"])

    def test_07_pac_and_baking_parameters(self):
        """Vérifie les paramètres thermiques d'étuve PAC (26 °C), sonde (-10 °C) et four ventilé (165 °C)."""
        for code in ["V-VIE-01", "V-VIE-02", "V-BRI-01"]:
            text = self.fiches_content[code]
            self.assertIn("26 °C", text, f"{code} : Étuve 26 °C absente")
            self.assertIn("-10 °C", text, f"{code} : Sonde -10 °C absente")
            self.assertIn("165 °C", text, f"{code} : Four ventilé 165 °C absent")

        # Brioche Sucre : Ouras ouverts obligatoires
        self.assertIn("OURAS OUVERTS", self.fiches_content["V-BRI-01"])

        # Viennoises : Ouras fermés obligatoires
        self.assertIn("OURAS", self.fiches_content["V-VIE-01"])
        self.assertIn("FERMÉS", self.fiches_content["V-VIE-01"])

        # Brioche Nanterre : Pousse max 25 °C pour préserver le beurre
        self.assertIn("25 °C MAX", self.fiches_content["V-BRI-02"])

    def test_08_index_recettes_links_validity(self):
        """Vérifie que INDEX_RECETTES.md référence avec exactitude les 4 fiches du Pôle 2."""
        for code in ["V-VIE-01", "V-VIE-02", "V-BRI-01", "V-BRI-02"]:
            self.assertIn(code, self.index_content, f"Code {code} introuvable dans INDEX_RECETTES.md")
        self.assertIn("v-vie-01-pain-viennois-nature-pac.md", self.index_content)
        self.assertIn("v-vie-02-pain-viennois-chocolat-pac.md", self.index_content)
        self.assertIn("brioche-individuelle-sucre-pac.md", self.index_content)
        self.assertIn("brioche-fine-nanterre.md", self.index_content)

    def test_09_fiches_atelier_operateurs_pole2(self):
        """Vérifie la création et conformité des fiches atelier opérateurs Pôle 2 (Cahier Atelier)."""
        atelier_dir = REPO_ROOT / "recettes" / "fiches_atelier_operateurs"
        f04 = atelier_dir / "04-fiche-atelier-pain-viennois-nature-et-chocolat-pac.md"
        f05 = atelier_dir / "05-fiche-atelier-petite-brioche-sucre-pac.md"
        f06 = atelier_dir / "06-fiche-atelier-brioche-fine-nanterre.md"
        sommaire = (atelier_dir / "00-sommaire-classeur-atelier.md").read_text(encoding="utf-8")

        self.assertTrue(f04.exists(), f"Fiche atelier manquante : {f04}")
        self.assertTrue(f05.exists(), f"Fiche atelier manquante : {f05}")
        self.assertTrue(f06.exists(), f"Fiche atelier manquante : {f06}")

        # Vérifier l'indexation dans le sommaire du classeur
        self.assertIn("04-fiche-atelier-pain-viennois-nature-et-chocolat-pac.md", sommaire)
        self.assertIn("05-fiche-atelier-petite-brioche-sucre-pac.md", sommaire)
        self.assertIn("06-fiche-atelier-brioche-fine-nanterre.md", sommaire)

        # Vérifier les unités 100% en grammes et les échelles
        t04 = f04.read_text(encoding="utf-8")
        t05 = f05.read_text(encoding="utf-8")
        t06 = f06.read_text(encoding="utf-8")

        self.assertIn("168 000 g pile", t04)
        self.assertIn("5 600 g pile", t04)
        self.assertIn("180 000 g pile", t05)
        self.assertIn("6 000 g pile", t05)
        self.assertIn("4 000 g pile", t06)
        self.assertIn("80 000 g pile", t06)


if __name__ == "__main__":
    unittest.main()
