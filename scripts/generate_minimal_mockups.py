import os
import subprocess

BASE_DIR = '/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie'
EXPORTS_DIR = os.path.join(BASE_DIR, 'exports_pdf')
PREVIEWS_DIR = os.path.join(EXPORTS_DIR, 'previews_v2')
os.makedirs(EXPORTS_DIR, exist_ok=True)
os.makedirs(PREVIEWS_DIR, exist_ok=True)

COMMON_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

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
}

.page {
  width: 210mm;
  height: 297mm;
  position: relative;
  overflow: hidden;
  page-break-after: always;
}

.page-left {
  padding: 16mm 18mm 14mm 14mm;
}

.page-right {
  padding: 16mm 14mm 14mm 18mm;
}

.spread-a3 {
  width: 420mm;
  height: 297mm;
  display: flex;
  page-break-after: always;
}

.spread-a3 .page-left {
  width: 210mm;
  height: 297mm;
  border-right: 1px dashed #e2e8f0;
  page-break-after: avoid;
}

.spread-a3 .page-right {
  width: 210mm;
  height: 297mm;
  page-break-after: avoid;
}
"""

# ==============================================================================
# MAQUETTE 1 : SUISSE MINIMALISTE (NOIR, BLANC, GRIS FINS, 1 ACCENT)
# ==============================================================================
CSS_M1 = """
.m1 {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Roboto', sans-serif;
  color: #111827;
  background: #ffffff;
}

.m1-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  border-bottom: 1.5px solid #111827;
  padding-bottom: 5mm;
  margin-bottom: 9mm;
}

.m1-kicker {
  font-size: 8pt;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: #6b7280;
  margin-bottom: 1.5mm;
}

.m1-title {
  font-size: 20pt;
  font-weight: 700;
  letter-spacing: -0.4px;
  color: #111827;
}

.m1-code {
  font-size: 9pt;
  font-weight: 600;
  color: #111827;
  border: 1px solid #d1d5db;
  padding: 1.5mm 3.5mm;
  border-radius: 2px;
}

.m1-section {
  font-size: 8.5pt;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  color: #6b7280;
  margin-bottom: 4mm;
}

.m1-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10mm;
}

.m1-table th {
  font-size: 8pt;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.6px;
  color: #6b7280;
  border-bottom: 1px solid #111827;
  padding: 2.5mm 2mm;
  text-align: left;
}

.m1-table th.num, .m1-table td.num {
  text-align: right;
}

.m1-table td {
  font-size: 9.5pt;
  padding: 2.6mm 2mm;
  border-bottom: 1px solid #f3f4f6;
  color: #111827;
}

.m1-table td.ing {
  font-weight: 500;
}

.m1-table td.num {
  font-weight: 600;
  font-size: 10pt;
}

.m1-table td.note {
  font-size: 8.2pt;
  color: #6b7280;
}

.m1-table tr.subtotal td {
  border-top: 1px solid #9ca3af;
  border-bottom: 1px solid #9ca3af;
  background: #f9fafb;
  font-weight: 700;
  padding: 3mm 2mm;
}

.m1-table tr.total td {
  border-top: 1.5px solid #111827;
  border-bottom: 1.5px solid #111827;
  font-weight: 700;
  font-size: 10.5pt;
  padding: 3.2mm 2mm;
}

.m1-steps {
  display: flex;
  flex-direction: column;
  gap: 3.5mm;
}

.m1-step {
  display: grid;
  grid-template-columns: 8mm 34mm 1fr;
  align-items: baseline;
  padding-bottom: 3mm;
  border-bottom: 1px solid #f3f4f6;
}

.m1-step-num {
  font-size: 9pt;
  font-weight: 700;
  color: #9ca3af;
}

.m1-step-label {
  font-size: 9.5pt;
  font-weight: 700;
  color: #111827;
}

.m1-step-val {
  font-size: 9.5pt;
  color: #374151;
  line-height: 1.4;
}

.m1-step-val strong {
  color: #111827;
}

.m1-kpi-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 6mm;
  margin-bottom: 10mm;
  padding: 4.5mm 0;
  border-top: 1px solid #e5e7eb;
  border-bottom: 1px solid #e5e7eb;
}

.m1-kpi-label {
  font-size: 7.5pt;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: #6b7280;
  margin-bottom: 1mm;
}

.m1-kpi-val {
  font-size: 13pt;
  font-weight: 700;
  color: #111827;
}

.m1-oura {
  margin-top: 8mm;
  padding: 4mm 5mm;
  border-left: 3px solid #dc2626;
  background: #fef2f2;
  font-size: 9.5pt;
  color: #991b1b;
}

