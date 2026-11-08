# Manuel Opérationnel d'Atelier : Rondo Croissomat SCM50
## Configuration Exacte d'Atelier : Découpe 3 Pistes & Enroulement Transversal

Ce manuel technique référence la configuration physique exacte de votre ligne **Rondo Croissomat SCM50** : alimentation sur rampe inclinée inox, découpe séquentielle en 3 matrices (ébarbage, refente 3 bandes, matrice triangulaire montante/descendante), séparation par rouleaux accélérateurs et enroulement transversal sous tablier à 3 manettes graduées.

---

## 1. Schéma Cinématique Réel de votre Croissomat SCM50

```mermaid
flowchart TD
    subgraph A["1. Poste d'Alimentation Amont"]
        A1["Repose-rouleau de pâte (Berceau)\nDéroulage côté fariné en dessous"]
        --> A2["Rampe inox inclinée de glissement\n(Bande 3,5 mm à 10–12 °C / Décompression libre)"]
    end
    subgraph B["2. Premier Tapis Convoyeur : Découpe Séquentielle 3 Matrices"]
        B1["Matrice 1 : Ébarbage des rives\n(Coupe nette des 2 bordures latérales)"]
        --> B2["Matrice 2 : Découpe longitudinale en 3 bandes\n(Refente en 3 pistes égales de 120–130 mm)"]
        --> B3["Matrice 3 : Poinçon triangulaire montant/descendant\n(Découpe simultanée des triangles 75 g sur les 3 pistes)"]
    end
    subgraph C["3. Poste de Séparation & Accélération"]
        C1["Duo de petits rouleaux séparateurs\nVitesse différentielle V2 > V1"]
        --> C2["Création de l'intervalle longitudinal (3 à 5 cm)\n+ Amorce d'étirement axial (+20 à +25 %)"]
    end
    subgraph D["4. Deuxième Tapis & Module d'Enroulement Transversal"]
        D1["Table de transfert & doigts d'orientation\n(Pas de brosse rotative -> Face sup nue impérative)"]
        --> D2["Module d'enroulement à 3 manettes sur coulisses rouges\n(Entrefait 5–6 mm, coin divergent, 3-4 spires lâches, clé à 6h)"]
        --> D3["Éjection Croissant Roulé 75 g sur plaque"]
    end
    A --> B --> C --> D
```

---

## 2. Analyse Technique de votre Séquence de Découpe en 3 Matrices

Contrairement aux systèmes rotatifs simples, votre machine utilise un découpage séquentiel étagé qui garantit une précision pondérale absolue ($\pm 1\text{ g}$ sur chaque croissant) :

### Matrice 1 • Ébarbage des Rives Latérales
* **Rôle** : Rogner les deux bordures extrêmes du pâton sur 5 à 10 mm.
* **Fonction atelier** : Supprime les rives irrégulières et les bourrelets de pâte morte pour calibrer la bande à la largeur utile exacte des 3 pistes. Les bandelettes de chutes tombent directement dans les bacs de récupération latéraux pour être recyclées.

### Matrice 2 • Refente Longitudinale en 3 Bandes Parallèles
* **Rôle** : Diviser la bande ébarbée en **3 pistes longitudinales strictement identiques**.
* **Calibrage** : Chaque bande mesure entre **120 et 130 mm de large** (correspondant exactement à la largeur de base du croissant 75 g).
* **Avantage rhéologique** : La refente en amont évite les contraintes de déchirement latéral lors de la frappe des triangles.

### Matrice 3 • Poinçon Triangulaire Montant & Descendant (Guillotine)
* **Rôle** : Découper les triangles en une seule frappe verticale simultanée sur les 3 bandes.
* **Fonctionnement** :
  * Le tapis marque un micro-arrêt indexé pendant la descente de la lame triangulaire biseautée.
  * Les **tampons éjecteurs à ressorts** maintiennent la pâte au tapis pendant la remontée de la lame (anti-soulèvement par effet ventouse).
* **Butée de hauteur** : Doit sectionner 100 % de l'épaisseur sans entailler la toile du tapis.

---

## 3. Le Dispositif de Séparation & Décalage : Les 2 Arbres à Galets Rainurés

Vos vidéos révèlent avec une précision parfaite le mécanisme central de séparation des croissants : **deux arbres transversaux en acier inox équipés chacun de 3 galets rainurés blancs montés avec des anneaux toriques en élastomère bleu**.

```
    [SORTIE DE DÉCOUPE GUILLOTINE]
    (Triangles imbriqués tête-bêche sans chute)
                 │
                 ▼
     ┌──────────────────────────────────────────────────────────┐
     │  ARBRE AMONT 1 : 3 Galets blancs + Anneaux toriques bleus│ ──> Pince la Rangée A (Base avant)
     └──────────────────────────────────────────────────────────┘
                 │
                 ▼  Accélération différentielle du tapis aval
     ┌──────────────────────────────────────────────────────────┐
     │  ARBRE AVAL 2 : 3 Galets blancs + Anneaux toriques bleus │ ──> Retient/Cadence la Rangée B (Pointe avant)
     └──────────────────────────────────────────────────────────┘
                 │
                 ▼
    [TRIANGLES PARFAITEMENT DÉCALÉS & SÉPARÉS]
    (Intervalle libre de 5 à 8 cm entre chaque pièce)
```

