import os
import json
import subprocess

BASE_DIR = '/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie'
EXPORTS_DIR = os.path.join(BASE_DIR, 'exports_pdf')
SUMMARY_JSON = os.path.join(BASE_DIR, 'scripts', 'extracted_summary.json')
PREVIEWS_DIR = os.path.join(EXPORTS_DIR, 'previews_cahier_m3')
os.makedirs(EXPORTS_DIR, exist_ok=True)
os.makedirs(PREVIEWS_DIR, exist_ok=True)

COMMON_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

@page {
  size: A4 portrait;
  margin: 0;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

body {
  margin: 0;
  padding: 0;
  background: #ffffff;
  font-variant-numeric: tabular-nums;
  -webkit-font-smoothing: antialiased;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  color: #0f172a;
}

.page {
  width: 210mm;
  height: 297mm;
  position: relative;
  overflow: hidden;
  page-break-after: always;
}

.page:last-child {
  page-break-after: auto;
}

.page-left {
  padding: 15mm 18mm 14mm 14mm;
}

.page-right {
  padding: 15mm 14mm 14mm 18mm;
}
"""

CSS_M3 = """
.m3 {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  color: #0f172a;
  background: #ffffff;
}

.m3-topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #0f172a;
  color: #ffffff;
  padding: 4.2mm 5.5mm;
  border-radius: 3px;
  margin-bottom: 6mm;
  gap: 4mm;
}

.m3-title {
  font-size: 15.5pt;
  font-weight: 800;
  letter-spacing: -0.3px;
  line-height: 1.15;
}

.m3-badge {
  background: #2563eb;
  color: #ffffff;
  font-size: 8.2pt;
  font-weight: 700;
  padding: 1.5mm 3.2mm;
  border-radius: 2px;
  white-space: nowrap;
  flex-shrink: 0;
}

.m3-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 6.5mm;
}

.m3-table th {
  font-size: 7.8pt;
  font-weight: 700;
  text-transform: uppercase;
  color: #475569;
  border-bottom: 2px solid #0f172a;
  padding: 1.8mm 2mm;
  text-align: left;
}

.m3-table th.num, .m3-table td.num {
  text-align: right;
  white-space: nowrap;
}

.m3-table td {
  font-size: 9.5pt;
  padding: 2.0mm 2mm;
  border-bottom: 1px solid #e2e8f0;
}

.m3-table td.num {
  font-weight: 700;
  font-size: 10pt;
}

.m3-table.compact td {
  font-size: 8.7pt;
  padding: 1.45mm 1.8mm;
}

.m3-table.compact td.num {
  font-size: 9.2pt;
}

.m3-dot {
  display: inline-block;
  width: 2.4mm;
  height: 2.4mm;
  border-radius: 50%;
  margin-right: 2mm;
  vertical-align: middle;
}

.dot-1 { background: #2563eb; }
.dot-2 { background: #d97706; }
.dot-3 { background: #16a34a; }

.m3-table tr.subtotal td {
  background: #f1f5f9;
  font-weight: 700;
  border-top: 1.5px solid #64748b;
  border-bottom: 1.5px solid #64748b;
}

.m3-table tr.total td {
  background: #eff6ff;
  color: #1e3a8a;
  font-weight: 800;
  font-size: 10.2pt;
  border-top: 2px solid #2563eb;
  border-bottom: 2px solid #2563eb;
}

.m3-table.compact tr.total td {
  font-size: 9.5pt;
}

.m3-h2 {
  font-size: 9.8pt;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #0f172a;
  margin-bottom: 3mm;
  display: flex;
  align-items: center;
  gap: 2mm;
}

.m3-chrono {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 3mm;
  margin-bottom: 5.5mm;
}

.m3-chrono-item {
  border: 1px solid #cbd5e1;
  border-radius: 3px;
  padding: 3mm 4mm;
}

.m3-chrono-item .m3-step-head {
  display: block;
  font-size: 9.5pt;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 0.8mm;
}

.m3-chrono-item span {
  font-size: 8.6pt;
  color: #475569;
  line-height: 1.32;
}

.m3-big-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 3.5mm;
  margin-bottom: 5.5mm;
}

.m3-big-box {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-radius: 3px;
  padding: 3mm 3.5mm;
  text-align: center;
}

.m3-big-box .val {
  font-size: 13pt;
  font-weight: 800;
  color: #0f172a;
}

.m3-big-box .lbl {
  font-size: 7.2pt;
  font-weight: 600;
  text-transform: uppercase;
  color: #64748b;
  margin-top: 0.8mm;
}

.m3-alert {
  background: #fef2f2;
  border: 1.5px solid #ef4444;
  color: #991b1b;
  border-radius: 3px;
  padding: 3.2mm 4.5mm;
  font-size: 9.2pt;
  font-weight: 700;
  text-align: center;
  margin-top: 3mm;
}

.m3-footer {
  position: absolute;
  bottom: 9mm;
  left: 14mm;
  right: 14mm;
  display: flex;
  justify-content: space-between;
  font-size: 7.5pt;
  color: #94a3b8;
  border-top: 1px solid #f1f5f9;
  padding-top: 2mm;
}

/* Couverture & Sommaire */
.m3-cover {
  padding: 22mm 20mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: #0f172a;
  color: #ffffff;
}

.m3-cover-kicker {
  font-size: 9.5pt;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: #60a5fa;
  margin-bottom: 6mm;
}

.m3-cover-title {
  font-size: 34pt;
  font-weight: 800;
  line-height: 1.08;
  letter-spacing: -0.8px;
  margin-bottom: 6mm;
}

.m3-cover-sub {
  font-size: 13pt;
  color: #cbd5e1;
  line-height: 1.45;
  max-width: 140mm;
}

.m3-cover-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 5mm;
  margin-top: 14mm;
}

.m3-cover-card {
  border: 1px solid #334155;
  background: #1e293b;
  border-radius: 4px;
  padding: 5mm;
}

.m3-cover-card .num {
  font-size: 18pt;
  font-weight: 800;
  color: #60a5fa;
  margin-bottom: 1.5mm;
}

.m3-cover-card .txt {
  font-size: 9.5pt;
  color: #e2e8f0;
  line-height: 1.35;
}

.m3-cover-foot {
  border-top: 1px solid #334155;
  padding-top: 6mm;
  display: flex;
  justify-content: space-between;
  font-size: 8.5pt;
  color: #94a3b8;
}

.toc-pole {
  margin-bottom: 6mm;
}

.toc-pole-title {
  font-size: 9.5pt;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.4px;
  color: #0f172a;
  background: #f1f5f9;
  border-left: 3.5px solid #2563eb;
  padding: 2mm 3mm;
  margin-bottom: 2.5mm;
}

.toc-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 1.8mm 2mm;
  border-bottom: 1px solid #e2e8f0;
  font-size: 9.3pt;
}

.toc-code {
  font-weight: 700;
  color: #2563eb;
  width: 24mm;
  flex-shrink: 0;
  font-size: 8.5pt;
}

.toc-name {
  font-weight: 600;
  color: #0f172a;
  flex: 1;
}

.toc-pages {
  font-weight: 700;
  color: #475569;
  width: 22mm;
  text-align: right;
  font-size: 8.8pt;
}

.legend-box {
  border: 1px solid #cbd5e1;
  background: #f8fafc;
  border-radius: 3px;
  padding: 4mm 5mm;
  margin-top: 8mm;
}

.legend-title {
  font-size: 9pt;
  font-weight: 800;
  text-transform: uppercase;
  margin-bottom: 2.5mm;
  color: #0f172a;
}

