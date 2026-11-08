# Manuel Opérationnel d'Atelier : Rondo Croissomat SCM50
## Réglages d'Étirement, d'Amorce & d'Enroulement Parfaits (Croissant 75 g)

Ce guide technique est calibré directement pour votre modèle : la **Rondo Croissomat SCM50 (Seewer Rondo)** avec tapis amont incliné, rouleaux de découpe sous carter à barreaux et **module d'enroulement transversal à coulisses de réglage graduées rouges**.

---

## 1. Cartographie des Organes de la Machine

```mermaid
flowchart LR
    subgraph A["1. Station Amont de Découpe (Droite)"]
        A1["Tapis convoyeur d'entrée incliné\n(Bande de pâte à 10–12 °C)"]
        --> A2["Rouleau presseur & guidage latéral jaune\n(Plaquage sans écrasement)"]
        --> A3["Cylindres rotatifs de découpe triangulaire\n(Sous carter sécurisé à barreaux)"]
    end
    subgraph B["2. Station Centrale d'Orientation & Transfert"]
        B1["Table intermédiaire sous grille inox\n(Poignée étoile de déverrouillage)"]
        --> B2["Doigts d'orientation & Tapis accélérateur\n(Allongement axial +25 à +30 % de 18 à 24 cm)"]
        --> B3["Brosses rotatives d'époussetage\n(Zéro farine résiduelle entre spires)"]
    end
    subgraph C["3. Station d'Enroulement Transversale (Gauche)"]
        C1["Manette Supérieure Avant (Coulisse Rouge 1)\nRéglage Entrefait d'Amorce (5–6 mm)"]
        --> C2["Manette Supérieure Arrière (Coulisse Rouge 2)\nRéglage Angle de Pincement / Pente Divergente"]
        --> C3["Manette Inférieure (Coulisse Rouge 3)\nRéglage Sortie & Serrage des Spires (Laplace)"]
        --> C4["Sortie Croissant Roulé (75 g)\nClé plaquée à 6h / 3 à 4 spires lâches"]
    end
    A --> B --> C
```

---

## 2. Le Bloc d'Enroulement Transversal : Maîtrise des 3 Manettes à Coulisses Rouges

Le panneau latéral gauche est le centre nerveux du façonnage. Les trois manettes à poignée étoile noire coulissent dans des arcs de cercle munis de **réglettes graduées rouges**.

```
       [ENTRÉE DU TRIANGLE]
                 │
                 ▼
     ┌───────────────────────┐
     │  (Manette 1 - Haut/Av)│ ──> [HAUTEUR D'AMORCE] : 5 à 6 mm (1,5x épaisseur de pâte)
     │  (Manette 2 - Haut/Ar)│ ──> [ANGLE DU TABLIER] : Pente divergente d'accompagnement
     │                       │
     │  (Manette 3 - Bas)    │ ──> [SERRAGE DES SPIRES] : Calibrage 3 à 4 spires lâches + Clé à 6h
     └───────────────────────┘
                 │
                 ▼
     [ÉJECTION CROISSANT ROULÉ]
```

### Manette 1 • Coulisse Supérieure Avant (Entrefait d'Amorce)
* **Fonction** : Ajuste l'espacement entre le tapis convoyeur inférieur et la lèvre d'attaque de la bande supérieure d'enroulement.
* **Réglage étalon pour Croissant 75 g (Abaisse 3,5 mm)** :
  * Régler l'entrefait à **5,0 – 6,0 mm** (repère intermédiaire sur la réglette rouge).
  * **Si trop ouvert (graduation haute)** : La base du triangle ne trouve pas de résistance, elle glisse sur 5 à 8 cm avant de s'enrouler. Le croissant sort court, sans noyau serré, avec seulement 2 spires molles.
  * **Si trop fermé (graduation basse)** : La base heurte le tapis supérieur, plisse en accordéon et s'écrase. Le feuilletage est broyé, ce qui entraîne une fuite de beurre massive en cuisson.