.m1-footer {
  position: absolute;
  bottom: 10mm;
  left: 14mm;
  right: 14mm;
  display: flex;
  justify-content: space-between;
  font-size: 7.5pt;
  color: #9ca3af;
}
"""

def html_m1():
    left = """
    <div class="page page-left m1">
      <div class="m1-header">
        <div>
          <div class="m1-kicker">Viennoiserie • Pâte Levée Feuilletée</div>
          <h1 class="m1-title">Croissant Pur Beurre</h1>
        </div>
        <div class="m1-code">V-PLF-01</div>
      </div>

      <div class="m1-section">Pesées directes (en grammes)</div>
      <table class="m1-table">
        <thead>
          <tr>
            <th>Ingrédient</th>
            <th class="num">1 Bac</th>
            <th class="num">10 Bacs</th>
            <th class="num">20 Bacs</th>
            <th style="padding-left:5mm;">Repère</th>
          </tr>
        </thead>
        <tbody>
          <tr><td class="ing">Farine Gruau T45</td><td class="num">3 130 g</td><td class="num">31 300 g</td><td class="num">62 600 g</td><td class="note" style="padding-left:5mm;">En 1er en cuve</td></tr>
          <tr><td class="ing">Farine Tradition T65</td><td class="num">1 340 g</td><td class="num">13 400 g</td><td class="num">26 800 g</td><td class="note" style="padding-left:5mm;"></td></tr>
          <tr><td class="ing">Eau glacée (+1 °C)</td><td class="num">2 015 g</td><td class="num">20 150 g</td><td class="num">40 300 g</td><td class="note" style="padding-left:5mm;">Avec glaçons fondus</td></tr>
          <tr><td class="ing">Sucre cristal</td><td class="num">394 g</td><td class="num">3 940 g</td><td class="num">7 880 g</td><td class="note" style="padding-left:5mm;"></td></tr>
          <tr><td class="ing">Trimoline</td><td class="num">157 g</td><td class="num">1 570 g</td><td class="num">3 140 g</td><td class="note" style="padding-left:5mm;"></td></tr>
          <tr><td class="ing">Levure fraîche Or</td><td class="num">188 g</td><td class="num">1 880 g</td><td class="num">3 760 g</td><td class="note" style="padding-left:5mm;">Éloigner du sel</td></tr>
          <tr><td class="ing">Poudre de lait 26 %</td><td class="num">180 g</td><td class="num">1 800 g</td><td class="num">3 600 g</td><td class="note" style="padding-left:5mm;"></td></tr>
          <tr><td class="ing">Améliorant S500 Kimo</td><td class="num">90 g</td><td class="num">900 g</td><td class="num">1 800 g</td><td class="note" style="padding-left:5mm;">± 1 g strict</td></tr>
          <tr><td class="ing">Sel fin</td><td class="num">90 g</td><td class="num">900 g</td><td class="num">1 800 g</td><td class="note" style="padding-left:5mm;">± 1 g strict</td></tr>
          <tr><td class="ing">Vinaigre blanc 8°</td><td class="num">36 g</td><td class="num">360 g</td><td class="num">720 g</td><td class="note" style="padding-left:5mm;">Dans l'eau</td></tr>
          <tr><td class="ing">Margarine Opal cuve</td><td class="num">380 g</td><td class="num">3 800 g</td><td class="num">7 600 g</td><td class="note" style="padding-left:5mm;">Au passage en 2e vitesse</td></tr>
          <tr class="subtotal">
            <td>Détrempe nette</td><td class="num">8 000 g</td><td class="num">80 000 g</td><td class="num">160 000 g</td><td class="note" style="padding-left:5mm;">1 bac Paneo</td>
          </tr>
          <tr><td class="ing">Beurre tourage Debic 82 %</td><td class="num">2 000 g</td><td class="num">20 000 g</td><td class="num">40 000 g</td><td class="note" style="padding-left:5mm;">1 plaque / bac</td></tr>
          <tr class="total">
            <td>Total Pâton Touré</td><td class="num">10 000 g</td><td class="num">100 000 g</td><td class="num">200 000 g</td><td class="note" style="padding-left:5mm;">130 pièces / bac</td>
          </tr>
        </tbody>
      </table>

      <div class="m1-section">Pétrissage & Refroidissement (J-1)</div>
      <div class="m1-steps">
        <div class="m1-step">
          <div class="m1-step-num">01</div>
          <div class="m1-step-label">Frasage</div>
          <div class="m1-step-val"><strong>5 min en 1re vitesse</strong> (tout sauf margarine).</div>
        </div>
        <div class="m1-step">
          <div class="m1-step-num">02</div>
          <div class="m1-step-label">Pétrissage</div>
          <div class="m1-step-val">Ajouter la margarine. <strong>4 min 30 s en 2e vitesse</strong>. Arrêt au 1er décollement.</div>
        </div>
        <div class="m1-step">
          <div class="m1-step-num">03</div>
          <div class="m1-step-label">Température</div>
          <div class="m1-step-val">Sortie cuve : <strong>20 °C à 21 °C</strong>.</div>
        </div>
        <div class="m1-step">
          <div class="m1-step-num">04</div>
          <div class="m1-step-label">Mise en bac</div>
          <div class="m1-step-val">Diviser à <strong>8 000 g</strong>. Étaler en plaque de <strong>3 cm</strong> d'épaisseur.</div>
        </div>
        <div class="m1-step" style="border-bottom:none;">
          <div class="m1-step-num">05</div>
          <div class="m1-step-label">Froid</div>
          <div class="m1-step-val"><strong>30 min à -35 °C</strong> puis 12–15 h à <strong>+1 °C</strong>.</div>
        </div>
      </div>

      <div class="m1-footer">
        <span>Cahier d'Atelier • Style 1 : Minimaliste Suisse</span>
        <span>1 / 2</span>
      </div>
    </div>
    """

    right = """
    <div class="page page-right m1">
      <div class="m1-header">
        <div>
          <div class="m1-kicker">Exécution Laminoir, Façonnage & Four</div>
          <h2 class="m1-title" style="font-size:17pt;">Croissant Pur Beurre</h2>
        </div>
        <div class="m1-code">12 FILMS</div>
      </div>

      <div class="m1-kpi-row">
        <div>
          <div class="m1-kpi-label">Bande finale</div>
          <div class="m1-kpi-val">3,5 mm</div>
        </div>
        <div>
          <div class="m1-kpi-label">Triangle</div>
          <div class="m1-kpi-val">100 × 250 mm</div>
        </div>
        <div>
          <div class="m1-kpi-label">Poids cru</div>
          <div class="m1-kpi-val">77 g ± 2 g</div>
        </div>
      </div>

      <div class="m1-section">Tourage Laminoir (Jour J)</div>
      <div class="m1-steps" style="margin-bottom:9mm;">
        <div class="m1-step">
          <div class="m1-step-num">01</div>
          <div class="m1-step-label">Températures</div>
          <div class="m1-step-val">Pâte à <strong>+2 / +4 °C</strong> • Beurre souple à <strong>+12 / +14 °C</strong>.</div>
        </div>
        <div class="m1-step">
          <div class="m1-step-num">02</div>
          <div class="m1-step-label">Enchâssement</div>
          <div class="m1-step-val">Beurre au centre, rabattre les 2 ailes bord à bord.</div>
        </div>
        <div class="m1-step">
          <div class="m1-step-num">03</div>
          <div class="m1-step-label">1er Tour Double</div>
          <div class="m1-step-val">Allonger à <strong>85–90 cm</strong>, plier en portefeuille (4 plis). Repos <strong>15 min à +2 °C</strong>.</div>
        </div>
        <div class="m1-step">
          <div class="m1-step-num">04</div>
          <div class="m1-step-label">2e Tour Simple</div>
          <div class="m1-step-val">Tourner d'un quart de tour (90°), allonger à <strong>65 cm</strong>, plier en 3.</div>
        </div>
        <div class="m1-step" style="border-bottom:none;">
          <div class="m1-step-num">05</div>
          <div class="m1-step-label">Drossage & Repos</div>
          <div class="m1-step-val">Rogner les 4 bords sur 5 mm. Repos <strong>45 min à +2 °C</strong> sous film.</div>
        </div>
      </div>

      <div class="m1-section">Réglages Croissomat SCM50 & Couchage</div>
      <div class="m1-steps" style="margin-bottom:9mm;">
        <div class="m1-step">
          <div class="m1-step-num">A</div>
          <div class="m1-step-label">Manettes</div>
          <div class="m1-step-val">Droite (entrée) : <strong>2,2–2,5</strong> • Gauche (sortie) : <strong>3,0–3,2</strong> • Bas : <strong>7,5–8,0</strong>.</div>
        </div>
        <div class="m1-step">
          <div class="m1-step-num">B</div>
          <div class="m1-step-label">Farinage inversé</div>
          <div class="m1-step-val">Face farinée contre le tapis. Face vierge dessus.</div>
        </div>
        <div class="m1-step" style="border-bottom:none;">
          <div class="m1-step-num">C</div>
          <div class="m1-step-label">Couchage</div>
          <div class="m1-step-val">Pointe (clé) posée <strong>en dessous à 6 h</strong>. 15 pièces par plaque 600×400.</div>
        </div>
      </div>

      <div class="m1-section">Cuisson Fournil</div>
      <div class="m1-kpi-row" style="margin-bottom:4mm;">
        <div>
          <div class="m1-kpi-label">Four ventilé</div>
          <div class="m1-kpi-val">175 °C</div>
        </div>
        <div>
          <div class="m1-kpi-label">Buée</div>
          <div class="m1-kpi-val">3 secondes</div>
        </div>
        <div>
          <div class="m1-kpi-label">Durée totale</div>
          <div class="m1-kpi-val">17 minutes</div>
        </div>
      </div>

      <div class="m1-oura">
        <strong>Oura :</strong> Ouvrir en grand à <strong>14 minutes</strong>. Ressuage 15 min sur grille après sortie.
      </div>

      <div class="m1-footer">
        <span>Cahier d'Atelier • Style 1 : Minimaliste Suisse</span>
        <span>2 / 2</span>
      </div>
    </div>
    """
    return left, right

# ==============================================================================
# MAQUETTE 2 : ÉDITORIAL CHAUD & CLASSE (SÉRIF NOBLE, FILETS LAITON, RESPIRATION)
# ==============================================================================
CSS_M2 = """
.m2 {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  color: #1c1917;
  background: #fdfcf9;
}

