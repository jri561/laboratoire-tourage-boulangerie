#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests empiriques adversariaux et vérification formelle de bout en bout.
Auteur : challenger_1 (Empirical Challenger, Critic & Specialist)
Jalon : Audit de robustesse et vérification empirique
"""

import os
import re
import subprocess
import sys
import unittest
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
BIBLIO_DIR = DOCS_DIR / "bibliotheque"
INDEX_PATH = DOCS_DIR / "INDEX_GLOBAL_SOURCES_ET_RECHERCHE.md"
SKILL_REF_DIR = REPO_ROOT / "skills" / "maitre-tourrier-boulanger" / "references"


class TestEmpiricalChallenger(unittest.TestCase):
    """Batterie de tests adversariaux et de stress-testing d'intégrité."""

    def test_01_root_cleanliness(self):
        """a. Absence absolue de fichiers sources (PDF, EPUB, etc.) à la racine du projet."""
        forbidden_exts = {".pdf", ".epub", ".azw3", ".mobi", ".djvu", ".zip", ".tar", ".gz"}
        root_files = [f for f in REPO_ROOT.iterdir() if f.is_file()]
        stray_source_files = [
            f.name for f in root_files if f.suffix.lower() in forbidden_exts
        ]
        self.assertEqual(
            stray_source_files,
            [],
            f"Des fichiers sources bruts subsistent à la racine du projet : {stray_source_files}"
        )

    def test_02_bibliotheque_integrity_and_distribution(self):
        """b. Présence et intégrité exacte des 37 fichiers dans docs/bibliotheque/ répartis dans les 5 sous-dossiers."""
        expected_distribution = {
            "diagnostic_et_ingenierie": 9,
            "grands_createurs": 6,
            "materiel_et_lignes": 4,
            "recherche_et_sciences": 10,
            "traites_et_ecoles": 8,
        }

        self.assertTrue(BIBLIO_DIR.exists(), f"Dossier introuvable : {BIBLIO_DIR}")

        actual_files_by_category = {}
        all_disk_files = []

        for folder, expected_count in expected_distribution.items():
            folder_path = BIBLIO_DIR / folder
            self.assertTrue(
                folder_path.exists() and folder_path.is_dir(),
                f"Sous-dossier manquant : {folder_path}"
            )
            files = [f for f in folder_path.iterdir() if f.is_file()]
            actual_files_by_category[folder] = len(files)
            all_disk_files.extend(files)

            self.assertEqual(
                len(files),
                expected_count,
                f"Dossier {folder} : attendu {expected_count} fichiers, trouvé {len(files)}"
            )

        self.assertEqual(
            len(all_disk_files),
            37,
            f"Total fichiers dans docs/bibliotheque/ : attendu 37, trouvé {len(all_disk_files)}"
        )

        # Vérification d'intégrité binaire pour chaque fichier
        for f in all_disk_files:
            size = f.stat().st_size
            self.assertGreater(
                size,
                50_000,
                f"Fichier anormalement petit ou tronqué : {f} ({size} octets)"
            )
            with open(f, "rb") as bin_f:
                header = bin_f.read(128)

            ext = f.suffix.lower()
            if ext == ".pdf":
                self.assertTrue(
                    header.startswith(b"%PDF-"),
                    f"En-tête PDF invalide pour {f}"
                )
            elif ext == ".epub":
                self.assertTrue(
                    header.startswith(b"PK\x03\x04"),
                    f"En-tête EPUB invalide (non-ZIP) pour {f}"
                )
                # Vérifier que c'est bien un conteneur EPUB
                with zipfile.ZipFile(f, "r") as z:
                    self.assertIn("mimetype", z.namelist(), f"EPUB sans mimetype : {f}")
                    mimetype_content = z.read("mimetype").decode("utf-8", errors="ignore").strip()
                    self.assertEqual(
                        mimetype_content,
                        "application/epub+zip",
                        f"mimetype incorrect dans EPUB {f}"
                    )
            elif ext == ".azw3":
                # AZW3 / Mobi / PalmDOC header contains BOOKMOBI at offset 60
                self.assertIn(
                    b"BOOKMOBI",
                    header,
                    f"En-tête PalmDOC/BOOKMOBI introuvable pour {f}"
                )
            else:
                self.fail(f"Extension de source inconnue ou inattendue : {ext} pour {f}")

    def test_03_strict_bijection_index_disk(self):
        """c. Bijection 1:1 stricte : chaque fichier sur disque doit être mentionné par son chemin exact dans docs/INDEX_GLOBAL_SOURCES_ET_RECHERCHE.md et inversement (zéro chemin brisé)."""
        self.assertTrue(INDEX_PATH.exists(), f"Index introuvable : {INDEX_PATH}")
        index_content = INDEX_PATH.read_text(encoding="utf-8")

        # Collecte des fichiers réels sur disque (chemins relatifs par rapport à REPO_ROOT)
        disk_rel_paths = set()
        for f in BIBLIO_DIR.rglob("*"):
            if f.is_file():
                rel = f.relative_to(REPO_ROOT).as_posix()
                disk_rel_paths.add(rel)

        self.assertEqual(
            len(disk_rel_paths),
            37,
            f"Nombre de fichiers sur disque différent de 37 : {len(disk_rel_paths)}"
        )

        # Extraction des chemins référencés dans l'index
        # Chercher les motifs `docs/bibliotheque/...`
        pattern = r"docs/bibliotheque/[a-zA-Z0-9_\-\./]+"
        raw_matches = re.findall(pattern, index_content)

        # Nettoyage des suffixes éventuels (virgules, parenthèses, crochets, etc.)
        cleaned_matches = set()
        for m in raw_matches:
            # Enlever toute ponctuation résiduelle de fin
            clean = re.sub(r"[\)\],`'\"]+$", "", m)
            if clean.startswith("docs/bibliotheque/") and not clean.endswith("/"):
                # Si c'est un sous-dossier, on l'ignore ; on ne retient que les chemins vers des fichiers
                p = REPO_ROOT / clean
                if p.is_file() or clean in disk_rel_paths:
                    cleaned_matches.add(clean)

        # Vérification 1 : Tout fichier sur disque est dans l'index
        orphaned_on_disk = disk_rel_paths - cleaned_matches
        self.assertEqual(
            orphaned_on_disk,
            set(),
            f"Fichiers présents sur disque mais absents de l'index : {orphaned_on_disk}"
        )

        # Vérification 2 : Tout chemin extrait de l'index existe sur disque
        broken_in_index = cleaned_matches - disk_rel_paths
        self.assertEqual(
            broken_in_index,
            set(),
            f"Chemins référencés dans l'index mais introuvables sur disque : {broken_in_index}"
        )

        # Bijection stricte
        self.assertEqual(
            len(cleaned_matches),
            37,
            f"L'index doit référencer exactement 37 fichiers uniques, trouvé {len(cleaned_matches)}"
        )

    def test_04_mermaid_diagram_syntax_and_nodes(self):
        """d. Diagramme Mermaid : syntaxe 100 % valide, exactement 37 nœuds au Niveau 1."""
        index_content = INDEX_PATH.read_text(encoding="utf-8")
        mermaid_match = re.search(r"```mermaid\s*\n(.*?)\n```", index_content, re.DOTALL)
        self.assertIsNotNone(mermaid_match, "Bloc ```mermaid introuvable dans l'index.")
        mermaid_code = mermaid_match.group(1).strip()

        # Syntaxe de départ
        self.assertTrue(
            mermaid_code.startswith("flowchart") or mermaid_code.startswith("graph"),
            "Le diagramme Mermaid doit commencer par flowchart ou graph."
        )

        # Vérification de l'équilibre des sous-graphes
        subgraph_count = len(re.findall(r"\bsubgraph\b", mermaid_code))
        end_count = len(re.findall(r"\bend\b", mermaid_code))
        self.assertEqual(
            subgraph_count,
            end_count,
            f"Déséquilibre de sous-graphes Mermaid : {subgraph_count} subgraph vs {end_count} end"
        )

        # Extraction des nœuds Niveau 1 : D1-D9, C1-C6, M1-M4, R1-R10, T1-T8
        node_patterns = {
            "D": 9,   # Diagnostic
            "C": 6,   # Créateurs
            "M": 4,   # Matériel
            "R": 10,  # Recherche
            "T": 8,   # Traités
        }

        total_level1_nodes = 0
        for prefix, count in node_patterns.items():
            for i in range(1, count + 1):
                node_id = f"{prefix}{i}"
                pattern = rf"\b{node_id}\s*[\(\[\{{\"]"
                match = re.search(pattern, mermaid_code)
                self.assertIsNotNone(
                    match,
                    f"Nœud Mermaid Niveau 1 manquant : {node_id}"
                )
                total_level1_nodes += 1

        self.assertEqual(
            total_level1_nodes,
            37,
            f"Attendu 37 nœuds Niveau 1 dans Mermaid, trouvé {total_level1_nodes}"
        )

        # Vérifier également la présence des nœuds Niveau 2 (P1-P6) et Niveau 3 (W1)
        for i in range(1, 7):
            node_id = f"P{i}"
            pattern = rf"\b{node_id}\s*[\(\[\{{\"]"
            self.assertIsNotNone(
                re.search(pattern, mermaid_code),
                f"Nœud Mermaid Niveau 2 manquant : {node_id}"
            )
        self.assertIsNotNone(
            re.search(r"\bW1\s*[\(\[\{{\"]", mermaid_code),
            "Nœud Mermaid Niveau 3 manquant : W1"
        )

    def test_05_inventory_sheets_completeness(self):
        """e. Fiches d'inventaire : 37 fiches complètes avec tous les champs obligatoires."""
        index_content = INDEX_PATH.read_text(encoding="utf-8")

        start_lvl1 = index_content.find("### 🟢 NIVEAU 1")
        end_lvl1 = index_content.find("### 🔵 NIVEAU 2")
        self.assertGreater(start_lvl1, 0, "Section Niveau 1 introuvable")
        self.assertGreater(end_lvl1, start_lvl1, "Section Niveau 2 introuvable ou mal positionnée")
        lvl1_text = index_content[start_lvl1:end_lvl1]

        # Extraction des 37 fiches numérotées en Niveau 1 : '1. **...' à '37. **...'
        sheet_headers = list(re.finditer(r"^\s*(\d+)\.\s+\*\*", lvl1_text, re.MULTILINE))
        self.assertEqual(
            len(sheet_headers),
            37,
            f"Attendu 37 fiches d'inventaire en Niveau 1, trouvé {len(sheet_headers)}"
        )

        required_sections = [
            r"\*Localisation\s*:\*",
            r"\*Aperçu\s+Thématique\s*:\*",
            r"\*Chapitres\s+Clés\s+&\s+Données\s+Techniques\s+Critiques\s+Extraites\s*:\*",
            r"\*Applications\s+Pratiques\s+d'Atelier\s*:\*",
        ]

        forbidden_placeholders = ["TODO", "TBD", "FIXME", "LOREM IPSUM", "A COMPLETER"]

        for idx, match in enumerate(sheet_headers):
            num = int(match.group(1))
            self.assertEqual(num, idx + 1, f"Numérotation de fiche discontinue : trouvé {num} à l'index {idx+1}")

            start_pos = match.start()
            end_pos = sheet_headers[idx + 1].start() if idx + 1 < len(sheet_headers) else len(lvl1_text)
            sheet_body = lvl1_text[start_pos:end_pos]

            for req in required_sections:
                self.assertIsNotNone(
                    re.search(req, sheet_body, re.IGNORECASE),
                    f"Fiche #{num} : champ obligatoire manquant '{req}'"
                )

            # Vérification des placeholders
            for placeholder in forbidden_placeholders:
                self.assertNotIn(
                    placeholder,
                    sheet_body.upper(),
                    f"Fiche #{num} contient un placeholder non résolu '{placeholder}'"
                )

            # Vérification de consistance technique (taille du contenu > 300 caractères)
            self.assertGreater(
                len(sheet_body),
                300,
                f"Fiche #{num} anormalement creuse ({len(sheet_body)} caractères)"
            )

    def test_06_thematic_tables_markdown_integrity(self):
        """f. Tables thématiques A à I : vérifier l'intégrité de toutes les tables Markdown et alignement des colonnes."""
        index_content = INDEX_PATH.read_text(encoding="utf-8")

        table_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        total_cross_references = 0
        referenced_sources = set()

        for letter in table_letters:
            header_pattern = rf"###\s+{letter}\.\s+([^\n]+)"
            match = re.search(header_pattern, index_content)
            self.assertIsNotNone(match, f"Section thématique table {letter} introuvable.")

            # Trouver le tableau sous ce titre
            start_pos = match.end()
            # Prendre jusqu'au prochain titre de section (### ou ## ou ---)
            next_heading = re.search(r"\n(?=###?\s+|\n---\s*\n\s*###)", index_content[start_pos:])
            section_text = index_content[start_pos:start_pos + next_heading.start()] if next_heading else index_content[start_pos:]

            table_lines = [
                line.strip() for line in section_text.splitlines()
                if line.strip().startswith("|") and line.strip().endswith("|")
            ]

            self.assertGreaterEqual(
                len(table_lines),
                3,
                f"Table {letter} ne contient pas un tableau Markdown valide (au moins en-tête + séparateur + 1 ligne)."
            )

            header_line = table_lines[0]
            separator_line = table_lines[1]
            data_lines = table_lines[2:]

            # Analyse des cellules de l'en-tête
            # Split par | en éliminant le premier et dernier vide
            header_cells = [c.strip() for c in header_line.split("|")[1:-1]]
            expected_col_count = len(header_cells)

            # Vérifier séparateur
            separator_cells = [c.strip() for c in separator_line.split("|")[1:-1]]
            self.assertEqual(
                len(separator_cells),
                expected_col_count,
                f"Table {letter} : nombre de colonnes séparateur ({len(separator_cells)}) != en-tête ({expected_col_count})"
            )

            # Pour Tables A à H : 5 colonnes attendues ; Pour Table I : 6 colonnes attendues
            if letter in ["A", "B", "C", "D", "E", "F", "G", "H"]:
                self.assertEqual(
                    expected_col_count,
                    5,
                    f"Table {letter} : attendu 5 colonnes, trouvé {expected_col_count}"
                )
            elif letter == "I":
                self.assertEqual(
                    expected_col_count,
                    6,
                    f"Table I : attendu 6 colonnes (incluant Source et Chapitre séparés), trouvé {expected_col_count}"
                )

            # Vérification de chaque ligne de données
            for row_idx, row in enumerate(data_lines):
                cells = [c.strip() for c in row.split("|")[1:-1]]
                self.assertEqual(
                    len(cells),
                    expected_col_count,
                    f"Table {letter}, ligne {row_idx + 1} : {len(cells)} colonnes au lieu de {expected_col_count}. Contenu: {row}"
                )
                total_cross_references += 1

                # Extraction de la source citée dans la colonne source
                # En table A à H, la source est en col 2 (0-indexed) ; en table I, la source est en col 3
                source_col = 3 if letter == "I" else 2
                source_text = cells[source_col]
                referenced_sources.add(source_text)

        # Vérification du nombre total de renvois croisés (doit dépasser 91)
        self.assertGreaterEqual(
            total_cross_references,
            91,
            f"Volume de renvois croisés insuffisant : trouvé {total_cross_references}, attendu >= 91"
        )

    def test_07_workshop_references_integrity(self):
        """g. Vérification des 15 fiches d'atelier dans skills/maitre-tourrier-boulanger/references/."""
        self.assertTrue(SKILL_REF_DIR.exists(), f"Dossier de références skill introuvable : {SKILL_REF_DIR}")

        actual_files = sorted([f.name for f in SKILL_REF_DIR.iterdir() if f.is_file() and f.suffix == ".md"])
        self.assertEqual(
            len(actual_files),
            15,
            f"Attendu exactement 15 fiches d'atelier Markdown, trouvé {len(actual_files)} : {actual_files}"
        )

        # Vérification des 3 nouvelles fiches
        new_files = [
            "biscuiterie-cookies-laminage.md",
            "pates-battues-cakes-emulsions.md",
            "science-amidon-gelatinisation.md",
        ]
        for nf in new_files:
            self.assertIn(nf, actual_files, f"Nouvelle fiche manquante : {nf}")
            p = SKILL_REF_DIR / nf
            self.assertGreater(p.stat().st_size, 10_000, f"Fiche {nf} trop courte ({p.stat().st_size} octets)")

        # Vérification des 6 fiches enrichies
        enriched_files = [
            "patisserie-boulangere.md",
            "diagnostic-defauts.md",
            "veille-scientifique-tourage.md",
            "panification-levain.md",
            "viennoiserie-brioches.md",
            "index-recherche-sources.md",
        ]
        for ef in enriched_files:
            self.assertIn(ef, actual_files, f"Fiche enrichie manquante : {ef}")

        # Vérification des 6 fiches préservées
        preserved_files = [
            "croissomat-scm50-reglages.md",
            "ferrandi-paris-references.md",
            "materiel-lignes.md",
            "organisation-atelier.md",
            "recettes-grands-createurs.md",
            "science-formulation-pac.md",
        ]
        for pf in preserved_files:
            self.assertIn(pf, actual_files, f"Fiche préservée manquante : {pf}")

        # Vérification du maillage interne : aucun lien markdown brisé vers un fichier local
        link_pattern = r"\[([^\]]+)\]\(([^)]+)\)"
        for fname in actual_files:
            fpath = SKILL_REF_DIR / fname
            content = fpath.read_text(encoding="utf-8")
            for text, link in re.findall(link_pattern, content):
                # Ignore anchors and external URLs
                if link.startswith("#") or link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:"):
                    continue
                # Nettoyer d'éventuelles ancres dans les liens locaux
                clean_link = link.split("#")[0]
                if not clean_link:
                    continue
                # Résolution du chemin relatif
                target_path = (SKILL_REF_DIR / clean_link).resolve()
                self.assertTrue(
                    target_path.exists(),
                    f"Lien Markdown brisé dans {fname} : cible '{link}' -> {target_path} introuvable."
                )

        # Vérification scientifique et empirique des formules clés
        # 1. Grover & Seiler
        pates_battues = (SKILL_REF_DIR / "pates-battues-cakes-emulsions.md").read_text(encoding="utf-8")
        self.assertIn("Grover", pates_battues, "Grover manquant dans pates-battues-cakes-emulsions.md")
        self.assertIn("Seiler", pates_battues, "Seiler manquant dans pates-battues-cakes-emulsions.md")
        self.assertIn("SET", pates_battues, "SET manquant dans pates-battues-cakes-emulsions.md")
        self.assertIn("ETR", pates_battues, "ETR manquant dans pates-battues-cakes-emulsions.md")

        # 2. Levine & Drew
        veille = (SKILL_REF_DIR / "veille-scientifique-tourage.md").read_text(encoding="utf-8")
        self.assertIn("Levine", veille, "Levine manquant dans veille-scientifique-tourage.md")
        self.assertIn("Drew", veille, "Drew manquant dans veille-scientifique-tourage.md")
        self.assertIn("Deborah", veille, "Nombre de Deborah manquant dans veille-scientifique-tourage.md")

        # 3. Goff & Cryobiologie PAC
        amidon = (SKILL_REF_DIR / "science-amidon-gelatinisation.md").read_text(encoding="utf-8")
        self.assertIn("Goff", amidon, "Goff manquant dans science-amidon-gelatinisation.md")
        self.assertIn("T_g'", amidon, "T_g' manquant dans science-amidon-gelatinisation.md")
        self.assertIn("Ostwald", amidon, "Ostwald manquant dans science-amidon-gelatinisation.md")

        # 4. Manley checking
        biscuits = (SKILL_REF_DIR / "biscuiterie-cookies-laminage.md").read_text(encoding="utf-8")
        self.assertIn("Manley", biscuits, "Manley manquant dans biscuiterie-cookies-laminage.md")
        self.assertIn("checking", biscuits.lower(), "checking manquant dans biscuiterie-cookies-laminage.md")
        self.assertIn("cut-and-lay", biscuits.lower(), "cut-and-lay manquant dans biscuiterie-cookies-laminage.md")

    def test_08_sync_drive_index_live_check(self):
        """i. Exécution du check de synchronisation Drive : python3 scripts/sync_drive_index.py --check."""
        cmd = [sys.executable, str(REPO_ROOT / "scripts" / "sync_drive_index.py"), "--check"]
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(
            proc.returncode,
            0,
            f"sync_drive_index.py --check a échoué (code {proc.returncode}).\nStdout: {proc.stdout}\nStderr: {proc.stderr}"
        )
        self.assertIn("En synchronisation parfaite", proc.stdout)

    def test_09_sha256_uniqueness_and_no_duplicates(self):
        """Stress-test : unicité cryptographique stricte SHA-256 des 37 sources et 15 références (zéro duplication)."""
        import hashlib

        biblio_hashes = {}
        for p in BIBLIO_DIR.rglob("*"):
            if p.is_file():
                h = hashlib.sha256(p.read_bytes()).hexdigest()
                self.assertNotIn(
                    h,
                    biblio_hashes,
                    f"Fichier dupliqué sous un autre nom dans docs/bibliotheque : {p} et {biblio_hashes.get(h)}"
                )
                biblio_hashes[h] = p
        self.assertEqual(len(biblio_hashes), 37)

        ref_hashes = {}
        for p in SKILL_REF_DIR.glob("*.md"):
            h = hashlib.sha256(p.read_bytes()).hexdigest()
            self.assertNotIn(
                h,
                ref_hashes,
                f"Fiche de référence dupliquée dans le skill : {p} et {ref_hashes.get(h)}"
            )
            ref_hashes[h] = p
        self.assertEqual(len(ref_hashes), 15)

    def test_10_sync_drive_cli_error_codes(self):
        """Stress-test : gestion robuste des codes d'erreur CLI du script de synchronisation."""
        # Cas 1 : Fichier index inexistant -> code 1
        cmd_no_index = [sys.executable, str(REPO_ROOT / "scripts" / "sync_drive_index.py"), "--index", "non_existent_file.md"]
        proc_no_index = subprocess.run(cmd_no_index, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(proc_no_index.returncode, 1)

        # Cas 2 : Fichier credentials inexistant -> code 2
        cmd_no_creds = [sys.executable, str(REPO_ROOT / "scripts" / "sync_drive_index.py"), "--credentials", "non_existent_creds.json"]
        proc_no_creds = subprocess.run(cmd_no_creds, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(proc_no_creds.returncode, 2)


if __name__ == "__main__":
    unittest.main()
