# Traité des Pâtes Battues, Cakes de Voyage & Physico-Chimie des Émulsions
## Référentiel Scientifique, Modélisation Prédictive $a_w$ & Protocoles d'Atelier (E.B. Bennion, Stéphane Glacier, Christophe Felder)

Ce document formalise la science des pâtes battues (*cake batters*), la microstructure des émulsions huile-dans-eau, le calcul prédictif de l'activité de l'eau ($a_w$) par la méthode de Grover et la loi de Seiler, ainsi que les règles de conduite thermique des gâteaux de voyage longue conservation.

---

## 1. Physico-Chimie Fondamentale des Émulsions de Pâte Battue (Bennion, Bamford & Bent)
*Source de référence : The Technology of Cake Making, 6e Édition, Chapitres 10 & 21.*

### A. Microstructure Colloïdale
La pâte à cake n'est pas une simple suspension, mais une **émulsion huile-dans-eau (o/w) métastable** hautement complexe :
* **Phase Continue Aqueuse** : Solution saturée en saccharose, glucose et minéraux, au sein de laquelle sont dispersées les protéines solubles des œufs (ovalbumine, conalbumine) et les granules d'amidon de farine non gonflés.
* **Phase Dispersée Lipidique** : Gouttelettes de matière grasse (triglycérides du beurre ou shortenings) stabilisées à l'interface par des agents tensioactifs naturels (lécithine et lipoprotéines du jaune d'œuf) ou de synthèse (monoglycérides distillés).
* **Phase Gazeuse Emprisonnée** : Micro-bulles d'air incorporées mécaniquement au cours du battage, logées préférentiellement au sein de la matière grasse plastique.

```
┌────────────────────────────────────────────────────────────────────────┐
│                      PHASE CONTINUE AQUEUSE                            │
│           (Eau + Sucres dissous + Protéines d'œuf + Sels)              │
│                                                                        │
│        ┌──────────────┐                  ┌──────────────┐              │
│        │   Gouttelette│                  │ Micro-bulle  │              │
│        │  de Beurre/MG│                  │  d'Air       │              │
│        │  (Triglycé-  │                  │  (Nucléation │              │
│        │   rides)     │                  │   de vapeur) │              │
│        └──────┬───────┘                  └──────┬───────┘              │
│               ▲                                 ▲                      │
│               └──────── Émulsifiant Lécithine ──┘                      │
│                                                                        │
│       [Granule d'Amidon Cru]        [Granule d'Amidon Cru]             │
└────────────────────────────────────────────────────────────────────────┘
```

### B. Le Rôle Vital de l'Aération et le Principe de Nucléation
* **Facteur d'Expansion Volumique** : Au cours de la cuisson, une pâte à cake subit une expansion volumique de l'ordre de **30 à 35 fois son volume initial**.
* **Origine Physique de l'Expansion** :
  * L'air introduit au batteur ne représente en réalité que **10 % du volume d'expansion final**.
  * Les **90 % restants sont fournis par la vaporisation de l'eau** en vapeur d'eau au cours de la chauffe, complétée par le dioxyde de carbone dégagé par la levure chimique.
* **Principe Absolu de Nucléation (*Nuclei Theory*)** :
  * La vapeur d'eau et le gaz $\mathrm{CO_2}$ ne peuvent pas créer spontanément de nouvelles bulles au sein du liquide visqueux : ils ne peuvent que diffuser dans les micro-cavités d'air préexistantes.
  * Si une pâte est préparée sous vide partiel ou dégazée, elle reste totalement plate et compacte au four, quelle que soit la quantité de levure chimique incorporée. Le travail mécanique du crémage conditionne donc à 100 % l'alvéolage final.

### C. Métrologie du Foisonnement : La Densité Relative ($\mathrm{RD}$)
Le foisonnement d'air est mesuré en atelier par la **Densité Relative (Relative Density, $\mathrm{RD}$)** :
$$\mathrm{RD} = \frac{\text{Masse d'un volume défini de pâte}}{\text{Masse du même volume d'eau pure à 20 }^\circ\mathrm{C}}$$

* **Plage Optimale de Densité** : **$\mathrm{RD} = 0{,}70\text{ à }0{,}85$** (pour cakes de voyage et marbrés).
* **Analyse des Écarts Rhéologiques** :
  * *$\mathrm{RD} < 0{,}65$ (Sur-foisonnement)* : Excès d'air piégé. Les parois cellulaires sont trop fines ; sous la pression de vapeur d'eau vers 75 °C, les bulles coalescent et éclatent avant la gélatinisation de l'amidon $\rightarrow$ **effondrement central en dôme cratère**.
  * *$\mathrm{RD} > 0{,}90$ (Sous-foisonnement)* : Pâte insuffisamment battue ou trop dense $\rightarrow$ transmission thermique lente, mie lourde, compacte, collante et grasse en bouche.

