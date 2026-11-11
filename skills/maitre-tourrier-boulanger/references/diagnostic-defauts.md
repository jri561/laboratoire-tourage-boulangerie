# Répertoire de Résolution d'Incidents & Diagnostic des Défauts (Troubleshooting)

Guide méthodique de résolution d'incidents en laboratoire de panification et viennoiserie mécanisée.

---

## 1. Défauts de Pousse & Fermentation

### A. Cloques blanches sous la croûte après cuisson
* **Mécanisme** : Condensation excessive dans l'étuve ou chambre froide humide saturée ($> 85\text{ \% HR}$). L'eau liquide dissout localement les sucres et hydrolyse superficiellement l'amidon. À la cuisson, cette eau vaporise brutalement sous l'épiderme en créant des cloques vitreuses.
* **Action corrective** :
  1. Abaisser l'hygrométrie de l'étuve à 75–78 % max.
  2. Assurer un ressuyage de surface de 15 minutes en froid ventilé sec avant la dorure.

### B. Grisement de la pâte et taches noires au lendemain
* **Mécanisme** : Activité de la Polyphénol Oxydase (PPO) du son de blé lors d'un stockage au froid prolongé (> 12 h) avec un pH de pâte trop élevé (> 5,6) ou une descente thermique trop lente.
* **Action corrective** :
  1. Ajouter 0,8 % de vinaigre blanc d'alcool dans l'eau de coulage pour tamponner le pH entre 5,0 et 5,2.
  2. Vérifier la descente flash en cellule : la surface doit atteindre 0 °C et le cœur < 6 °C en moins de 35 min.

### C. Affaissement des pièces lors de la cuisson directe PAC
* **Mécanisme** : Arrêt de pousse trop tardif (> 80 % du volume). La trame alvéolaire est étirée à sa limite critique de rupture ; lors du deuxième passage en froid négatif (-10 °C), la contraction thermique brise les ponts de gluten affaiblis.
* **Action corrective** :
  1. Stopper la pousse strictement à 70–75 % (le pâton doit garder une fermeté élastique sous le doigt).
  2. Vérifier la température à cœur à la sonde lors du 2e blocage : -10 °C strict.

---

## 2. Défauts de Tourage & Laminage

### A. Fuite de beurre sur plaque et semelle frite
* **Mécanisme** :
  * Films de beurre trop épais (> 45 µm), typique des schémas à 2 tours simples (9 films).
  * Température d'étuve excessive (> 27 °C) dépassant le point de fusion du beurre (34–36 °C).
* **Action corrective** :
  1. Passer impérativement au schéma 1 Tour Double + 1 Tour Simple (12 films de beurre, 25–30 µm).
  2. Plafonner la consigne d'étuve à 25–26 °C.