.m2-header {
  border-bottom: 1px solid #b45309;
  padding-bottom: 5mm;
  margin-bottom: 8mm;
}

.m2-kicker {
  font-size: 8pt;
  font-weight: 600;
  letter-spacing: 1.8px;
  text-transform: uppercase;
  color: #b45309;
  margin-bottom: 1.5mm;
}

.m2-title-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.m2-title {
  font-family: 'Playfair Display', 'Source Serif Pro', Georgia, serif;
  font-size: 22pt;
  font-weight: 700;
  color: #1c1917;
}

.m2-ref {
  font-size: 9pt;
  color: #78716c;
  font-weight: 500;
}

.m2-section {
  font-family: 'Playfair Display', 'Source Serif Pro', Georgia, serif;
  font-size: 11.5pt;
  font-weight: 600;
  color: #92400e;
  margin-bottom: 4mm;
}

.m2-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 9mm;
  background: #ffffff;
}

.m2-table th {
  font-size: 7.8pt;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: #78716c;
  border-bottom: 1px solid #d6d3d1;
  padding: 2.5mm 3mm;
  text-align: left;
}

.m2-table th.num, .m2-table td.num {
  text-align: right;
}

.m2-table td {
  font-size: 9.2pt;
  padding: 2.4mm 3mm;
  border-bottom: 1px solid #f5f5f4;
}

