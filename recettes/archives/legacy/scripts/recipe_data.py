# -*- coding: utf-8 -*-

RECIPES = [
    # -------------------------------------------------------------------------
    # FICHE 01 : CRÊPES DE FROMENT
    # -------------------------------------------------------------------------
    {
        "id": "01_Crepes_Froment_Girocrepes",
        "code": "FICHE ATELIER 01",
        "family": "traiteur",
        "family_label": "TRAITEUR & GIROCRÊPES",
        "title": "Crêpes de Froment (Girocrêpes)",
        "subtitle": "Pâte à crêpes sur machine Girocrêpes — Pesée en 2 temps (1. Frasage → 2. Allongement)",
        "flash": [
            {"lbl": "T° Tambour", "val": "215 °C", "class": "alert"},
            {"lbl": "Temps Passage", "val": "16 Secondes", "class": "amber"},
            {"lbl": "Programme", "val": "Prog. [CRÊPES] (Fouet)", "class": ""},
            {"lbl": "Filtration", "val": "Chinois étamine", "class": "green"},
        ],
        "tables": [
            {
                "headers": ["Ingrédients", "12 Pqts (2kg)", "25 Pqts (4kg)", "37 Pqts (6kg)", "50 Pqts (8kg)", "65 Pqts (10kg)", "75 Pqts (12kg)", "85 Pqts (14kg)", "100 Pqts (16kg)"],
                "align": ["left", "right", "right", "right", "right", "right", "right", "right", "right"],
                "rows": [
                    ["1. Eau (1ʳᵉ partie)", "1 650 g", "2 900 g", "4 550 g", "5 800 g", "7 300 g", "8 750 g", "10 200 g", "11 650 g"],
                    ["1. Œufs entiers liquides", "1 300 g", "2 600 g", "3 900 g", "5 200 g", "6 500 g", "7 800 g", "9 100 g", "10 400 g"],
                    ["1. Sucre semoule", "600 g", "1 200 g", "1 800 g", "2 400 g", "3 000 g", "3 600 g", "4 200 g", "4 800 g"],
                    ["1. Poudre de lait entier", "300 g", "600 g", "900 g", "1 200 g", "1 500 g", "1 800 g", "2 100 g", "2 400 g"],
                    ["1. Sel fin", "30 g", "55 g", "85 g", "110 g", "140 g", "165 g", "195 g", "220 g"],
                    ["1. Farine T55", "2 000 g", "4 000 g", "6 000 g", "8 000 g", "10 000 g", "12 000 g", "14 000 g", "16 000 g"],
                    ["2. Eau (2ᵉ partie)", "1 050 g", "2 100 g", "3 150 g", "4 200 g", "5 250 g", "6 300 g", "7 350 g", "8 400 g"],
                    ["2. Huile de colza", "210 g", "420 g", "630 g", "840 g", "1 050 g", "1 260 g", "1 470 g", "1 680 g"],
                ],
                "total": ["POIDS TOTAL APPAREIL", "7 140 g", "13 875 g", "21 015 g", "27 750 g", "34 740 g", "41 675 g", "48 615 g", "55 550 g"]
            }
        ],
        "col1": {
            "title": "1. Préparation au Batteur (Fouet)",
            "steps": [
                "<strong>Étape 1 • Frasage :</strong> Verser dans la cuve tous les ingrédients <strong>(1)</strong> et lancer le <strong>Programme [CRÊPES] — Phase 1</strong> jusqu'à obtenir une pâte bien lisse et sans grumeaux.",
                "<strong>Étape 2 • Allongement :</strong> Ajouter la seconde partie d'eau et l'huile de colza <strong>(2)</strong> en <strong>Phase 2</strong> pour détendre l'appareil.",
                "<strong>Étape 3 • Filtration :</strong> Passer systématiquement l'appareil au chinois étamine avant de garnir la trémie."
            ]
        },
        "col2": {
            "title": "2. Conduite de la Girocrêpes",
            "steps": [
                "<strong>Réglage du tambour :</strong> Chauffer et réguler le tambour à <strong>215 °C</strong>.",
                "<strong>Temps de cuisson :</strong> Régler la rotation entre <strong>16 et 18 secondes</strong> selon la coloration désirée.",
                "<strong>Conduite en continu :</strong> Utiliser la pâte immédiatement sans temps de repos et maintenir un niveau régulier dans la trémie."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 02 : GALETTES DE BLÉ NOIR
    # -------------------------------------------------------------------------
    {
        "id": "02_Galettes_Ble_Noir_Girocrepes",
        "code": "FICHE ATELIER 02",
        "family": "traiteur",
        "family_label": "TRAITEUR & GIROCRÊPES",
        "title": "Galettes de Blé Noir (Girocrêpes)",
        "subtitle": "Pâte à galettes de sarrasin sur machine Girocrêpes — Pesée en 2 temps (1. Frasage → 2. Allongement)",
        "flash": [
            {"lbl": "T° Tambour", "val": "230 °C", "class": "alert"},
            {"lbl": "Temps Passage", "val": "32 Secondes", "class": "amber"},
            {"lbl": "Programme", "val": "Prog. [GALETTES] (Fouet)", "class": ""},
            {"lbl": "Allergènes", "val": "Gluten & Lait", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["Ingrédients", "1 Paquet", "10 Paquets", "20 Paquets", "30 Paquets", "40 Paquets", "50 Paquets"],
                "align": ["left", "right", "right", "right", "right", "right", "right"],
                "rows": [
                    ["1. Eau (1ʳᵉ partie)", "275 g", "2 750 g", "5 500 g", "8 250 g", "11 000 g", "13 750 g"],
                    ["1. Poudre de lait entier", "25 g", "250 g", "500 g", "750 g", "1 000 g", "1 250 g"],
                    ["1. Sel fin", "7 g", "65 g", "130 g", "195 g", "260 g", "325 g"],
                    ["1. Farine de blé noir", "200 g", "2 000 g", "4 000 g", "6 000 g", "8 000 g", "10 000 g"],
                    ["1. Farine T55", "55 g", "550 g", "1 100 g", "1 650 g", "2 200 g", "2 750 g"],
                    ["1. Œufs entiers liquides", "55 g", "550 g", "1 100 g", "1 650 g", "2 200 g", "2 750 g"],
                    ["2. Eau (2ᵉ partie)", "100 g", "1 000 g", "2 000 g", "3 000 g", "4 000 g", "5 000 g"],
                ],
                "total": ["POIDS TOTAL APPAREIL", "717 g", "7 165 g", "14 330 g", "21 495 g", "28 660 g", "35 825 g"]
            }
        ],
        "col1": {
            "title": "1. Préparation au Batteur (Fouet)",
            "steps": [
                "<strong>Étape 1 • Frasage :</strong> Réunir dans la cuve tous les ingrédients <strong>(1)</strong> et lancer le <strong>Programme [GALETTES] — Phase 1</strong> pour obtenir une base bien lisse.",
                "<strong>Étape 2 • Allongement :</strong> Verser progressivement la seconde partie d'eau <strong>(2)</strong> en <strong>Phase 2</strong> jusqu'à obtenir une fluidité homogène."
            ]
        },
        "col2": {
            "title": "2. Conduite de la Girocrêpes",
            "steps": [
                "<strong>Cuisson sur tambour :</strong> Cuire à <strong>230 °C</strong> pendant <strong>32 secondes</strong> pour bien saisir la galette.",
                "<strong>Suivi de la pâte :</strong> Le blé noir épaissit au repos ; redonner un coup de fouet dans le bac s'il patiente plus de 30 minutes.",
                "<strong>Information allergènes :</strong> Cette recette contient de la farine de froment (gluten) et de la poudre de lait."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 03 : KOUIGN-AMANN CRU SURGELÉ
    # -------------------------------------------------------------------------
    {
        "id": "03_Kouign_Amann_Cru_Surgele",
        "code": "FICHE ATELIER 03",
        "family": "viennoiserie",
        "family_label": "VIENNOISERIE & TOURAGE",
        "title": "Kouign-Amann — Cru Surgelé",
        "subtitle": "Format Individuel (100 g) & Format Partage (4 et 6 personnes) — Détrempe en bacs de 5 kg",
        "flash": [
            {"lbl": "Détrempe / Bac", "val": "5,00 kg pile", "class": "green"},
            {"lbl": "Bloc Beurre Sucré", "val": "2 kg Beurre + 2 kg Sucre + 20g Sel", "class": "amber"},
            {"lbl": "Programme Pétrin", "val": "Prog. [KOUIGN-AMANN]", "class": ""},
            {"lbl": "Cuisson Four", "val": "160 °C • Retourné à froid", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["Ingrédients", "1 Pâton (90p)", "2 Pâtons (180p)", "5 Pâtons (450p)", "10 Pâtons (900p)", "12 Pâtons (1 080p)"],
                "align": ["left", "right", "right", "right", "right", "right"],
                "rows": [
                    ["1. Farine T65 Tradition", "2 750 g", "5 500 g", "13 750 g", "27 500 g", "33 000 g"],
                    ["1. Eau froide (+1 °C)", "1 450 g", "2 900 g", "7 250 g", "14 500 g", "17 400 g"],
                    ["1. Sucre semoule", "180 g", "360 g", "900 g", "1 800 g", "2 160 g"],
                    ["1. Poudre de lait entier", "70 g", "140 g", "350 g", "700 g", "840 g"],
                    ["1. Améliorant Kimo Short", "60 g", "120 g", "300 g", "600 g", "720 g"],
                    ["1. Sel fin", "50 g", "100 g", "250 g", "500 g", "600 g"],
                    ["1. Levure fraîche Or", "140 g", "280 g", "700 g", "1 400 g", "1 680 g"],
                    ["2. Margarine OPALE", "300 g", "600 g", "1 500 g", "3 000 g", "3 600 g"],
                    ["SOUS-TOTAL DÉTREMPE AU BAC", "5 000 g", "10 000 g", "25 000 g", "50 000 g", "60 000 g"],
                    ["3. Beurre de tourage (Plaque 2 kg)", "2 000 g", "4 000 g", "10 000 g", "20 000 g", "24 000 g"],
                    ["3. Sucre semoule (tourage)", "2 000 g", "4 000 g", "10 000 g", "20 000 g", "24 000 g"],
                    ["3. Fleur de sel Guérande", "20 g", "40 g", "100 g", "200 g", "240 g"],
                ],
                "total": ["POIDS TOTAL PÂTON FINI", "9 020 g", "18 040 g", "45 100 g", "90 200 g", "108 240 g"]
            }
        ],
        "col1": {
            "title": "1. Pétrissage, Tourage & Façonnages",
            "steps": [
                "<strong>Étape 1 • Frasage :</strong> Mettre tous les ingrédients <strong>(1)</strong> dans la cuve et lancer le <strong>Programme [KOUIGN-AMANN]</strong>.",
                "<strong>Étape 2 • Incorporation :</strong> Au passage en 2ᵉ vitesse, ajouter la margarine Opale <strong>(2)</strong> jusqu'au décollement de la pâte (sortie entre <strong>18 et 20 °C</strong>). Peser des pâtons de <strong>5,00 kg par bac</strong>, passer 20 min en cellule à -35 °C puis laisser reposer une nuit à +4 °C.",
                "<strong>Étape 3 • Tourage (2 Tours Simples) :</strong> Enfermer le sucre et la fleur de sel <strong>(3)</strong> au cœur de la plaque de beurre de 2 kg. Enchâsser ce bloc dans le pâton de 5 kg et donner <strong>2 tours simples</strong> au laminoir.",
                "<strong>Façonnage Individuel (100 g) :</strong> Abaisser au programme Laminoir, rouler en boudin régulier et détailler des tronçons de <strong>100 g</strong>. Déposer à plat en moule graissé sur un lit de cassonade.",
                "<strong>Façonnage Partage (4 et 6 pers.) :</strong> Abaisser au programme Laminoir, détailler des carrés de <strong>400 g (cercle Ø 20 cm)</strong> ou <strong>600 g (cercle Ø 24 cm)</strong> et rabattre les quatre coins vers le centre sur un fond de cassonade. Surgeler à -35 °C."
            ]
        },
        "col2": {
            "title": "2. Pousse, Cuisson & Retournement",
            "steps": [
                "<strong>Décongélation :</strong> Sortir les pièces la veille et laisser décongeler 10 à 12 h en chambre froide à +4 °C.",
                "<strong>Pousse douce (24 °C max) :</strong> Faire pousser 1 h 30 à 1 h 45 à <strong>24 °C maximum (75–80 % HR)</strong> pour ne pas faire fondre le beurre sucré.",
                "<strong>Mise sous grille :</strong> Poser une grille inox seule sur des cales de 3,5 cm (sans feuille de cuisson) afin de garder un fond bien plat.",
                "<strong>Cuisson à 160 °C :</strong> Compter <strong>28 min</strong> pour l'individuel (100 g), <strong>33 min</strong> pour le 4 parts (400 g) et <strong>37 min</strong> pour le 6 parts (600 g), en ouvrant l'oura sur les dernières minutes.",
                "<strong>Finition retournée :</strong> Laisser figer au froid après cuisson, puis démouler et retourner chaque pièce pour présenter la face caramélisée sur le dessus."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 04 : VIENNOISE NATURE & CHOCOLAT
    # -------------------------------------------------------------------------
    {
        "id": "04_Viennoise_Nature_Chocolat_PAC",
        "code": "FICHE ATELIER 04",
        "family": "viennoiserie",
        "family_label": "VIENNOISERIE & TOURAGE",
        "title": "Viennoise (Nature & Chocolat) — PAC",
        "subtitle": "Pâte viennoise en pétrissées de 16 ou 32 bacs — Processus Prêt-à-Cuire (PAC)",
        "flash": [
            {"lbl": "Programme Pétrin", "val": "Prog. [VIENNOISE]", "class": ""},
            {"lbl": "Calibres", "val": "Nature 285 g / Choc 142 g", "class": "green"},
            {"lbl": "Dorure Pistolet", "val": "Dorure Végétale (1 L)", "class": "amber"},
            {"lbl": "Cycle Froid", "val": "Cru -18°C → Pousse → PAC -10°C", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["Ingrédients", "Nature 16 Bacs", "Nature 32 Bacs", "Choc 16 Bacs", "Choc 32 Bacs"],
                "align": ["left", "right", "right", "right", "right"],
                "rows": [
                    ["1. Farine de Gruau T45", "29 400 g", "58 800 g", "25 500 g", "51 000 g"],
                    ["1. Farine T65 Tradition", "12 600 g", "25 200 g", "11 000 g", "22 000 g"],
                    ["1. Eau froide (+1 °C)", "13 800 g", "27 600 g", "12 000 g", "24 000 g"],
                    ["1. Œufs entiers liquides", "8 000 g", "16 000 g", "7 000 g", "14 000 g"],
                    ["1. Pâte fermentée", "8 400 g", "16 800 g", "7 300 g", "14 600 g"],
                    ["1. Sucre semoule", "5 200 g", "10 400 g", "4 500 g", "9 000 g"],
                    ["1. Trimoline", "1 700 g", "3 400 g", "1 500 g", "3 000 g"],
                    ["1. Poudre de lait entier", "1 250 g", "2 500 g", "1 100 g", "2 200 g"],
                    ["1. Améliorant Kimo Short", "1 050 g", "2 100 g", "900 g", "1 800 g"],
                    ["1. Améliorant Soft'r", "400 g", "800 g", "350 g", "700 g"],
                    ["1. Sel fin", "850 g", "1 700 g", "750 g", "1 500 g"],
                    ["1. Extrait de vanille", "100 g", "200 g", "100 g", "200 g"],
                    ["1. Levure fraîche Or", "1 900 g", "3 800 g", "1 650 g", "3 300 g"],
                    ["2. Margarine OPALE", "8 000 g", "16 000 g", "7 000 g", "14 000 g"],
                    ["3. Pépites chocolat noir (+4 °C)", "—", "—", "11 800 g", "23 600 g"],
                ],
                "total": ["POIDS TOTAL DE PÂTE", "92 650 g", "185 300 g", "92 450 g", "184 900 g"]
            }
        ],
        "col1": {
            "title": "1. Pétrissage & Refroidissement en Bacs",
            "steps": [
                "<strong>Étape 1 • Frasage & Réseau :</strong> Verser tous les ingrédients <strong>(1)</strong> dans la cuve et lancer le <strong>Programme [VIENNOISE]</strong> pour construire le réseau de gluten.",
                "<strong>Étape 2 • Incorporation :</strong> Au signal en 2ᵉ vitesse, ajouter la margarine Opale froide <strong>(2)</strong> en morceaux jusqu'au décollement complet (sortie entre <strong>19 et 21 °C</strong>).",
                "<strong>Étape 3 • Pépites de chocolat :</strong> Pour la version chocolat, incorporer les pépites bien froides <strong>(3)</strong> en 1ʳᵉ vitesse sur la fin du cycle.",
                "<strong>Refroidissement en bacs :</strong> Diviser en bacs d'environ <strong>5,80 kg</strong> et passer 25 à 30 min en cellule à -35 °C pour raffermir la pâte avant façonnage."
            ]
        },
        "col2": {
            "title": "2. Façonnage, Dorure Végétale & Cuisson PAC",
            "steps": [
                "<strong>Division & Façonnage :</strong> Passer le bac froid à la diviseuse 20 parts : façonner directement les pièces Nature (285 g), ou recouper chaque pâton en deux pour les Chocolat (142 g).",
                "<strong>1er Dorage & Surgélation Cru :</strong> Pulvériser la <strong>Dorure Végétale</strong>, rayer les pièces, puis surgeler à -35 °C avant stockage à -18 °C.",
                "<strong>Décongélation & Pousse :</strong> Après décongélation à +4 °C, pousser à 26–27 °C (80 % HR) et stopper la pousse aux deux tiers du développement (<strong>65 à 70 % du volume</strong>).",
                "<strong>2ᵉ Dorage & Blocage PAC :</strong> Appliquer un léger voile de <strong>Dorure Végétale</strong>, saisir en cellule jusqu'à <strong>-10 °C à cœur (sonde)</strong> et conserver sous housse à -18 °C.",
                "<strong>Cuisson directe congelé (165 °C) :</strong> Cuire sans décongélation préalable pendant <strong>9 min</strong> pour la Chocolat et <strong>11 min</strong> pour la Nature."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 05 : FEUILLETAGE INVERSÉ
    # -------------------------------------------------------------------------
    {
        "id": "05_Feuilletage_Inverse",
        "code": "FICHE ATELIER 05",
        "family": "viennoiserie",
        "family_label": "VIENNOISERIE & TOURAGE",
        "title": "Feuilletage Inversé",
        "subtitle": "Tourage 1 Tour Simple + 2 Tours Doubles (48 feuillets) — Beurre Manié & Détrempe",
        "flash": [
            {"lbl": "Pâton Fini", "val": "7,13 kg / pâton", "class": ""},
            {"lbl": "Tourage", "val": "1 Simple + 2 Doubles", "class": "amber"},
            {"lbl": "Programme", "val": "Prog. Laminoir", "class": "green"},
            {"lbl": "Repos Plaque", "val": "1 h à +4 °C avant four", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["Ingrédients", "Rôle", "1 Pâton (7,13 kg)", "4 Pâtons (28,5 kg)"],
                "align": ["left", "left", "right", "right"],
                "rows": [
                    ["1. Beurre sec de tourage", "Tempéré 14–16 °C", "2 500 g", "10 000 g"],
                    ["1. Farine T55", "Frasée à la feuille", "750 g", "3 000 g"],
                    ["SOUS-TOTAL 1 • BEURRE MANIÉ (EXTÉRIEUR)", "Cadrer et refroidir", "3 250 g", "13 000 g"],
                    ["2. Eau froide (+2 °C)", "Base détrempe", "1 300 g", "5 200 g"],
                    ["2. Sel fin", "Dissoudre dans l'eau", "65 g", "260 g"],
                    ["2. Vinaigre blanc", "Dissoudre dans l'eau", "20 g", "80 g"],
                    ["2. Farine T55 ou T65", "Fraser sans corser", "2 500 g", "10 000 g"],
                    ["SOUS-TOTAL 2 • DÉTREMPE (INTÉRIEUR)", "Cadrer et refroidir", "3 885 g", "15 540 g"],
                ],
                "total": ["POIDS TOTAL PÂTON FINI", "Beurre Manié + Détrempe", "7 135 g", "28 540 g"]
            }
        ],
        "col1": {
            "title": "1. Préparation & Tourage (J-1)",
            "steps": [
                "<strong>Bloc 1 • Beurre manié (extérieur) :</strong> Mélanger le beurre de tourage et la farine <strong>(1)</strong> à la feuille juste le temps d'homogénéiser l'ensemble sans chauffer la matière. Cadrer en rectangle et réserver au froid à +4 °C.",
                "<strong>Bloc 2 • Détrempe (intérieur) :</strong> Dissoudre le sel et le vinaigre dans l'eau bien froide, verser sur la farine <strong>(2)</strong> et fraser brièvement au crochet sans donner de corps. Cadrer et refroidir à +4 °C.",
                "<strong>1er Cycle de tourage :</strong> Enfermer la détrempe froide au centre du beurre manié. Donner <strong>1 tour simple</strong> suivi immédiatement d'<strong>1 tour double</strong>.",
                "<strong>2ᵉ Cycle & Repos :</strong> Laisser reposer 2 h au froid (+4 °C), donner le <strong>second tour double</strong>, puis filmer au contact et laisser reposer toute la nuit à +4 °C."
            ]
        },
        "col2": {
            "title": "2. Abaisse & Cuisson",
            "steps": [
                "<strong>Abaisse & Détaillage :</strong> Abaisser progressivement au programme Laminoir sans brusquer le pâton, puis détailler les pièces (galettes, mille-feuilles, fonds de tartes).",
                "<strong>Repos sur plaque :</strong> Laisser reposer les pièces détaillées au moins <strong>1 heure au froid (+4 °C)</strong> avant d'enfourner pour éviter toute rétractation.",
                "<strong>Cuisson (170 à 175 °C) :</strong> Cuire pendant <strong>25 à 30 minutes</strong>, oura fermé au départ puis ouvert en fin de cuisson pour bien sécher le feuilletage."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 06 : PLF PRÊT-À-CUIRE (PAC) - 20 BACS
    # -------------------------------------------------------------------------
    {
        "id": "06_PLF_Pret_A_Cuire_PAC",
        "code": "FICHE ATELIER 06",
        "family": "viennoiserie",
        "family_label": "VIENNOISERIE & TOURAGE",
        "title": "PLF (Croissants & Pains au Chocolat) — PAC",
        "subtitle": "Pâte Levée Feuilletée en bacs de 8 kg — Processus Prêt-à-Cuire (PAC)",
        "flash": [
            {"lbl": "Détrempe / Bac", "val": "8,00 kg pile / bac", "class": "green"},
            {"lbl": "Programme Pétrin", "val": "Prog. [PLF] (18–20 °C)", "class": "amber"},
            {"lbl": "Dorure Pistolet", "val": "Dorure Végétale (1 L)", "class": ""},
            {"lbl": "Cuisson PAC", "val": "160–165 °C direct congelé", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["Ingrédients", "1 Bac (8,0 kg)", "10 Bacs (80 kg)", "20 Bacs (160 kg)"],
                "align": ["left", "right", "right", "right"],
                "rows": [
                    ["1. Farine de Gruau T45", "4 400 g", "44 000 g", "88 000 g"],
                    ["1. Eau froide (+1 °C)", "1 950 g", "19 500 g", "39 000 g"],
                    ["1. Sucre semoule", "400 g", "4 000 g", "8 000 g"],
                    ["1. Poudre de lait entier", "180 g", "1 800 g", "3 600 g"],
                    ["1. Trimoline", "160 g", "1 600 g", "3 200 g"],
                    ["1. Améliorant Kimo Short", "130 g", "1 300 g", "2 600 g"],
                    ["1. Sel fin", "90 g", "900 g", "1 800 g"],
                    ["1. Vinaigre blanc", "40 g", "400 g", "800 g"],
                    ["1. Levure fraîche Or", "250 g", "2 500 g", "5 000 g"],
                    ["2. Margarine OPALE", "400 g", "4 000 g", "8 000 g"],
                    ["SOUS-TOTAL DÉTREMPE AU BAC", "8 000 g", "80 000 g", "160 000 g"],
                    ["3. Beurre de tourage (Plaque 2 kg)", "2 000 g", "20 000 g", "40 000 g"],
                ],
                "total": ["POIDS TOTAL PÂTON TOURÉ", "10 000 g", "100 000 g", "200 000 g"]
            }
        ],
        "col1": {
            "title": "1. Pétrissage & Pointage Retardé (J-1)",
            "steps": [
                "<strong>Étape 1 • Frasage :</strong> Réunir dans la cuve tous les ingrédients <strong>(1)</strong> et lancer le <strong>Programme [PLF]</strong>.",
                "<strong>Étape 2 • Incorporation :</strong> Au passage en 2ᵉ vitesse, ajouter la margarine Opale <strong>(2)</strong> et laisser pétrir jusqu'au décollement complet du bassin (sortie entre <strong>18 et 20 °C</strong>).",
                "<strong>Mise en bacs :</strong> Peser des pâtons de <strong>8,00 kg par bac</strong>, passer 30 min en cellule à -35 °C puis laisser pointer 12 à 15 h en chambre froide (+2 à +4 °C)."
            ]
        },
        "col2": {
            "title": "2. Tourage, Dorure Végétale & Cuisson PAC",
            "steps": [
                "<strong>Étape 3 • Tourage (2 Tours Doubles) :</strong> Enchâsser la plaque de beurre de 2 kg <strong>(3)</strong> dans le pâton de 8 kg et donner <strong>2 tours doubles</strong> au laminoir. Laisser détendre 1 h au froid avant façonnage sur la ligne Rondo.",
                "<strong>Façonnage & 1ʳᵉ Surgélation :</strong> Détailler et façonner les pièces sur la ligne Rondo, puis surgeler à -35 °C et stocker à -18 °C.",
                "<strong>Pousse & Blocage PAC :</strong> Pousser à 26–27 °C (80 % HR) jusqu'à <strong>70 à 75 % du volume final</strong>. Raffermir 15 min à +4 °C, pulvériser la <strong>Dorure Végétale</strong>, bloquer en cellule à <strong>-10 °C à cœur (sonde)</strong> et housser à -18 °C.",
                "<strong>Cuisson directe congelé (165 °C) :</strong> Enfourner sans décongélation au programme Grand Four (ou environ <strong>14 min à 165 °C</strong> pour une recuisson d'après-midi)."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 07 : BROOKIE (CADRES 56x36 cm)
    # -------------------------------------------------------------------------
    {
        "id": "07_Brookie_Cadres_60x40",
        "code": "FICHE ATELIER 07",
        "family": "patisserie",
        "family_label": "PÂTISSERIE & BISCUITERIE",
        "title": "Brookie (Cadres 56x36 cm)",
        "subtitle": "Base Brownie + Abaisse Cookie en cadres 56x36 cm — Découpe en 30 rectangles",
        "flash": [
            {"lbl": "Cadre Inox", "val": "56 x 36 cm sur Silpat", "class": ""},
            {"lbl": "Poids / Cadre", "val": "3 460 g (2 260g + 1 200g)", "class": "amber"},
            {"lbl": "Découpe", "val": "30 parts (11,2 x 6 cm)", "class": "green"},
            {"lbl": "Cuisson Four", "val": "160–165 °C (24 à 26 min)", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["Partie A • Appareil Brownie", "1 Cadre", "10 Cadres", "15 Cadres"],
                "align": ["left", "right", "right", "right"],
                "rows": [
                    ["1. Chocolat noir 55 %", "450 g", "4 500 g", "6 750 g"],
                    ["1. Huile de colza", "450 g", "4 500 g", "6 750 g"],
                    ["2. Œufs entiers liquides", "500 g", "5 000 g", "7 500 g"],
                    ["2. Sucre semoule", "600 g", "6 000 g", "9 000 g"],
                    ["3. Farine T55", "180 g", "1 800 g", "2 700 g"],
                    ["3. Cacao en poudre 100 %", "70 g", "700 g", "1 050 g"],
                    ["3. Sel fin", "5 g", "50 g", "75 g"],
                    ["3. Levure chimique", "5 g", "50 g", "75 g"],
                ],
                "total": ["TOTAL A • BROWNIE", "2 260 g", "22 600 g", "33 900 g"]
            },
            {
                "headers": ["Partie B • Abaisse Cookie", "1 Cadre", "10 Cadres", "15 Cadres"],
                "align": ["left", "right", "right", "right"],
                "rows": [
                    ["1. Margarine OPALE", "220 g", "2 200 g", "3 300 g"],
                    ["1. Sucre Cassonade", "150 g", "1 500 g", "2 250 g"],
                    ["1. Sucre semoule", "70 g", "700 g", "1 050 g"],
                    ["1. Gros sel", "10 g", "100 g", "150 g"],
                    ["2. Œufs entiers liquides", "100 g", "1 000 g", "1 500 g"],
                    ["3. Farine T55", "330 g", "3 300 g", "4 950 g"],
                    ["3. Poudre à crème", "30 g", "300 g", "450 g"],
                    ["3. Levure chimique", "10 g", "100 g", "150 g"],
                    ["4. Pépites chocolat noir", "280 g", "2 800 g", "4 200 g"],
                ],
                "total": ["TOTAL B • COOKIE (TOTAL A+B)", "1 200 g (3 460g)", "12 000 g (34,6kg)", "18 000 g (51,9kg)"]
            }
        ],
        "col1": {
            "title": "1. Fabrication & Montage en Cadres",
            "steps": [
                "<strong>Partie A • Appareil Brownie :</strong> <strong>1)</strong> Faire fondre le chocolat et y émulsionner l'huile de colza. <strong>2)</strong> Lier les œufs et le sucre à la feuille en 1ʳᵉ vitesse sans blanchir, puis verser le mélange chocolat-huile. <strong>3)</strong> Incorporer les poudres tamisées. Couler <strong>2 260 g par cadre</strong> et figer 10 min au froid.",
                "<strong>Partie B • Abaisse Cookie :</strong> <strong>1)</strong> Sabler la margarine Opale avec les sucres et le gros sel sans monter l'appareil. <strong>2)</strong> Ajouter les œufs en 1ʳᵉ vitesse. <strong>3)</strong> Fraser brièvement avec les poudres. <strong>4)</strong> Incorporer les pépites de chocolat. Étaler des pâtons de <strong>1 200 g</strong> au programme Laminoir entre deux feuilles au format du cadre (56x36 cm), piquer et surgeler.",
                "<strong>Assemblage :</strong> Déposer directement la plaque de cookie congelée sur la base brownie avant d'enfourner."
            ]
        },
        "col2": {
            "title": "2. Cuisson & Découpe (30 parts)",
            "steps": [
                "<strong>Cuisson (160–165 °C) :</strong> Cuire pendant <strong>24 à 26 minutes</strong> (18 min oura fermé, puis 6 à 8 min oura ouvert pour dorer le dessus du cookie).",
                "<strong>Décadrage & Refroidissement :</strong> Laisser tiédir 10 min, passer une lame fine le long du cadre pour décadrer à chaud, puis raffermir <strong>1 heure à +4 °C</strong>.",
                "<strong>Découpe (30 parts) :</strong> Au grand couteau chaud et réglet inox, détailler 5 bandes dans la longueur (11,2 cm) par 6 bandes dans la largeur (6,0 cm) pour obtenir <strong>30 rectangles réguliers</strong>."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 08 : BROWNIE FONDANT CHOCOLAT
    # -------------------------------------------------------------------------
    {
        "id": "08_Brownie_Fondant_Chocolat",
        "code": "FICHE ATELIER 08",
        "family": "patisserie",
        "family_label": "PÂTISSERIE & BISCUITERIE",
        "title": "Brownie Fondant Chocolat (Cadres 56x36 cm)",
        "subtitle": "Appareil Brownie en cadres 56x36 cm — Découpe en 35 carrés épais",
        "flash": [
            {"lbl": "Programme", "val": "Prog. [BROWNIE] (Feuille)", "class": ""},
            {"lbl": "Poids / Cadre", "val": "3 000 g (+400 g Pécan)", "class": "amber"},
            {"lbl": "Découpe", "val": "35 carrés 8x7,2 cm (85g)", "class": "green"},
            {"lbl": "Cuisson Four", "val": "160 °C (22 à 25 min)", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["Ingrédients", "1 Cadre (3,0 kg)", "10 Cadres (30 kg)", "15 Cadres (45 kg)"],
                "align": ["left", "right", "right", "right"],
                "rows": [
                    ["1. Chocolat noir 55 %", "600 g", "6 000 g", "9 000 g"],
                    ["1. Huile de colza", "600 g", "6 000 g", "9 000 g"],
                    ["2. Œufs entiers liquides", "660 g", "6 600 g", "9 900 g"],
                    ["2. Extrait de café Trablit", "5 g", "50 g", "75 g"],
                    ["2. Sucre semoule", "800 g", "8 000 g", "12 000 g"],
                    ["3. Farine T55", "235 g", "2 350 g", "3 525 g"],
                    ["3. Cacao en poudre 100 %", "90 g", "900 g", "1 350 g"],
                    ["3. Sel fin", "5 g", "50 g", "75 g"],
                    ["3. Levure chimique", "5 g", "50 g", "75 g"],
                    ["SOUS-TOTAL BROWNIE NATURE", "3 000 g", "30 000 g", "45 000 g"],
                    ["4. Option : Noix de pécan", "+ 400 g", "+ 4 000 g", "+ 6 000 g"],
                ],
                "total": ["POIDS TOTAL (NATURE / PÉCAN)", "3,0 kg / 3,4 kg", "30 kg / 34 kg", "45 kg / 51 kg"]
            }
        ],
        "col1": {
            "title": "1. Fabrication au Batteur (Feuille)",
            "steps": [
                "<strong>Étape 1 • Fonte :</strong> Faire fondre le chocolat noir entre 45 et 50 °C, puis incorporer l'huile de colza au fouet pour obtenir une émulsion lisse.",
                "<strong>Étape 2 • Liaison :</strong> Réunir les œufs, l'extrait de café et le sucre <strong>(2)</strong> dans la cuve. Lancer le <strong>Programme [BROWNIE]</strong> à la feuille en 1ʳᵉ vitesse sans incorporer d'air, puis verser le mélange chocolat-huile.",
                "<strong>Étape 3 • Poudres :</strong> Ajouter la farine, le cacao, le sel et la levure tamisés <strong>(3)</strong> et mélanger juste le temps de lisser l'appareil.",
                "<strong>Étape 4 • Coulage :</strong> Couler <strong>3 000 g d'appareil par cadre</strong> sur toile Silpat, et parsemer les noix de pécan <strong>(4)</strong> en surface pour la version Pécan."
            ]
        },
        "col2": {
            "title": "2. Cuisson & Découpe (35 carrés)",
            "steps": [
                "<strong>Cuisson (160 °C) :</strong> Cuire pendant <strong>22 à 25 minutes</strong> oura fermé : le dessus doit former une fine croûte satinée tout en gardant un cœur fondant.",
                "<strong>Décadrage & Refroidissement :</strong> Décadrer à chaud 10 min après la sortie du four, puis passer <strong>1 heure en chambre froide à +4 °C</strong> pour figer le cœur avant la coupe.",
                "<strong>Découpe (35 carrés) :</strong> Au couteau chaud et réglet inox, couper 7 bandes dans la longueur (8,0 cm) par 5 bandes dans la largeur (7,2 cm) pour obtenir <strong>35 carrés sans chute</strong>."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 09 : GAMME MUFFINS ATELIER
    # -------------------------------------------------------------------------
    {
        "id": "09_Muffins_Gamme_Atelier",
        "code": "FICHE ATELIER 09",
        "family": "patisserie",
        "family_label": "PÂTISSERIE & BISCUITERIE",
        "title": "Gamme Muffins Atelier (120 g)",
        "subtitle": "Moulage en plaques de 24 moules — Puits formé à chaud & Cœur pâte à tartiner apparent",
        "flash": [
            {"lbl": "Calibre Cru", "val": "120 g / moule (24/pl.)", "class": ""},
            {"lbl": "Programme", "val": "Prog. [MUFFINS] (Feuille)", "class": "amber"},
            {"lbl": "Finition", "val": "Puits à chaud + Nutolade 20g", "class": "green"},
            {"lbl": "Cuisson Four", "val": "165 °C (22 min)", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["1. Muffins Chocolat", "1 Plaque (24 p.)", "5 Plaques (120 p.)", "10 Plaques (240 p.)", "15 Plaques (360 p.)"],
                "align": ["left", "right", "right", "right", "right"],
                "rows": [
                    ["1. Œufs entiers liquides", "400 g", "1 800 g", "3 550 g", "5 350 g"],
                    ["1. Sucre semoule", "480 g", "2 150 g", "4 300 g", "6 450 g"],
                    ["1. Sel fin", "15 g", "70 g", "135 g", "200 g"],
                    ["2. Eau tempérée", "700 g", "3 150 g", "6 200 g", "9 350 g"],
                    ["2. Huile de colza", "500 g", "2 250 g", "4 450 g", "6 700 g"],
                    ["3. Farine T55", "1 040 g", "4 700 g", "9 250 g", "13 950 g"],
                    ["3. Poudre de lait entier", "100 g", "450 g", "900 g", "1 350 g"],
                    ["3. Levure chimique", "55 g", "250 g", "500 g", "750 g"],
                    ["4. Pépites chocolat noir", "160 g", "750 g", "1 500 g", "2 200 g"],
                    ["SOUS-TOTAL PÂTE CUVE", "3 450 g", "15 570 g", "30 785 g", "46 300 g"],
                    ["4. Fourrage Nutolade apparent (~20g/pce)", "+ 500 g", "+ 2 500 g", "+ 5 000 g", "+ 7 500 g"],
                ],
                "total": ["TOTAL AVEC FOURRAGE", "3 950 g", "18 070 g", "35 785 g", "53 800 g"]
            },
            {
                "headers": ["2. Muffins Noisette", "1 Plaque (24 p.)", "5 Plaques (120 p.)", "10 Plaques (240 p.)", "15 Plaques (360 p.)"],
                "align": ["left", "right", "right", "right", "right"],
                "rows": [
                    ["1. Œufs entiers liquides", "400 g", "1 800 g", "3 550 g", "5 350 g"],
                    ["1. Sucre semoule", "480 g", "2 150 g", "4 300 g", "6 450 g"],
                    ["1. Sel fin", "15 g", "70 g", "135 g", "200 g"],
                    ["2. Eau tempérée", "700 g", "3 150 g", "6 200 g", "9 350 g"],
                    ["2. Huile de colza", "500 g", "2 250 g", "4 450 g", "6 700 g"],
                    ["3. Farine T55", "780 g", "3 500 g", "6 950 g", "10 450 g"],
                    ["3. Poudre de noisettes", "260 g", "1 200 g", "2 300 g", "3 500 g"],
                    ["3. Poudre de lait entier", "100 g", "450 g", "900 g", "1 350 g"],
                    ["3. Levure chimique", "55 g", "250 g", "500 g", "750 g"],
                    ["4. Noisettes concassées", "160 g", "750 g", "1 500 g", "2 200 g"],
                    ["4. Fourrage apparent (~20g/pce)", "+ 500 g", "+ 2 500 g", "+ 5 000 g", "+ 7 500 g"],
                ],
                "total": ["TOTAL AVEC FOURRAGE", "3 950 g", "18 070 g", "35 785 g", "53 800 g"]
            }
        ],
        "col1": {
            "title": "1. Fabrication au Batteur (Feuille)",
            "steps": [
                "<strong>Étape 1 • Blanchiment :</strong> Mettre les œufs, le sucre et le sel <strong>(1)</strong> dans la cuve et lancer le <strong>Programme [MUFFINS] — Phase 1</strong> pour blanchir légèrement le mélange.",
                "<strong>Étape 2 • Liquides :</strong> Verser l'eau tempérée et l'huile de colza <strong>(2)</strong> en 1ʳᵉ vitesse jusqu'à obtenir une émulsion homogène.",
                "<strong>Étape 3 • Poudres :</strong> Incorporer en une fois toutes les poudres tamisées <strong>(3)</strong> et arrêter le batteur dès que la pâte est lisse.",
                "<strong>Étape 4 • Dressage :</strong> Pocher <strong>120 g de pâte par moule</strong> et parsemer le dessus de pépites de chocolat ou d'éclats de noisettes <strong>(4)</strong>."
            ]
        },
        "col2": {
            "title": "2. Cuisson & Garnissage Apparent",
            "steps": [
                "<strong>Cuisson (165 °C) :</strong> Cuire pendant <strong>22 minutes</strong> oura fermé.",
                "<strong>Empreinte à chaud :</strong> Dès la sortie du four, tant que la mie est chaude et souple, enfoncer un petit pilon rond au centre de chaque muffin pour creuser un puits net sans faire de miettes.",
                "<strong>Garnissage apparent :</strong> Une fois les muffins refroidis, pocher environ <strong>20 g de pâte à tartiner</strong> dans chaque puits en formant un beau dôme apparent sur le dessus.",
                "<strong>Conservation :</strong> Ranger en caisses doublées d'une housse plastique et surgeler à -18 °C."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 10 : FRANGIPANE & GÂTEAU NANTAIS
    # -------------------------------------------------------------------------
    {
        "id": "10_Frangipane_Gateau_Nantais",
        "code": "FICHE ATELIER 10",
        "family": "patisserie",
        "family_label": "PÂTISSERIE & BISCUITERIE",
        "title": "Frangipane & Gâteau Nantais",
        "subtitle": "1. Frangipane 80/20 • 2. Appareil Gâteau Nantais au Rhum • 3. Glaçage Royal",
        "flash": [
            {"lbl": "Programme", "val": "Prog. [FRANGIPANE] (Feuille)", "class": ""},
            {"lbl": "Ratio Base", "val": "80 % Amande / 20 % Pâtiss.", "class": "amber"},
            {"lbl": "Calibres Nantais", "val": "Indiv 100 g / Grand 450 g", "class": "green"},
            {"lbl": "Glaçage", "val": "Sur gâteaux froids", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["1. Crème Pâtissière & Frangipane", "Lot Standard", "Double Lot", "Consigne"],
                "align": ["left", "right", "right", "left"],
                "rows": [
                    ["1. Eau froide", "1 500 g", "3 000 g", "Fouetter avec la poudre"],
                    ["1. Poudre pâtissière à froid", "600 g", "1 200 g", "Laisser épaissir 5 min"],
                    ["SOUS-TOTAL 1 • CRÈME PÂTISSIÈRE", "2 100 g", "4 200 g", "Ajoutée en fin de mélange"],
                    ["2. Beurre pommade", "2 000 g", "4 000 g", "Crémer avec le sucre"],
                    ["2. Sucre semoule", "2 000 g", "4 000 g", "Sans chauffer"],
                    ["3. Œufs entiers liquides", "1 600 g", "3 200 g", "En filet en V1"],
                    ["3. Poudre d'amande blanche", "2 000 g", "4 000 g", "Incorporer en V1"],
                    ["3. Farine T55", "600 g", "1 200 g", "Incorporer en V1"],
                ],
                "total": ["TOTAL FRANGIPANE FINIE", "10 300 g", "20 600 g", "Mélanger pâtissière + amande"]
            },
            {
                "headers": ["2. Appareil Gâteau Nantais", "Petit Lot", "Grand Lot", "Consigne"],
                "align": ["left", "right", "right", "left"],
                "rows": [
                    ["1. Frangipane finie (Tableau 1)", "1 000 g", "10 300 g", "À la feuille en V1"],
                    ["1. Levure chimique", "10 g", "100 g", "Mélanger à la frangipane"],
                    ["2. Rhum ambré 45°", "120 g", "1 250 g", "Verser en filet en V1"],
                ],
                "total": ["TOTAL GÂTEAU NANTAIS", "1 130 g", "11 650 g", "Indiv. 100 g / 4 pers. 450 g"]
            },
            {
                "headers": ["3. Glaçage Royal au Rhum", "Petit Lot", "Grand Lot (x4)", "Consigne"],
                "align": ["left", "right", "right", "left"],
                "rows": [
                    ["1. Gélatine (feuilles)", "4 g (2 f.)", "16 g (8 f.)", "Ramollir à l'eau froide"],
                    ["2. Rhum ambré 45°", "80 g", "320 g", "Tiédir à 50 °C avec trimoline"],
                    ["2. Trimoline", "50 g", "200 g", "Y fondre la gélatine"],
                    ["3. Sucre glace tamisé", "500 g", "2 000 g", "Lisser sans bulles"],
                ],
                "total": ["TOTAL GLAÇAGE ROYAL", "634 g", "2 536 g", "Glacer à la palette à froid"]
            }
        ],
        "col1": {
            "title": "1. Frangipane & Gâteau Nantais",
            "steps": [
                "<strong>Étape 1 • Crème pâtissière :</strong> Fouetter vivement l'eau froide et la poudre à crème <strong>(1)</strong>, puis laisser épaissir 5 minutes.",
                "<strong>Étapes 2 & 3 • Crème d'amande :</strong> Lancer le <strong>Programme [FRANGIPANE]</strong> à la feuille : crémer le beurre pommade et le sucre <strong>(2)</strong> sans chauffer, verser les œufs en filet, puis incorporer la poudre d'amande et la farine <strong>(3)</strong> en 1ʳᵉ vitesse.",
                "<strong>Étape 4 • Frangipane :</strong> Incorporer la crème pâtissière réservée en fin de mélange pour obtenir une frangipane bien lisse.",
                "<strong>Gâteau Nantais (Tableau 2) :</strong> Détendre la frangipane avec la levure chimique et le rhum ambré en 1ʳᵉ vitesse. Cuire à <strong>165 °C</strong> : compter <strong>25 à 30 min</strong> en individuel (100 g) et <strong>40 à 45 min</strong> en format partage (450 g)."
            ]
        },
        "col2": {
            "title": "2. Glaçage Royal au Rhum",
            "steps": [
                "<strong>Préparation du glaçage (Tableau 3) :</strong> Faire ramollir la gélatine dans l'eau froide, puis la dissoudre dans le rhum et la trimoline tiédis à 50 °C.",
                "<strong>Mise au point :</strong> Verser ce liquide tiède sur le sucre glace tamisé et mélanger doucement au fouet sans incorporer de bulles d'air.",
                "<strong>Finition :</strong> Étaler une fine couche régulière de glaçage à la palette sur les gâteaux complètement refroidis."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 11 : GAMME COOKIES (80 KG & 160 KG — FORMULE V3)
    # -------------------------------------------------------------------------
    {
        "id": "11_Cookies_80g_Fourres",
        "code": "FICHE ATELIER 11",
        "family": "patisserie",
        "family_label": "PÂTISSERIE & BISCUITERIE",
        "title": "Gamme Cookies (80 kg & 160 kg)",
        "subtitle": "Demi-Cuve (80 kg) & Pleine Cuve (160 kg) — Classique, Noisette & Déclinaisons Gourmet",
        "flash": [
            {"lbl": "Programme", "val": "Prog. [COOKIES] (Feuille)", "class": ""},
            {"lbl": "Calibre", "val": "80 g aplati", "class": "amber"},
            {"lbl": "Cuisson PAC", "val": "165 °C (13 à 14 min)", "class": "green"},
            {"lbl": "Ouras Four", "val": "Ouverts en continu", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["Ingrédients", "Classique 80 kg (1 000p)", "Classique 160 kg (2 000p)", "Noisette 80 kg (1 000p)", "Noisette 160 kg (2 000p)"],
                "align": ["left", "right", "right", "right", "right"],
                "rows": [
                    ["1. Margarine OPALE", "14 500 g", "29 000 g", "14 500 g", "29 000 g"],
                    ["1. Sucre Cassonade", "10 000 g", "20 000 g", "10 000 g", "20 000 g"],
                    ["1. Sucre semoule", "4 800 g", "9 600 g", "4 800 g", "9 600 g"],
                    ["1. Gros sel", "600 g", "1 200 g", "600 g", "1 200 g"],
                    ["2. Œufs entiers liquides", "6 400 g", "12 800 g", "5 600 g", "11 200 g"],
                    ["2. Extrait de vanille liquide", "250 g", "500 g", "800 g", "1 600 g"],
                    ["3. Farine T55", "22 000 g", "44 000 g", "21 800 g", "43 600 g"],
                    ["3. Poudre à crème", "1 900 g", "3 800 g", "1 900 g", "3 800 g"],
                    ["3. Cacao en poudre 100 %", "—", "—", "300 g", "600 g"],
                    ["3. Levure chimique", "700 g", "1 400 g", "700 g", "1 400 g"],
                    ["4. Pépites chocolat noir", "19 100 g", "38 200 g", "14 100 g", "28 200 g"],
                    ["4. Noisettes hachées torréfiées", "—", "—", "5 000 g", "10 000 g"],
                ],
                "total": ["TOTAL MASSE CUVE", "80 250 g", "160 500 g", "80 100 g", "160 200 g"]
            }
        ],
        "col1": {
            "title": "1. Fabrication au Batteur (Feuille)",
            "steps": [
                "<strong>Étape 1 • Sablage court :</strong> Mettre la margarine Opale, les sucres et le gros sel <strong>(1)</strong> dans la cuve. Lancer le <strong>Programme [COOKIES]</strong> pour lisser la matière sans jamais la foisonner.",
                "<strong>Étape 2 • Liquides :</strong> Incorporer les œufs et l'arôme vanille <strong>(2)</strong> en 1ʳᵉ vitesse.",
                "<strong>Étape 3 • Poudres :</strong> Ajouter l'ensemble des poudres tamisées <strong>(3)</strong> et fraser très brièvement en 1ʳᵉ vitesse sans corser la pâte.",
                "<strong>Étape 4 • Garniture :</strong> Verser les pépites de chocolat et les noisettes torréfiées <strong>(4)</strong> sur les derniers tours de cuve juste pour bien les répartir."
            ]
        },
        "col2": {
            "title": "2. Dressage, Cuisson & Garnis Gourmet",
            "steps": [
                "<strong>Dressage & Surgélation :</strong> Dresser des pièces de <strong>80 g</strong> sur plaques, aplatir légèrement les dômes à l'aide d'une plaque propre, puis surgeler et stocker en caisses houssées à -18 °C.",
                "<strong>Cuisson directe congelé (165 °C) :</strong> Enfourner sans décongélation pendant <strong>13 à 14 minutes, ouras ouverts en continu</strong>. Sortir les plaques dès que le pourtour est doré et que le cœur est encore souple.",
                "<strong>Déclinaison 1 • Choco-Noisette :</strong> Sur cookie refroidi, pocher une rosace de <strong>pâte à tartiner Nutolade</strong> et parsemer de chunks au chocolat au lait.",
                "<strong>Déclinaison 2 • Style Bueno :</strong> Sur cookie Noisette refroidi, pocher une rosace de <strong>fourrage noisette blanche</strong> et décorer d'éclats de noisettes torréfiées.",
                "<strong>Déclinaison 3 • Caramel Pécan :</strong> Sur cookie Classique refroidi, pocher une rosace de <strong>caramel au beurre salé</strong> et parsemer de noix de pécan."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 12 : CAKES DE VOYAGE (GRAND FORMAT 3 KG)
    # -------------------------------------------------------------------------
    {
        "id": "12_Cakes_De_Voyage",
        "code": "FICHE ATELIER 12",
        "family": "patisserie",
        "family_label": "PÂTISSERIE & BISCUITERIE",
        "title": "Cakes de Voyage (Format 3 kg)",
        "subtitle": "Citron-Pavot, Fruits Confits & Marbré 50/50 — Moules grand format de 3 kg",
        "flash": [
            {"lbl": "Poids Moule", "val": "3 060 g cru (3,0 kg cuit)", "class": ""},
            {"lbl": "Programme", "val": "Prog. [CAKES] (Feuille)", "class": "amber"},
            {"lbl": "Cuisson Four", "val": "155 °C (75 min)", "class": "green"},
            {"lbl": "Règle Four", "val": "Porte fermée 60 min", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["1. Cakes Citron-Pavot & Fruits Confits", "Citron (10 C.)", "Citron (15 C.)", "Fruits (10 C.)", "Fruits (15 C.)"],
                "align": ["left", "right", "right", "right", "right"],
                "rows": [
                    ["1. Mix IREKS (Citron / Golden)", "16 000 g", "24 000 g", "12 350 g", "18 500 g"],
                    ["1. Œufs entiers liquides", "5 600 g", "8 400 g", "5 900 g", "8 850 g"],
                    ["1. Huile végétale neutre", "4 800 g", "7 200 g", "4 950 g", "7 400 g"],
                    ["1. Eau tempérée", "3 600 g", "5 400 g", "2 450 g", "3 700 g"],
                    ["2. Pavot bleu / Fruits confits", "600 g", "900 g", "4 950 g", "7 450 g"],
                ],
                "total": ["POIDS TOTAL (3,06 KG / MOULE)", "30 600 g", "45 900 g", "30 600 g", "45 900 g"]
            },
            {
                "headers": ["2. Cake Marbré 50/50 (1 Pâte Golden + 1 Pâte Choc)", "Par Pâte (10 C.)", "Total (10 C.)", "Par Pâte (15 C.)", "Total (15 C.)"],
                "align": ["left", "right", "right", "right", "right"],
                "rows": [
                    ["1. Mix Mella Golden OU Mella Choc", "7 350 g", "14 700 g", "11 000 g", "22 000 g"],
                    ["1. Huile végétale neutre", "3 550 g", "7 100 g", "5 350 g", "10 700 g"],
                    ["1. Œufs entiers liquides", "2 950 g", "5 900 g", "4 400 g", "8 800 g"],
                    ["1. Eau tempérée", "1 450 g", "2 900 g", "2 200 g", "4 400 g"],
                ],
                "total": ["TOTAL MARBRÉ (1,53 KG x 2 / MOULE)", "15 300 g", "30 600 g", "22 950 g", "45 900 g"]
            }
        ],
        "col1": {
            "title": "1. Fabrication au Batteur (Feuille)",
            "steps": [
                "<strong>Étape 1 • Mélange :</strong> Réunir tous les ingrédients <strong>(1)</strong> dans la cuve et lancer le <strong>Programme [CAKES]</strong> à la feuille jusqu'à obtenir un appareil lisse et brillant.",
                "<strong>Étape 2 • Garniture :</strong> Incorporer le pavot bleu ou les fruits confits <strong>(2)</strong> en 1ʳᵉ vitesse sur la fin du cycle.",
                "<strong>Version Marbré 50/50 (Tableau 2) :</strong> Préparer séparément une cuve de pâte nature (Golden) et une cuve de pâte chocolat (Choc)."
            ]
        },
        "col2": {
            "title": "2. Moulage & Cuisson",
            "steps": [
                "<strong>Moulage :</strong> Peser <strong>3 060 g d'appareil par moule</strong> (pour le Marbré, alterner quatre couches de 765 g en croisant les deux pâtes).",
                "<strong>Cheminée :</strong> Fendre le dessus du cake sur toute sa longueur avec une corne trempée dans l'huile pour guider le développement au four.",
                "<strong>Cuisson (155 °C — 75 min) :</strong> Cuire pendant 1 h 15 à 155 °C en gardant la <strong>porte du four strictement fermée durant les 60 premières minutes</strong>. Démouler 10 min après la sortie du four."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 13 : GAMME QUICHES TRAITEUR
    # -------------------------------------------------------------------------
    {
        "id": "13_Quiches_Traiteur",
        "code": "FICHE ATELIER 13",
        "family": "traiteur",
        "family_label": "TRAITEUR & GIROCRÊPES",
        "title": "Gamme Quiches Traiteur (48 pcs / Caisse)",
        "subtitle": "Chèvre-Épinard, Lardon & Poireaux — Garnissage direct avec légumes surgelés",
        "flash": [
            {"lbl": "Légumes", "val": "Mis congelés directement", "class": "green"},
            {"lbl": "Appareil", "val": "50 % Œufs / 50 % Crème 35%", "class": "amber"},
            {"lbl": "Sel", "val": "Lardon 4g/kg • Autres 8g/kg", "class": ""},
            {"lbl": "Cuisson Four", "val": "170 °C (30 à 35 min)", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["1. Quiche Chèvre-Épinard (150 g)", "Par Pièce", "10 Caisses (480p)", "20 Caisses (960p)", "30 Caisses (1 440p)"],
                "align": ["left", "right", "right", "right", "right"],
                "rows": [
                    ["1. Œufs entiers liquides", "45 g", "21,6 kg", "43,2 kg", "64,8 kg"],
                    ["1. Crème liquide 35 % MG", "45 g", "21,6 kg", "43,2 kg", "64,8 kg"],
                    ["1. Sel fin (8 g/kg)", "0,7 g", "350 g", "700 g", "1 050 g"],
                    ["1. Poivre moulu", "0,15 g", "65 g", "130 g", "195 g"],
                    ["1. Noix de muscade", "0,05 g", "20 g", "40 g", "60 g"],
                    ["SOUS-TOTAL 1 • APPAREIL LIQUIDE", "90 g", "43,2 kg", "86,4 kg", "129,6 kg"],
                    ["2. Épinards congelés", "40 g", "19,2 kg", "38,4 kg", "57,6 kg"],
                    ["2. Chèvre en rondelles / dés", "20 g", "9,6 kg", "19,2 kg", "28,8 kg"],
                ],
                "total": ["TOTAL CHÈVRE-ÉPINARD", "150 g", "72,0 kg", "144,0 kg", "216,0 kg"]
            },
            {
                "headers": ["2. Quiche Lardon (140 g) & 3. Quiche Poireaux (160 g)", "Lardon (Pce)", "Lardon (10 C.)", "Poireaux (Pce)", "Poireaux (10 C.)", "Poireaux (20 C.)"],
                "align": ["left", "right", "right", "right", "right", "right"],
                "rows": [
                    ["1. Œufs entiers liquides", "50 g", "24,0 kg", "50 g", "24,0 kg", "48,0 kg"],
                    ["1. Crème liquide 35 % MG", "50 g", "24,0 kg", "50 g", "24,0 kg", "48,0 kg"],
                    ["1. Sel fin (4 g/kg ou 8 g/kg)", "0,4 g", "190 g", "0,8 g", "380 g", "760 g"],
                    ["1. Poivre moulu", "0,2 g", "100 g", "0,15 g", "70 g", "140 g"],
                    ["1. Noix de muscade", "0,05 g", "25 g", "0,05 g", "25 g", "50 g"],
                    ["SOUS-TOTAL 1 • APPAREIL LIQUIDE", "100 g", "48,0 kg", "100 g", "48,0 kg", "96,0 kg"],
                    ["2. Lardons crus / Poireaux congelés", "30 g", "14,4 kg", "50 g", "24,0 kg", "48,0 kg"],
                    ["2. Emmental râpé", "10 g", "4,8 kg", "10 g", "4,8 kg", "9,6 kg"],
                ],
                "total": ["TOTAL LARDON / POIREAUX", "140 g", "67,2 kg", "160 g", "76,8 kg", "153,6 kg"]
            }
        ],
        "col1": {
            "title": "1. Appareil & Garnissage Direct Congelé",
            "steps": [
                "<strong>Étape 1 • Appareil à quiche :</strong> Fouetter ensemble les œufs entiers, la crème liquide, le sel, le poivre et la noix de muscade <strong>(1)</strong> jusqu'à homogénéité.",
                "<strong>Étape 2 • Garnissage des fonds :</strong> Répartir les légumes <strong>directement congelés</strong> (ou les lardons crus) ainsi que le fromage <strong>(2)</strong> au fond des tartelettes.",
                "<strong>Coulage :</strong> Verser l'appareil liquide <strong>(1)</strong> par-dessus la garniture jusqu'au bord du moule."
            ]
        },
        "col2": {
            "title": "2. Cuisson & Conditionnement",
            "steps": [
                "<strong>Cuisson (170 °C) :</strong> Cuire au four ventilé pendant <strong>30 à 35 minutes</strong> oura fermé, jusqu'à obtenir une belle coloration dorée et une tenue ferme à cœur.",
                "<strong>Ressuage :</strong> Démouler tiède et laisser refroidir sur grille pour préserver le croustillant du fond avant la mise en caisses de 48 pièces."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 14 : RÉFÉRENTIEL DORURES & SIROPS
    # -------------------------------------------------------------------------
    {
        "id": "14_Dorures_Et_Sirops_Referentiel",
        "code": "FICHE RÉFÉRENTIEL 14",
        "family": "referentiel",
        "family_label": "RÉFÉRENTIEL TECHNIQUE",
        "title": "Référentiel : Dorures & Sirops",
        "subtitle": "Dorure Végétale prête à l'emploi, Recette de Dorure Spéciale, Dorure Pinceau & Sirop 44° Brix",
        "flash": [
            {"lbl": "Croissants / Viennoises", "val": "Dorure Végétale (Bidon 1 L)", "class": "green"},
            {"lbl": "Dorure Spéciale", "val": "Recette Maison Pistolet", "class": ""},
            {"lbl": "Dorure Feuilletage", "val": "Pinceau (Jaunes + Crème)", "class": "amber"},
            {"lbl": "Sirop Lustrage", "val": "44° Brix (1 kg eau + 800g sucre)", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["1. Dorure Pistolet (Végétale & Recette Spéciale)", "Base 1 L", "Base 3 L", "Affectation"],
                "align": ["left", "right", "right", "left"],
                "rows": [
                    ["STANDARD • Dorure Végétale (Bidon 1 L)", "1 000 g", "3 000 g", "Croissants, Pains choco, Viennoises, Brioches"],
                    ["1. Œufs entiers liquides", "300 g", "900 g", "Recette Dorure Spéciale"],
                    ["1. Jaunes d'œufs liquides", "300 g", "900 g", "Recette Dorure Spéciale"],
                    ["1. Crème liquide 35 % MG", "300 g", "900 g", "Recette Dorure Spéciale"],
                    ["1. Sucre semoule", "20 g", "60 g", "Recette Dorure Spéciale"],
                    ["1. Sel fin", "10 g", "30 g", "Recette Dorure Spéciale"],
                ],
                "total": ["TOTAL DORURE SPÉCIALE", "930 g", "2 790 g", "Mixer, chinoiser et stocker à +4 °C"]
            },
            {
                "headers": ["2. Dorure Feuilletage (Pinceau)", "Base 1 L", "Base 2 L", "Affectation"],
                "align": ["left", "right", "right", "left"],
                "rows": [
                    ["1. Jaunes d'œufs liquides", "670 g", "1 340 g", "Galettes, Feuilletage inversé"],
                    ["1. Crème liquide 35 % MG", "330 g", "660 g", "Galettes, Feuilletage inversé"],
                ],
                "total": ["TOTAL DORURE PINCEAU", "1 000 g", "2 000 g", "2 couches fines (15 min à +4 °C entre les 2)"]
            },
            {
                "headers": ["3. Sirop de Lustrage (44° Brix)", "Petit Lot", "Grand Lot", "Affectation"],
                "align": ["left", "right", "right", "left"],
                "rows": [
                    ["1. Eau", "1 000 g", "3 000 g", "Porter à ébullition avec le sucre"],
                    ["1. Sucre semoule", "800 g", "2 400 g", "Refroidir avant usage"],
                ],
                "total": ["TOTAL SIROP 44° BRIX", "1 800 g", "5 400 g", "Froid sur Pains aux raisins et Oranais chauds"]
            }
        ],
        "col1": {
            "title": "1. Préparation & Application des Dorures",
            "steps": [
                "<strong>Dorure Végétale (Bidon 1 L) :</strong> S'utilise pure au pistolet sur l'ensemble des croissants, pains au chocolat, viennoises et petites brioches.",
                "<strong>Dorure Spéciale Maison (Tableau 1) :</strong> Mixer soigneusement les cinq ingrédients et passer au chinois étamine avant de remplir le pistolet.",
                "<strong>Dorure Feuilletage (Tableau 2) :</strong> Mélanger les jaunes et la crème sans faire mousser. Passer deux couches fines au pinceau en laissant figer 15 min au froid entre les deux."
            ]
        },
        "col2": {
            "title": "2. Sirop de Lustrage & Hygiène",
            "steps": [
                "<strong>Sirop de lustrage 44° Brix (Tableau 3) :</strong> Porter l'eau et le sucre à franche ébullition pendant 1 minute, puis laisser refroidir complètement avant d'en lustrer les viennoiseries chaudes.",
                "<strong>Hygiène & Conservation :</strong> Conserver toutes les dorures filmées et datées en chambre froide à <strong>+4 °C</strong>, et rincer le pistolet à l'eau chaude après chaque utilisation."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 15 : PETITES BRIOCHES AU SUCRE
    # -------------------------------------------------------------------------
    {
        "id": "15_Brioches_Individuelles_Sucre_PAC",
        "code": "FICHE ATELIER 15",
        "family": "viennoiserie",
        "family_label": "VIENNOISERIE & TOURAGE",
        "title": "Petites Brioches au Sucre — PAC",
        "subtitle": "Bacs de 2,40 kg (40 pièces = Diviseuse 20 parts recoupées en 2) — Processus Prêt-à-Cuire",
        "flash": [
            {"lbl": "Pesée / Bac", "val": "2 400 g = 40 pcs (Div.20 x 2)", "class": "green"},
            {"lbl": "Programme Pétrin", "val": "Prog. [BRIOCHE]", "class": "amber"},
            {"lbl": "Dorure Pistolet", "val": "Dorure Végétale (1 L)", "class": ""},
            {"lbl": "Cuisson PAC", "val": "165 °C (11 à 13 min, ouras)", "class": "alert"},
        ],
        "tables": [
            {
                "headers": ["Ingrédients", "1 Pièce (Coût)", "1 Bac (40 pcs)", "5 Bacs (200 pcs)", "10 Bacs (400 pcs)", "25 Bacs (1 000 pcs)", "50 Bacs (2 000 pcs)"],
                "align": ["left", "right", "right", "right", "right", "right", "right"],
                "rows": [
                    ["1. Farine de Gruau T45", "30 g", "1 200 g", "6 000 g", "12 000 g", "30 000 g", "60 000 g"],
                    ["1. Eau froide (+1 °C)", "8,25 g", "330 g", "1 650 g", "3 300 g", "8 250 g", "16 500 g"],
                    ["1. Œufs entiers liquides", "7,5 g", "300 g", "1 500 g", "3 000 g", "7 500 g", "15 000 g"],
                    ["1. Sucre semoule", "4,25 g", "170 g", "850 g", "1 700 g", "4 250 g", "8 500 g"],
                    ["1. Poudre de lait entier", "1,25 g", "50 g", "250 g", "500 g", "1 250 g", "2 500 g"],
                    ["1. Trimoline", "0,75 g", "30 g", "150 g", "300 g", "750 g", "1 500 g"],
                    ["1. Améliorant Kimo Short", "0,6 g", "25 g", "125 g", "250 g", "625 g", "1 250 g"],
                    ["1. Améliorant Soft'r", "0,25 g", "10 g", "50 g", "100 g", "250 g", "500 g"],
                    ["1. Sel fin", "0,6 g", "25 g", "125 g", "250 g", "625 g", "1 250 g"],
                    ["1. Levure fraîche Or", "1,5 g", "60 g", "300 g", "600 g", "1 500 g", "3 000 g"],
                    ["2. Huile de colza", "5,0 g", "200 g", "1 000 g", "2 000 g", "5 000 g", "10 000 g"],
                    ["SOUS-TOTAL PÂTE AU BAC", "60 g", "2 400 g", "12 000 g", "24 000 g", "60 000 g", "120 000 g"],
                    ["3. Sucre Grain 10 (avant four)", "+ 6 g", "+ 240 g", "+ 1 200 g", "+ 2 400 g", "+ 6 000 g", "+ 12 000 g"],
                ],
                "total": ["TOTAL AVEC SUCRE GRAIN", "66 g", "2 640 g", "13 200 g", "26 400 g", "66 000 g", "132 000 g"]
            }
        ],
        "col1": {
            "title": "1. Pétrissage & Mise en Bacs",
            "steps": [
                "<strong>Étape 1 • Frasage & Réseau :</strong> Mettre tous les ingrédients <strong>(1)</strong> dans la cuve et lancer le <strong>Programme [BRIOCHE]</strong> pour bien développer le réseau de gluten.",
                "<strong>Étape 2 • Incorporation de l'huile :</strong> En 2ᵉ vitesse, verser l'huile de colza <strong>(2)</strong> en filet continu jusqu'à absorption complète et décollement de la pâte (sortie entre <strong>22 et 24 °C</strong>).",
                "<strong>Mise en bacs :</strong> Peser des pâtons de <strong>2 400 g par bac</strong> (40 pièces), laisser pointer 20 min à température ambiante puis raffermir 30 min au froid à +4 °C."
            ]
        },
        "col2": {
            "title": "2. Division (20 x 2), Pousse & Cuisson PAC",
            "steps": [
                "<strong>Division & Boulage (40 pcs / bac) :</strong> Diviser le bac de 2,40 kg avec la diviseuse 20 parts, recouper chaque pâton en deux pour obtenir <strong>40 pièces de 60 g</strong>, puis bouler et disposer par 24 sur plaque.",
                "<strong>Pousse :</strong> Mettre en pousse à 26–27 °C (80 % HR) et arrêter aux trois quarts du développement (<strong>70 à 75 % du volume</strong>).",
                "<strong>Blocage PAC :</strong> Passer 10 min à +4 °C, pulvériser la <strong>Dorure Végétale</strong>, saisir en cellule jusqu'à <strong>-10 °C à cœur (sonde)</strong> puis stocker sous housse à -18 °C.",
                "<strong>Grainage & Cuisson directe congelé (165 °C) :</strong> Juste avant d'enfourner les pièces congelées, humidifier d'un voile de <strong>Dorure Végétale</strong> et parsemer le <strong>sucre Grain 10 (3)</strong>. Cuire <strong>11 à 13 min à 165 °C, ouras ouverts</strong>."
            ]
        }
    },

    # -------------------------------------------------------------------------
    # FICHE 16 : REGISTRE GÉNÉRAL DES CUISSONS D'ATELIER
    # -------------------------------------------------------------------------
    {
        "id": "16_Registre_General_Cuissons_Atelier",
        "code": "RÉFÉRENTIEL CUISSONS 16",
        "family": "referentiel",
        "family_label": "RÉFÉRENTIEL TECHNIQUE",
        "title": "Registre Général des Barèmes de Cuisson",
        "subtitle": "Grand Four Ventilé (Programmes) & Repères Recuissons Après-Midi (Températures fixes & Temps approximatifs)",
        "flash": [
            {"lbl": "Grand Four Ventilé", "val": "Lancer Programme Produit", "class": "green"},
            {"lbl": "Recuissons Après-Midi", "val": "T° fixe + Temps approx. (~)", "class": "amber"},
            {"lbl": "Préchauffage PAC", "val": "+15 °C au-dessus consigne", "class": "alert"},
            {"lbl": "Lustrage", "val": "Sirop 44° froid sur chaud", "class": ""},
        ],
        "tables": [
            {
                "headers": ["1. Viennoiserie & Pâtes Tourées", "Support", "Départ", "T° Fixe", "Temps Approx.", "Ouras", "Finition"],
                "align": ["left", "left", "center", "center", "center", "left", "left"],
                "rows": [
                    ["Croissant (75 g)", "Plaque Silpat", "Congelé PAC", "165 °C", "~ 14 min", "Ouvrir fin", "Dorure végétale"],
                    ["Pain au Chocolat (85 g)", "Plaque Silpat", "Congelé PAC", "165 °C", "~ 14 min", "Ouvrir fin", "Dorure végétale"],
                    ["Viennoise Nature (285 g)", "Plaque Silpat", "Congelé PAC", "165 °C", "~ 11 min", "Fermé", "Dorure végétale"],
                    ["Viennoise Choc (142 g)", "Plaque Silpat", "Congelé PAC", "165 °C", "~ 9 min", "Fermé", "Dorure végétale"],
                    ["Chausson aux Pommes", "Plaque Silpat", "Congelé / Frais", "165 °C", "~ 30 min", "Ouvrir fin", "Sirop / Dorure"],
                    ["Croissant aux Amandes", "Plaque Silpat", "Garni amande", "165 °C", "~ 30 min", "Fermé", "Sucre glace froid"],
                    ["Kouign-Amann (Décong. four)", "Plaque", "Sortie congél.", "165 °C", "~ 4 min", "Fermé", "Remise en T° rapide"],
                    ["Kouign-Amann (Cuisson crue)", "Moule / Cercle", "Pousse 24 °C", "160 °C", "~ 28–37 min", "Ouvrir fin", "Retourné à froid"],
                    ["Brioche au Sucre (60 g)", "Plaque (24 pcs)", "Congelé PAC", "165 °C", "~ 11–13 min", "Ouverts continu", "Dorure vég. + Grain 10"],
                    ["Raisins / Suisse / Oranais", "Plaque Silpat", "Congelé PAC", "165 °C", "~ 15–17 min", "Ouvrir fin", "Sirop 44° (Rais./Oran.)"],
                    ["Feuilletage Inversé", "Plaque Silpat", "Repos 1h +4°C", "170–175 °C", "~ 25–30 min", "Ouvrir fin", "Dorure pinceau"],
                ],
                "total": ["CUISSON PAC", "Zéro décongélation", "-10 °C cœur", "T° Fixe", "Temps indicatif", "Sécher vapeur", "Ressuage grille"]
            },
            {
                "headers": ["2. Pâtisserie, Biscuiterie & Traiteur", "Support", "Départ", "T° Fixe", "Temps Approx.", "Ouras", "Finition"],
                "align": ["left", "left", "center", "center", "center", "left", "left"],
                "rows": [
                    ["Brookie (3 460 g)", "Cadre 56x36", "Frais (+4 °C)", "160–165 °C", "~ 24–26 min", "Ouvrir à 18 min", "Découpe +4 °C (30 p.)"],
                    ["Brownie (3 000 g)", "Cadre 56x36", "Frais coulé", "160 °C", "~ 22–25 min", "Fermé", "Découpe +4 °C (35 p.)"],
                    ["Cookies (80 g)", "Plaque Silpat", "Congelé PAC", "165 °C", "~ 13–14 min", "Ouverts continu", "Garnis Gourmet à froid"],
                    ["Muffins (120 g)", "Plaque 24 m.", "Frais poché", "165 °C", "~ 22 min", "Fermé", "Puits chaud + Nutolade"],
                    ["Cakes (3 060 g)", "Moule 3 kg", "Frais coulé", "155 °C", "~ 75 min", "Fermé 60 min", "Cheminée à l'huile"],
                    ["Gâteau Nantais", "Moule métal", "Frais poché", "165 °C", "~ 25–30 / 40–45m", "Fermé", "Glaçage rhum à froid"],
                    ["Quiches (140–160 g)", "Tartelette", "Légumes cong.", "170 °C", "~ 30–35 min", "Fermé", "Ressuage grille"],
                    ["Crêpes Froment", "Girocrêpes", "Chinoisé", "215 °C", "16 secondes", "Continu", "Sans repos"],
                    ["Galettes Blé Noir", "Girocrêpes", "Appareil lisse", "230 °C", "32 secondes", "Continu", "Coup de fouet / 30 min"],
                ],
                "total": ["RECUISSONS", "Température fixe", "Temps approx.", "Ventilé", "Surveiller œil", "Vérifier tirage", "Ressuage grille"]
            }
        ],
        "col1": {
            "title": "1. Grand Four Ventilé & Recuissons d'Après-Midi",
            "steps": [
                "<strong>Fournées sur le grand four ventilé :</strong> Sélectionner directement le <strong>programme de cuisson</strong> correspondant au produit.",
                "<strong>Recuissons de l'après-midi (petites quantités) :</strong> Respecter la <strong>température fixe</strong> du tableau. Les temps de cuisson sont donnés <strong>à titre approximatif (~)</strong> car quelques plaques cuisent plus rapidement qu'un chariot complet : toujours contrôler la coloration à l'œil.",
                "<strong>Préchauffage & Ouras :</strong> Monter le four 15 °C au-dessus de la consigne avant d'enfourner les pièces congelées, et ouvrir l'oura en fin de cuisson pour évacuer l'humidité."
            ]
        },
        "col2": {
            "title": "2. Gestes en Sortie de Four",
            "steps": [
                "<strong>Muffins :</strong> Former le puits central au pilon dès la sortie du four, tant que le cœur est bien chaud.",
                "<strong>Kouign-Amann :</strong> Laisser figer au froid avant de démouler et de retourner les pièces sur grille.",
                "<strong>Cadres Brownie & Brookie :</strong> Décadrer à chaud 10 min après sortie du four, puis raffermir 1 h à +4 °C avant de détailler au couteau."
            ]
        }
    }
]
