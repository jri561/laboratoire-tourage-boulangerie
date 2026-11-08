# Laboratoire R&D : Tourage, Viennoiserie & Boulangerie d'Excellence

Ce projet centralise l'ingénierie des formulations, le catalogue des fiches techniques d'atelier et les référentiels scientifiques pour la production artisanale et semi-industrielle mécanisée.

---

## 1. Structure du Projet

```
laboratoire-tourage-boulangerie/
├── INDEX_RECETTES.md              # Tableau de bord général des produits et statuts
├── README.md                      # Guide d'exploitation du projet
├── recettes/
│   ├── catalogue/                 # Fiches techniques validées en production
│   │   ├── croissant-pac-excellence.md
│   │   ├── brioche-fine-nanterre.md
│   │   └── baguette-tradition-autolyse.md
│   ├── essais/                    # Formulations en cours de test au labo
│   └── archives/                  # Anciennes versions et recettes historiques
├── scripts/
│   └── calculateur_fournee.py     # Calcul automatique des pesées et balance eau/glace
└── skills/
    └── maitre-tourrier-boulanger/ # Le cerveau expert embarqué avec le projet
        ├── SKILL.md               # Directives de formulation et de posture
        └── references/            # Les 8 guides d'expertise scientifique et atelier
            ├── veille-scientifique-tourage.md
            ├── science-formulation-pac.md
            ├── viennoiserie-brioches.md
            ├── panification-levain.md
            ├── patisserie-boulangere.md
            ├── materiel-lignes.md
            ├── diagnostic-defauts.md
            └── organisation-atelier.md
```

---

## 2. Exploitation Rapide

### Calculer une fournée selon la météo
Pour obtenir les pesées exactes au gramme près et savoir s'il faut ajouter de la glace paillette :

```bash
# Exemple pour 10 bacs de PLF PAC avec une température de labo à 26 °C :
python3 scripts/calculateur_fournee.py --bacs 10 --t-piece 26.0 --t-farine 22.0
```

---

## 3. Gestion des Versions (Recipe-as-Code avec Git)

Chaque modification de paramètre ou ajustement de formule fait l'objet d'un commit documenté :
* `git status` : Voir les recettes modifiées.
* `git add recettes/` : Préparer les fiches à sauvegarder.
* `git commit -m "Ajustement : réduction levure à 4.0% suite à essai étuve"` : Enregistrer la version.

---

## 4. Portabilité & Sauvegarde Cloud

Le dossier `skills/maitre-tourrier-boulanger/` est inclus directement dans ce projet. Si vous changez d'ordinateur ou travaillez à distance, le simple clonage de ce dépôt restaure à la fois toutes vos recettes et les compétences d'ingénierie de l'agent.