.m2-table td.num {
  font-weight: 600;
}

.m2-table tr.subtotal td {
  background: #fafaf9;
  border-top: 1px solid #a8a29e;
  border-bottom: 1px solid #a8a29e;
  font-weight: 700;
}

.m2-table tr.total td {
  background: #fef3c7;
  border-top: 1.5px solid #b45309;
  border-bottom: 1.5px solid #b45309;
  font-weight: 700;
  color: #78350f;
}

.m2-card {
  background: #ffffff;
  border: 1px solid #e7e5e4;
  border-radius: 3px;
  padding: 4.5mm 5.5mm;
  margin-bottom: 6mm;
}

.m2-list {
  list-style: none;
}

.m2-list li {
  font-size: 9.3pt;
  line-height: 1.55;
  padding: 1.5mm 0;
  border-bottom: 1px solid #f5f5f4;
  color: #292524;
}

.m2-list li:last-child {
  border-bottom: none;
}

.m2-list li strong {
  color: #1c1917;
}

.m2-specs-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 4mm;
  margin-bottom: 6mm;
}

.m2-spec-box {
  background: #ffffff;
  border: 1px solid #e7e5e4;
  padding: 3.5mm 4.5mm;
  border-radius: 3px;
}

.m2-spec-lbl {
  font-size: 7.5pt;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: #78716c;
}

.m2-spec-val {
  font-size: 12pt;
  font-weight: 700;
  color: #1c1917;
  margin-top: 1mm;
}