### B. Déchirement des pièces sur la ligne Croissomat
* **Mécanisme** : Pâte manquant d'extensibilité ($L$). Causes probables : sur-pétrissage en 2e vitesse, farine trop tenace ($P/L > 0,90$), sur-oxydation par excès d'acide ascorbique (> 2,5 % d'améliorant), ou absence de relaxation sur tapis (snapback).
* **Action corrective** :
  1. Abaisser l'améliorant à 2,0 % strict.
  2. Couper le gruau avec 30 % de T65 Tradition pure sans additifs.
  3. Laisser flotter la bande 60 secondes libres sur le tapis avant découpe.

### C. Feuilletage compact et mie briochée
* **Mécanisme** : Nombre de tours excessif (> 40 films de beurre) ou beurre trop chaud (> 16 °C) qui a fondu dans la détrempe au laminage.
* **Action corrective** :
  1. Respecter l'écart thermique pâte/beurre < 3 °C (pâte 2–4 °C, beurre sec 12–14 °C).
  2. Réduire le nombre de plis à 12 films.

---

## 3. Défauts de Biscuiterie & Pâtes Laminées Séchées (Duncan Manley)

### A. Phénomène de Checking (Craquelage différé post-cuisson)
* **Mécanisme physico-chimique selon Manley (Manual 4 & 3rd Ed.)** :
  * À la sortie du four, un gradient d'humidité résiduelle critique existe entre le centre humide ($H_{\text{centre}} \approx 4 - 7\%$) et la périphérie sèche ($H_{\text{bord}} \le 1 - 1{,}5\%$).
  * Au cours du refroidissement, l'eau migre spontanément du centre vers la périphérie pour équilibrer les potentiels hydriques.
  * En absorbant cette humidité, les parois externes subissent une expansion dimensionnelle, tandis que le centre, en séchant, se contracte.
  * Ce différentiel d'expansion/contraction crée des contraintes internes de traction qui dépassent la limite de rupture de la matrice d'amidon gélatinisé et de gluten cuit rigidifiée.
  * Il en résulte des micro-fissures capillaires invisibles à l'emballage, qui se propagent et provoquent la casse spontanée et différée des biscuits quelques heures à quelques jours après conditionnement.
* **Facteurs aggravants d'atelier** :
  * Courants d'air froid sur les tapis de sortie de four.
  * Refroidissement forcé trop brutal par ventilateurs d'air ambiant.
  * Cuisson trop vive en zone 3 masquant un sous-séchage du cœur de pâte.
* **Actions correctives** :
  1. **Règle d'or de ressuage Manley** : Le temps de refroidissement doit obligatoirement être égal à **1,5 à 2,0 fois la durée de cuisson**, sous un capot tunnel fermé et isolé évitant tout choc thermique.
  2. Régler la zone 3 du four en chaleur douce ($140 - 150\text{ }^\circ\text{C}$) avec tirage d'ouras ouvert au maximum pour ramener l'humidité globale du biscuit sous **1,5 % à 2,0 %**.
  3. Pour les lignes à haute cadence, implanter un module de séchage diélectrique haute fréquence (RF) post-cuisson : les ondes chauffent sélectivement l'eau libre du centre sans sur-colorer la bordure.
  4. Conditionner sous film thermo-scellable à haute barrière (OPP métallisé) pour maintenir l'activité de l'eau à $a_w \le 0{,}30$, bien en dessous du seuil critique de plastification de l'amidon ($a_w = 0{,}35 - 0{,}40$, Manley Manual 6).

### B. Cloquage superficiel (Blistering) et bulles d'éclatement
* **Mécanisme** : Pâte manquant de détente viscoélastique ($De \gg 1$), condensation d'eau sur le pâton en bouche de four, ou mauvaise dispersion/dissolution des poudres chimiques (notamment le carbonate acide d'ammonium / sel d'ammoniaque $\mathrm{NH_4HCO_3}$) créant des poches de gaz localisées sous l'épiderme.
* **Actions correctives** :
  1. Laisser flotter la nappe de pâte laminée au moins 60 secondes libres sur le tapis de décompression avant la tête de découpe.
  2. Dissoudre préalablement le sel d'ammoniaque et le bicarbonate dans une fraction de l'eau de coulage tiédie.
  3. Piquer systématiquement les pâtons (rouleau piqueur mécanique calibré) pour évacuer la vapeur d'eau sans cloquage.

### C. Rétraction dimensionnelle et déformation post-découpe
* **Mécanisme** : Réduction d'épaisseur trop écrasante par passe au laminoir (> 40 %) ayant sur-étiré le réseau élastique de gluten, ou tension excessive du tapis d'entraînement vers la guillotine rotative.
* **Actions correctives** :
  1. Plafonner le taux de réduction à **30–35 % par passe**.
  2. Pratiquer le laminage croisé avec rotation à 90° de la bande (*cross-laminating*) pour distribuer les tensions dans les deux directions axiales et garantir l'isotropie dimensionnelle.

---

## 4. Défauts des Pâtes Battues, Cakes de Voyage & Émulsions (Bennion, Bamford & Bent)

### A. Tranchage / Grainage de l'émulsion au crémage (Curdling & Déphasage)
* **Mécanisme selon Bennion (6e éd., Chap. 10 & 21)** :
  * Rupture de l'émulsion huile-dans-eau (o/w). Les micro-gouttelettes aqueuses apportées par les œufs ne parviennent plus à être dispersées dans la matrice lipidique continue et coalescent en poches libres de liquide.
  * Conséquence : la pâte perd sa capacité de rétention d'air, le foisonnement s'effondre, la mie devient compacte, humide et zébrée de stries vitreuses, avec une texture grasse en bouche.
* **Causes racines** :
  * Température des ovoproduits trop basse ($T_{\text{œufs}} < 15\text{ }^\circ\text{C}$) qui fige les triglycérides du beurre.
  * Incorporation trop rapide et massive des œufs entiers liquides sans temps de liaison mécanique.
  * Vitesse de mélange excessive ou insuffisante au batteur.
* **Actions correctives** :
  1. **Tempérer impérativement tous les ingrédients à 18 °C – 20 °C** avant démarrage du crémage.
  2. Incorporer les œufs de façon très fractionnée (par fractions de 10 à 15 % du volume total), en laissant l'appareil reprendre une texture crémeuse et lisse entre chaque apport.
  3. En cas d'amorce de tranchage, ajouter immédiatement 5 % de la farine tamisée prévue dans la recette : l'amidon absorbe l'eau libre excédentaire et rétablit la consistance colloïdale.
  4. Pour les formulations industrielles riches en sucre et liquide (*High Ratio*), utiliser des émulsifiants alpha-gel (monoglycérides distillés ou esters de polyglycérol PGE).

### B. Affaissement central au four (Cratère / Effondrement de la mie)
* **Mécanisme** : Sur-foisonnement d'air lors du crémage mécanique ou surdosage d'agents levants chimiques amenant une densité relative trop faible ($\mathrm{RD} < 0{,}65$). Lors de la cuisson, la pression de vapeur d'eau dilate les micro-bulles au-delà de la capacité de résistance du réseau protéique et de l'amidon avant leur gélatinisation thermique. Les bulles coalescent, les parois éclatent, les gaz s'échappent et le centre du gâteau s'effondre sous son propre poids.
* **Actions correctives** :
  1. Contrôler rigoureusement la densité relative de l'appareil cru : **cibler $\mathrm{RD} = 0{,}70 - 0{,}85$**.
  2. Réduire le dosage de levure chimique (baking powder) à 1,0 – 1,5 % du poids de farine.
  3. Vérifier la chauffe de sole du four : une chaleur de sole insuffisante retarde la fixation de la base et amplifie l'effondrement central.

### C. Mie dense, serrée et lourde (Sous-développement de structure)
* **Mécanisme** : Sous-foisonnement d'air au crémage ($\mathrm{RD} > 0{,}90$), poudres à lever éventées ou sous-dosées, ou développement intempestif du réseau de gluten (*corsage*) lors du mélange final de la farine.
* **Actions correctives** :
  1. Conduire le crémage beurre-sucre pendant 8 à 10 minutes à vitesse moyenne jusqu'à blanchiment et texture mousseuse légère.
  2. Incorporer la farine tamisée délicatement à vitesse lente (1re vitesse ou maryse manuelle), en stoppant immédiatement dès disparition des traces de farine.

### D. Croûte poisseuse et collante après emballage
* **Mécanisme** : Activité de l'eau excessive ($a_w > 0{,}82$) provoquant la dissolution superficielle des sucres de surface, ou ensachage prématuré sur gâteau tiède emprisonnant la vapeur condensée sous le film étanche.
* **Actions correctives** :
  1. Rééquilibrer la formule selon la méthode des Équivalents Sucrose de Grover (Bennion Chap. 29, p. 386–397) : substituer 10 à 15 % du saccharose par du miel, du glycérol ($\mathrm{SE} = 4{,}0$) ou du sorbitol ($\mathrm{SE} = 2{,}0$) pour lier l'eau libre et abaisser l'activité de l'eau sous **$a_w \le 0{,}75$**.
  2. Laisser ressuer les gâteaux au minimum 2 heures à température ambiante jusqu'à température à cœur $< 25\text{ }^\circ\text{C}$ avant mise sous sachet barrière.

---

## 5. Défauts de Gélatinisation de l'Amidon & Texturation des Crèmes (Sjöö & Nilsson, Eliasson)

### A. Liquéfaction et synérèse des crèmes et flans pâtissiers au repos
* **Mécanisme physico-chimique selon Sjöö & Nilsson (2e éd., Chap. 15) et Eliasson** :
  * *Sous-cuisson enzymatique* : Si la crème n'a pas atteint la température critique de dénaturation complète ($> 82 - 85\text{ }^\circ\text{C}$) ou n'a pas été maintenue pendant au moins **2 minutes complètes à ébullition vive**, les alpha-amylases endogènes naturellement présentes dans les jaunes d'œufs ne sont pas détruites. Ces enzymes continuent de cliver enzymatiquement les macromolécules d'amylose et d'amylopectine à froid, liquéfiant le gel et provoquant un suintement massif de phase aqueuse (synérèse).
  * *Antiplastification par excès de sucre* : Une concentration très élevée en saccharose immobilise l'eau libre et repousse le point de gélatinisation de l'amidon de blé ou de maïs de 60 °C à plus de 80–90 °C. Si la chauffe est interrompue trop tôt, les granules ne gonflent pas et le gel ne se forme pas.
* **Actions correctives** :
  1. Maintenir une **ébullition franche et active pendant 2 minutes complètes chrono** au fond de la casserole sous fouettage énergique.
  2. Respecter le ratio d'amidon de maïs / poudre à crème : 90 g à 100 g par litre de liquide.
  3. Laisser refroidir le flan cuit 4 h à température ambiante puis 4 h à +4 °C strict avant découpe pour stabiliser le gel d'amylose.

### B. Rétrogradation brutale et texture caoutchouteuse cassante
* **Mécanisme** : Réassociation et cristallisation excessive des chaînes linéaires d'amylose au froid positif (+2 °C à +4 °C), expulsant l'eau hors du réseau gélifié et donnant un aspect granuleux et dur.
* **Actions correctives** :
  1. Remplacer 20 à 30 % de la poudre à crème par de l'amidon de maïs cireux (*waxy maize*, 100 % amylopectine) ou de la fécule de tapioca acétylée, insensible à la rétrogradation à court terme.
  2. Émulsionner 3 à 5 % de beurre doux hors du feu : les acides gras et monoglycérides forment des **complexes d'inclusion hélicoïdaux en V avec l'amylose** (Eliasson Chap. 15), bloquant stériquement sa recristallisation.

### C. Déphasage et structure spongieuse à la décongélation (Pâtes et inserts PAC)
* **Mécanisme** : Lors de la conservation en froid négatif instable (fluctuations thermiques à $-15\text{ }^\circ\text{C}$ au lieu de $-18\text{ }^\circ\text{C}$), le phénomène de **mûrissement d'Ostwald** induit la fusion des petits cristaux de glace et leur redéposition sous forme de gros cristaux acérés. Ces macro-cristaux déchirent les granules d'amidon gélatinisés et perforent la matrice protéique. À la décongélation, l'eau libérée ne peut plus être réabsorbée par les chaînes rétrogradées et s'écoule hors du produit.
* **Actions correctives** :
  1. Stocker impérativement les pièces et pâtons sous **$-18\text{ }^\circ\text{C}$ strict**, bien en dessous de la température de transition vitreuse maximale cryo-concentrée $T_g'$ ($-12\text{ }^\circ\text{C}$ à $-15\text{ }^\circ\text{C}$, Goff).
  2. Pour les garnitures de fruits et crèmes destinées à la surgélation, employer exclusivement des amidons modifiés réticulés stables aux cycles gel/dégel ou de la pectine NH thermo-réversible.

---

## Renvois Croisés & Sources Primaires du Laboratoire
* Pour la thermodynamique des fours et la cinétique du checking : voir `references/biscuiterie-cookies-laminage.md` et Manley Manual 4.
* Pour la physico-chimie des émulsions et le calcul de l'activité de l'eau de Grover : voir `references/pates-battues-cakes-emulsions.md` et Bennion Chapitre 29 (p. 386–397).
* Pour la macromolécule d'amidon, les courbes RVA et la cryobiologie $T_g'$ : voir `references/science-amidon-gelatinisation.md`, Sjöö & Nilsson (2017) et Eliasson (2004).

