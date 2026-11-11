# Audit R&D Chirurgical & Blindage du Pôle Brioches & Pains Viennois (PAC / Surgelé)
## Rapport d'Ingénierie Agroalimentaire, Échelles 30 Bacs & Standardisation Atelier Hub & Spoke

**Auteur :** Ingénieur R&D Senior en Boulangerie Industrielle & Spécialiste Pâtes Levées Riches  
**Périmètre :** Pôle 2 — Viennoiserie Générale & Pâtes Levées Riches (`V-VIE-01`, `V-VIE-02`, `V-BRI-01`, `V-BRI-02`)  
**Laboratoire :** Laboratoire Central de Tourage & Boulangerie (Alimentation de 2 à 3 boutiques Hub & Spoke)  
**Équipements :** Pétrin spirale 200 kg, Diviseuse hydraulique 20 parts, Façonneuse à tapis, Cellule flash -35 °C  
**Date :** Novembre 2026 | **Classification :** Référentiel Technique & Contrat de Vérité (Zéro Complaisance)

---

## 1. Contrat de Vérité & Challenge Sans Complaisance des Recettes Historiques

### 1.1. Autopsie de l'Ancien Procédé : Pourquoi le Pointage 24 h en Bacs au Froid Créait une Irrégularité Inacceptable

Dans l'organisation historique d'atelier, la pâte viennoise subissait un pétrissage suivi d'une mise immédiate en bacs plastiques empilés (type bacs Paneo 8 kg) en chambre froide positive (+3 °C à +4 °C) pendant 18 à 24 heures avant d'être divisée et façonnée le lendemain.

Ce schéma, séduisant sur le papier pour l'organisation du planning, constitue une **aberration thermomécanique et biochimique majeure** sur des pâtes enrichies :

```
             GRADIENT THERMIQUE DANS UN BAC DE PÂTE DE 8 KG (ÉPAISSEUR 10 CM)
   ┌────────────────────────────────────────────────────────────────────────┐
   │ BORD EXTÉRIEUR (Au contact de l'air à +3 °C)                           │
   │ T° = +3 °C en 90 min  ➔ Fermentation stoppée  ➔ Pâte ferme et tenace   │
   │   ┌────────────────────────────────────────────────────────────────┐   │
   │   │ ZONE INTERMÉDIAIRE                                             │   │
   │   │ T° = +6 °C à +8 °C en 4 h ➔ Fermentation modérée              │   │
   │   │   ┌────────────────────────────────────────────────────────┐   │   │
   │   │   │ CŒUR DU BAC (Inertie massique d'un isolant thermique)   │   │   │
   │   │   │ T° = +18 °C à +12 °C pendant plus de 6 heures !         │   │   │
   │   │   │ ➔ Fermentation galopante, acidification (pH < 4,7)      │   │   │
   │   │   │ ➔ Protéolyse du gluten, pâte molle, collante et gazeuse │   │   │
   │   │   └────────────────────────────────────────────────────────┘   │   │
   │   └────────────────────────────────────────────────────────────────┘   │
   └────────────────────────────────────────────────────────────────────────┘
```

#### Démonstration Thermodynamique (Loi de Fourier) :
La pâte boulangère est un composite diphasique (solide-gaz) possédant une diffusivité thermique très faible ($\alpha \approx 1{,}4 \times 10^{-7}\text{ m}^2/\text{s}$). Selon l'équation de la chaleur de Fourier unidimensionnelle :
$$\frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2}$$
Le temps caractéristique de pénétration thermique $\tau$ est proportionnel au carré de l'épaisseur : $\tau \propto \frac{L^2}{\alpha}$.
* Dans un bac de 10 cm d'épaisseur ($L = 0{,}05\text{ m}$ au demi-axe), le cœur met **plus de 5 à 6 heures** à descendre sous 6 °C.
* Pendant ces 5 heures, la levure *Saccharomyces cerevisiae* fonctionne à son métabolisme optimal ($18\text{--}24\text{ }^\circ\text{C}$).
* **Triple défaillance en atelier** :
  1. **Gradient de Force et de Densité Rhéologique** : Lors du basculement du bac dans la cuve de la diviseuse 20 parts, les morceaux découpés en périphérie sont très denses, froids et rigides ($W$ apparent élevé, $P/L > 0{,}9$), tandis que les morceaux découpés au cœur sont tièdes, alvéolés de gaz carbonique et affaiblis ($P/L < 0{,}4$).
  2. **Comportement Asymétrique sur Façonneuse à Tapis** : Lorsqu'un pâton hétérogène pénètre entre les deux cylindres de laminage puis sous la planche d'enroulement à tapis, la partie molle cède immédiatement sous la pression tandis que la partie rigide résiste. L'enroulement se fait de biais : le boudin ressort incurvé (« effet banane »), avec un diamètre irrégulier et une clé vrillée.
  3. **Acidification & Clivage du Gluten** : La sur-fermentation du cœur abaisse le pH sous 4,8 par production d'acide acétique et lactique, ce qui active les protéases acides endogènes de la farine. Le réseau de gluténines est partiellement hydrolysé, provoquant le déchirement superficiel des boudins lors du passage entre les tapis.

