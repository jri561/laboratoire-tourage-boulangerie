# Cahier de Recettes & Protocoles de Fabrication — Laboratoire Tourage & Viennoiserie

## 1. Objectif du Projet
Ce projet standardise et modernise l'ensemble des fiches techniques d'atelier d'une boulangerie-pâtisserie artisanale équipée pour le travail en gros volumes (ligne automatique Rondo Polyline, machine continue Girocrêpes, pétrin spirale 20 bacs / 160–200 kg, dresseuse automatique de cookies, cadres inox de cuisson et cellules de surgélation rapide).

Les fiches sont conçues pour un usage intensif en atelier sous **pochettes plastiques transparentes (classeur / porte-vues d'atelier ouvert à plat)** :
- **Architecture Universelle en Double Page Vis-à-Vis (2 pages A4 portrait par recette — 37 pages au total)** :
  - **Page de Gauche (`1/2 • Poste de Pesée`)** : Uniquement l'en-tête épuré, les 4 repères flash et les tableaux de pesées en **très gros caractères (`15 px à 18 px`)** lisibles à 1,50 m devant la balance.
  - **Page de Droite (`2/2 • Poste Batteur & Four`)** : Marche à suivre pas à pas sur toute la largeur de la page en **gros caractères (`14 px à 16,5 px`, interligne aéré `1.55`)**, réglages machines et barème de cuisson.
- **Ordre Chronologique des Pesées & Codes Couleurs Synchronisés** :
  - Les ingrédients sont classés de haut en bas dans l'ordre exact où l'opérateur les pèse et les verse dans la cuve, avec des pastilles colorées identiques dans le tableau et dans le protocole :
    - **`[1]` Bleu (`#0284c7`)** : Base Cuve / Frasage V1 / Crémage.
    - **`[2]` Ambre (`#d97706`)** : Incorporation 2ᵉ phase (ex. Margarine Opale en V2, Huile de colza en filet, 2ᵉ Eau d'allongement, Liaison Œufs/Sucre).
    - **`[3]` Vert (`#059669`)** : Poudres tamisées ou Beurre de tourage.
    - **`[4]` Violet (`#7c3aed`)** : Inclusions finales (pépites de chocolat, noisettes, noix de pécan).
  - **Code Couleur par Famille de Produits** : Ambre/Cuivre (Viennoiserie & Tourage), Bordeaux/Cacao (Pâtisserie & Biscuiterie), Vert Émeraude (Traiteur & Girocrêpes), Bleu Ardoise (Référentiels).
- **Zéro Waterjet** : Découpe manuelle nette au couteau de tour et réglet inox sur appareils raffermis à froid positif (+4 °C).
- Dimensions utiles des cadres inox 60x40 standard : **56 cm x 36 cm réels**.
- **Ligne de Sel 100 % isolée** : chaque ingrédient critique possède sa propre ligne dédiée pour éliminer tout risque d'erreur de pesée.

---

## 2. Structure du Dossier

```text
/home/toto/Documents/Recette/
├── README.md                                       # Documentation complète et historique technique
├── Cahier_Recettes_Atelier/                        # LIVRABLES OFFICIELS EN PRODUCTION (19 PAGES)
│   ├── Cahier_Recettes_Complet_Labo.pdf            # Recueil complet relié (19 pages avec couverture et sommaire)
│   ├── 00_Couverture.pdf                           # Page de garde officielle atelier
│   ├── 00_Sommaire.pdf                             # Sommaire général et règles d'atelier
│   ├── 01_Crepes_Froment_Girocrepes.pdf            # Fiche Atelier 01 (Émulsion 5 min V5 + allongement 3-4 min V.moyenne)
│   ├── 02_Galettes_Ble_Noir_Girocrepes.pdf         # Fiche Atelier 02 (230 °C / 32 s, eau -5%, allergènes gluten/lactose)
│   ├── 03_Kouign_Amann_Cru_Surgele.pdf             # Fiche Atelier 03 (1 pl. 2kg beurre = 2kg sucre = 5kg détrempe, Pomme & Framboise)
│   ├── 04_Viennoise_Nature_Chocolat_PAC.pdf        # Fiche Atelier 04 (16 et 32 bacs, Kimo Short 2% + Soft'r 1%, Froid Retardé PAC)
│   ├── 05_Feuilletage_Inverse.pdf                  # Fiche Atelier 05 (1 tour simple + 2 tours doubles = 48 feuillets)
│   ├── 06_PLF_Pret_A_Cuire_PAC.pdf                 # Fiche Atelier 06 (Pétrin 20 bacs / 160 kg, pesées arrondies, Opale 400g/bac)
│   ├── 07_Brookie_Cadres_60x40.pdf                 # Fiche Atelier 07 (Cadres 56x36 cm, 30 rect. 11,2x6 cm ~115g, Zéro Chute)
│   ├── 08_Brownie_Fondant_Chocolat.pdf             # Fiche Atelier 08 (Cadres 56x36 cm, 3 000 g, 35 carrés 8x7,2 cm ~85g, Zéro Chute)
│   ├── 09_Muffins_Gamme_Atelier.pdf                # Fiche Atelier 09 (Base huile universelle Classique & Noisette)
│   ├── 10_Frangipane_Gateau_Nantais.pdf            # Fiche Atelier 10 (Pâtissière à froid, frangipane 80/20, rhum 54°)
│   ├── 11_Cookies_Classique_Noisette.pdf           # Fiche Atelier 11 (Pleine Cuve 160 kg, étalement four congelé, Toppings Nutolade/Bueno)
│   ├── 12_Cakes_De_Voyage.pdf                      # Fiche Atelier 12 (Format 3,00 kg net, règle porte fermée 60 min)
│   ├── 13_Quiches_Traiteur.pdf                     # Fiche Atelier 13 (Caisse 48 pièces, sel lardon 4g/kg, légumes surgelés pressés)
│   ├── 14_Dorures_Et_Sirops_Referentiel.pdf        # Fiche Référentiel (Dorure pistolet sel/mucine, sirop 44° Brix)
│   ├── 15_Brioches_Individuelles_Sucre_PAC.pdf     # Fiche Atelier 15 (Bacs 40 pcs = 2,40 kg, diviseuse 20 x 2, coût 1 pièce)
│   ├── 16_Registre_General_Cuissons_Atelier.pdf    # Fiche Référentiel 16 (Programmes Grand Four + T° fixes & temps approx. recuissons)
│   ├── Affiche_Programmes_Ligne_Rondo.pdf          # Fiche 1 page dédiée Ligne Rondo (N° programmes & produits, 10 lignes vierges, sans épaisseurs)
│   ├── Affiche_Cuissons_Apres_Midi.pdf             # Fiche 1 page dédiée Recuissons Après-Midi (Four 165 °C, repères simples 14 min, 11 min, 9 min...)
│   └── Sources_HTML_Modifiables/                   # Fichiers HTML modifiables en 1 clic (Rondo, Cuissons après-midi, fiches)
├── scripts/
│   ├── recipe_data.py                              # Base de données structurée des 17 fiches (15 fiches + 1 annexe + 1 registre cuissons)
│   └── build_cahier.py                             # Moteur de génération HTML -> PDF haute densité & vérification
└── Archive/                                        # HISTORIQUE ANTÉRIEUR CONSOLIDÉ
    ├── Sources_Word/                               # 55 anciens documents de travail .docx
    └── Anciens_PDF/                                # 39 anciens exports PDF (fiches labo et porte-vues v1/v2)
```

---

## 3. Synthèse des Évolutions Techniques d'Atelier

| Fiche | Arbitrages Techniques & Paramètres Validés |
| :--- | :--- |
| **01 • Crêpes Girocrêpes** | Formule traditionnelle pure **sans vanille** (recette validée client 400–600 crêpes/jour). **Huile de colza** en 2ᵉ phase (coût optimisé et émulsion stable qui ne fige/tranche jamais dans l'appareil froid, contrairement au beurre fondu). Cuisson 215 °C / 16 s. Chinois étamine obligatoire. |
| **02 • Galettes Sarrasin** | Cuisson ajustée à **230 °C pendant 32 secondes**. Eau totale réduite de 5 %. Maintien des 6 colonnes (1 à 50 paquets). Alerte sanitaire allergènes (**Contient Gluten & Lactose**). Essai miel programmé en fiche R&D. |
| **03 • Kouign-Amann** | **Individuel 100 g (Roulé, 90 pcs/pâton) & Partage 4/6 pers (Pliage Douarnenez)**. **Détrempe renforcée à 5,00 kg pile / bac** (base `2 750 g` Farine T65 Tradition, `1 450 g` eau froide, `280 g` Opale en V2, `180 g` sucre, `140 g` levure Or, `80 g` lait, `65 g` Kimo Short, `55 g` sel) pour **1 Plaque de 2 kg beurre de tourage + 2 000 g sucre + 20 g Fleur de Sel de Guérande = 9,02 kg le pâton fini**. **2 TOURS SIMPLES**. Déclinaisons Partage à 6 mm : **4 pers = 400 g (20x20 cm)** et **6 pers = 600 g (24x24 cm)**. Cuisson 160 °C (28 à 38 min). **Démoulage & Retournement à froid**. |
| **04 • Viennoise PAC** | **Formule 100 % Harmonisée Nature & Chocolat** : **70 % Gruau T45 / 30 % T65** et **Kimo Short à 2,5 %** sur toutes les colonnes (16 et 32 bacs). Maintien de la Margarine OPALE. Pétrissage V2 commun (7–8 min maigre + 5–6 min Opale) et inclusion pépites froides (45 s max). Procédé Jour Même avec flash froid 25–30 min à -35 °C en bacs pour façonnage froid ferme sans dégradation nocturne. Cycle Double Surgélation (Cru -18 °C $\rightarrow$ Pousse 65-70 % $\rightarrow$ PAC -10 °C). |
| **05 • Feuilletage Inversé** | Tourage corrigé à **1 tour simple + 2 tours doubles (48 feuillets)**. Repos 1 h obligatoire au froid sur plaque avant enfournement pour supprimer tout frettage. Formule d'atelier sans ajout superflu. |
| **06 • PLF PAC (Page Gauche)** | Pétrissée calibrée pour le **pétrin à 20 bacs (160 kg de détrempe + 40 kg de beurre)**. Hydratation à **44,0 %**. **Matière Grasse OPALE (`397 g/bac`)** incorporée au passage en V2 (programme pétrin `[PLF]`). **Dorure Végétale (bidon 1 L)** au pistolet. |
| **06b • Annexe Façonnages Rondo (Page Droite)** | **Annexe officielle en vis-à-vis** détaillant les 6 formes phares sur ligne Rondo Polyline : Croissant (75g), Pain au chocolat (85g), Pain aux raisins (90g), Pain suisse (120g), Oranais abricot (100g), Cinnamon roll (75g). Renvoi à l'**Affiche Murale des Programmes Machines** et barèmes de cuisson PAC direct à 165 °C. |
| **07 • Brookie Cadres (56x36 cm)** | Cadres inox réels 56x36 cm. Format rectangle : **30 parts de 11,2 x 6,0 cm (~115 g brut, ZÉRO CHUTE)**. Appareil Brownie (2 267 g) + **Abaisse Cookie V3 Sandwich 56x36 cm congelée (1 200 g)** laminée à 5,5 mm entre 2 papiers cuisson et piquée au pique-vite (montage en 3 s, zéro casse). Découpe manuelle nette à +4 °C. |
| **08 • Brownie Épais (56x36 cm)** | Format carré généreux et épais (20–22 mm cuit) : **35 carrés de 8,0 x 7,2 cm (~85,7 g brut, ZÉRO CHUTE)**. Masse à **3 000 g net / cadre**. **Ajout extrait de café Trablit (5 g/cadre)** dans les œufs liquides comme exhausteur naturel de cacao sans goût de café. Cuisson 160 °C (22–25 min). |
| **09 • Gamme Muffins (Cœur Apparent)** | Formule base huile colza avec pépites/noisettes dans la masse (165 g) et semées sur le pourtour. Marge de cuve incluse. **Méthode « Puits à Chaud » sans douille à fourrer** : empreinte au pilon rond dès la sortie du four (zéro miette, 1 s/muffin) puis **pochage apparent à froid (20–25 g de Nutolade)** en dôme brillant au sommet. |
| **10 • Frangipane & Nantais** | Frangipane 80/20 liée naturellement par sa farine T55 (600 g). Dérivation Nantais rectifiée avec **Rhum ambré 45 % vol.** Glaçage royal au rhum et trimoline. |
| **11 • Gamme Cookies (80 & 160 kg)** | **Demi-Cuve 80 kg (1 000 pcs) & Pleine Cuve 160 kg (2 000 pcs de 80 g)**. **Formule V3 authentique restaurée** : **68 % Cassonade (`20 kg`) / 32 % Sucre blanc (`9,6 kg`)**, **Poudre à crème (`3,8 kg`)**, **Gros sel (`1,2 kg`)** sablé court sans monter, et équilibre liquide constant (`12,8 kg` œufs sur Classique vs `11,2 kg` œufs + `1,6 kg` vanille sur Noisette). **3 Déclinaisons « Cookies Garnis Gourmet »** (~25 g pochés après cuisson : **1.** Nutolade Puratos + chunks lait, **2.** Style Bueno crème blanche noisette + éclats, **3.** Caramel beurre salé + noix de pécan). |
| **12 • Cakes de Voyage** | Format moule 3,00 kg net (coulage 3,06 kg). Règle d'or de cuisson : porte fermée les 60 premières minutes. Trait d'huile à la corne pour la cheminée. Mix IREKS conservé sans altération. |
| **13 • Quiches Traiteur** | **Légumes IQF (épinards, poireaux) intégrés directement congelés** dans les fonds de tartelettes avant coulage de l'appareil 50/50. Sel réduit à 4 g/kg sur la quiche lardon contre 8 g/kg sur chèvre et poireaux. |
| **14 • Référentiel Dorures** | **Dorure Végétale prête à l'emploi (Bidon 1 L)** en standard au pistolet sur Croissants, Viennoises et Brioches. Conservation sur la fiche de la **Recette Dorure Spéciale Maison** (œufs/jaunes/crème/sucre/sel). Sirop universel à **44° Brix** (800 g sucre / 1 000 g eau). |
| **15 • Brioches au Sucre PAC** | **Bacs de 2,40 kg pour 40 pièces de 60 g** (adapté à la diviseuse 20 parts : 20 pâtons de 120 g recoupés en 2 = 40 brioches) + **Colonne Coût Unitaire « 1 Pièce (60 g) »**. Dorure Végétale (bidon 1 L) et grainage Sucre Grain 10 (6 g/pièce = 240 g/bac) avant enfournement direct congelé. |
| **16 • Registre Général des Cuissons** | **Fiche référentiel maître affichable au poste four** : tableau récapitulatif des 20 fabrications de l'atelier (températures, temps testés labo, réglages d'ouras et buées, et protocoles de finitions sortie de four). |
| **Affiche Murale Programmes Machines** | Affiche dédiée 2 pages A4 ([`Affiche_Murale_Programmes_Machines.pdf`](file:///home/toto/Documents/Recette/Cahier_Recettes_Atelier/Affiche_Murale_Programmes_Machines.pdf)) à plastifier près des pétrins, batteurs, laminoir et ligne Rondo Polyline (grandes cases blanches pour noter/modifier les numéros de programmes au feutre effaçable sans réimprimer le cahier). |
| **Annexe R&D • Fiche d'Essais Labo** | Registre formalisé [`FICHE_ESSAIS_LABO.md`](file:///home/toto/Documents/Recette/FICHE_ESSAIS_LABO.md) pour tester les variantes sans impacter la production (miel galettes, fleur de sel Kouign-Amann, fécule quiches, toppings cookies garnis). |

---

## 4. Commandes d'Exploitation

### Régénérer l'ensemble des fiches et le livret relié
```bash
python3 scripts/build_cahier.py
```

### Modifier une recette
1. Éditer les pesées ou consignes dans [`scripts/recipe_data.py`](file:///home/toto/Documents/Recette/scripts/recipe_data.py).
2. Lancer la compilation : `python3 scripts/build_cahier.py`.
3. Les PDF individuels et le livret complet dans [`Cahier_Recettes_Atelier/`](file:///home/toto/Documents/Recette/Cahier_Recettes_Atelier) sont mis à jour instantanément.