---

## 2. Comparatif Mécanique des Méthodes de Fabrication (Bennion Chap. 10)

| Paramètre | Méthode Crémage (*Sugar Batter*) | Méthode Farine (*Flour Batter*) | Méthode Tout-en-un (*All-In*) |
| :--- | :--- | :--- | :--- |
| **Principe mécanique** | Beurre + Sucre battus en mousse, puis œufs par fractions, farine en fin de cycle. | Beurre + Farine battus ensemble ; œufs + sucre montés séparément au ruban. | Tous les ingrédients battus simultanément en une seule passe à grande vitesse. |
| **Type d'émulsion** | Émulsion o/w inversée en fin de mélange. Risque de tranchage (*curdling*) si œufs froids. | Émulsion protégée par l'enrobage lipidique direct des granules de farine. | Émulsion forcée par des tensioactifs chimiques (phase alpha-gel). |
| **Propriété clé** | Mie très fine, moelleuse, texture fondante traditionnelle. | **Portance exceptionnelle des inclusions lourdes** (fruits confits, pépites). | Tolère des taux de liquide et sucre supérieurs à 100 % (*High Ratio*). |
| **Usage d'atelier** | Cakes traditionnels, marbrés, quatre-quarts d'orfèvrerie. | Cakes aux fruits anglais, plum cakes, cakes riches en inclusions. | Génoises industrielles, cupcakes longue conservation. |

---

## 3. Modélisation Prédictive de l'Activité de l'Eau ($a_w$) & Durée de Vie selon Seiler
*Source : Bennion, Bamford & Bent, Chapitre 29 (Water activity in flour confectionery product development, p. 386–397), d'après les travaux de D.W. Grover (1947) et D.A.L. Seiler (FMBRA).*

La conservation des cakes sans conservateur chimique repose exclusivement sur le contrôle de l'**Activité de l'Eau ($a_w$)**, représentant la fraction d'eau libre disponible pour le métabolisme microbien.

### A. La Méthode des Équivalents Sucrose (SE) de Grover
Chaque ingrédient possède un pouvoir d'abaissement de l'activité de l'eau exprimé en **Équivalents Sucrose (Sucrose Equivalents, $\mathrm{SE}$)** par rapport au saccharose ($\mathrm{SE} = 1{,}0$) :