.m2-footer {
  position: absolute;
  bottom: 10mm;
  left: 14mm;
  right: 14mm;
  display: flex;
  justify-content: space-between;
  font-size: 7.5pt;
  color: #a8a29e;
  border-top: 1px solid #e7e5e4;
  padding-top: 3mm;
}
"""

def html_m2():
    left = """
    <div class="page page-left m2">
      <div class="m2-header">
        <div class="m2-kicker">Fiche Technique n° 01 • Pâte Levée Feuilletée</div>
        <div class="m2-title-row">
          <h1 class="m2-title">Croissant Pur Beurre</h1>
          <span class="m2-ref">Code V-PLF-01 • 130 pcs / bac</span>
        </div>
      </div>

      <div class="m2-section">Pesées d'atelier</div>
      <table class="m2-table">
        <thead>
          <tr>
            <th>Matière première</th>
            <th class="num">1 Bac</th>
            <th class="num">10 Bacs</th>
            <th class="num">20 Bacs</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>Farine Gruau T45</td><td class="num">3 130 g</td><td class="num">31 300 g</td><td class="num">62 600 g</td></tr>
          <tr><td>Farine Tradition T65</td><td class="num">1 340 g</td><td class="num">13 400 g</td><td class="num">26 800 g</td></tr>
          <tr><td>Eau glacée (+1 °C)</td><td class="num">2 015 g</td><td class="num">20 150 g</td><td class="num">40 300 g</td></tr>
          <tr><td>Sucre cristal blanc</td><td class="num">394 g</td><td class="num">3 940 g</td><td class="num">7 880 g</td></tr>
          <tr><td>Trimoline (sucre inverti)</td><td class="num">157 g</td><td class="num">1 570 g</td><td class="num">3 140 g</td></tr>
          <tr><td>Levure fraîche Or <span style="color:#78716c; font-size:8pt;">(loin du sel)</span></td><td class="num">188 g</td><td class="num">1 880 g</td><td class="num">3 760 g</td></tr>
          <tr><td>Poudre de lait entier 26 %</td><td class="num">180 g</td><td class="num">1 800 g</td><td class="num">3 600 g</td></tr>
          <tr><td>Améliorant S500 Kimo</td><td class="num">90 g</td><td class="num">900 g</td><td class="num">1 800 g</td></tr>
          <tr><td>Sel fin</td><td class="num">90 g</td><td class="num">900 g</td><td class="num">1 800 g</td></tr>
          <tr><td>Vinaigre blanc 8° <span style="color:#78716c; font-size:8pt;">(dans l'eau)</span></td><td class="num">36 g</td><td class="num">360 g</td><td class="num">720 g</td></tr>
          <tr><td>Margarine Opal cuve <span style="color:#78716c; font-size:8pt;">(en 2e vitesse)</span></td><td class="num">380 g</td><td class="num">3 800 g</td><td class="num">7 600 g</td></tr>
          <tr class="subtotal"><td>Sous-total Détrempe</td><td class="num">8 000 g</td><td class="num">80 000 g</td><td class="num">160 000 g</td></tr>
          <tr><td>Beurre tourage Debic 82 % <span style="color:#78716c; font-size:8pt;">(plaques 2 kg)</span></td><td class="num">2 000 g</td><td class="num">20 000 g</td><td class="num">40 000 g</td></tr>
          <tr class="total"><td>Total Pâton Prêt</td><td class="num">10 000 g</td><td class="num">100 000 g</td><td class="num">200 000 g</td></tr>
        </tbody>
      </table>

      <div class="m2-section">Pétrissage & Refroidissement (J-1)</div>
      <div class="m2-card">
        <ul class="m2-list">
          <li><strong>1. Frasage :</strong> 5 min en 1re vitesse.</li>
          <li><strong>2. Pétrissage :</strong> Incorporer la margarine Opal. 4 min 30 s en 2e vitesse (arrêt au 1er décollement).</li>
          <li><strong>3. Température cible :</strong> 20 °C à 21 °C en sortie de cuve.</li>
          <li><strong>4. Mise en bac :</strong> Peser 8 000 g par bac, étaler à 3 cm d'épaisseur.</li>
          <li><strong>5. Froid :</strong> 30 min en cellule à -35 °C, puis nuit à +1 °C.</li>
        </ul>
      </div>

      <div class="m2-footer">
        <span>Cahier d'Atelier • Style 2 : Éditorial Chaud</span>
        <span>Page de gauche</span>
      </div>
    </div>
    """

    right = """
    <div class="page page-right m2">
      <div class="m2-header">
        <div class="m2-kicker">Tourage, Façonnage & Cuisson</div>
        <div class="m2-title-row">
          <h2 class="m2-title" style="font-size:19pt;">Croissant Pur Beurre</h2>
          <span class="m2-ref">12 Films • Rondo & SCM50</span>
        </div>
      </div>

      <div class="m2-section">1. Tourage (Jour J)</div>
      <div class="m2-card">
        <ul class="m2-list">
          <li><strong>Températures :</strong> Pâte à +2 / +4 °C • Beurre souple à +12 / +14 °C.</li>
          <li><strong>Enchâssement :</strong> Beurre centré, ailes rabattues bord à bord.</li>
          <li><strong>1er Tour Double :</strong> Allonger à 85–90 cm, plier en 4. Repos 15 min à +2 °C.</li>
          <li><strong>2e Tour Simple :</strong> Pivoter à 90°, allonger à 65 cm, plier en 3.</li>
          <li><strong>Finition :</strong> Rogner les 4 chants sur 5 mm. Repos 45 min à +2 °C sous plastique.</li>
        </ul>
      </div>

      <div class="m2-section">2. Découpe & Enroulement Croissomat</div>
      <div class="m2-specs-grid">
        <div class="m2-spec-box">
          <div class="m2-spec-lbl">Laminage final</div>
          <div class="m2-spec-val">Épaisseur 3,5 mm • Largeur 400 mm</div>
        </div>
        <div class="m2-spec-box">
          <div class="m2-spec-lbl">Découpe triangle</div>
          <div class="m2-spec-val">100 × 250 mm • Poids 77 g ± 2 g</div>
        </div>
      </div>
      <div class="m2-card">
        <ul class="m2-list">
          <li><strong>Manettes SCM50 :</strong> Entrée (droite) <strong>2,2–2,5</strong> • Sortie (gauche) <strong>3,0–3,2</strong> • Bas <strong>7,5–8,0</strong>.</li>
          <li><strong>Sens de bande :</strong> Face farinée dessous (contre le tapis).</li>
          <li><strong>Couchage :</strong> 15 pièces par plaque, pointe (clé) bloquée en dessous à 6 h.</li>
        </ul>
      </div>

      <div class="m2-section">3. Cuisson</div>
      <div class="m2-specs-grid" style="grid-template-columns: repeat(4, 1fr);">
        <div class="m2-spec-box">
          <div class="m2-spec-lbl">Four ventilé</div>
          <div class="m2-spec-val">175 °C</div>
        </div>
        <div class="m2-spec-box">
          <div class="m2-spec-lbl">Buée</div>
          <div class="m2-spec-val">3 s</div>
        </div>
        <div class="m2-spec-box" style="border-color:#fca5a5; background:#fef2f2;">
          <div class="m2-spec-lbl" style="color:#991b1b;">Oura ouvert</div>
          <div class="m2-spec-val" style="color:#991b1b;">À 14 min</div>
        </div>
        <div class="m2-spec-box">
          <div class="m2-spec-lbl">Cuisson</div>
          <div class="m2-spec-val">17 min</div>
        </div>
      </div>

      <div class="m2-footer">
        <span>Cahier d'Atelier • Style 2 : Éditorial Chaud</span>
        <span>Page de droite</span>
      </div>
    </div>
    """
    return left, right

# ==============================================================================
# MAQUETTE 3 : ATELIER DIRECT (GÉANT LISIBLE À 1,5 M, PASTILLES DISCRÈTES)
# ==============================================================================
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
  padding: 4.5mm 6mm;
  border-radius: 3px;
  margin-bottom: 7mm;
}

.m3-title {
  font-size: 17pt;
  font-weight: 800;
  letter-spacing: -0.3px;
}

.m3-badge {
  background: #2563eb;
  color: #ffffff;
  font-size: 8.5pt;
  font-weight: 700;
  padding: 1.5mm 3.5mm;
  border-radius: 2px;
}

.m3-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 8mm;
}

.m3-table th {
  font-size: 8pt;
  font-weight: 700;
  text-transform: uppercase;
  color: #475569;
  border-bottom: 2px solid #0f172a;
  padding: 2mm 2mm;
  text-align: left;
}

.m3-table th.num, .m3-table td.num {
  text-align: right;
}

.m3-table td {
  font-size: 9.8pt;
  padding: 2.3mm 2mm;
  border-bottom: 1px solid #e2e8f0;
}

.m3-table td.num {
  font-weight: 700;
  font-size: 10.5pt;
}

.m3-dot {
  display: inline-block;
  width: 2.5mm;
  height: 2.5mm;
  border-radius: 50%;
  margin-right: 2mm;
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
  font-size: 10.8pt;
  border-top: 2px solid #2563eb;
  border-bottom: 2px solid #2563eb;
}

.m3-h2 {
  font-size: 10pt;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #0f172a;
  margin-bottom: 3.5mm;
  display: flex;
  align-items: center;
  gap: 2mm;
}

.m3-chrono {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 3.5mm;
  margin-bottom: 6mm;
}

.m3-chrono-item {
  border: 1px solid #cbd5e1;
  border-radius: 3px;
  padding: 3.5mm 4.5mm;
}

.m3-chrono-item .m3-step-head {
  display: block;
  font-size: 10pt;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 1mm;
}

.m3-chrono-item span {
  font-size: 9pt;
  color: #475569;
  line-height: 1.35;
}

.m3-big-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 4mm;
  margin-bottom: 7mm;
}

.m3-big-box {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-radius: 3px;
  padding: 3.5mm 4mm;
  text-align: center;
}

.m3-big-box .val {
  font-size: 14pt;
  font-weight: 800;
  color: #0f172a;
}

.m3-big-box .lbl {
  font-size: 7.5pt;
  font-weight: 600;
  text-transform: uppercase;
  color: #64748b;
  margin-top: 1mm;
}

.m3-alert {
  background: #fef2f2;
  border: 1.5px solid #ef4444;
  color: #991b1b;
  border-radius: 3px;
  padding: 3.5mm 5mm;
  font-size: 9.8pt;
  font-weight: 700;
  text-align: center;
  margin-top: 5mm;
}

.m3-footer {
  position: absolute;
  bottom: 10mm;
  left: 14mm;
  right: 14mm;
  display: flex;
  justify-content: space-between;
  font-size: 7.5pt;
  color: #94a3b8;
}
"""

def html_m3():
    left = """
    <div class="page page-left m3">
      <div class="m3-topbar">
        <div class="m3-title">CROISSANT PUR BEURRE PAC</div>
        <div class="m3-badge">V-PLF-01 • 130 PCS / BAC</div>
      </div>

      <div class="m3-h2">1. Pesées en grammes</div>
      <table class="m3-table">
        <thead>
          <tr>
            <th>Ingrédient</th>
            <th class="num">1 Bac</th>
            <th class="num">10 Bacs</th>
            <th class="num">20 Bacs</th>
          </tr>
        </thead>
        <tbody>
          <tr><td><span class="m3-dot dot-1"></span>Farine Gruau T45</td><td class="num">3 130 g</td><td class="num">31 300 g</td><td class="num">62 600 g</td></tr>
          <tr><td><span class="m3-dot dot-1"></span>Farine Tradition T65</td><td class="num">1 340 g</td><td class="num">13 400 g</td><td class="num">26 800 g</td></tr>
          <tr><td><span class="m3-dot dot-1"></span>Eau glacée (+1 °C)</td><td class="num">2 015 g</td><td class="num">20 150 g</td><td class="num">40 300 g</td></tr>
          <tr><td><span class="m3-dot dot-1"></span>Sucre cristal</td><td class="num">394 g</td><td class="num">3 940 g</td><td class="num">7 880 g</td></tr>
          <tr><td><span class="m3-dot dot-1"></span>Trimoline</td><td class="num">157 g</td><td class="num">1 570 g</td><td class="num">3 140 g</td></tr>
          <tr><td><span class="m3-dot dot-1"></span>Levure fraîche Or</td><td class="num">188 g</td><td class="num">1 880 g</td><td class="num">3 760 g</td></tr>
          <tr><td><span class="m3-dot dot-1"></span>Poudre de lait 26 %</td><td class="num">180 g</td><td class="num">1 800 g</td><td class="num">3 600 g</td></tr>
          <tr><td><span class="m3-dot dot-1"></span>Améliorant S500 Kimo</td><td class="num">90 g</td><td class="num">900 g</td><td class="num">1 800 g</td></tr>
          <tr><td><span class="m3-dot dot-1"></span>Sel fin</td><td class="num">90 g</td><td class="num">900 g</td><td class="num">1 800 g</td></tr>
          <tr><td><span class="m3-dot dot-1"></span>Vinaigre blanc 8°</td><td class="num">36 g</td><td class="num">360 g</td><td class="num">720 g</td></tr>
          <tr><td><span class="m3-dot dot-2"></span>Margarine Opal (en 2e vit.)</td><td class="num">380 g</td><td class="num">3 800 g</td><td class="num">7 600 g</td></tr>
          <tr class="subtotal"><td>Détrempe nette</td><td class="num">8 000 g</td><td class="num">80 000 g</td><td class="num">160 000 g</td></tr>
          <tr><td><span class="m3-dot dot-3"></span>Beurre Debic 82 % (tourage)</td><td class="num">2 000 g</td><td class="num">20 000 g</td><td class="num">40 000 g</td></tr>
          <tr class="total"><td>TOTAL PÂTON TOURÉ</td><td class="num">10 000 g</td><td class="num">100 000 g</td><td class="num">200 000 g</td></tr>
        </tbody>
      </table>

      <div class="m3-h2">2. Pétrissage & Froid (J-1)</div>
      <div class="m3-chrono">
        <div class="m3-chrono-item">
          <span class="m3-step-head">Frasage : 5 min V1</span>
          <span>Tous ingrédients bleus, loin du sel pour la levure.</span>
        </div>
        <div class="m3-chrono-item">
          <span class="m3-step-head">Pétrissage : 4 min 30 s V2</span>
          <span>Ajouter margarine Opal. Stop au 1er décollement.</span>
        </div>
        <div class="m3-chrono-item">
          <span class="m3-step-head">Sortie cuve : 20–21 °C</span>
          <span>Étaler 8 000 g par bac sur 3 cm d'épaisseur.</span>
        </div>
        <div class="m3-chrono-item">
          <span class="m3-step-head">Flash : 30 min à -35 °C</span>
          <span>Puis stocker 12 à 15 h à +1 °C.</span>
        </div>
      </div>

      <div class="m3-footer">
        <span>Cahier d'Atelier • Style 3 : Poste Direct</span>
        <span>Gauche</span>
      </div>
    </div>
    """

    right = """
    <div class="page page-right m3">
      <div class="m3-topbar" style="background:#1e293b;">
        <div class="m3-title" style="font-size:15pt;">TOURAGE, FAÇONNAGE & CUISSON</div>
        <div class="m3-badge" style="background:#16a34a;">12 FILMS</div>
      </div>

      <div class="m3-h2">3. Tourage Laminoir</div>
      <div class="m3-chrono" style="margin-bottom:7mm;">
        <div class="m3-chrono-item">
          <span class="m3-step-head">1. Enchâssement</span>
          <span>Pâte +2/+4 °C • Beurre +12/+14 °C. Rabattre bord à bord.</span>
        </div>
        <div class="m3-chrono-item">
          <span class="m3-step-head">2. Tour Double (4 plis)</span>
          <span>Allonger 85–90 cm. Plier en 4. Repos <strong>15 min à +2 °C</strong>.</span>
        </div>
        <div class="m3-chrono-item">
          <span class="m3-step-head">3. Tour Simple (3 plis)</span>
          <span>Pivot 90°. Allonger 65 cm. Plier en 3.</span>
        </div>
        <div class="m3-chrono-item">
          <span class="m3-step-head">4. Drossage & Détente</span>
          <span>Rogner 4 bords (5 mm). Repos <strong>45 min à +2 °C</strong>.</span>
        </div>
      </div>

      <div class="m3-h2">4. Découpe & Croissomat SCM50</div>
      <div class="m3-big-grid">
        <div class="m3-big-box">
          <div class="val">3,5 mm</div>
          <div class="lbl">Épaisseur bande</div>
        </div>
        <div class="m3-big-box">
          <div class="val">100 × 250</div>
          <div class="lbl">Triangle (mm)</div>
        </div>
        <div class="m3-big-box">
          <div class="val">77 g ± 2 g</div>
          <div class="lbl">Poids cru</div>
        </div>
      </div>

      <div class="m3-chrono" style="margin-bottom:7mm;">
        <div class="m3-chrono-item">
          <span class="m3-step-head">Manettes SCM50</span>
          <span>Droite : <strong>2,2–2,5</strong> • Gauche : <strong>3,0–3,2</strong> • Bas : <strong>7,5–8,0</strong></span>
        </div>
        <div class="m3-chrono-item">
          <span class="m3-step-head">Pose & Clé</span>
          <span>Face farinée dessous. Clé calée à <strong>6 h en dessous</strong> (15/plaque).</span>
        </div>
      </div>

      <div class="m3-h2">5. Cuisson Fournil</div>
      <div class="m3-big-grid" style="margin-bottom:4mm;">
        <div class="m3-big-box">
          <div class="val">175 °C</div>
          <div class="lbl">Four ventilé</div>
        </div>
        <div class="m3-big-box">
          <div class="val">3 s</div>
          <div class="lbl">Buée départ</div>
        </div>
        <div class="m3-big-box">
          <div class="val">17 min</div>
          <div class="lbl">Temps total</div>
        </div>
      </div>

      <div class="m3-alert">
        OUVRIR L'OURA EN GRAND À 14 MINUTES CHRONO • RESSUAGE 15 MIN SUR GRILLE
      </div>

      <div class="m3-footer">
        <span>Cahier d'Atelier • Style 3 : Poste Direct</span>
        <span>Droite</span>
      </div>
    </div>
    """
    return left, right

def render_pdf(name, css, left, right):
    # A4 portrait facing pages
    html_a4 = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>{COMMON_CSS}@page {{ size: A4 portrait; margin: 0; }}{css}</style></head><body>{left}{right}</body></html>"""
    p_a4_html = os.path.join(EXPORTS_DIR, f"{name}_A4.html")
    p_a4_pdf = os.path.join(EXPORTS_DIR, f"{name}_A4.pdf")
    with open(p_a4_html, 'w', encoding='utf-8') as f:
        f.write(html_a4)
    subprocess.run(['google-chrome', '--headless', '--disable-gpu', '--no-sandbox', f'--print-to-pdf={p_a4_pdf}', p_a4_html], capture_output=True)

    # A3 landscape spread preview
    html_a3 = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>{COMMON_CSS}@page {{ size: A3 landscape; margin: 0; }}{css}</style></head><body><div class="spread-a3">{left}{right}</div></body></html>"""
    p_a3_html = os.path.join(EXPORTS_DIR, f"{name}_A3_livre_ouvert.html")
    p_a3_pdf = os.path.join(EXPORTS_DIR, f"{name}_A3_livre_ouvert.pdf")
    with open(p_a3_html, 'w', encoding='utf-8') as f:
        f.write(html_a3)
    subprocess.run(['google-chrome', '--headless', '--disable-gpu', '--no-sandbox', f'--print-to-pdf={p_a3_pdf}', p_a3_html], capture_output=True)

    # Render PNG preview of A3 spread
    subprocess.run(['pdftoppm', '-png', '-r', '150', p_a3_pdf, os.path.join(PREVIEWS_DIR, name)], capture_output=True)
    print(f"[OK] {name} -> A4 ({os.path.getsize(p_a4_pdf):,} o) | A3 ({os.path.getsize(p_a3_pdf):,} o)")

if __name__ == '__main__':
    l1, r1 = html_m1()
    render_pdf("V2_Maquette_1_Suisse_Minimal", CSS_M1, l1, r1)

    l2, r2 = html_m2()
    render_pdf("V2_Maquette_2_Editorial_Classe", CSS_M2, l2, r2)

    l3, r3 = html_m3()
    render_pdf("V2_Maquette_3_Atelier_Direct", CSS_M3, l3, r3)