### Manette 2 • Coulisse Supérieure Arrière (Angle de Convergence / Pente)
* **Fonction** : Définit la pente de la chambre d'enroulement entre l'entrée et la sortie.
* **Réglage étalon** :
  * Le canal doit former un **coin divergent progressif** s'ouvrant de 5–6 mm à l'entrée jusqu'à **28–32 mm** au centre.
  * Cette ouverture progressive permet d'accueillir le volume croissant du cylindre de pâte au fur et à mesure que les 3 à 4 spires s'enroulent sur elles-mêmes, sans comprimer le cœur.

### Manette 3 • Coulisse Inférieure (Pression Finale & Calage de la Clé)
* **Fonction** : Contrôle la pression d'éjection et la position angulaire de la pointe du croissant à la sortie.
* **Réglage étalon (Loi de Laplace $T = \Delta P \cdot r$)** :
  * Régler en position **légère / souple**.
  * **Test tactile impératif** : L'opérateur doit pouvoir glisser l'extrémité du petit doigt dans les cavités latérales du croissant cru sans forcer. Si le trou est complètement obturé ou écrasé, le croissant est trop serré.
  * **Calage de la pointe (La Clé)** : Faire coulisser cette manette de quelques millimètres pour ajuster le moment exact où le croissant quitte le tapis supérieur. **La pointe du triangle doit terminer impérativement plaquée sous le croissant (à 6 heures)** contre le tapis récepteur.

---

## 3. Le Dispositif d'Étirement Axial (L'Allongement du Triangle)

Sur la Rondo SCM50, l'obtention d'un croissant élancé dépend de l'élongation préalable du triangle entre la station de découpe et le module d'enroulement :

1. **Rapport Géométrique Idéal** :
   * **Dimensions brutes découpées** : Base = 120–130 mm | Hauteur = 180–200 mm.
   * **Dimensions après étirement axial** : Base = 120–130 mm | **Hauteur étirée = 240 à 260 mm** (Gain d'élongation de **+25 % à +30 %**).
2. **Mécanisme d'entraînement de la SCM50** :
   * Le tapis intermédiaire fonctionne à une vitesse légèrement supérieure ($V_2 > V_1$) pour étirer le triangle pendant qu'un rouleau/patin souple retient temporairement la pointe ou la base.
   * **Condition biochimique indispensable** : Ce taux d'allongement sans déchirure n'est possible que si la détrempe contient **30 % de Farine T65 Tradition** (extensibilité $L$, $P/L \le 0,62$) et que la bande a bénéficié de sa **décompression libre de 60 secondes** sur le tapis incliné.

---

## 4. Matrice de Dépannage Immédiat au Poste SCM50

| Constat Visuel sur le Croissant | Cause Mécanique sur la SCM50 | Correction Immédiate |
| :--- | :--- | :--- |
| **Croissant trapu, "boudiné", 2 spires** | Triangle pas assez étiré en hauteur | Augmenter l'écart de vitesse d'étirement ; vérifier que la bande est à 10–12 °C. |
| **Déchirure de la pâte à l'entrée de l'enrouleur** | Manette 1 trop basse (entrée trop étroite) | Remonter la Manette 1 de 2 à 3 mm sur la réglette rouge supérieure. |
| **Croissant qui se débobine en étuve** | Excès de farine de fleusage entre les spires | Régler les brosses rotatives d'époussetage pour balayer à sec les deux faces. |
| **Éclatement de la spire externe en étuve** | Manette 3 trop serrée (enroulement trop sous tension) | Ouvrir la Manette 3 (desserrer l'arc inférieur) pour aérer le noyau central. |
| **Pointe qui rebique vers le haut en cuisson** | Clé mal positionnée à l'éjection (pointe à midi au lieu de 6h) | Déplacer la Manette 3 de ± 5 mm jusqu'à ce que la pointe retombe sous le corps. |
| **Croissant asymétrique (forme en banane tordue)** | Triangle arrivant de biais sous l'enrouleur | Réaligner les guides latéraux et doigts d'orientation sur la table centrale. |