---

### 1.2. Validation Scientifique du Procédé « Méthode Directe le Jour Même »

Le bannissement du pointage 24 h et le passage en **Méthode Directe le Jour Même** élimine radicalement ces trois défauts :

$$\text{Pétrissage (Sortie 19–21 °C)} \longrightarrow \text{Pointage cuve 15–20 min} \longrightarrow \text{Division & Façonnage mécanique} \longrightarrow \text{Surgélation flash -35 °C}$$

1. **Homogénéité Thermique à 100 %** : L'ensemble de la cuve (168 kg) est à la même température ($\pm 0{,}5\text{ }^\circ\text{C}$). Zéro gradient thermique, zéro différence de densité.
2. **Élasticité Contrôlée & Rectitude Absolue** : La pâte possède une extensibilité ($L$) optimale et homogène. Le boudin s'enroule de manière parfaitement coaxiale sur la façonneuse à tapis. Les viennoises sortent rigoureusement droites, de section cylindrique constante, avec une soudure axiale nette qui ne s'ouvre pas à la pousse.
3. **Maîtrise Cryogénique Immédiate** : En figeant la pâte immédiatement après façonnage en cellule flash à -35 °C, on bloque l'activité enzymatique avant toute phase de dégradation du gluten.

---

### 1.3. Challenge des 3 Pièges d'Atelier en Méthode Directe

1. **Risque de collage sur les tapis de façonneuse** : Température de sortie pétrin verrouillée à **19 °C – 21 °C max** par utilisation de Tangzhong à +4 °C et d'eau glacée à +1 °C.
2. **Risque de retrait élastique (*Snapback*)** : **Détente obligatoire de 8 à 10 minutes** sur table sous bâche plastique étanche avant passage dans la façonneuse à tapis.
3. **Risque d'écrasement des inclusions** : Dans la viennoise chocolat (`V-VIE-02`), pépites de chocolat 50 % maintenues à **+4 °C**, incorporées en **1ʳᵉ vitesse lente (V1) pendant 45 à 60 secondes maximum**.

---

## 2. Analyse Critique R&D : Le Tangzhong à Grande Échelle (30 Bacs / 168 kg)

### 2.1. L'Interrogation Légitime du Chef d'Atelier : Faut-il Cuire 23 kg de Tangzhong ?

Sur une fournée de 30 bacs (168 kg net de pâte viennoise, soit ~76 kg de farine totale) :
* Farine Tangzhong (5 %) : **3,79 kg**
* Eau Tangzhong (25 %) : **18,95 kg**
* **Masse totale de Tangzhong à chauffer à 65 °C** : **22,74 kg** !

