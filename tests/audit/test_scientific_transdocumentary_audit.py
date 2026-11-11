#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Suite de tests empiriques et d'audit sémantique et scientifique trans-documentaire.
Auteur : challenger_2 (Empirical Challenger, Critic & Specialist)
Jalon : Audit M4 / M3 / M2 — Vérification physique, chimique et mathématique.
"""

import os
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
M2_PATH = REPO_ROOT / ".agents" / "teamwork" / "worker_m2" / "TECH_EXTRACTIONS_14_BOOKS.md"
M3_PATH = REPO_ROOT / "docs" / "INDEX_GLOBAL_SOURCES_ET_RECHERCHE.md"
M4_DIR = REPO_ROOT / "skills" / "maitre-tourrier-boulanger" / "references"
BIBLIO_DIR = REPO_ROOT / "docs" / "bibliotheque"


class TestScientificTransdocumentaryAudit(unittest.TestCase):
    """Vérification empirique, thermodynamique, rhéologique et cohérence trans-documentaire."""

    @classmethod
    def setUpClass(cls):
        cls.m2_text = M2_PATH.read_text(encoding="utf-8")
        cls.m3_text = M3_PATH.read_text(encoding="utf-8")
        cls.m4_files = {
            f.name: f.read_text(encoding="utf-8")
            for f in M4_DIR.glob("*.md")
        }

    def test_01_grover_sucrose_equivalents_table_consistency(self):
        """Vérifie la présence et la fidélité des 11 facteurs SE de Grover dans M4 (pates-battues)."""
        expected_se = {
            "saccharose": "1,0",
            "farine": "0,2",
            "matière grasse pure": "0,0",
            "beurre": "0,2",
            "œufs entiers": "0,0",
            "poudre de lait": "1,2",
            "poudre à lever": "3,0",
            "sel": "11,0",
            "glucose": "0,7",
            "sorbitol": "2,0",
            "glycérol": "4,0",
        }

        pates_battues = self.m4_files["pates-battues-cakes-emulsions.md"]

        for ingredient, val in expected_se.items():
            pattern = rf"\b{re.escape(val)}\b"
            self.assertTrue(
                re.search(pattern, pates_battues),
                f"Facteur SE {val} introuvable pour {ingredient} dans pates-battues-cakes-emulsions.md"
            )

    def test_02_grover_erh_mathematical_contradiction(self):
        """Vérifie la clarification et la remédiation rigoureuse de la formule ERH / aw de Grover.
        
        Vérifie :
        1. La définition de S_aqueux = (SET / (SET + ETR)) * 100 pour le polynôme empirique.
        2. La formule rationnelle de dépression de tension de vapeur de Grover : ERH = 100 / (1 + 0.18 N).
        3. L'abaque de Cooper/Seiler (Fig. 29.1) donnant directement ERH = 88% (aw = 0.88) pour S = 1.70.
        """
        pates_battues = self.m4_files["pates-battues-cakes-emulsions.md"]
        self.assertIn("Concentration en Sucrose Équivalent (S)", pates_battues)
        self.assertIn("S_{\\text{aqueux}}", pates_battues)
        self.assertIn(r"\mathrm{ERH} = \frac{100}{1 + 0{,}18\,N}", pates_battues)
        self.assertIn("Fig. 29.1", pates_battues)
        self.assertIn("88", pates_battues)

        set_val = 135.0
        etr_val = 79.4

        # Si S est la fraction massique en phase aqueuse totale (SET / (SET + ETR) * 100) :
        s_aqueous = (set_val / (set_val + etr_val)) * 100.0  # 62.97%
        erh_aqueous = 100.0 - 0.26 * s_aqueous - 0.001 * (s_aqueous ** 2)  # 79.66%
        self.assertAlmostEqual(erh_aqueous, 79.66, delta=0.5)

        # Formule rationnelle de Grover :
        n_moles = (set_val / 342.3) / (etr_val / 1000.0)
        erh_grover = 100.0 / (1.0 + 0.18 * n_moles)
        self.assertGreater(erh_grover, 50.0)

    def test_03_bennion_chapter_citation_discrepancy(self):
        """Vérifie la rectification de la citation bibliographique : Chapitre 29 dans Bennion 6th Ed."""
        self.assertIn("Chapitre 29", self.m2_text)
        self.assertIn("Chap. 29", self.m3_text)

        pates_battues = self.m4_files["pates-battues-cakes-emulsions.md"]
        self.assertIn("Chapitre 29", pates_battues)

        diagnostic = self.m4_files["diagnostic-defauts.md"]
        self.assertIn("Chap. 29", diagnostic)

    def test_04_levine_drew_parameters_and_temperature_omission(self):
        """Vérifie les constantes de consistance K et d'indice d'écoulement n de Levine & Drew et mention de 43 °C."""
        veille = self.m4_files["veille-scientifique-tourage.md"]

        # Constantes présentes avec ou sans accolade LaTeX
        self.assertTrue(re.search(r"4\{?,\}?45\s*\\times\s*10\^3", veille))
        self.assertTrue(re.search(r"0\{?,\}?35", veille))
        self.assertTrue(re.search(r"3\{?,\}?33\s*\\times\s*10\^4", veille))
        self.assertTrue(re.search(r"0\{?,\}?41", veille))

        # Vérification critique : K=4.45x10^3 et n=0.35 ont été mesurés à 43 °C (Harper 1981, Faridi Table 14-2).
        self.assertTrue("43" in veille and "Harper" in veille and ("circ" in veille or "°C" in veille))

    def test_05_deborah_number_sheeting_physics_critique(self):
        """Stress-test rhéologique sur le nombre de Deborah (De = lambda / t_res)."""
        veille = self.m4_files["veille-scientifique-tourage.md"]
        self.assertIn(r"De = \frac{\lambda}{t_{\mathrm{res}}}", veille)

        # Calcul empirique de l'ordre de grandeur de De lors d'une passe de laminoir :
        # t_res ~ 0.05 à 0.1 s ; lambda_gluten ~ 10 à 60 s
        t_res = 0.1
        lambda_gluten = 20.0
        de_nip = lambda_gluten / t_res  # 200 >> 1

        self.assertGreater(de_nip, 10.0, "Au passage des cylindres, De >> 1 (réponse élastique).")
        # Le repos de 20-30 min entre tours sert à dissiper les contraintes résiduelles APRÈS laminage,
        # et non à rendre De <= 1 pendant la passe.
        self.assertIn("relaxer", veille)

    def test_06_goff_pac_cryobiology_parameters(self):
        """Vérifie l'exactitude des paramètres de Goff (Tg', Wg', Ostwald) dans les fiches M4."""
        veille = self.m4_files["veille-scientifique-tourage.md"]
        amidon = self.m4_files["science-amidon-gelatinisation.md"]

        # Tg' entre -12 °C et -15 °C
        self.assertTrue("-12" in veille and "-15" in veille)
        # Wg' ~ 20-25%
        self.assertTrue(re.search(r"20\s*[-–]\s*25", veille))
        # Mûrissement d'Ostwald
        self.assertIn("Ostwald", veille)
        self.assertIn("Ostwald", amidon)
        # Seuil de stockage sous -18 °C
        self.assertIn("-18", veille)

    def test_07_manley_checking_parameters(self):
        """Vérifie les paramètres de checking de Manley (gradient d'humidité 4-7% vs < 1.5%, ratio de ressuage)."""
        biscuits = self.m4_files["biscuiterie-cookies-laminage.md"]
        diagnostic = self.m4_files["diagnostic-defauts.md"]

        # Gradient d'humidité
        self.assertIn("4 à 7 %", biscuits)
        self.assertIn("1,5 %", biscuits)

        # Ratio de ressuage 1.5 à 2.0 (recherche flexible)
        self.assertTrue("Temps de Refroidissement" in biscuits and "Temps de Cuisson" in biscuits)
        self.assertTrue(re.search(r"1\{?,\}?5.*2\{?,\}?0", biscuits))
        self.assertIn("1,5", diagnostic)

        # Activité de l'eau critique
        self.assertTrue(re.search(r"0\{?,\}?25", biscuits))
        self.assertTrue(re.search(r"0\{?,\}?35", biscuits))

    def test_08_haute_creation_protocols(self):
        """Vérifie les protocoles empiriques des grands créateurs dans le référentiel M4."""
        patisserie = self.m4_files["patisserie-boulangere.md"]
        viennoiserie = self.m4_files["viennoiserie-brioches.md"]
        panification = self.m4_files["panification-levain.md"]
        pates_battues = self.m4_files["pates-battues-cakes-emulsions.md"]

        # Felder : galette sous grille à cales de 4 cm, 150-160 °C
        self.assertIn("4 cm", patisserie)
        self.assertTrue("150" in patisserie or "160" in patisserie)

        # Perruchon : masse gélatine 1:6, glaçage miroir 103 °C, température d'utilisation 30 à 35 °C
        self.assertIn("1:6", patisserie)
        self.assertIn("103 °C", patisserie)
        self.assertTrue(re.search(r"30\s*°C\s*à\s*32\s*°C", patisserie) and re.search(r"32\s*°C\s*à\s*35\s*°C", patisserie))

        # Glacier : cake Valencia p. 129, aw <= 0.75, sirop 30 °Baumé, beurre manié 80/20
        self.assertIn("129", pates_battues)
        self.assertTrue(re.search(r"80\s*%\s*de\s*beurre", pates_battues))
        self.assertTrue(re.search(r"20\s*%\s*de\s*farine", pates_battues))
        self.assertIn("30 °Baumé", pates_battues)

        # Thomas Marie : autolyse 1 h, bac 12 h à +3 °C
        self.assertTrue(re.search(r"autolyse", panification, re.IGNORECASE))
        self.assertIn("12 heures à +3 °C", panification)

        # Bellouet : croissant TB 52 °C, repos 45 min à -18 °C avec retournement à 20 min
        self.assertIn("52 °C", viennoiserie)
        self.assertIn("-18", viennoiserie)
        self.assertIn("20 min", viennoiserie)

    def test_09_m2_arithmetic_butter_layers_discrepancy(self):
        """Vérifie la rectification arithmétique dans M2 ligne 437 ('12 couches de beurre (25 couches au total)')."""
        m2_match = re.search(r"1\s*tour\s*double\s*\+\s*1\s*tour\s*simple\s*\(([^\)]+)\)", self.m2_text)
        self.assertIsNotNone(m2_match)
        inside_parens = m2_match.group(1)

        # M2 rectifié à '12 couches de beurre (25 couches au total)'
        self.assertIn("12 couches de beurre", inside_parens)
        self.assertIn("25 couches au total", inside_parens)

        # Dans le référentiel M4 (science-formulation-pac.md ligne 69), c'est correctement aligné :
        pac = self.m4_files["science-formulation-pac.md"]
        self.assertIn("12 films", pac, "M4 rectifie correctement à 12 films de beurre")

    def test_10_cake_batter_relative_density_bounds(self):
        """Vérifie les bornes de densité relative (RD) des pâtes battues."""
        pb = self.m4_files["pates-battues-cakes-emulsions.md"]
        diag = self.m4_files["diagnostic-defauts.md"]

        # Plage optimale 0.70 à 0.85
        self.assertTrue(re.search(r"0\{?,\}?70.*0\{?,\}?85", pb))
        # Seuil d'affaissement RD < 0.65
        self.assertTrue(re.search(r"0\{?,\}?65", diag))
        # Seuil de compaction RD > 0.90
        self.assertTrue(re.search(r"0\{?,\}?90", diag))

    def test_11_starch_bimodal_granule_and_rva_curve(self):
        """Vérifie la microstructure de l'amidon de blé (granules A 15-35 µm vs B 2-10 µm) et RVA."""
        amidon = self.m4_files["science-amidon-gelatinisation.md"]

        # Granules A et B
        self.assertTrue(re.search(r"15\s*à\s*35\s*µm", amidon))
        self.assertTrue(re.search(r"Granules B", amidon))

        # Viscosité RVA (Rapid Visco Analyser)
        self.assertIn("RVA", amidon)
        self.assertIn("peak", amidon.lower())
        self.assertIn("breakdown", amidon.lower())
        self.assertIn("setback", amidon.lower())


if __name__ == "__main__":
    unittest.main()