$$\text{Sucrose Équivalent Total (SET)} = \sum_{i} \left( \frac{Q_i \times \mathrm{SE}_i}{100} \right)$$
$$\text{Eau Totale Résiduelle (ETR)} = \left[ \sum_{i} \left( \frac{Q_i \times M_i}{100} \right) \right] - \text{Perte en eau à la cuisson et ressuage}$$
$$\text{Concentration en Sucrose Équivalent (S)} = \frac{\text{SET}}{\text{ETR}} \times 100 \quad (\text{g de soluté équivalent pour } 100\text{ g d'eau})$$
$$\text{Pourcentage massique en phase aqueuse totale} \quad S_{\text{aqueux}} = \frac{\text{SET}}{\text{SET} + \text{ETR}} \times 100 \quad (\%)$$

### B. Table des Facteurs $\mathrm{SE}$ et Teneurs en Eau ($M_i$)
*Tableau officiel d'ingénierie selon Bennion & Bent (p. 408) :*

| Ingrédient | Facteur $\mathrm{SE}$ | Eau $M_i$ (%) | Rôle Fonctionnel dans l'Appareil |
| :--- | :---: | :---: | :--- |
| **Saccharose (Sucre semoule / glace)** | **1,0** | 0,1 % | Fixation d'eau par liaisons hydrogène, flaveur sucrée. |
| **Farine de blé standard (T55)** | **0,2** | 14,0 % | Rétention d'eau par l'amidon et le réseau protéique. |
| **Beurre frais 82 % MG** | **0,2** | 16,0 % | Apport de phase grasse plastique et fraction aqueuse laitière. |
| **Matière grasse pure (Huile, Shortening)** | **0,0** | 0,0 % | Neutre sur l'$a_w$, plastifiant de texture. |
| **Œufs entiers liquides** | **0,0** | 75,0 % | Apporteur majeur d'eau libre et d'émulsifiants (jaune). |
| **Poudre de lait écrémé** | **1,2** | 3,0 % | Pouvoir osmotique élevé des protéines solubles et du lactose. |
| **Poudre à lever (*Baking powder*)** | **3,0** | 1,0 % | Sels minéraux ionisés abaissant fortement la tension de vapeur. |
| **Chlorure de sodium (Sel fin)** | **11,0** | 0,2 % | Abaisseur osmotique extrême (puissance ionique $\mathrm{Na^+/Cl^-}$). |
| **Sirop de glucose cristal 42 DE** | **0,7** | 20,0 % | Agent anti-cristallisant, maintien de la plasticité. |
| **Sorbitol liquide (70 % extrait sec)** | **2,0** | 30,0 % | Polyol humectant efficace, modérément sucrant. |
| **Glycérol pur (Glycérine végétale)** | **4,0** | 0,5 % | **Abaisseur d'$a_w$ le plus puissant**, agent anti-dessèchement. |

### C. La Loi de Durée de Vie sans Moisissure de David Seiler (*Mould-Free Shelf-Life*) & Calculs d'ERH
Le calcul des équivalents sucrose permet d'estimer l'Humidité Relative d'Équilibre ($\mathrm{ERH} = a_w \times 100$) selon trois approches physico-chimiques complémentaires documentées dans Bennion (Chapitre 29) :

1. **Abaque de conversion de Cooper & Seiler (Bennion Fig. 29.1, p. 388)** *(Méthode de référence d'atelier)* :
   * Relie directement le ratio de Grover $S_{\text{ratio}} = \frac{\text{SET}}{\text{ETR}}$ à l'ERH mesurée.
   * Pour la recette étalon de cake de Bennion (Table 29.4, $\text{SET} = 135{,}0\ \mathrm{kg}$, $\text{ETR} = 79{,}4\ \mathrm{kg}$, soit un ratio $S = \text{SET}/\text{ETR} = 1{,}70$), la Fig. 29.1 donne directement :
     $$\mathbf{\mathrm{ERH} = 88\,\% \quad (a_w = 0{,}88)}$$
     garantissant une durée de vie sans moisissure étalonnée à 7–8 jours à 21 °C.

2. **Formule rationnelle de dépression de tension de vapeur de Grover (1947)** :
   $$\mathrm{ERH} = \frac{100}{1 + 0{,}18\,N}$$
   où $N = \frac{\text{SET} / 342{,}3}{\text{ETR} / 1000}$ représente le nombre de moles de soluté équivalent pour 100 g d'eau ($342{,}3\ \mathrm{g/mol}$ étant la masse molaire du saccharose $\mathrm{C_{12}H_{22}O_{11}}$).

3. **Polynôme empirique de Norrish / Money & Born** :
   $$\mathrm{ERH} \approx 100 - 0{,}26\,S_{\text{aqueux}} - 0{,}001\,S_{\text{aqueux}}^2$$
   *Attention critique d'ingénierie* : Dans ce polynôme empirique, la variable $S$ représente impérativement le **pourcentage massique de saccharose dans la phase aqueuse totale** (solides solubles + eau) :
   $$S_{\text{aqueux}} = \frac{\text{SET}}{\text{SET} + \text{ETR}} \times 100$$
   (Pour le cake étalon Bennion Table 29.4 : $S_{\text{aqueux}} = \frac{135{,}0}{135{,}0 + 79{,}4} \times 100 = 62{,}97\,\%$, ce qui donne $\mathrm{ERH} \approx 79{,}7\,\%$, $a_w \approx 0{,}80$). Injecter le ratio sur l'eau seule ($S = 170{,}03$) dans ce polynôme produirait une valeur aberrante de 26,9 % ($a_w = 0{,}27$, niveau d'un biscuit sec).

Durée de vie prédictive sans altération fongique à température ambiante ($21\text{ }^\circ\text{C}$) selon Seiler :

```
    ERH (%)       aw       DURÉE DE VIE SANS MOISISSURE (21 °C)
    ─────────────────────────────────────────────────────────────
    86 %         0,86      8 jours   (Risque très élevé de moisissure rapide)
    84 %         0,84      13 jours  (Cake ménager standard)
    82 %         0,82      18 jours  (Gâteau de voyage court)
    80 %         0,80      24 jours  (Seuil artisanal de sécurité)
    77 %         0,77      35 jours  (Gâteau de voyage boutique stabilisé)
    75 %         0,75      > 45 jours (Stabilisation par Miel / Glycérol)
    ≤ 70 %       ≤ 0,70    INHIBITION TOTALE (Zéro développement fongique)
```

*Règle d'atelier d'excellence* : Pour formuler un gâteau de voyage commercialisable sans conservateur sur **21 à 30 jours à 20 °C**, la cible impérative est :
$$\mathbf{a_w \le 0{,}75\text{ à }0{,}77}$$
Obtenue en substituant 5 à 10 % du sucre cristallisé par du miel ($\mathrm{SE} \approx 1{,}1$), du sucre inverti Trimoline ($\mathrm{SE} \approx 1{,}3$) ou de la glycérine végétale ($\mathrm{SE} = 4{,}0$).

---

## 4. Formulation & Conduite des Gâteaux de Voyage d'Excellence (Glacier & Felder)

### A. Règles d'Ingénierie d'Atelier de Stéphane Glacier MOF (*Tartes et Gâteaux de Voyage*)
1. **Technique du Beurre Manié de Moulage (p. 198)** :
   * Mélanger intimement **80 % de beurre doux fondu tiède** et **20 % de farine T55 tamisée**.
   * Laisser figer au frais jusqu'à consistance d'une pommade souple.
   * Enduire les moules au pinceau : la farine fait barrière entre le métal chaud et le sucre en cours de caramélisation, garantissant un démoulage sans déchirement de croûte.
2. **Cheminée Axiale Guidée** :
   * Avant enfournement, déposer au cornet un fin cordon de beurre pommade (ou tremper une corne dans du beurre liquide ou de l'huile neutre) le long de la ligne médiane du cake.
   * La chaleur fait fondre la zone beurrée avant la prise de croûte, canalisant la libération de vapeur et la poussée de la levure chimique dans un sillon médian net et rectiligne.
3. **Cuisson Douce Bridée sous Plaque (p. 129)** :
   * Cuisson à **145 °C en four ventilé** (ou 160 °C sole) pendant 50 à 55 minutes.
   * Poser une feuille de cuisson et une grille rigide sur le haut des moules : le cake gonfle jusqu'à venir buter sur la feuille, figeant des parois à angle droit parfaites pour les cakes contemporains parallélépipédiques.
4. **Imbibage à Froid & Barrière d'Évaporation** :
   * Dès le démoulage à chaud ou après 20 min de ressuage, badigeonner ou immerger brièvement les cakes dans un sirop froid à **30 °Baumé**.
   * Le choc thermique provoque l'aspiration instantanée du liquide à l'intérieur de la mie superficielle, créant une barrière hydro-régulatrice qui compense la perte d'eau de cuisson.

### B. Formulations Étalons de Gâteaux de Voyage

#### 1. Cake Valencia aux Amandes (Stéphane Glacier MOF, p. 129)
* Beurre noisette clarifié à chaud (cuit à 145 °C pour évaporer l'eau) : 825 g
* Blancs d'œufs tempérés à 20 °C : 885 g
* Sucre semoule blanc : 990 g
* Miel liquide toutes fleurs (humectant naturel) : 80 g
* Poudre d'amande grise avec peau : 250 g
* Poudre d'amande blanche émondée : 250 g
* Farine T55 panifiable : 330 g
* Poudre à lever chimique : 12 g
* *Procédé* : Monter les blancs au ruban avec le sucre et le miel, incorporer les poudres tamisées, finir par le beurre noisette tiède à 45 °C. Cuisson 50 min à 145 °C.

#### 2. Cake Marbré Traditionnel (Christophe Felder & Camille Lesecq, *Gâteaux*, p. 142)
* **Appareil Vanille** : Beurre doux pommade 120 g, sucre semoule 180 g, œufs entiers tempérés 150 g (3 pièces), farine T55 180 g, levure chimique 5 g, crème fleurette liquide 35 % 75 g, gousse de vanille Bourbon 1 pièce.
* **Appareil Chocolat Grand Cru** : Prélever 1/3 de l'appareil vanille, incorporer 25 g de poudre de cacao 100 % pure tamisée et 20 g de lait entier tiède pour compenser la rétention d'eau du cacao.
* *Dressage* : Alterner les couches vanille et chocolat, marbrer à la fourchette en spirale, pocher le trait de beurre axiale, cuire à 150 °C pendant 55 minutes.

#### 3. Financiers d'Orfèvrerie au Beurre Noisette
* Blancs d'œufs crus : 200 g | Sucre glace : 200 g | Poudre d'amande brute : 80 g | Farine T55 : 80 g | Miel d'acacia : 15 g | Beurre doux noisette : 180 g (cuit jusqu'à cessation du crépitement de l'eau, filtré au chinois étamine).
* Repos obligatoire de l'appareil 12 h à +4 °C. Cuisson four vif à 190 °C pendant 12 à 15 minutes pour obtenir une collerette dorée et un cœur moelleux.

---

## Renvois Croisés & Sources Primaires du Laboratoire
* Pour la résolution des pannes de tranchage, affaissement et mie dense : voir `diagnostic-defauts.md` (Section 4).
* Pour l'imperméabilisation et la cuisson des tartes d'atelier : voir `patisserie-boulangere.md` (Sections 5 et 7).
* Pour la science macromoléculaire de la rétrogradation et l'antiplastification : voir `references/science-amidon-gelatinisation.md`.
* Sources primaires : E.B. Bennion, G.S.T. Bamford & A.J. Bent (*The Technology of Cake Making 6th Ed.*, Chapitre 29, p. 386–397), Stéphane Glacier MOF (*Tartes et Gâteaux de Voyage*), Christophe Felder & Camille Lesecq (*Gâteaux*).