### 3.1 Pourquoi ce Double Arbre à Galets est Indispensable ?
1. **La contrainte géométrique du zéro chute** :
   * La guillotine triangulaire découpe la pâte en imbriquant les triangles tête-bêche (une base en avant, la pointe voisine en avant) pour ne générer aucun déchet de pâte.
   * Si les triangles continuaient leur course ensemble, ils se toucheraient bord à bord et entreraient en collision frontale dans l'enrouleur.
2. **Le déphasage spatial & temporel (Staggering)** :
   * L'arbre 1 applique ses 3 galets sur la première série de triangles (ceux dont la base avance en premier) pour assurer leur entraînement immédiat par le tapis aval plus rapide.
   * L'arbre 2, décalé géométriquement, temporise la seconde série de triangles (ceux dont la pointe avance en premier).
   * **Résultat visuel (net sur vos vidéos)** : Dès le passage sous les deux barres, les triangles imbriqués se décrochent et s'espacent de **5 à 8 cm**, formant une file indienne cadencée et parfaitement isolée sur chaque piste !
3. **L'entaille de base** :
   * Vos vidéos montrent très nettement la **fente axiale de 10 à 15 mm découpée au centre de la base de chaque triangle**. Cette entaille permet aux cornes du croissant de s'écarter harmonieusement lors du roulage sous tablier sans former de bourrelet compact au cœur.

---

### 3.2 Les 3 Réglages Clés d'Atelier sur vos Deux Arbres à Galets

* **1. Centrage Latéral Strict des Galets sur les Pistes** :
  * Chaque galet blanc coulisse sur son axe cylindrique et se bloque par une vis pointeau six pans (BTR).
  * **Règle** : Le galet doit appuyer **rigoureusement au milieu de l'axe longitudinal du triangle**.
  * *Si le galet est décalé de 5 mm vers un côté* : Il appuie sur l'arête biseautée au lieu du centre, ce qui fait pivoter le triangle en travers $\rightarrow$ le triangle entre de biais dans l'enrouleur et produit un croissant tordu en virgule.
* **2. Pression d'Appui des Arbres (Hauteur & Ressorts)** :
  * Les deux arbres sont montés sur des paliers latéraux réglables.
  * **Pression idéale** : Un pincement doux mais franc. Les anneaux bleus doivent adhérer à la pâte pour l'entraîner sans jamais marquer de sillon permanent dans les 3,5 mm d'épaisseur ni écraser les 12 feuillets de beurre.
  * *Si la pression est trop faible* : Le galet patine sur la pâte (danger aggravé s'il y a de la farine sur le dessus !) $\rightarrow$ le triangle n'est pas accéléré, les pièces restent collées entre elles.
  * *Si la pression est trop forte* : Écrasement du feuilletage au centre et risque de déchirement de la pointe fine.
* **3. Entretien & Dégraissage des Anneaux Toriques Bleus** :
  * Les anneaux bleus en élastomère assurent le coefficient d'adhérence nécessaire avec la pâte.
  * **Consigne de fin de poste** : Nettoyer les anneaux à l'éponge humide non abrasive. Si du beurre ou de l'huile s'y dépose, les anneaux perdent leur grip, patinent et désynchronisent la séparation des triangles.

---

## 4. Pourquoi l'Absence de Brosse Rotative Rend la Règle de Déroulage Cruciale

Votre machine ne possède pas de brosses rotatives d'époussetage pour balayer la pâte avant l'enrouleur. 

* **Si la face supérieure était farinée** :
  * Cette farine ne serait jamais éliminée.
  * Elle entrerait directement sous le tablier d'enroulement et se retrouverait **emprisonnée entre les spires**.
  * **Sanction immédiate** : Les couches ne peuvent pas fusionner, et le croissant **se débobine en étuve ou s'ouvre en ressort au four**.
* **La Solution Définitive** :
  * Le laminoir farine le dessus lors de l'abaisse.
  * **Vous déroulez impérativement côté fariné en dessous (contre le tapis)**.
  * **Résultat** : La face supérieure qui entre dans la SCM50 est **rigoureusement nue, mate et sans farine volante**. Les triangles s'enroulent sur eux-mêmes avec une adhérence parfaite, sans aucun risque de débobinage !

---

## 5. Synthèse des Réglages au Poste d'Enroulement (Panneau Latéral Gauche)

Une fois les triangles séparés par les rouleaux et orientés base en tête :
* **Manette Supérieure Avant (Coulisse 1)** : Entrefait d'amorce calé à **5–6 mm** pour que la base du triangle accroche instantanément sans plisser.
* **Manette Supérieure Arrière (Coulisse 2)** : Angle en **coin divergent montant vers 28–32 mm** pour accompagner le grossissement du cylindre sans comprimer la mie.
* **Manette Inférieure (Coulisse 3)** : Réglée **souple (3 à 4 spires lâches, loi de Laplace)** + calage pour que la pointe du triangle termine **plaquée sous le croissant (à 6 heures)** contre la plaque de cuisson.