#### Diagnostic Sans Complaisance :
1. **Contrainte Thermique & Risque HACCP** : Chauffer 23 kg d'empois d'amidon à 65 °C exige un cuiseur industriel ou un gros batteur chauffant. Si l'atelier doit le faire en casseroles, le risque d'accrochage/brûlage au fond est immense. De plus, **refroidir 23 kg de gel chaud de 65 °C à +4 °C** demande un passage prolongé en cellule de refroidissement rapide. Dans un laboratoire avec 3 opérateurs, cela devient un goulot d'étranglement de main-d'œuvre.
2. **Les 3 Alternatives Technologiques Supérieures** :
   * **Alternative 1 (Recommandée - Zéro Cuisson) : Farine Pré-gélatinisée Clean Label (Amidon Prégélifié de Blé)**  
     Au lieu de cuire de la farine crue, le moulin fournit une farine dont l'amidon a déjà été gélatinisé par extrusion thermique et séché. Il suffit de la mélanger directement à l'eau froide (+4 °C) en cuve ! Zéro cuisson, zéro refroidissement, 100 % du pouvoir de rétention d'eau conservé.
   * **Alternative 2 (Artisanale Robuste) : Auto-Échaudage Statique J-1**  
     Peser 3,8 kg de farine T65 dans un bac inox la veille au soir (J-1). Verser dessus 19,0 kg d'eau bouillante (95 °C) en une seule fois. Mélanger vivement 30 secondes au fouet ou Bamix. Couvrir hermétiquement et stocker directement en chambre froide positive (+2 °C/+4 °C). Le mélange passe la nuit au froid et est à +4 °C au matin.
   * **Alternative 3 (Bio-Enzymatique Industrielle) : Complexe Amylase Maltogénique + Trimoline**  
     Supprimer le Tangzhong liquide. Compenser en montant l'hydratation cuve de 2 %, la Trimoline à 4,5 % et en utilisant un complexe d'alpha-amylases maltogéniques thermo-résistantes (type Puratos Soft'r Fresh). Les amylases clivent les chaînes latérales d'amylopectine pendant la cuisson au four, empêchant la recristallisation pendant 7 jours sans aucune préparation préalable.

---

## 3. Mécanique de la Diviseuse Hydraulique : Résolution du Problème des Bacs Brioches

### 3.1. Pourquoi les Bacs de 2,4 kg Échouaient Mécaniquement
Une cuve de diviseuse hydraulique standard 20 parts mesure environ **40 cm $\times$ 50 cm** (surface de 2 000 cm²).
* Une masse de **2,4 kg de pâte** étalée dans cette cuve forme une couche d'une épaisseur moyenne de seulement **1,1 cm** !
* Lors de la descente du plateau de tassage hydraulique :
  - La pression hydraulique s'exerce mal sur une galette aussi mince.
  - La pâte refuse de remplir les 4 coins de la cuve.
  - Les couteaux écrasent la pâte au lieu de la sectionner net, provoquant des variations de poids de $\pm 15\text{ g}$ par pâton.

### 3.2. Solution Chirurgicale : Le Bac Optimisé de 4,80 kg (ou 6,00 kg) avec Découpe en Quatre

```
      DIVISION HYDRAULIQUE 20 PARTS             DÉCOUPE EN 4 AU COUPE-PÂTE EN CROIX
   ┌──────────────────────────────────┐            ┌──────────────┬──────────────┐
   │                                  │            │              │              │
   │   PÂTON DE BAC = 4,80 KG         │            │  PÂTON 1     │  PÂTON 2     │
   │   Épaisseur en cuve = 2,5 cm     │  ───────►  │  (60 g cru)  │  (60 g cru)  │
   │   Tassage hydraulique parfait    │            │              │              │
   │   20 divisions de 240 g net      │            ├──────────────┼──────────────┤
   │                                  │            │  PÂTON 3     │  PÂTON 4     │
   │                                  │            │  (60 g cru)  │  (60 g cru)  │
   └──────────────────────────────────┘            └──────────────┴──────────────┘
                                                    ➔ 80 BRIOCHETTES DE 60 G / BAC
```

* **Option Standard d'Atelier (Calibre 60 g cru)** :
  * Bac pesé à **4,80 kg net pile** (épaisseur en cuve = 2,5 cm).
  * La diviseuse délivre **20 rectangles pesant exactement 240 g**.
  * D'un coup double de coupe-pâte en croix (un trait longitudinal, un trait transversal), l'opérateur sépare chaque rectangle en **4 carrés rigoureusement égaux de 60 g**.
  * **Rendement : 80 briochettes de 60 g par bac** (soit 800 pièces en 10 bacs).
* **Option Calibre Gourmand (Standardisation Bacs 6,00 kg)** :
  * Si l'atelier souhaite utiliser strictement le même bac de **6,00 kg** que pour les viennoises :
  * 20 divisions de 300 g $\rightarrow$ coupées en 4 d'un coup de coupe-pâte = **80 briochettes de 75 g cru** (~68 g cuit).
  * Format très vendeur en vitrine, manipulation ultra-rapide.

---

## 4. Standardisation des Échelles, Matières Grasses & Capacités (Pétrin 200 kg & 30 Bacs)

### 4.1. Arbitrage Technique Définitif sur les Matières Grasses (Contrat de Vérité)
1. **Pains Viennois (`V-VIE-01` & `V-VIE-02`) $\longrightarrow$ Margarine OPALE Cuve 18 %** :
   * **Justification rhéologique & mécanique** : La margarine Opale possède un profil de matière grasse solide (SFC) cristallisé à température ambiante (point de fusion $34\text{--}36\text{ }^\circ\text{C}$). À 19–21 °C en sortie de cuve, elle confère à la pâte une plasticité et un corps structuré indispensables pour le façonnage sur façonneuse à tapis. Les boudins ne s'affaissent pas, ne patinent pas sur le feutre et conservent leur cambrure et leurs grignes nettes sans s'étaler.
2. **Petites Brioches au Sucre (`V-BRI-01`) $\longrightarrow$ Huile de Colza Neutre 18 %** :
   * **Justification biochimique & fraîcheur** : Contrairement au façonnage en boudin allongé, la briochette est boulée en sphère. L'huile de colza est composée à 100 % de triglycérides insaturés liquides qui ne cristallisent pas, même à $\le -10\text{ }^\circ\text{C}$. Elle enrobe les grains d'amidon, retarde la rétrogradation de l'amylose et confère une texture filante et un fondant extrême pendant 7 jours sans rancissement.

### 4.2. Tableau Synthétique des Calibres Homologués du Pôle 2 (100 % en GRAMMES)

| Code Produit | Dénomination | Calibre Cru | Calibre Cuit | Poids Net Bac | Nb Pièces / Bac | Échelle 30 Bacs (Pétrin 200 kg) | Matière Grasse Retenue |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `V-VIE-01` | **Pain Viennois Nature** | **280 g** | **~266 g** | **5 600 g** | 20 pièces | **168 000 g net** (600 pcs) | **Margarine OPALE cuve (18 %)** |
| `V-VIE-02` | **Pain Viennois Chocolat**| **140 g** | **~133 g** | **5 600 g** | 40 pièces | **168 000 g net** (1 200 pcs) | **Margarine OPALE cuve (18 %)** |
| `V-BRI-01` | **Brioche Individuelle Sucre**| **75 g** | **~75 g fini**| **6 000 g** | 80 pièces | **180 000 g net** (2 400 pcs) | **Huile de colza neutre (18 %)** |
| `V-BRI-02` | **Brioche Fine Nanterre** | **400 g** | **~365 g** | **4 000 g** | 10 pièces | **80 000 g net** (200 pcs / 20 b.)| **Beurre doux 82 % (45 %) + Tangzhong** |

*Taux d'occupation de la cuve 200 kg à 30 bacs (168 000 g à 180 000 g net) : **84 % à 90 %** (conforme aux abaques constructeurs pour limiter l'échauffement mécanique).*

---

## 5. Synthèse Économique & Marges Brutes Révisées

* Coût pâte viennoise crue : **1,102 € HT / kg**.
* **Pain Viennois Nature (280 g cru / ~266 g cuit)** :
  * Coût matière = $0{,}280 \times 1{,}102 + 0{,}075 = \mathbf{0{,}384\text{ \euro\ HT}}$.
  * Prix Vente TTC Boutique = 1,90 € TTC (1,801 € HT).
  * **Marge Brute = 78,7 %**.
* **Pain Viennois Chocolat (140 g cru / ~133 g cuit)** :
  * Coût matière = $0{,}125 \times 1{,}102 + 0{,}015 \times 5{,}20 + 0{,}060 = \mathbf{0{,}276\text{ \euro\ HT}}$.
  * Prix Vente TTC Boutique = 1,60 € TTC (1,517 € HT).
  * **Marge Brute = 81,8 %**.