.legend-item {
  font-size: 8.6pt;
  color: #334155;
  margin-bottom: 1.5mm;
  line-height: 1.35;
}
"""

# Données opérationnelles exactes issues des 24 fiches de recettes/catalogue/
SPECS = {
    "V-PLF-01": {
        "title": "CROISSANT PUR BEURRE PAC",
        "badge": "V-PLF-01 • 130 PCS / BAC",
        "right_badge": "12 FILMS",
        "sec2": "2. Pétrissage & Froid (J-1)",
        "steps2": [
            ("Frasage : 5 min V1", "Verser poudres et liquides bleus en cuve. Éloigner la levure du sel."),
            ("Pétrissage : 4 min 30 s V2", "Ajouter margarine Opal. Stop impératif au 1er décollement."),
            ("Sortie cuve : 20–21 °C", "Diviser à <strong>8 000 g</strong> par bac. Étaler en galette de 3 cm."),
            ("Flash : 30–35 min à -35 °C", "Puis stocker 12 à 15 h à <strong>0 / +1,5 °C</strong>."),
        ],
        "sec3": "3. Tourage Laminoir (Jour J)",
        "steps3": [
            ("1. Enchâssement", "Pâte +2/+4 °C • Beurre +12/+14 °C. Rabattre bord à bord."),
            ("2. Tour Double (4 plis)", "Allonger 85–90 cm, plier en 4. Repos <strong>15 min à +2 °C</strong>."),
            ("3. Tour Simple (3 plis)", "Pivot 90°, allonger 60–65 cm, plier en 3."),
            ("4. Drossage & Détente", "Rogner 4 bords sur 5 mm. Repos <strong>45 min à +2 °C</strong>."),
        ],
        "sec4": "4. Découpe & Croissomat SCM50",
        "calibres": [("3,5 mm", "Épaisseur bande"), ("120 × 190", "Triangle (mm)"), ("75 g ± 1 g", "Poids cru")],
        "steps4": [
            ("Manettes SCM50", "Droite : <strong>2,2–2,5</strong> • Gauche : <strong>3,0–3,2</strong> • Bas : <strong>7,5–8,0</strong>"),
            ("Farinage & Clé", "Face farinée contre le tapis. Clé posée <strong>en dessous à 6 h</strong>."),
        ],
        "sec5": "5. Cuisson Directe Congelé (-18 °C)",
        "cuisson": [("160–165 °C", "Four ventilé"), ("3 s", "Buée départ"), ("16–18 min", "Temps total")],
        "alert": "ZÉRO DÉCONGÉLATION • OUVRIR L'OURA À 14 MINUTES • RESSUAGE 15 MIN SUR GRILLE",
    },
    "V-PLF-02": {
        "title": "PAIN AU CHOCOLAT ÉQUERRE PAC",
        "badge": "V-PLF-02 • 130 PCS / BAC",
        "right_badge": "12 FILMS",
        "sec2": "2. Pétrissage & Froid (J-1)",
        "steps2": [
            ("Frasage : 5 min V1", "Poudres et liquides bleus. Levure séparée du sel."),
            ("Pétrissage : 4 min 30 s V2", "Ajouter margarine Opal. Stop au 1er décollement."),
            ("Sortie cuve : 20–21 °C", "Diviser à <strong>8 000 g</strong> par bac. Étaler sur 3 cm."),
            ("Flash : 30–35 min à -35 °C", "Puis stocker 12 à 15 h à <strong>0 / +1,5 °C</strong>."),
        ],
        "sec3": "3. Tourage Unifié (1D + 1S)",
        "steps3": [
            ("1. Enchâssement", "Pâte +2/+4 °C • Beurre +12/+14 °C. Rabattre bord à bord."),
            ("2. Tour Double (4 plis)", "Allonger 85–90 cm, plier en 4. Repos <strong>15 min à +2 °C</strong>."),
            ("3. Tour Simple (3 plis)", "Pivot 90°, allonger 60–65 cm, plier en 3."),
            ("4. Drossage & Détente", "Rogner 4 bords. Repos <strong>45 min à +2 °C</strong> sous film."),
        ],
        "sec4": "4. Façonnage & Barre Chocolat",
        "calibres": [("3,5 mm", "Abaisse bande"), ("10 g (160)", "Barre chocolat"), ("85 g brut", "75 g pâte + 10 g")],
        "steps4": [
            ("Pose barre 10 g", "Bande ~42–44 cm. Poser 1 barre à 2–3 cm du bord d'attaque."),
            ("Roulage & Clé", "Enrouler sans serrer. Clé calée <strong>en dessous</strong> sur plaque."),
        ],
        "sec5": "5. Cuisson Directe Congelé (-18 °C)",
        "cuisson": [("160–165 °C", "Four ventilé"), ("3 s", "Buée départ"), ("18–20 min", "Temps total")],
        "alert": "ZÉRO DÉCONGÉLATION • OUVRIR LES OURAS À 14 MINUTES • RESSUAGE SUR GRILLE",
    },
    "V-PLF-03": {
        "title": "PAIN AUX RAISINS ESCARGOT PAC",
        "badge": "V-PLF-03 • 175 PCS / BAC",
        "right_badge": "12 FILMS",
        "sec2": "2. Pétrissage & Crème Pâtissière",
        "steps2": [
            ("Pâte : 5 min V1 + 4,5 min V2", "Sortie 20–21 °C. Flash 30 min à -35 °C puis +1 °C."),
            ("Crème à froid", "Mixer eau + lait froid + préparation crème <strong>3 min V2</strong>."),
            ("Raisins sultanines", "Égoutter ou peser nets, sans cristaux ni rafles."),
            ("Sirop 44° Brix", "1 000 g eau + 800 g sucre : bouillir <strong>1 min</strong>, refroidir."),
        ],
        "sec3": "3. Tourage & Garnissage Polyline",
        "steps3": [
            ("1. Tourage 1D + 1S", "Même conduite que croissant (12 films). Détente 45 min +2 °C."),
            ("2. Abaisse fine : 3,0 mm", "Largeur bande 40–42 cm. Température bande 10–12 °C."),
            ("3. Étaler crème & raisins", "Crème souple sur bande (laisser 2 cm de bord nu mouillé)."),
            ("4. Roulage & Tranchage", "Rouler en boudin serré, bloquer au froid puis trancher."),
        ],
        "sec4": "4. Calibres & Mise en Plaque",
        "calibres": [("3,0 mm", "Abaisse bande"), ("90 g brut", "55+20+15 g"), ("175–178 pcs", "Par bac")],
        "steps4": [
            ("Queue sous la pièce", "Replier la queue finale <strong>sous l'escargot</strong> pour éviter l'ouverture."),
            ("Lustrage sortie four", "Passer le sirop 44° Brix <strong>froid</strong> dès la sortie sur pièces chaudes."),
        ],
        "sec5": "5. Cuisson Directe Congelé (-18 °C)",
        "cuisson": [("160–165 °C", "Four ventilé"), ("3 s", "Buée départ"), ("16–18 min", "Temps total")],
        "alert": "OUVRIR LES OURAS À 13–14 MINUTES • LUSTRAGE AU SIROP FROID SUR PIÈCES CHAUDES",
    },
    "V-PLF-04": {
        "title": "PAIN SUISSE CHOCOLATINE PAC",
        "badge": "V-PLF-04 • 130 PCS / BAC",
        "right_badge": "12 FILMS",
        "sec2": "2. Pétrissage & Crème Pépites",
        "steps2": [
            ("Pâte : 5 min V1 + 4,5 min V2", "Sortie 20–21 °C. Flash 30 min à -35 °C puis +1 °C."),
            ("Crème pâtissière", "Eau + poudre lait + mix crème : <strong>3 min V2</strong>. Filmer à +4 °C."),
            ("Pépites cuisson", "Calibre 500–600 pcs/100 g, réparties régulièrement sur crème."),
            ("Stockage détrempe", "8 000 g/bac en plaque 3 cm, repos 12–15 h à +1 °C."),
        ],
        "sec3": "3. Tourage & Montage",
        "steps3": [
            ("1. Tourage 1D + 1S", "12 films identiques au croissant. Repos 45 min à +2 °C."),
            ("2. Abaisse : 3,0 mm", "Bande large 46–48 cm. Laisser détendre 60 s sur tapis."),
            ("3. Garniture centrale", "Étaler la crème sur une moitié + parsemer les pépites."),
            ("4. Pliage & Découpe", "Rabattre la pâte sur la crème, dorer/souder, découper net."),
        ],
        "sec4": "4. Calibres & Pose Plaque",
        "calibres": [("3,0 mm", "Abaisse bande"), ("110 g brut", "75+25+10 g"), ("130 pcs", "Par bac")],
        "steps4": [
            ("Soudure ferme", "Souder la bordure au pinceau humide avant découpe guillotine."),
            ("Espacement plaque", "Poser soudure dessous, espacer pour la pousse et le feuilletage."),
        ],
        "sec5": "5. Cuisson Directe Congelé (-18 °C)",
        "cuisson": [("160–165 °C", "Four ventilé"), ("3 s", "Buée départ"), ("15–17 min", "Temps total")],
        "alert": "OUVRIR LES OURAS À 13 MINUTES POUR SÉCHER ET CROUSTILLER LA CROÛTE",
    },
    "V-PLF-05": {
        "title": "ORANAIS AUX ABRICOTS PAC",
        "badge": "V-PLF-05 • 140 PCS / BAC",
        "right_badge": "12 FILMS",
        "sec2": "2. Pétrissage & Préparation",
        "steps2": [
            ("Pâte : 5 min V1 + 4,5 min V2", "Sortie 20–21 °C. Flash 30 min à -35 °C puis +1 °C."),
            ("Crème pâtissière", "Mélanger au fouet 3 min V2. Maintenir fraîche à +4 °C."),
            ("Abricots oreillons", "Égoutter soigneusement sur grille avant la dépose."),
            ("Sirop de lustrage", "Préparer sirop 44° Brix froid pour la finition sortie four."),
        ],
        "sec3": "3. Tourage & Façonnage Carré",
        "steps3": [
            ("1. Tourage 1D + 1S", "12 films (1 Tour Double + 1 Tour Simple). Repos 45 min +2 °C."),
            ("2. Abaisse : 3,0 mm", "Largeur bande ~48 cm. Détente sur tapis avant découpe."),
            ("3. Carrés + Crème", "Découper des carrés réguliers. Dresser la crème en diagonale."),
            ("4. Oreillons & Pliage", "Poser 2 demi-abricots, rabattre les 2 pointes opposées au centre."),
        ],
        "sec4": "4. Calibres & Finition",
        "calibres": [("3,0 mm", "Abaisse bande"), ("2 oreillons", "Abricots / pce"), ("140 pcs", "Par bac")],
        "steps4": [
            ("Soudure centrale", "Humidifier légèrement les 2 pointes et presser ferme au centre."),
            ("Lustrage brillant", "Lustrer les abricots au sirop froid dès la sortie du four."),
        ],
        "sec5": "5. Cuisson Directe Congelé (-18 °C)",
        "cuisson": [("160–165 °C", "Four ventilé"), ("3 s", "Buée départ"), ("15–17 min", "Temps total")],
        "alert": "OUVRIR LES OURAS À 13 MINUTES POUR ÉVACUER LA VAPEUR DE L'ABRICOT",
    },
    "V-PLF-06": {
        "title": "CINNAMON ROLL FEUILLETÉ PAC",
        "badge": "V-PLF-06 • 140 PCS / BAC",
        "right_badge": "12 FILMS",
        "sec2": "2. Pétrissage & Mélange Cannelle",
        "steps2": [
            ("Pâte : 5 min V1 + 4,5 min V2", "Sortie 20–21 °C. Flash 30 min à -35 °C puis +1 °C."),
            ("Beurre pommade", "Assouplir le beurre d'appareil à 18–20 °C (texture crémeuse)."),
            ("Sucre cannelle", "Mélanger cassonade + cannelle moulue à sec avant étalage."),
            ("Glaçage / Sirop", "Sirop 44° Brix dès sortie four ou glaçage royal à tiède."),
        ],
        "sec3": "3. Tourage & Roulage",
        "steps3": [
            ("1. Tourage 1D + 1S", "12 films (1 Tour Double + 1 Tour Simple). Repos 45 min +2 °C."),
            ("2. Abaisse : 2,8–3,0 mm", "Bande ~40 cm. Température de bande 10–12 °C."),
            ("3. Tartinage & Sucre", "Étaler beurre pommade, saupoudrer le mélange sucre-cannelle."),
            ("4. Roulage & Moules", "Rouler serré, trancher net et déposer en cercles ou moules."),
        ],
        "sec4": "4. Calibres & Pose",
        "calibres": [("2,8–3,0 mm", "Abaisse bande"), ("~40 cm", "Largeur bande"), ("140 pcs", "Par bac")],
        "steps4": [
            ("Tranchage net", "Bloquer le boudin au froid avant découpe pour des spires nettes."),
            ("Finition tiède", "Napper au sirop 44° Brix ou glacer dès tiédissement."),
        ],
        "sec5": "5. Cuisson Directe Congelé (-18 °C)",
        "cuisson": [("160–165 °C", "Four ventilé"), ("2–3 s", "Buée départ"), ("15–17 min", "Temps total")],
        "alert": "OUVRIR LES OURAS À 12–13 MINUTES POUR CARAMÉLISER SANS BRÛLER LE SUCRE",
    },
    "V-PLF-07": {
        "title": "CRUFFIN FEUILLETÉ D'ATELIER PAC",
        "badge": "V-PLF-07 • 122 PCS / BAC",
        "right_badge": "12 FILMS",
        "sec2": "2. Pétrissage & Froid (J-1)",
        "steps2": [
            ("Frasage : 5 min V1", "Ingrédients bleus en cuve, levure éloignée du sel."),
            ("Pétrissage : 4 min 30 s V2", "Ajouter margarine Opal. Stop au 1er décollement."),
            ("Sortie cuve : 20–21 °C", "Diviser à <strong>8 000 g</strong> par bac. Étaler sur 3 cm."),
            ("Flash : 30–35 min à -35 °C", "Puis stocker 12 à 15 h à <strong>0 / +1,5 °C</strong>."),
        ],
        "sec3": "3. Tourage & Façonnage Nœud",
        "steps3": [
            ("1. Tourage 1D + 1S", "12 films (1 Tour Double + 1 Tour Simple). Repos 45 min +2 °C."),
            ("2. Abaisse fine : 2,5 mm", "Bande ~48–50 cm pour éviter tout point lourd en alvéole."),
            ("3. Bandelettes & Fente", "Découper bandelettes, fendre axialement sans couper le bout."),
            ("4. Roulage en turban", "Enrouler feuillets tranchés vers l'extérieur en moules graissés."),
        ],
        "sec4": "4. Calibres & Moules",
        "calibres": [("2,5 mm", "Abaisse fine"), ("80 g brut", "Poids cru"), ("122–125 pcs", "Par bac")],
        "steps4": [
            ("Orientation feuillets", "Feuilletage tranché orienté <strong>vers le haut</strong> dans l'alvéole."),
            ("Enrobage à chaud", "Démouler brûlant sur grille et rouler au sucre vanillé."),
        ],
        "sec5": "5. Cuisson Directe (Silicone / Métal)",
        "cuisson": [("165–170 °C", "Four ventilé"), ("3 s", "Buée départ"), ("20–22 min", "Silicone (17–19 métal)")],
        "alert": "OUVRIR LES OURAS À 16–17 MIN (14 MIN MÉTAL) • DÉMOULER BRÛLANT DÈS SORTIE",
    },
    "V-KOU-01": {
        "title": "KOUIGN-AMANN BRETON PAC",
        "badge": "V-KOU-01 • 88 INDIV / BAC",
        "right_badge": "9 FILMS",
        "sec2": "2. Pétrissage & Masse Sucre-Beurre",
        "steps2": [
            ("Frasage : 7 min V1", "Ingrédients bleus, eau glacée. Zéro pointage."),
            ("Pétrissage : 3–4 min V2", "Sortie cuve <strong>20–21 °C</strong>. Galette 3 cm."),
            ("Flash : 20 min à -35 °C", "Bloquer à cœur sous +4 °C."),
            ("Plaque Sucre-Beurre", "2 000 g beurre 84 % + 1 800 g sucre + 20 g fleur de sel (+4 °C)."),
        ],
        "sec3": "3. Tourage : 2 Tours Simples",
        "steps3": [
            ("1. Enchâssement", "Envelopper la plaque sucre-beurre (3 820 g) dans la détrempe."),
            ("2. 1er Tour Simple (10 mm)", "Plier en 3. Repos <strong>15 min à +2 °C</strong>."),
            ("3. 2e Tour Simple (8 mm)", "Pivot 90°, plier en 3. Drossage des chants."),
            ("4. Flash Moules : 45 min -35 °C", "Démouler gelé, stocker -18 °C. Décongeler 12 h à +4 °C."),
        ],
        "sec4": "4. Calibres & Pousse Douce",
        "calibres": [("6 mm / 4 mm", "Indiv / Partage"), ("100 g / 400 g", "Indiv / 4 pers."), ("88 / 22 pcs", "Par bac 8,82 kg")],
        "steps4": [
            ("Pousse 23–24 °C max", "2 h à 2 h 30 (75 % HR) en moule silicone avec cassonade au fond."),
            ("Grille permanente", "Feuille sulfurisée + grille inox posée dessus avant enfournement."),
        ],
        "sec5": "5. Cuisson Sous Grille Permanente",
        "cuisson": [("200 -> 175 °C", "Flash 1 min -> 175 °C"), ("Oura fermé", "Puis ouvert 5–6 min"), ("24–30 min", "Selon format")],
        "alert": "OURAS À FOND LES 5–6 DERNIÈRES MIN • RETOURNER SUR GRILLE APRÈS 4–6 MIN DE REPOS",
    },
    "P-FEU-01": {
        "title": "FEUILLETAGE INVERSÉ UNIVERSEL",
        "badge": "P-FEU-01 • 4 PÂTONS (29,14 KG)",
        "right_badge": "48 STRATES",
        "sec2": "2. Beurre Manié & Détrempe (J-1)",
        "steps2": [
            ("Beurre Manié (13 000 g)", "Beurre Debic 82 % (+12/+14 °C) + farine. Cadrer 4 × 3 250 g à +4 °C."),
            ("Margarine OPAL cuve", "Dés froids (+16/+18 °C) en détrempe. Zéro fonte."),
            ("Détrempe (16 140 g)", "Frasage court sans élasticité. Cadrer 4 × 4 035 g à +4 °C."),
            ("Règle thermique", "Jamais de froid négatif entre tours : garder pâton à +10/+12 °C."),
        ],
        "sec3": "3. Conduite 3 Tours (1S + 2D)",
        "steps3": [
            ("1. Enchâssement inversé", "Détrempe (4 035 g) enfermée dans le beurre manié (3 250 g)."),
            ("2. 1er Tour Simple (3 plis)", "Allonger à 8 mm par passes ≤ 20 %. Pivoter 90°."),
            ("3. 2e Tour Double (4 plis)", "Plier en portefeuille. Repos <strong>1 h 30–2 h à +4 °C</strong>."),
            ("4. 3e Tour Double (4 plis)", "Pivot 90°, allonger 8 mm, plier en 4. Maturation 12–24 h à +4 °C."),
        ],
        "sec4": "4. Abaisse en Croix & Rognures",
        "calibres": [("3,0 mm", "Galettes / Tartes"), ("7 285 g", "Poids 1 pâton"), ("48 strates", "Feuilletage pur")],
        "steps4": [
            ("Laminage en croix", "Passes ≤ 20 %. Laisser flotter <strong>15 min sur tapis</strong> avant découpe."),
            ("Rognures zéro déchet", "Réunir à plat, repos 2 h à +4 °C, abaisser à 2,5–3,0 mm."),
        ],
        "sec5": "5. Cuisson Référence (Feuilletage)",
        "cuisson": [("185 °C", "Four ventilé / sole"), ("Oura ouvert", "Fin de cuisson"), ("25–45 min", "Selon garniture")],
        "alert": "ZÉRO FROID NÉGATIF ENTRE TOURS • REPOS 15 MIN SUR TAPIS AVANT DÉCOUPE",
    },
    "V-VIE-01": {
        "title": "PAIN VIENNOIS NATURE PAC",
        "badge": "V-VIE-01 • 20 PCS / BAC",
        "right_badge": "MÉTHODE DIRECTE",
        "sec2": "2. Pétrissage Haute Rétention",
        "steps2": [
            ("Frasage : 5 min V1", "Ingrédients bleus en cuve avec couple Soft'r / Kimo."),
            ("Pétrissage : 7–8 min V2", "4 min lissage + 3–4 min jusqu'au <strong>voile complet</strong>."),
            ("Sortie cuve : 19–21 °C", "Pointage en cuve filmée : <strong>15–20 min</strong> à 20–22 °C."),
            ("Division : 5 600 g / bac", "Diviser 20 parts de 280 g. Détente 8–10 min sous bâche."),
        ],
        "sec3": "3. Façonnage & Stocks PAC",
        "steps3": [
            ("1. Façonnage & Scarification", "Façonner en baguettes 22–24 cm. Dorer avant cellule/étuve."),
            ("2. Stock 1 (Cru non poussé)", "Flash <strong>35 min à -35 °C</strong> -> stockage à -18 °C."),
            ("3. Pousse (26 °C / 80 % HR)", "<strong>1 h 45 à 2 h 00</strong>. Puis 10 min à +4 °C."),
            ("4. Stock 2 PAC (Prêt-à-cuire)", "Flash -35 °C jusqu'à <strong>-10 °C à cœur</strong> -> -18 °C."),
        ],
        "sec4": "4. Calibres & Rendement",
        "calibres": [("280 g cru", "~266 g cuit"), ("22–24 cm", "Longueur pièce"), ("20 pcs / bac", "10 / plaque")],
        "steps4": [
            ("1re Dorure Végétale", "Appliquer au pinceau avant mise en cellule ou en étuve."),
            ("Décongélation Stock 1", "Si départ cru gelé : 8–10 h à +2/+4 °C avant étuve."),
        ],
        "sec5": "5. Cuisson Directe Congelé (-18 °C)",
        "cuisson": [("180 -> 165 °C", "Préchauffage -> Régul."), ("Oura fermé", "11 min strictes"), ("11 min", "Temps exact")],
        "alert": "ZÉRO DÉCONGÉLATION • OURAS STRICTEMENT FERMÉS PENDANT LES 11 MINUTES",
    },
    "V-VIE-02": {
        "title": "PAIN VIENNOIS CHOCOLAT PAC",
        "badge": "V-VIE-02 • 40 PCS / BAC",
        "right_badge": "MÉTHODE DIRECTE",
        "sec2": "2. Pétrissage Anti-Marbrage",
        "steps2": [
            ("Frasage : 5 min V1", "Ingrédients bleus en cuve. Température cible stricte."),
            ("Pétrissage : 4 min V2", "Ajouter margarine Opale tempérée à 14–16 °C en petits dés."),
            ("Pépites : 45–60 s en V1", "Repasser en <strong>1re vitesse lente</strong> pour zéro marbrage."),
            ("Sortie : 19–21 °C", "Pointage cuve filmée 15–20 min. Bacs de 5 600 g."),
        ],
        "sec3": "3. Division 20×2 & Stocks PAC",
        "steps3": [
            ("1. Division 20×2", "Couper 20 pâtons de 280 g en 2 -> <strong>40 pièces de 140 g</strong>."),
            ("2. Stock 1 (Cru non poussé)", "Flash <strong>35 min à -35 °C</strong> -> stockage à -18 °C."),
            ("3. Pousse (26 °C / 80 % HR)", "<strong>1 h 30 à 1 h 45</strong>. Puis 10 min à +4 °C."),
            ("4. Stock 2 PAC (Prêt-à-cuire)", "Flash -35 °C jusqu'à <strong>-10 °C à cœur</strong> -> -18 °C."),
        ],
        "sec4": "4. Calibres & Rendement",
        "calibres": [("140 g cru", "~133 g cuit"), ("14–16 cm", "Longueur pièce"), ("40 pcs / bac", "18 / plaque")],
        "steps4": [
            ("Détente avant façonnage", "8–10 min sous bâche plastique étanche sur tour inox."),
            ("1re Dorure Végétale", "Passer au pinceau avant mise en cellule ou étuve."),
        ],
        "sec5": "5. Cuisson Directe Congelé (-18 °C)",
        "cuisson": [("180 -> 165 °C", "Préchauffage -> Régul."), ("Oura fermé", "9 min strictes"), ("9 min", "Temps exact")],
        "alert": "PÉPITES EN V1 LENTE 45–60 S MAX • OURAS STRICTEMENT FERMÉS PENDANT 9 MIN",
    },
    "V-BRI-01": {
        "title": "BRIOCHE INDIVIDUELLE SUCRE PAC",
        "badge": "V-BRI-01 • 80 PCS / BAC",
        "right_badge": "COLZA • 75 G",
        "sec2": "2. Pétrissage & Pointage Froid",
        "steps2": [
            ("Frasage : 5 min V1", "Ingrédients bleus avec couple Kimo / Soft'r."),
            ("Pétrissage : 4 + 6–7 min V2", "4 min V2 puis incorporer huile de colza, 6–7 min V2."),
            ("Sortie cuve : 20–22 °C", "Pointer <strong>20 min à 20–22 °C</strong> sous film étanche."),
            ("Froid division : 25 min +4 °C", "Figer la pâte en bac 6 000 g pour coupe nette."),
        ],
        "sec3": "3. Division 20×4 & Blocage PAC",
        "steps3": [
            ("1. Division 20×4", "20 pâtons de 300 g coupés en 4 -> <strong>80 boules de 75 g</strong>."),
            ("2. Boulage & Plaquage", "Bouler serré, poser 24 pièces par plaque 60×40."),
            ("3. Pousse (26 °C / 80 % HR)", "<strong>1 h 45 à 2 h 00</strong>. Puis 10 min à +4 °C."),
            ("4. Dorure, Grainage & PAC", "Dorer (Bamix), sucrer gros grains. Flash <strong>-10 °C cœur</strong>."),
        ],
        "sec4": "4. Calibres & Option Stock 1",
        "calibres": [("75 g cru", "~75 g cuit sucré"), ("24 pcs", "Par plaque 60×40"), ("80 pcs / bac", "Bac 6 000 g")],
        "steps4": [
            ("Décongélation Stock 1", "Si départ cru gelé : 8–10 h à +4 °C avant d'entrer en étuve."),
            ("Sucre perlé", "Déposer généreusement juste après dorure avant flash."),
        ],
        "sec5": "5. Cuisson Directe Congelé (-18 °C)",
        "cuisson": [("180 -> 165 °C", "Préchauffage -> Régul."), ("Oura ouvert", "En continu"), ("11–13 min", "Temps total")],
        "alert": "OURAS GRANDS OUVERTS EN CONTINU POUR SÉCHER LE DÔME ET GARDER LE SUCRE SEC",
    },
    "P-FRA-01": {
        "title": "FRANGIPANE 80/20 & GALETTES PAC",
        "badge": "P-FRA-01 • INSERTS -18 °C",
        "right_badge": "CYCLE J / J+1",
        "sec2": "2. Préparation Frangipane 80/20",
        "steps2": [
            ("Crème d'amande (Feuille)", "Beurre pommade + sucre + poudre d'amandes + farine T65 + œufs."),
            ("Sans foisonnement", "Mélanger en V1 lente pour éviter le gonflement excessif au four."),
            ("Assemblage 80 / 20", "Incorporer la crème pâtissière froide lissée au mélange amande."),
            ("Inserts biseautés -18 °C", "Pocher douille n°14, congeler à -18 °C sur Silpat."),
        ],
        "sec3": "3. Montage Galettes (Cycle J / J+1)",
        "steps3": [
            ("1. Montage sur Silpat", "Disque feuilletage inversé 3 mm + insert gelé + fève."),
            ("2. Soudure à l'EAU PURE", "Humidifier le pourtour à l'eau, poser le chapeau, chiqueter."),
            ("3. Repos nuit à +4 °C", "Mettre en échelle <strong>12 à 15 h à +4 °C</strong> + 1re dorure."),
            ("4. Rayage & Flash -35 °C", "Rayer à 45° (0,5 mm) + 4–5 cheminées. Flash 40 min (-10 °C cœur)."),
        ],
        "sec4": "4. Calibres & Vitrification",
        "calibres": [("3,0 mm", "Feuilletage inversé"), ("4 cm", "Cales Felder four"), ("30° Brix", "Sirop miroir")],
        "steps4": [
            ("Sirop vitrification", "500 g eau + 600 g sucre + 100 g glucose : bouillir 1 min."),
            ("2e Dorure", "Appliquer juste avant rayage après sortie d'échelle +4 °C."),
        ],
        "sec5": "5. Cuisson Sous Cales Felder",
        "cuisson": [("190 -> 165–170 °C", "Congelée (175 décong.)"), ("Oura ouvert", "12–15 dernières min"), ("42–50 min", "35–42 min décongelée")],
        "alert": "SOUDURE À L'EAU PURE • CALES 4 CM • OUVRIR OURAS 12–15 DERNIÈRES MINUTES",
    },
    "P-GAL-02": {
        "title": "GALETTES POMME & TRIO POIRE-NUTOLADE",
        "badge": "P-GAL-02 / 03 • ÉPIPHANIE",
        "right_badge": "CYCLE J / J+1",
        "sec2": "2. Préparation des Garnitures",
        "steps2": [
            ("Option Pommes Topfil", "100 % Puratos Topfil Pommes prêt à pocher, tenue parfaite."),
            ("Trio Poire-Nutolade", "Socle insert frangipane 80/20 gelé -18 °C (barrière anti-détrempe)."),
            ("Poires & Nutolade", "Pocher la Nutolade sur l'insert et répartir les dés de poires."),
            ("Fonds de pâte", "Disques feuilletage inversé 3,0 mm sur Silpat, <strong>sans semoule</strong>."),
        ],
        "sec3": "3. Assemblage & Workflow J / J+1",
        "steps3": [
            ("1. Montage & Soudure", "Fond 3 mm + garniture + fève. Souder à l'eau pure."),
            ("2. Échelle nuit +4 °C", "Stocker <strong>12 à 15 h à +4 °C</strong> pour figer la soudure."),
            ("3. Rayage & 4–5 Évents", "Lame à 45° (prof. 0,5 mm) + 4 à 5 cheminées franches au centre."),
            ("4. Flash -35 °C (40 min)", "Sonde à cœur ≤ -10 °C. Stocker sous film à -18 °C."),
        ],
        "sec4": "4. Calibres & Architecture",
        "calibres": [("3,0 mm", "Abaisse sole/voûte"), ("4–5 évents", "Cheminées vapeur"), ("-18 °C", "Stock Épiphanie")],
        "steps4": [
            ("Zéro semoule", "Le Topfil lié et l'insert frangipane suppriment le besoin de semoule."),
            ("Chapeau rayé", "Ne jamais percer jusqu'à la garniture hors des 4–5 cheminées."),
        ],
        "sec5": "5. Cuisson Directe Congelée (-18 °C)",
        "cuisson": [("165–170 °C", "Four ventilé / soles"), ("Oura ouvert", "12–15 dernières min"), ("38–48 min", "Selon format")],
        "alert": "4 À 5 CHEMINÉES OBLIGATOIRES • OUVRIR LES OURAS LES 12–15 DERNIÈRES MINUTES",
    },
    "P-NAN-01": {
        "title": "GÂTEAU NANTAIS DE VOYAGE",
        "badge": "P-NAN-01 • INDIV 100 G / 450 G",
        "right_badge": "RHUM 45°",
        "sec2": "2. Préparation Batteur (Feuille)",
        "steps2": [
            ("Crémage doux", "Beurre pommade + sucre + poudre d'amandes en 1re vitesse."),
            ("Œufs & Farine", "Incorporer œufs progressivement puis farine en V1 sans corser."),
            ("Rhum de masse", "Ajouter le rhum 45° en fin de mélange en V1."),
            ("Sirop d'imbibage", "Eau + sucre bouillis 1 min, rhum hors feu. Utiliser à 40 °C."),
        ],
        "sec3": "3. Dosage, Punchage & Glaçage",
        "steps3": [
            ("1. Moules aluminium", "Pulvériser agent démoulant. Peser 100 g ou 450 g net."),
            ("2. Punchage à chaud", "Imbiber au pinceau dès la sortie du four avec sirop tiède 40 °C."),
            ("3. Glaçage Royal Rhum", "Tiédir rhum + trimoline à 45 °C, dissoudre gélatine essorée."),
            ("4. Nappage & Figeage", "Glacer sur gâteau refroidi. Laisser figer <strong>25 min à l'air libre</strong>."),
        ],
        "sec4": "4. Calibres & Conservation",
        "calibres": [("100 g / 450 g", "Indiv / Partage"), ("~40 °C", "Sirop punchage"), ("21 jours", "DLC 18–20 °C")],
        "steps4": [
            ("Couleur cible", "Surface dorée ambrée uniforme, bord légèrement rétracté du moule."),
            ("Stockage ambiant", "Sous cloche ou film alimentaire à 18–20 °C jusqu'à 21 jours."),
        ],
        "sec5": "5. Cuisson Four Ventilé",
        "cuisson": [("165 °C", "Four ventilé"), ("Oura fermé", "Toute la cuisson"), ("25–28 / 40–45", "Min (100 g / 450 g)")],
        "alert": "OURA FERMÉ TOUTE LA CUISSON • PUNCHER AU SIROP TIÈDE (40 °C) DÈS SORTIE FOUR",
    },
    "B-BRK-01": {
        "title": "BROOKIE EN CADRES 56×36 CM",
        "badge": "B-BRK-01 • 30 PARTS / CADRE",
        "right_badge": "CADRE 60×40",
        "sec2": "2. Cookie Laminé & Appareil Brownie",
        "steps2": [
            ("Cookie (Feuille V1)", "Sabler poudres/matière grasse, œufs V1, pépites 30 s max."),
            ("Laminage : 5,5 mm", "Abaisser à 5,5 mm, couper gabarit <strong>56 × 36 cm</strong> (1 200 g). Durcir."),
            ("Brownie (Sans foisonner)", "Fondre chocolat 55 % à 45–50 °C. Mélanger V1 homogène."),
            ("Coulage en cadre", "<strong>2 260 g</strong> brownie au fond + abaisse cookie gelée dessus."),
        ],
        "sec3": "3. Montage, Décadrage & Coupe",
        "steps3": [
            ("1. Cadre 56 × 36 × 4 cm", "Posé sur toile Silpat propre sur plaque 60×40."),
            ("2. Tiédissement : 10 min", "À sortie four, attendre 10 min puis décoller au couteau fin."),
            ("3. Figeage : 2 h à +4 °C", "Passage obligatoire en chambre froide pour coupe nette."),
            ("4. Découpe : 30 parts", "Au réglet inox et lame chaude sans écraser le cookie."),
        ],
        "sec4": "4. Calibres & Répartition",
        "calibres": [("56 × 36 cm", "Cadre inox H 4 cm"), ("2 260 + 1 200 g", "Brownie + Cookie"), ("30 parts", "Par cadre")],
        "steps4": [
            ("Égalisation brownie", "Lisser à la palette coudée avant de poser l'abaisse cookie gelée."),
            ("Zéro chute", "Le gabarit 56×36 cm épouse l'intérieur exact du cadre."),
        ],
        "sec5": "5. Cuisson Double Phase",
        "cuisson": [("175 -> 160–165 °C", "Préchauff. -> Régul."), ("Oura 18' F / 8' O", "Fermé puis ouvert"), ("24–26 min", "Temps total")],
        "alert": "OURAS FERMÉS 18 MIN (CŒUR FONDANT) PUIS OUVERTS 6–8 MIN (COOKIE CROUSTILLANT)",
    },
    "B-BRW-01": {
        "title": "BROWNIE FONDANT INTENSE CHOCOLAT",
        "badge": "B-BRW-01 • 35 CARRÉS / CADRE",
        "right_badge": "CADRE 56×36",
        "sec2": "2. Appareil au Batteur (Feuille)",
        "steps2": [
            ("Fonte chocolat : 45–50 °C", "Chocolat noir 55 % fondu + huile de colza émulsionnée au fouet."),
            ("Mélange sans foisonner", "Tourner <strong>1 à 2 min en 1re vitesse</strong> uniquement."),
            ("Noix & Pépites", "Incorporer en fin de mélange en V1 sur quelques tours."),
            ("Pesée sur balance", "Poser plaque + Silpat + cadre 56×36 sur balance tarée."),
        ],
        "sec3": "3. Coulage, Cuisson & Découpe",
        "steps3": [
            ("1. Coulage : 3 000 g net", "Verser exactement 3 000 g par cadre, lisser à la palette."),
            ("2. Décadrage à chaud", "Repos <strong>10 min</strong> sortie four, passer couteau fin, lever cadre."),
            ("3. Figeage : 1–2 h à +4 °C", "Indispensable en chambre froide avant découpe."),
            ("4. Découpe : 35 carrés", "5 × 7 parts nettes de <strong>85 g brut</strong> (lame chaude)."),
        ],
        "sec4": "4. Calibres & Rendement",
        "calibres": [("3 000 g net", "Par cadre 56×36"), ("85 g brut", "Carré unitaire"), ("35 carrés", "Zéro chute")],
        "steps4": [
            ("Test fin de cuisson", "Le centre doit rester <strong>légèrement tremblotant</strong> sous le doigt."),
            ("Cadence lot", "5 cadres = 175 parts • 10 cadres = 350 parts."),
        ],
        "sec5": "5. Cuisson Douce (Oura Fermé)",
        "cuisson": [("170 -> 160 °C", "Préchauff. -> Régul."), ("Oura fermé", "Toute la cuisson"), ("22–25 min", "Selon charge")],
        "alert": "OURAS RIGOUREUSEMENT FERMÉS TOUTE LA CUISSON • CENTRE LÉGÈREMENT TREMBLOTANT",
    },
    "B-CKI-01": {
        "title": "COOKIES CLASSIQUES & NOISETTE",
        "badge": "B-CKI-01 • CALIBRE 80 G",
        "right_badge": "PAC -18 °C",
        "sec2": "2. Sablage Batteur (Feuille V1)",
        "steps2": [
            ("Sablage : 2 min max V1", "Margarine OPALE + cassonade + sucre blanc + gros sel (zéro foisonnement)."),
            ("Liquides : 45–60 s V1", "Verser œufs liquides et émulsionner brièvement en V1."),
            ("Frasage poudres", "Ajouter farines + levure chimique tamisées en V1."),
            ("Inclusions : 30 s V1", "Pépites chocolat / noisettes réparties sans frictionner."),
        ],
        "sec3": "3. Dressage Coupe-Fil & Flash PAC",
        "steps3": [
            ("1. Calibrage 80 g cru", "Dresser au coupe-fil ou portionner à 80 g réguliers sur Silpat."),
            ("2. Flash : 35 min à -35 °C", "Congeler les plaques chargées en cellule flash."),
            ("3. Stockage -18 °C", "Décoller et conditionner en cartons sous housse étanche."),
            ("4. Départ four -18 °C", "Enfourner directement congelé sur toile Silpat, zéro décongélation."),
        ],
        "sec4": "4. Calibres & Poids",
        "calibres": [("80 g cru", "Portion dressée"), ("72–74 g", "Poids cuit visé"), ("15 min", "Figeage sur plaque")],
        "steps4": [
            ("Aspect sortie four", "Pourtour blond ambré doré, cœur encore souple au toucher."),
            ("Ne pas toucher chauds", "Laisser figer <strong>15 min sur plaque</strong> avant transfert."),
        ],
        "sec5": "5. Cuisson Directe Congelé (-18 °C)",
        "cuisson": [("180 -> 165 °C", "Préchauff. -> Régul."), ("Oura ouvert", "En continu"), ("13–14 min", "Chrono")],
        "alert": "OURAS OUVERTS EN CONTINU • NE JAMAIS TOUCHER CHAUDS (FIGEAGE 15 MIN SUR PLAQUE)",
    },
    "B-MUF-01": {
        "title": "MUFFINS ATELIER PÉPITES & CŒUR",
        "badge": "B-MUF-01 / 02 • 120 G",
        "right_badge": "DÔME BLAST",
        "sec2": "2. Préparation au Batteur",
        "steps2": [
            ("Mélange doux", "Combiner liquides et poudres sans battre excessivement."),
            ("Incorporation pépites", "En fin de mélange en 1re vitesse lente."),
            ("Caissettes tulipes 120 g", "Disposer en plaques d'atelier 24 moules."),
            ("Dosage calibré", "Pocher ou doser régulièrement dans chaque caissette tulipe."),
        ],
        "sec3": "3. Pilon à Chaud & Garnissage",
        "steps3": [
            ("1. Contrôle cœur : 94–96 °C", "Vérifier à la sonde thermique en fin de cuisson."),
            ("2. Technique du pilon", "À chaud dès sortie four, creuser un puits net sans miettes."),
            ("3. Garnissage cœur", "Injecter Nutolade (B-MUF-01) ou Tartiner Noisette (B-MUF-02)."),
            ("4. Conditionnement", "Refroidir sur grille avant filmage ou surgélation."),
        ],
        "sec4": "4. Calibres & Moules",
        "calibres": [("120 g", "Caissette tulipe"), ("24 moules", "Par plaque"), ("94–96 °C", "Cœur cuit")],
        "steps4": [
            ("Effet dôme coffee shop", "Obtenu grâce au choc thermique initial de 5 min à 205–210 °C."),
            ("Variantes", "B-MUF-01 (Chocolat / Nutolade) • B-MUF-02 (Noisette / Tartiner)."),
        ],
        "sec5": "5. Cuisson 2 Paliers (Thermal Blast)",
        "cuisson": [("205–210 -> 165 °C", "5 min -> 17 min"), ("Oura fermé", "Palier 1 (5 min)"), ("22 min", "Temps total")],
        "alert": "PALIER 1 : 5 MIN À 205–210 °C OURA FERMÉ • PUIS DESCENDRE À 165 °C (17 MIN)",
    },
    "B-CAK-01": {
        "title": "CAKES DE VOYAGE FORMAT 3 KG",
        "badge": "B-CAK-01 / 02 / 03 • 3 KG",
        "right_badge": "MOULE 50×10×10",
        "sec2": "2. Préparation Batteur Planétaire",
        "steps2": [
            ("Mélange base Golden", "Mix Rex Mella + œufs + huile + eau au batteur selon temps d'atelier."),
            ("Citron Pavot (01)", "Ajouter zestes citron naturel + graines de pavot en V1."),
            ("Marbré 50/50 (02)", "Alterner 4 couches : 1 530 g Golden + 1 530 g Choc par moule."),
            ("Fruits Confits (03)", "Macédoine égouttée & enrobée incorporée en dernier en V1."),
        ],
        "sec3": "3. Moulage Calibré & Ressuage",
        "steps3": [
            ("1. Pesée exacte : 3 060 g", "Poser le moule inox 50×10×10 cm sur balance tarée, couler 3 060 g."),
            ("2. Porte fermée 60 min", "Ne jamais ouvrir le four durant la 1re heure de cuisson."),
            ("3. Contrôle lame", "La lame plantée au cœur doit ressortir sèche après 75 min."),
            ("4. Démoulage & Ressuage", "Démouler et laisser refroidir complètement sur grille avant tranchage."),
        ],
        "sec4": "4. Calibres & Rendement",
        "calibres": [("50×10×10 cm", "Moule inox"), ("3 060 g cru", "3,0 kg cuit net"), ("10 / 15", "Moules par lot")],
        "steps4": [
            ("Marbrage 4 couches", "765 g Golden -> 765 g Choc -> 765 g Golden -> 765 g Choc."),
            ("Vente au poids", "Format conçu pour tranches épaisses en boutique et buffet."),
        ],
        "sec5": "5. Cuisson Longue Douce",
        "cuisson": [("155 °C", "Four ventilé / soles"), ("Oura fermé", "Toute la cuisson"), ("75 min", "1 h 15 min")],
        "alert": "INTERDICTION ABSOLUE D'OUVRIR LA PORTE DU FOUR PENDANT LES 60 PREMIÈRES MINUTES",
    },
    "C-CRP-01": {
        "title": "CRÊPES DE FROMENT GIROCRÊPES",
        "badge": "C-CRP-01 • CARROUSEL CONTINU",
        "right_badge": "TAMBOUR 215 °C",
        "sec2": "2. Frasage Biphasique (Anti-Grumeaux)",
        "steps2": [
            ("Phase 1 : Frasage serré", "Farine + sucre + sel + œufs + partie du lait : battre serré sans grumeaux."),
            ("Phase 2 : Allongement", "Détendre progressivement avec le reste du lait en V1."),
            ("Émulsion lipidique", "Incorporer la matière grasse en dernier pour viscosité régulière."),
            ("Tamisage & Repos", "Filtrer au chinois avant transfert en bac d'alimentation pompe."),
        ],
        "sec3": "3. Conduite Carrousel Girocrêpes",
        "steps3": [
            ("1. Préchauffage tambour", "Stabiliser le tambour rotatif exactement à <strong>215 °C (± 3 °C)</strong>."),
            ("2. Réglage racleur", "Vérifier l'épaisseur du film déposé pour une crêpe souple."),
            ("3. Surveillance continue", "Maintenir l'alimentation homogène et racler les bords si besoin."),
            ("4. Empilage & Refroidissement", "Empiler par paquets calibrés et filmer après refroidissement."),
        ],
        "sec4": "4. Paramètres Machine",
        "calibres": [("215 °C", "Tambour régulé"), ("± 3 °C", "Tolérance"), ("2 temps", "Frasage + Allong.")],
        "steps4": [
            ("Viscosité constante", "Mélanger régulièrement le bac tampon pour éviter la décantation."),
            ("Zéro grumeau", "Le frasage serré initial garantit une pâte lisse sans passage mixeur."),
        ],
        "sec5": "5. Cuisson Tambour Rotatif",
        "cuisson": [("215 °C", "Tambour chauffant"), ("Continu", "Carrousel auto"), ("~45–60 s", "Par tour tambour")],
        "alert": "TEMPÉRATURE TAMBOUR 215 °C (± 3 °C) • FILTRAGE AU CHINOIS OBLIGATOIRE AVANT POMPE",
    },
    "C-GAL-01": {
        "title": "GALETTES BLÉ NOIR GIROCRÊPES",
        "badge": "C-GAL-01 • SARRASIN CONTINU",
        "right_badge": "TAMBOUR 230 °C",
        "sec2": "2. Frasage Biphasique Sarrasin",
        "steps2": [
            ("Phase 1 : Frasage serré", "Farine de blé noir + gros sel + eau initiale : battre ferme."),
            ("Hydratation progressive", "Allonger en Phase 2 pour obtenir une viscosité constante."),
            ("Repos d'hydratation", "Laisser reposer la pâte <strong>30 min</strong> pour gonflement sarrasin."),
            ("Filtrage chinois", "Passer au chinois étamine avant mise en bac machine."),
        ],
        "sec3": "3. Conduite Carrousel Girocrêpes",
        "steps3": [
            ("1. Préchauffage : 230 °C", "Réguler le tambour rotatif à <strong>230 °C (± 3 °C)</strong>."),
            ("2. Graissage / Réglage", "Vérifier l'accroche et la coloration dentelée caractéristique."),
            ("3. Décollement continu", "Contrôler la souplesse au pliage dès la sortie de bande."),
            ("4. Conditionnement", "Laisser tiédir à plat avant empilage et mise sous film."),
        ],
        "sec4": "4. Paramètres Machine",
        "calibres": [("230 °C", "Tambour régulé"), ("± 3 °C", "Tolérance"), ("30 min", "Repos hydratation")],
        "steps4": [
            ("Brassage bac", "Remuer le bac régulièrement : le sarrasin décante plus vite que le froment."),
            ("Viscosité", "Ajuster avec un léger filet d'eau si épaississement en fin de service."),
        ],
        "sec5": "5. Cuisson Tambour Sarrasin",
        "cuisson": [("230 °C", "Tambour chauffant"), ("Continu", "Carrousel auto"), ("~45–60 s", "Par tour tambour")],
        "alert": "TEMPÉRATURE TAMBOUR 230 °C (± 3 °C) • REPOS 30 MIN OBLIGATOIRE AVANT CUISSON",
    },
    "T-QCH-01": {
        "title": "GAMME QUICHES TRAITEUR (Ø 100 MM)",
        "badge": "T-QCH-01 / 02 / 03 • 48 PCS",
        "right_badge": "CAISSE 48 PCS",
        "sec2": "2. Appareil Universel & Garnitures",
        "steps2": [
            ("Appareil maître (1 kg)", "Œufs + crème + lait + sel (8 g/kg) + épices. Mixer sans mousser."),
            ("Lorraine (01) — 140 g", "Lardons blanchis/revenus + emmental + appareil universel."),
            ("Chèvre Épinards (02) — 150 g", "Épinards IQF + fromage de chèvre + appareil universel."),
            ("Poireaux (03) — 160 g", "50 g poireaux émincés IQF + 10 g emmental + 100 g appareil."),
        ],
        "sec3": "3. Assemblage & Conditionnement",
        "steps3": [
            ("1. Fonds brisés Michard", "Disposer les moules alu Ø 100 mm crus sur plaques de four."),
            ("2. Garnissage solide", "Peser la garniture solide exacte au fond de chaque tartelette."),
            ("3. Coulage appareil", "Compléter à ras bord avec l'appareil universel sans déborder."),
            ("4. Ressuage & Stockage", "Démouler/refroidir sur grille. Cartons de 48 pièces."),
        ],
        "sec4": "4. Calibres & Conservation",
        "calibres": [("Ø 100 mm", "Moule alu cannelé"), ("140–160 g", "Selon variété"), ("4 j / 6 mois", "Frais +4 / Gel -18")],
        "steps4": [
            ("Régénération boutique", "<strong>10–12 min à 180 °C</strong> au four chaud (micro-ondes proscrit)."),
            ("Conditionnement", "Cartons de 48 pièces conditionnées sur grille."),
        ],
        "sec5": "5. Cuisson Four Ventilé",
        "cuisson": [("170 °C", "Four ventilé"), ("Oura fermé", "Puis sec fin"), ("30–35 min", "Temps total")],
        "alert": "MICRO-ONDES FORMELLEMENT PROSCRIT EN RÉGÉNÉRATION • FOUR CHAUD 180 °C (10–12 MIN)",
    },
    "R-DOR-01": {
        "title": "DORURES D'ATELIER & SIROP 44° BRIX",
        "badge": "R-DOR-01 • R-SIR-01",
        "right_badge": "RÉFÉRENTIEL",
        "sec2": "2. Préparation Dorures & Sirop",
        "steps2": [
            ("Dorure Pistolet (01A)", "Œufs + lait/crème + sel (10 g/L) + sucre (20 g/L) pour fluidité."),
            ("Filtration chinoise", "Passer au chinois étamine fin pour éviter de boucher la buse."),
            ("Dorure Pinceau (01B)", "Spécifique galettes & pithiviers (jaunes + crème, zéro bavure)."),
            ("Sirop 44° Brix (R-SIR-01)", "1 000 g eau + 800 g sucre : bouillir <strong>1 min chrono</strong>."),
        ],
        "sec3": "3. Application Pistolet & Pinceau",
        "steps3": [
            ("1. Pistolet (1,5 bar)", "Basse pression, voile fin uniforme sur viennoiseries froides."),
            ("2. Pinceau Feuilletage", "Passer à plat sur galette sans couler sur la tranche (chiquetage)."),
            ("3. Séchage 15 min à +4 °C", "Figer la 1re dorure au froid avant rayage net à la lame."),
            ("4. Lustrage post-cuisson", "Appliquer le sirop 44° Brix <strong>froid</strong> sur pièces brûlantes."),
        ],
        "sec4": "4. Repères d'Utilisation",
        "calibres": [("1,5 bar", "Pression pistolet"), ("15 min +4 °C", "Séchage galette"), ("48 h max", "DLC dorure +4 °C")],
        "steps4": [
            ("Pains raisins / Oranais", "Lustrer au pinceau dès la sortie du four au sirop 44° Brix froid."),
            ("Hygiène pistolet", "Nettoyage et désinfection complète du godet chaque fin de poste."),
        ],
        "sec5": "5. Cuisson Sirop & Stockage",
        "cuisson": [("103 °C / 1 min", "Ébullition sirop"), ("Froid", "Application sortie four"), ("+4 °C (48 h)", "Conservation dorure")],
        "alert": "FILTRATION CHINOISE ÉTAMINE OBLIGATOIRE • NE JAMAIS DORER LA TRANCHE DU FEUILLETAGE",
    },
}

POLES_META = [
    ("1. VIENNOISERIES FEUILLETÉES & TOURAGE", [
        "V-PLF-01", "V-PLF-02", "V-PLF-03", "V-PLF-04", "V-PLF-05", "V-PLF-06", "V-PLF-07", "V-KOU-01", "P-FEU-01"
    ]),
    ("2. VIENNOISERIE GÉNÉRALE & PÂTES LEVÉES", [
        "V-VIE-01", "V-VIE-02", "V-BRI-01"
    ]),
    ("3. PÂTISSERIE BOULANGÈRE & ÉPIPHANIE", [
        "P-FRA-01", "P-GAL-02", "P-NAN-01"
    ]),
    ("4. BISCUITERIE, CAKES & SNACKING", [
        "B-BRK-01", "B-BRW-01", "B-CKI-01", "B-MUF-01", "B-CAK-01"
    ]),
    ("5. CRÊPERIE, TRAITEUR & RÉFÉRENTIELS", [
        "C-CRP-01", "C-GAL-01", "T-QCH-01", "R-DOR-01"
    ]),
]


def build_cover():
    return """
    <div class="page m3-cover">
      <div>
        <div class="m3-cover-kicker">Laboratoire Central • Production Boulangerie & Pâtisserie</div>
        <h1 class="m3-cover-title">CAHIER DE RECETTES<br>D'ATELIER</h1>
        <p class="m3-cover-sub">
          Fiches techniques standardisées en double page face-à-face.<br>
          Page de gauche : pesées en grammes et préparation.<br>
          Page de droite : tourage, façonnage, calibres et cuisson.
        </p>

        <div class="m3-cover-grid">
          <div class="m3-cover-card">
            <div class="num">24 FICHES</div>
            <div class="txt">5 pôles de production couvrant viennoiserie, pâtisserie, biscuiterie, crêperie et traiteur.</div>
          </div>
          <div class="m3-cover-card">
            <div class="num">100 % GRAMMES</div>
            <div class="txt">Zéro virgule sur les balances. Échelles directes par bac, moule, cadre ou caisse.</div>
          </div>
          <div class="m3-cover-card">
            <div class="num">DOUBLE PAGE A4</div>
            <div class="txt">Ouverture à plat au poste de travail : toute la recette sous les yeux sans tourner la page.</div>
          </div>
          <div class="m3-cover-card">
            <div class="num">REPÈRES VISUELS</div>
            <div class="txt">Pastilles d'ordre d'incorporation et alertes ouras critiques pour zéro erreur en fournil.</div>
          </div>
        </div>
      </div>

      <div class="m3-cover-foot">
        <span>STYLE ATELIER DIRECT • LECTURE RAPIDE</span>
        <span>51 PAGES • FORMAT IMPRESSION RECTO-VERSO</span>
      </div>
    </div>
    """


def build_sommaire(page_map, total_pages):
    def render_pole(title, codes):
        rows_html = []
        for c in codes:
            spec = SPECS[c]
            p_left, p_right = page_map[c]
            rows_html.append(
                f'<div class="toc-row">'
                f'<span class="toc-code">{c}</span>'
                f'<span class="toc-name">{spec["title"]}</span>'
                f'<span class="toc-pages">p. {p_left}–{p_right}</span>'
                f'</div>'
            )
        return f'<div class="toc-pole"><div class="toc-pole-title">{title}</div>{"".join(rows_html)}</div>'

    left_poles = "".join(render_pole(t, cs) for t, cs in POLES_META[:2])
    right_poles = "".join(render_pole(t, cs) for t, cs in POLES_META[2:])

    left_html = f"""
    <div class="page page-left m3">
      <div class="m3-topbar">
        <div class="m3-title">SOMMAIRE GÉNÉRAL (1/2)</div>
        <div class="m3-badge">PÔLES 1 & 2</div>
      </div>

      {left_poles}

      <div class="legend-box">
        <div class="legend-title">Code Couleur des Balances & Règles d'Atelier</div>
        <div class="legend-item"><span class="m3-dot dot-1"></span><strong>Pastille Bleue :</strong> Phase 1 (Poudres, liquides, base détrempe ou appareil principal).</div>
        <div class="legend-item"><span class="m3-dot dot-2"></span><strong>Pastille Ambre :</strong> Phase 2 (Matière grasse cuve, inclusions, garnitures ou 2e vitesse).</div>
        <div class="legend-item"><span class="m3-dot dot-3"></span><strong>Pastille Verte :</strong> Phase 3 (Beurre de tourage, montage final ou finition four).</div>
        <div class="legend-item" style="margin-top:2mm; color:#991b1b;"><strong>Règle d'Or :</strong> Toujours tarer la balance avant chaque ajout. Respecter les températures de sortie cuve et l'ouverture des ouras.</div>
      </div>

      <div class="m3-footer">
        <span>Cahier Complet d'Atelier • Sommaire</span>
        <span>2 / {total_pages}</span>
      </div>
    </div>
    """

    right_html = f"""
    <div class="page page-right m3">
      <div class="m3-topbar" style="background:#1e293b;">
        <div class="m3-title">SOMMAIRE GÉNÉRAL (2/2)</div>
        <div class="m3-badge" style="background:#16a34a;">PÔLES 3, 4 & 5</div>
      </div>

      {right_poles}

      <div class="m3-footer">
        <span>Cahier Complet d'Atelier • Sommaire</span>
        <span>3 / {total_pages}</span>
      </div>
    </div>
    """
    return left_html + right_html


def build_recipe_spread(recipe_data, p_left, p_right, total_pages):
    code = recipe_data["code"]
    spec = SPECS[code]
    headers = recipe_data["headers"]
    rows = recipe_data["rows"]

    compact_cls = " compact" if len(rows) >= 15 else ""
    th_html = "".join(
        f'<th{"" if i == 0 else " class=\"num\""}>{h}</th>'
        for i, h in enumerate(headers)
    )

    tr_list = []
    for r in rows:
        rtype = r.get("type", "normal")
        dot = r.get("dot", "dot-1")
        ing = r.get("ingredient", "")
        cols = r.get("cols", [])
        # Align cols length to headers - 1
        while len(cols) < len(headers) - 1:
            cols.append("")
        cols = cols[: len(headers) - 1]

        if rtype == "subtotal":
            tds = f'<td>{ing}</td>' + "".join(f'<td class="num">{c}</td>' for c in cols)
            tr_list.append(f'<tr class="subtotal">{tds}</tr>')
        elif rtype == "total":
            tds = f'<td>{ing.upper()}</td>' + "".join(f'<td class="num">{c}</td>' for c in cols)
            tr_list.append(f'<tr class="total">{tds}</tr>')
        else:
            tds = f'<td><span class="m3-dot {dot}"></span>{ing}</td>' + "".join(f'<td class="num">{c}</td>' for c in cols)
            tr_list.append(f'<tr>{tds}</tr>')

    steps2_html = "".join(
        f'<div class="m3-chrono-item"><span class="m3-step-head">{h}</span><span>{b}</span></div>'
        for h, b in spec["steps2"]
    )

    left_html = f"""
    <div class="page page-left m3">
      <div class="m3-topbar">
        <div class="m3-title">{spec["title"]}</div>
        <div class="m3-badge">{spec["badge"]}</div>
      </div>

      <div class="m3-h2">1. Pesées en grammes</div>
      <table class="m3-table{compact_cls}">
        <thead><tr>{th_html}</tr></thead>
        <tbody>{"".join(tr_list)}</tbody>
      </table>

      <div class="m3-h2">{spec["sec2"]}</div>
      <div class="m3-chrono">{steps2_html}</div>

      <div class="m3-footer">
        <span>{recipe_data["pole"]}</span>
        <span>{p_left} / {total_pages}</span>
      </div>
    </div>
    """

    steps3_html = "".join(
        f'<div class="m3-chrono-item"><span class="m3-step-head">{h}</span><span>{b}</span></div>'
        for h, b in spec["steps3"]
    )
    calibres_html = "".join(
        f'<div class="m3-big-box"><div class="val">{v}</div><div class="lbl">{l}</div></div>'
        for v, l in spec["calibres"]
    )
    steps4_html = "".join(
        f'<div class="m3-chrono-item"><span class="m3-step-head">{h}</span><span>{b}</span></div>'
        for h, b in spec["steps4"]
    )
    cuisson_html = "".join(
        f'<div class="m3-big-box"><div class="val">{v}</div><div class="lbl">{l}</div></div>'
        for v, l in spec["cuisson"]
    )

    right_html = f"""
    <div class="page page-right m3">
      <div class="m3-topbar" style="background:#1e293b;">
        <div class="m3-title" style="font-size:14.5pt;">EXÉCUTION, CALIBRES & CUISSON</div>
        <div class="m3-badge" style="background:#16a34a;">{spec["right_badge"]}</div>
      </div>

      <div class="m3-h2">{spec["sec3"]}</div>
      <div class="m3-chrono">{steps3_html}</div>

      <div class="m3-h2">{spec["sec4"]}</div>
      <div class="m3-big-grid">{calibres_html}</div>
      <div class="m3-chrono">{steps4_html}</div>

      <div class="m3-h2">{spec["sec5"]}</div>
      <div class="m3-big-grid" style="margin-bottom:4mm;">{cuisson_html}</div>

      <div class="m3-alert">{spec["alert"]}</div>

      <div class="m3-footer">
        <span>Cahier d'Atelier • {code}</span>
        <span>{p_right} / {total_pages}</span>
      </div>
    </div>
    """

    return left_html + right_html


def main():
    with open(SUMMARY_JSON, 'r', encoding='utf-8') as f:
        recipes = json.load(f)

    total_pages = 1 + 2 + len(recipes) * 2  # 1 cover + 2 sommaire + 48 recipe pages = 51
    page_map = {}
    cur_page = 4
    for r in recipes:
        page_map[r["code"]] = (cur_page, cur_page + 1)
        cur_page += 2

    pages_html = [build_cover(), build_sommaire(page_map, total_pages)]
    for r in recipes:
        pl, pr = page_map[r["code"]]
        pages_html.append(build_recipe_spread(r, pl, pr, total_pages))

    full_html = (
        f'<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
        f'<style>{COMMON_CSS}{CSS_M3}</style></head>'
        f'<body>{"".join(pages_html)}</body></html>'
    )

    out_html = os.path.join(EXPORTS_DIR, 'Cahier_Complet_Atelier_Double_Page_A4.html')
    out_pdf = os.path.join(EXPORTS_DIR, 'Cahier_Complet_Atelier_Double_Page_A4.pdf')

    with open(out_html, 'w', encoding='utf-8') as f:
        f.write(full_html)

    res = subprocess.run(
        ['google-chrome', '--headless', '--disable-gpu', '--no-sandbox', f'--print-to-pdf={out_pdf}', out_html],
        capture_output=True, text=True
    )
    if res.returncode != 0:
        raise RuntimeError(f"Chrome PDF error: {res.stderr}")

    print(f"[OK] Generated {out_pdf} ({os.path.getsize(out_pdf):,} bytes)")


if __name__ == '__main__':
    main()
