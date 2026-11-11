import os
import base64
import subprocess

BASE_DIR = '/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie'
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
VECTORS_DIR = os.path.join(DOCS_DIR, 'vectors')
EXPORTS_DIR = os.path.join(BASE_DIR, 'exports_pdf')
os.makedirs(EXPORTS_DIR, exist_ok=True)

def get_base64_img(filename):
    path = os.path.join(DOCS_DIR, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
            return f"data:image/jpeg;base64,{encoded}"
    return ""

def get_svg_content(filename):
    path = os.path.join(VECTORS_DIR, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('<?xml'):
                content = content[content.find('?>')+2:].strip()
            return content
    return ""

# Load assets
img_croissant = get_base64_img('photo_croissant_alveolage_excellence.jpg')
img_chocolat = get_base64_img('photo_pain_chocolat_coupe_excellence.jpg')
img_kouign = get_base64_img('photo_kouign_amann_excellence.jpg')

svg_12_films = get_svg_content('tourage_12_films_schema.svg')
svg_croissant_geom = get_svg_content('faconnage_croissant_geometrie.svg')
svg_chocolat_geom = get_svg_content('faconnage_pain_chocolat_geometrie.svg')
svg_cuisson_oura = get_svg_content('bareme_cuisson_oura.svg')
svg_kouign_tourage = get_svg_content('tourage_kouign_amann_schema.svg')

print("Loaded all photos and SVGs.")

# ==============================================================================
# COMMON CSS & RESET FOR PRINTED A4 SPREADS
# ==============================================================================
COMMON_PRINT_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,600&family=Inter:wght@400;500;600;700;800&family=Roboto+Condensed:wght@600;700&display=swap');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

@page {
  size: A4 portrait;
  margin: 0;
}

body {
  margin: 0;
  padding: 0;
  background-color: #cbd5e1;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  color: #0f172a;
  -webkit-font-smoothing: antialiased;
}

.page {
  width: 210mm;
  height: 297mm;
  position: relative;
  overflow: hidden;
  page-break-after: always;
  background-color: #ffffff;
}

/* Page Spreads Margins : Gutter is on the right for left page, on the left for right page */
.page-left {
  padding: 10mm 15mm 10mm 12mm;
}

.page-right {
  padding: 10mm 12mm 10mm 15mm;
}

.panoramic-spread {
  width: 420mm;
  height: 297mm;
  display: flex;
  background-color: #ffffff;
  page-break-after: always;
}
.panoramic-left {
  width: 210mm;
  height: 297mm;
  padding: 10mm 15mm 10mm 12mm;
  border-right: 1px dashed #cbd5e1;
  position: relative;
  overflow: hidden;
}
.panoramic-right {
  width: 210mm;
  height: 297mm;
  padding: 10mm 12mm 10mm 15mm;
  position: relative;
  overflow: hidden;
}
"""

# ==============================================================================
# STYLE 1 : GRAND LIVRE D'ART CULINAIRE (ÉDITION PRESTIGE / FERRANDI - DUCASSE)
# ==============================================================================
STYLE_1_CSS = """
/* STYLE 1 : GRAND LIVRE D'ART CULINAIRE */
.style1-body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: #1e1b18;
  background-color: #faf9f5;
}

.style1-page {
  background-color: #faf9f5;
  border: 1px solid #e7e3d8;
}

.style1-header {
  border-bottom: 2px solid #b45309;
  padding-bottom: 5px;
  margin-bottom: 8px;
  position: relative;
}

.style1-header::after {
  content: "";
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 100%;
  height: 1px;
  background-color: #d97706;
}

.style1-sup-title {
  font-family: 'Cinzel', 'Source Serif Pro', 'DejaVu Serif', serif;
  font-size: 8pt;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: #b45309;
  font-weight: 700;
  margin-bottom: 2px;
}

.style1-title {
  font-family: 'Cinzel', 'Playfair Display', 'Source Serif Pro', serif;
  font-size: 17pt;
  font-weight: 800;
  color: #0f172a;
  letter-spacing: 0.5px;
  margin-bottom: 3px;
  text-transform: uppercase;
}

.style1-meta {
  font-size: 8.5pt;
  color: #57534e;
  font-weight: 500;
  display: flex;
  justify-content: space-between;
}

.style1-gold-tag {
  background-color: #fef3c7;
  color: #92400e;
  padding: 2px 7px;
  border-radius: 3px;
  font-weight: 700;
  border: 1px solid #fde68a;
  font-size: 8pt;
}

.style1-quote {
  font-family: 'Playfair Display', 'Source Serif Pro', Georgia, serif;
  font-style: italic;
  font-size: 8.8pt;
  line-height: 1.35;
  color: #78350f;
  background-color: #fefce8;
  border-left: 3px solid #b45309;
  padding: 4px 10px;
  margin-bottom: 8px;
}

.style1-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
  margin-bottom: 8px;
  background-color: #ffffff;
  border: 1px solid #e7e5e4;
}

.style1-table th {
  background-color: #1c1917;
  color: #fef3c7;
  font-family: 'Cinzel', serif;
  font-size: 7.5pt;
  letter-spacing: 0.5px;
  padding: 4px 6px;
  text-align: left;
  border: 1px solid #292524;
}

.style1-table td {
  padding: 3.5px 6px;
  border: 1px solid #e7e5e4;
  color: #292524;
}

.style1-table tr:nth-child(even) {
  background-color: #fcfbf9;
}

.style1-table tr.total-row {
  background-color: #fef3c7;
  font-weight: 800;
  color: #78350f;
  border-top: 2px solid #b45309;
}

.style1-section-title {
  font-family: 'Cinzel', 'Source Serif Pro', serif;
  font-size: 9.5pt;
  font-weight: 800;
  letter-spacing: 1px;
  color: #78350f;
  text-transform: uppercase;
  border-bottom: 1px solid #e7e5e4;
  padding-bottom: 2px;
  margin: 6px 0 5px 0;
  display: flex;
  align-items: center;
  gap: 6px;
}

.style1-steps-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
  margin-bottom: 8px;
}

.style1-step-card {
  background-color: #ffffff;
  border: 1px solid #e7e5e4;
  border-top: 3px solid #b45309;
  padding: 5px 8px;
  border-radius: 3px;
}

.style1-step-card h4 {
  font-size: 8.5pt;
  color: #0f172a;
  font-weight: 700;
  margin-bottom: 2px;
}

.style1-step-card p {
  font-size: 7.8pt;
  color: #44403c;
  line-height: 1.3;
}

.style1-photo-container {
  border: 1px solid #d6d3d1;
  background-color: #ffffff;
  padding: 4px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.06);
  margin-bottom: 8px;
  border-radius: 4px;
}

.style1-photo-img {
  width: 100%;
  height: 52mm;
  object-fit: cover;
  border-radius: 2px;
  display: block;
}

.style1-photo-caption {
  font-size: 7.5pt;
  color: #78350f;
  font-weight: 600;
  text-align: center;
  padding-top: 3px;
  font-style: italic;
}

.style1-vector-box {
  background-color: #ffffff;
  border: 1px solid #e7e5e4;
  border-radius: 4px;
  padding: 4px;
  margin-bottom: 7px;
}

.style1-bake-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 7.8pt;
  margin-top: 4px;
  background-color: #ffffff;
  border: 1px solid #e7e5e4;
}

.style1-bake-table th {
  background-color: #78350f;
  color: #ffffff;
  padding: 3.5px 5px;
  font-size: 7.2pt;
  font-weight: 700;
  text-align: center;
}

.style1-bake-table td {
  padding: 4px 6px;
  border: 1px solid #e7e5e4;
  text-align: center;
}

.style1-oura-alert {
  background-color: #fef2f2;
  border: 1px solid #fecaca;
  color: #991b1b;
  font-weight: 800;
}

.style1-footer {
  position: absolute;
  bottom: 6mm;
  left: 12mm;
  right: 15mm;
  display: flex;
  justify-content: space-between;
  font-size: 7.5pt;
  color: #78716c;
  border-top: 1px solid #e7e5e4;
  padding-top: 4px;
}
"""

def generate_style_1_html():
    left_html = f"""
    <div class="style1-body style1-page panoramic-left">
      <div class="style1-header">
        <div class="style1-sup-title">Laboratoire de Tourage d'Excellence • Recette de Maître N°01</div>
        <h1 class="style1-title">Croissant Pur Beurre PAC</h1>
        <div class="style1-meta">
          <span><strong>Code :</strong> <code>V-PLF-01</code> | Pousse Lente 24 h</span>
          <span class="style1-gold-tag">Standard d'Or : 12 Films de Beurre</span>
          <span><strong>Rendement :</strong> 130 pièces de 77 g / pâton</span>
        </div>
      </div>

      <div class="style1-quote">
        « L’alvéolage en toile d'araignée n'est jamais le fruit du hasard : il résulte strictement de l'alternance géométrique de 12 films de matière grasse calibrés à 25-30 µm et d'une pâte préservée de tout écrouissage. »
      </div>

      <div class="style1-section-title">1. Formule Meunière & Pesées d'Atelier (100% Grammes • 0 Virgule)</div>
      <table class="style1-table">
        <thead>
          <tr>
            <th>Phase</th>
            <th>Ingrédient d'Atelier</th>
            <th>% Meun.</th>
            <th>1 Bac (8 000 g)</th>
            <th>10 Bacs (80 kg)</th>
            <th>Consigne Opérateur</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong style="color:#1d4ed8;">[1] Poudres</strong></td>
            <td><strong>Farine Gruau Rouge T45</strong></td>
            <td>70,0 %</td>
            <td><strong>3 130 g</strong></td>
            <td>31 300 g</td>
            <td>W 320, P/L 0,6. Tamisée en cuve.</td>
          </tr>
          <tr>
            <td><strong style="color:#1d4ed8;">[1] Poudres</strong></td>
            <td><strong>Farine Tradition T65 pure</strong></td>
            <td>30,0 %</td>
            <td><strong>1 340 g</strong></td>
            <td>13 400 g</td>
            <td>Apport extensibilité et arômes.</td>
          </tr>
          <tr>
            <td><strong style="color:#1d4ed8;">[1] Coulage</strong></td>
            <td><strong>Eau glacée (+1 °C) / Glace</strong></td>
            <td>45,0 %</td>
            <td><strong>2 015 g</strong></td>
            <td>20 150 g</td>
            <td>Compenser échauffement spirale.</td>
          </tr>
          <tr>
            <td><strong style="color:#1d4ed8;">[1] Poudres</strong></td>
            <td><strong>Sucre cristal blanc</strong></td>
            <td>8,8 %</td>
            <td><strong>394 g</strong></td>
            <td>3 940 g</td>
            <td>Nourriture levure & coloration.</td>
          </tr>
          <tr>
            <td><strong style="color:#1d4ed8;">[1] Poudres</strong></td>
            <td><strong>Trimoline (Sucre inverti)</strong></td>
            <td>3,5 %</td>
            <td><strong>157 g</strong></td>
            <td>1 570 g</td>
            <td>Fixateur de moelleux & cryoprotection.</td>
          </tr>
          <tr>
            <td><strong style="color:#1d4ed8;">[1] Poudres</strong></td>
            <td><strong>Levure fraîche L'Hirondelle Or</strong></td>
            <td>4,2 %</td>
            <td><strong>188 g</strong></td>
            <td>1 880 g</td>
            <td>Émiettée sur farine (loin du sel).</td>
          </tr>
          <tr>
            <td><strong style="color:#1d4ed8;">[1] Poudres</strong></td>
            <td><strong>Poudre de lait entier 26 %</strong></td>
            <td>4,0 %</td>
            <td><strong>180 g</strong></td>
            <td>1 800 g</td>
            <td>Extrait sec & saveur lactée.</td>
          </tr>
          <tr>
            <td><strong style="color:#1d4ed8;">[1] Poudres</strong></td>
            <td><strong>Sel fin de cuisine</strong></td>
            <td>2,0 %</td>
            <td><strong>90 g</strong></td>
            <td>900 g</td>
            <td>Pesée balance précision (±1 g).</td>
          </tr>
          <tr>
            <td><strong style="color:#1d4ed8;">[1] Poudres</strong></td>
            <td><strong>Améliorant S500 Kimo Short</strong></td>
            <td>2,0 %</td>
            <td><strong>90 g</strong></td>
            <td>900 g</td>
            <td>Plafonné strict : ne jamais surdoser.</td>
          </tr>
          <tr>
            <td><strong style="color:#1d4ed8;">[1] Coulage</strong></td>
            <td><strong>Vinaigre d'alcool blanc 8°</strong></td>
            <td>0,8 %</td>
            <td><strong>36 g</strong></td>
            <td>360 g</td>
            <td>Abaisse le pH, gain de plasticité.</td>
          </tr>
          <tr>
            <td><strong style="color:#d97706;">[2] Matière</strong></td>
            <td><strong>Margarine Opal cuve (500 g)</strong></td>
            <td>8,5 %</td>
            <td><strong>380 g</strong></td>
            <td>3 800 g</td>
            <td>Morceaux froids dès passage en V2.</td>
          </tr>
          <tr class="total-row">
            <td colspan="2">DÉTREMPE NETTE EN CUVE</td>
            <td>178,8 %</td>
            <td>8 000 g pile</td>
            <td>80 000 g pile</td>
            <td>Format bac Paneo (Base farine : 4 470 g).</td>
          </tr>
          <tr>
            <td><strong style="color:#15803d;">[3] Tourage</strong></td>
            <td><strong>Beurre Tourage Debic 82 %</strong></td>
            <td>25 % dét.</td>
            <td><strong>2 000 g (1 pl.)</strong></td>
            <td>20 000 g (10 pl.)</td>
            <td>1 plaque de 2 000 g pile / bac.</td>
          </tr>
          <tr class="total-row" style="background-color:#fde68a;">
            <td colspan="2">PÂTON COMPLET PRÊT AU TOURAGE</td>
            <td>223,8 %</td>
            <td>10 000 g pile</td>
            <td>100 000 g pile</td>
            <td>Rendement étalon : 130 croissants net.</td>
          </tr>
        </tbody>
      </table>

      <div class="style1-section-title">2. Protocole Opératoire Chrono (J-1)</div>
      <div class="style1-steps-grid">
        <div class="style1-step-card">
          <h4>1. Frasage (1ʳᵉ Vitesse)</h4>
          <p><strong>5 min chrono</strong> avec les poudres et l'eau glacée (+1 °C). Amalgame sans corsage.</p>
        </div>
        <div class="style1-step-card">
          <h4>2. Pétrissage (2ᵉ Vitesse)</h4>
          <p><strong>4 min 30 s à 5 min max</strong> avec margarine [2]. <strong>Arrêt au 1er décollement net</strong>. T° pâte : <strong>20 °C – 21 °C</strong>.</p>
        </div>
        <div class="style1-step-card">
          <h4>3. Règle des 3 cm (Loi de Fourier)</h4>
          <p>Diviser à <strong>8 000 g pile</strong>. Aplatir en galette de <strong>3 cm d'épaisseur</strong> dans le bac Paneo.</p>
        </div>
        <div class="style1-step-card">
          <h4>4. Froid Flash & Nuit Positive</h4>
          <p><strong>35 min flash à -35 °C</strong> (cœur sous +6 °C). Stockage nuit régulé à <strong>0 °C / +1,5 °C</strong> (proscrire +4 °C).</p>
        </div>
      </div>

      <div class="style1-footer">
        <span>Laboratoire Tourage & Boulangerie • Cahier de Recettes de Haute Volée</span>
        <span>Page Gauche • Fiche N°01</span>
      </div>
    </div>
    """

    right_html = f"""
    <div class="style1-body style1-page panoramic-right">
      <div class="style1-header">
        <div class="style1-sup-title">Guides Visuels Vectoriels & Conduite Thermique</div>
        <h2 class="style1-title" style="font-size:14pt;">Tourage 12 Films, Façonnage & Cuisson d'Excellence</h2>
        <div class="style1-meta">
          <span>Laminoir Rondo Compas • Enrouleur Croissomat SCM50</span>
          <span class="style1-gold-tag">Coupe Alvéolée Étalon</span>
        </div>
      </div>

      <!-- Studio photo macro of crumb -->
      <div class="style1-photo-container">
        <img class="style1-photo-img" src="{img_croissant}" alt="Alvéolage Croissant 12 Films"/>
        <div class="style1-photo-caption">Standard d'Or Atelier : Alvéolage en toile d'araignée régulier et brillant • Croûte dorée croustillante à fines écailles</div>
      </div>

      <!-- SVG 1: Tourage 12 Films -->
      <div class="style1-section-title">1. Guide Mécanique : Pliage des 12 Films de Beurre</div>
      <div class="style1-vector-box" style="height:44mm; overflow:hidden;">
        {svg_12_films}
      </div>

      <!-- SVG 2: Façonnage Croissant -->
      <div class="style1-section-title">2. Guide Découpe & Calage de la Clé à 6 Heures</div>
      <div class="style1-vector-box" style="height:44mm; overflow:hidden;">
        {svg_croissant_geom}
      </div>

      <!-- Baking Table with Damper Alert -->
      <div class="style1-section-title">3. Barème Thermique Fournil & Décompression d'Oura</div>
      <table class="style1-bake-table">
        <thead>
          <tr>
            <th>Préchauffage</th>
            <th>Température Régulée</th>
            <th>Buée Enfournement</th>
            <th>MINUTE OUVERTURE D'OURA</th>
            <th>Durée Totale</th>
            <th>Ressuage Grille</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>195 °C</strong></td>
            <td><strong>175 °C ventilé</strong></td>
            <td><strong>3 secondes</strong></td>
            <td class="style1-oura-alert">À 14 MIN CHRONO (OUVRIR EN GRAND)</td>
            <td><strong>17 minutes</strong></td>
            <td>15 min sur grille (air libre)</td>
          </tr>
        </tbody>
      </table>

      <div class="style1-footer">
        <span>Contrôle Qualité : Poids cuit cible 65 g ± 2 g • Facteur d'expansion ≥ 2,2</span>
        <span>Page Droite • Fiche N°01</span>
      </div>
    </div>
    """
    return left_html, right_html

# ==============================================================================
# STYLE 2 : LABORATOIRE INDUSTRIEL & SIGNALÉTIQUE SUISSE (RONDO / PURATOS)
# ==============================================================================
STYLE_2_CSS = """
/* STYLE 2 : LABORATOIRE INDUSTRIEL SUISSE */
.style2-body {
  font-family: 'Inter', 'Roboto Condensed', -apple-system, BlinkMacSystemFont, sans-serif;
  color: #0f172a;
  background-color: #ffffff;
}

.style2-page {
  background-color: #ffffff;
  border: 1px solid #cbd5e1;
}

.style2-badge-header {
  background-color: #0f172a;
  color: #ffffff;
  padding: 8px 12px;
  border-radius: 4px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.style2-code-pill {
  background-color: #0284c7;
  color: #ffffff;
  padding: 3px 8px;
  border-radius: 3px;
  font-weight: 800;
  font-size: 8.5pt;
  letter-spacing: 0.5px;
}

.style2-title {
  font-size: 15pt;
  font-weight: 900;
  color: #0f172a;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 4px 0 2px 0;
}

.style2-subline {
  font-size: 8.5pt;
  color: #64748b;
  font-weight: 600;
  margin-bottom: 8px;
}

.style2-alert-bar {
  background-color: #f0f9ff;
  border-left: 4px solid #0284c7;
  padding: 5px 8px;
  font-size: 8pt;
  color: #0369a1;
  font-weight: 600;
  margin-bottom: 8px;
  display: flex;
  justify-content: space-between;
}

.style2-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 7.8pt;
  margin-bottom: 8px;
}

.style2-table th {
  background-color: #1e293b;
  color: #ffffff;
  font-weight: 700;
  text-align: left;
  padding: 4px 6px;
  font-size: 7.5pt;
  border: 1px solid #1e293b;
}

.style2-table td {
  padding: 3.5px 6px;
  border: 1px solid #cbd5e1;
  color: #0f172a;
}

.style2-table tr:nth-child(even) {
  background-color: #f8fafc;
}

.style2-table tr.total-row {
  background-color: #e0f2fe;
  font-weight: 800;
  color: #0369a1;
  border-top: 2px solid #0284c7;
}

.style2-phase-1 { color: #0284c7; font-weight: 800; }
.style2-phase-2 { color: #d97706; font-weight: 800; }
.style2-phase-3 { color: #16a34a; font-weight: 800; }

.style2-block-title {
  background-color: #0f172a;
  color: #ffffff;
  font-size: 8.5pt;
  font-weight: 800;
  padding: 3px 8px;
  text-transform: uppercase;
  margin: 6px 0 4px 0;
  border-left: 4px solid #0284c7;
}

.style2-grid-params {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 5px;
  margin-bottom: 8px;
}

.style2-param-box {
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 3px;
  padding: 4px 6px;
  text-align: center;
}

.style2-param-val {
  font-size: 11pt;
  font-weight: 900;
  color: #0284c7;
}

.style2-param-lbl {
  font-size: 7pt;
  color: #64748b;
  font-weight: 700;
  text-transform: uppercase;
}

.style2-vector-box {
  background-color: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 4px;
  padding: 3px;
  margin-bottom: 6px;
}

.style2-photo-split {
  display: grid;
  grid-template-columns: 85mm 1fr;
  gap: 8px;
  margin-bottom: 6px;
  align-items: center;
}

.style2-photo-img {
  width: 100%;
  height: 48mm;
  object-fit: cover;
  border-radius: 3px;
  border: 1px solid #0f172a;
  display: block;
}

.style2-diag-box {
  background-color: #f8fafc;
  border: 1px solid #cbd5e1;
  border-radius: 3px;
  padding: 6px 8px;
  font-size: 7.5pt;
  line-height: 1.35;
}

.style2-footer {
  position: absolute;
  bottom: 6mm;
  left: 12mm;
  right: 15mm;
  display: flex;
  justify-content: space-between;
  font-size: 7.5pt;
  color: #64748b;
  border-top: 1px solid #cbd5e1;
  padding-top: 4px;
  font-weight: 600;
}
"""

def generate_style_2_html():
    left_html = f"""
    <div class="style2-body style2-page panoramic-left">
      <div class="style2-badge-header">
        <div>
          <span style="font-size:7.5pt; color:#94a3b8; font-weight:700; letter-spacing:1px; text-transform:uppercase;">Système Industriel d'Atelier • Standard Haute Précision</span>
          <div style="font-size:12pt; font-weight:900; color:#ffffff;">POSTE PÉTRISSAGE & PESÉES NUMÉRIQUES</div>
        </div>
        <div class="style2-code-pill">V-PLF-02 • 16 FILMS</div>
      </div>

      <div class="style2-title">Pain au Chocolat / Équerrage 16 Films</div>
      <div class="style2-subline">Pâte Levée Feuilletée Spéciale Découpe Polyline • Tolérances : Poudres ±1 g | Masses ±10 g</div>

      <div class="style2-alert-bar">
        <span><strong>Objectif Rhéologique :</strong> Extensibilité maximale sans snapback</span>
        <span><strong>Cadence Cible :</strong> 160 pièces / pâton 10 000 g</span>
      </div>

      <div class="style2-block-title">1. Tableau Chronologique des Pesées d'Atelier (100% Grammes)</div>
      <table class="style2-table">
        <thead>
          <tr>
            <th>Phase</th>
            <th>Composant Industriel</th>
            <th>% Meun.</th>
            <th>1 Bac (8 000 g)</th>
            <th>10 Bacs (80 kg)</th>
            <th>Spécification de Pesée</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="style2-phase-1">[1] BLEU</span></td>
            <td><strong>Farine Gruau Rouge T45 (Cadillac)</strong></td>
            <td>70,0 %</td>
            <td><strong>3 130 g</strong></td>
            <td>31 300 g</td>
            <td>Verser en 1er dans la cuve spirale.</td>
          </tr>
          <tr>
            <td><span class="style2-phase-1">[1] BLEU</span></td>
            <td><strong>Farine Tradition T65 pure</strong></td>
            <td>30,0 %</td>
            <td><strong>1 340 g</strong></td>
            <td>13 400 g</td>
            <td>Mélange homogène à sec avec Gruau.</td>
          </tr>
          <tr>
            <td><span class="style2-phase-1">[1] BLEU</span></td>
            <td><strong>Eau glacée (+0,5 °C) / Glace écaille</strong></td>
            <td>45,0 %</td>
            <td><strong>2 015 g</strong></td>
            <td>20 150 g</td>
            <td>Thermique de base TB 48 calibrée.</td>
          </tr>
          <tr>
            <td><span class="style2-phase-1">[1] BLEU</span></td>
            <td><strong>Sucre cristal blanc</strong></td>
            <td>8,8 %</td>
            <td><strong>394 g</strong></td>
            <td>3 940 g</td>
            <td>Peser sur les farines.</td>
          </tr>
          <tr>
            <td><span class="style2-phase-1">[1] BLEU</span></td>
            <td><strong>Trimoline (Sucre inverti)</strong></td>
            <td>3,5 %</td>
            <td><strong>157 g</strong></td>
            <td>1 570 g</td>
            <td>Anti-cristallisation froid négatif.</td>
          </tr>
          <tr>
            <td><span class="style2-phase-1">[1] BLEU</span></td>
            <td><strong>Levure fraîche L'Hirondelle Or</strong></td>
            <td>4,2 %</td>
            <td><strong>188 g</strong></td>
            <td>1 880 g</td>
            <td>Émietter en pluie fine (anti-grumeaux).</td>
          </tr>
          <tr>
            <td><span class="style2-phase-1">[1] BLEU</span></td>
            <td><strong>Poudre de lait entier 26 %</strong></td>
            <td>4,0 %</td>
            <td><strong>180 g</strong></td>
            <td>1 800 g</td>
            <td>Rétention d'eau et tendreté de mie.</td>
          </tr>
          <tr>
            <td><span class="style2-phase-1">[1] BLEU</span></td>
            <td><strong>Améliorant S500 Kimo Short</strong></td>
            <td>2,0 %</td>
            <td><strong>90 g</strong></td>
            <td>900 g</td>
            <td>Tolérance stricte ±1 g.</td>
          </tr>
          <tr>
            <td><span class="style2-phase-1">[1] BLEU</span></td>
            <td><strong>Sel fin de cuisine</strong></td>
            <td>2,0 %</td>
            <td><strong>90 g</strong></td>
            <td>900 g</td>
            <td>Force ionique réseau de gluten.</td>
          </tr>
          <tr>
            <td><span class="style2-phase-1">[1] BLEU</span></td>
            <td><strong>Vinaigre d'alcool blanc (8°)</strong></td>
            <td>0,8 %</td>
            <td><strong>36 g</strong></td>
            <td>360 g</td>
            <td>Diluer dans l'eau de coulage.</td>
          </tr>
          <tr>
            <td><span class="style2-phase-2">[2] AMBRE</span></td>
            <td><strong>Margarine Opal cuve (morceaux 500 g)</strong></td>
            <td>8,5 %</td>
            <td><strong>380 g</strong></td>
            <td>3 800 g</td>
            <td>Incorporer dès passage en 2e vitesse.</td>
          </tr>
          <tr class="total-row">
            <td colspan="2">DÉTREMPE NETTE ÉQUILIBRÉE</td>
            <td>178,8 %</td>
            <td>8 000 g pile</td>
            <td>80 000 g pile</td>
            <td>Poids calibré bac Paneo (Base 4 470 g).</td>
          </tr>
          <tr>
            <td><span class="style2-phase-3">[3] VERT</span></td>
            <td><strong>Beurre Tourage Debic 82 % (plaques 2 kg)</strong></td>
            <td>25 % dét.</td>
            <td><strong>2 000 g</strong></td>
            <td>20 000 g</td>
            <td>Assoupli au laminoir à +12 °C / +14 °C.</td>
          </tr>
          <tr class="total-row" style="background-color:#dbeafe;">
            <td colspan="2">PÂTON TOURÉ 16 FILMS TOTAL</td>
            <td>223,8 %</td>
            <td>10 000 g pile</td>
            <td>100 000 g pile</td>
            <td>160 pains au chocolat de 78 g / pâton.</td>
          </tr>
        </tbody>
      </table>

      <div class="style2-block-title">2. Paramètres de Cuve & Diagramme Thermique</div>
      <div class="style2-grid-params">
        <div class="style2-param-box">
          <div class="style2-param-val">5 min</div>
          <div class="style2-param-lbl">Frasage V1</div>
        </div>
        <div class="style2-param-box">
          <div class="style2-param-val">4 min 30</div>
          <div class="style2-param-lbl">Pétrissage V2</div>
        </div>
        <div class="style2-param-box">
          <div class="style2-param-val" style="color:#16a34a;">20–21 °C</div>
          <div class="style2-param-lbl">Sortie Cuve</div>
        </div>
        <div class="style2-param-box">
          <div class="style2-param-val" style="color:#dc2626;">-35 °C</div>
          <div class="style2-param-lbl">Flash 30 min</div>
        </div>
      </div>

      <div class="style2-footer">
        <span>Laboratoire Tourage & Boulangerie • Ligne Industrielle</span>
        <span>Page Gauche • Fiche N°02</span>
      </div>
    </div>
    """

    right_html = f"""
    <div class="style2-body style2-page panoramic-right">
      <div class="style2-badge-header" style="background-color:#0369a1;">
        <div>
          <span style="font-size:7.5pt; color:#bae6fd; font-weight:700; letter-spacing:1px; text-transform:uppercase;">Poste Ligne Automatique & Cuisson</span>
          <div style="font-size:12pt; font-weight:900; color:#ffffff;">CONDUITE POLYLINE, ENROULEMENT & OURAS</div>
        </div>
        <div class="style2-code-pill" style="background-color:#0f172a;">LIGNE 425 mm</div>
      </div>

      <!-- Photo & Alveolage split -->
      <div class="style2-photo-split">
        <img class="style2-photo-img" src="{img_chocolat}" alt="Coupe Pain au Chocolat 16 Films"/>
        <div class="style2-diag-box">
          <strong style="color:#0f172a; font-size:8.5pt;">STANDARD DE COUPE INDUSTRIEL :</strong><br/>
          • Alvéolage nid d'abeille régulier et soutenu.<br/>
          • Barres de chocolat noir 44 % bien écartées et intactes.<br/>
          • Feuilletage droit sans vrillage ni rétractation.<br/>
          • Absence totale de calandrage interne.<br/>
          <span style="color:#16a34a; font-weight:800; display:inline-block; margin-top:3px;">✔ Conforme audit meunier</span>
        </div>
      </div>

      <!-- SVG: Tourage 16 Films & Polyline -->
      <div class="style2-block-title">1. Schéma Mécanique : 2 Tours Doubles & Découpe Rectangles</div>
      <div class="style2-vector-box" style="height:44mm; overflow:hidden;">
        {svg_chocolat_geom}
      </div>

      <!-- SVG: Cuisson & Oura Timeline -->
      <div class="style2-block-title">2. Registre Thermique Four & Décompression Obligatoire</div>
      <div class="style2-vector-box" style="height:40mm; overflow:hidden;">
        {svg_cuisson_oura}
      </div>

      <!-- Flash Troubleshooting -->
      <div style="background-color:#fef2f2; border:1px solid #f87171; border-radius:4px; padding:5px 8px; font-size:7.5pt; margin-top:5px;">
        <strong style="color:#991b1b;">DIAGNOSTIC RAPIDE DÉFAUTS :</strong>
        <span style="color:#450a0a;">
          Déroulage à la pousse = Clé mal calée à plat sous le pâton. | 
          Feuilletage serré = Bande découpée sans temps de relaxation (respecter 60 s anti-snapback sur tapis).
        </span>
      </div>

      <div class="style2-footer">
        <span>Spécification Produit : 85 mm × 140 mm • Poids cru 78 g ± 2 g • Poids cuit 66 g</span>
        <span>Page Droite • Fiche N°02</span>
      </div>
    </div>
    """
    return left_html, right_html

# ==============================================================================
# STYLE 3 : ATELIER CONTEMPORAIN & MATIÈRE BRUTE (KOUIGN-AMANN / CARAMEL CHAUD)
# ==============================================================================
STYLE_3_CSS = """
/* STYLE 3 : ATELIER CONTEMPORAIN SOMBRE & CUIVRE CHAUD */
.style3-body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  color: #262626;
  background-color: #fafaf9;
}

.style3-page {
  background-color: #fafaf9;
  border: 1px solid #e5e5e5;
}

.style3-header {
  border-bottom: 2px solid #ea580c;
  padding-bottom: 6px;
  margin-bottom: 8px;
}

.style3-tag {
  background-color: #ea580c;
  color: #ffffff;
  font-size: 7.5pt;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 2px 7px;
  border-radius: 2px;
  display: inline-block;
}

.style3-title {
  font-size: 16pt;
  font-weight: 900;
  color: #171717;
  text-transform: uppercase;
  letter-spacing: -0.3px;
  margin: 4px 0 2px 0;
}

.style3-sub {
  font-size: 8.5pt;
  color: #737373;
  font-weight: 500;
}

.style3-ratio-box {
  background-color: #fff7ed;
  border: 1px solid #fdba74;
  border-radius: 4px;
  padding: 6px 10px;
  margin-bottom: 8px;
  font-size: 8.2pt;
  color: #9a3412;
}

.style3-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 7.8pt;
  margin-bottom: 8px;
  background-color: #ffffff;
  border: 1px solid #e5e5e5;
}

.style3-table th {
  background-color: #262626;
  color: #ffffff;
  font-weight: 700;
  padding: 4px 6px;
  font-size: 7.2pt;
  text-transform: uppercase;
  border: 1px solid #262626;
}

.style3-table td {
  padding: 3.5px 6px;
  border: 1px solid #e5e5e5;
}

.style3-table tr:nth-child(even) {
  background-color: #f5f5f4;
}

.style3-table tr.total-row {
  background-color: #fed7aa;
  font-weight: 800;
  color: #7c2d12;
}

.style3-section-title {
  font-size: 9pt;
  font-weight: 800;
  color: #c2410c;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  border-bottom: 1px solid #fed7aa;
  padding-bottom: 2px;
  margin: 6px 0 5px 0;
}

.style3-envelope-card {
  background-color: #ffffff;
  border: 1px solid #e5e5e5;
  border-left: 3px solid #ea580c;
  padding: 6px 10px;
  font-size: 7.8pt;
  line-height: 1.35;
  border-radius: 3px;
  margin-bottom: 8px;
}

.style3-photo-frame {
  background-color: #ffffff;
  border: 1px solid #e5e5e5;
  padding: 4px;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  margin-bottom: 7px;
}

.style3-photo-frame img {
  width: 100%;
  height: 50mm;
  object-fit: cover;
  border-radius: 2px;
  display: block;
}

.style3-vector-box {
  background-color: #ffffff;
  border: 1px solid #e5e5e5;
  border-radius: 4px;
  padding: 4px;
  margin-bottom: 7px;
}

.style3-bake-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
  margin-top: 4px;
}

.style3-bake-card {
  background-color: #ffffff;
  border: 1px solid #e5e5e5;
  border-top: 3px solid #ea580c;
  padding: 5px 8px;
  border-radius: 3px;
}

.style3-bake-card h5 {
  font-size: 8pt;
  color: #171717;
  font-weight: 800;
  margin-bottom: 2px;
}

.style3-bake-card p {
  font-size: 7.5pt;
  color: #525252;
  line-height: 1.3;
}

.style3-footer {
  position: absolute;
  bottom: 6mm;
  left: 12mm;
  right: 15mm;
  display: flex;
  justify-content: space-between;
  font-size: 7.5pt;
  color: #a3a3a3;
  border-top: 1px solid #e5e5e5;
  padding-top: 4px;
}
"""

def generate_style_3_html():
    left_html = f"""
    <div class="style3-body style3-page panoramic-left">
      <div class="style3-header">
        <span class="style3-tag">Tradition Bretonne & Cru Surgelé Cryo-Blindé</span>
        <h1 class="style3-title">Kouign-Amann au Ratio d'Or</h1>
        <div class="style3-sub">Code : <code>V-KOU-01</code> (Indiv 100 g) & <code>V-KOU-02</code> (Partage) • Beurre Manié Sucré (Plaques 3 820 g)</div>
      </div>

      <div class="style3-ratio-box">
        <strong>LE RATIO D'OR (PLAQUE 3 820 g ÉTALON) :</strong><br/>
        <strong>2 000 g</strong> Beurre tourage Debic 84 % + <strong>1 800 g</strong> Sucre extra-fin (≤ 200 µm) + <strong>20 g</strong> Fleur de sel = <strong>3 820 g pile</strong>.<br/>
        <em>Amalgame friction V1 en 2 minutes au pétrin. Zéro fuite de sirop au laminoir.</em>
      </div>

      <div class="style3-section-title">1. Tableau des Pesées au Gramme Près (Arrondis Nets)</div>
      <table class="style3-table">
        <thead>
          <tr>
            <th>Phase</th>
            <th>Composant d'Atelier</th>
            <th>% Meun.</th>
            <th>1 Bac (5 000 g dét.)</th>
            <th>5 Bacs (25 000 g)</th>
            <th>Consigne Pesée</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong style="color:#0284c7;">[1] Bleu</strong></td>
            <td><strong>Farine T65 Tradition pure</strong></td>
            <td>100,0 %</td>
            <td><strong>2 750 g</strong></td>
            <td>13 750 g</td>
            <td>W 280-300 force pure.</td>
          </tr>
          <tr>
            <td><strong style="color:#0284c7;">[1] Bleu</strong></td>
            <td><strong>Eau glacée (+0,5 °C) / Glace</strong></td>
            <td>51,6 %</td>
            <td><strong>1 420 g</strong></td>
            <td>7 100 g</td>
            <td>Hydratation bridée cryo.</td>
          </tr>
          <tr>
            <td><strong style="color:#0284c7;">[1] Bleu</strong></td>
            <td><strong>Sucre semoule fin (cuve)</strong></td>
            <td>1,8 %</td>
            <td><strong>50 g</strong></td>
            <td>250 g</td>
            <td>Bridé strict (anti-choc osmotique).</td>
          </tr>
          <tr>
            <td><strong style="color:#0284c7;">[1] Bleu</strong></td>
            <td><strong>Levure fraîche L'Hirondelle Or</strong></td>
            <td>6,0 %</td>
            <td><strong>165 g</strong></td>
            <td>825 g</td>
            <td>Surdosage cryo osmotolérant.</td>
          </tr>
          <tr>
            <td><strong style="color:#0284c7;">[1] Bleu</strong></td>
            <td><strong>Améliorant S500 Kimo Short</strong></td>
            <td>2,5 %</td>
            <td><strong>70 g</strong></td>
            <td>350 g</td>
            <td>Barrière anti-GSH froid négatif.</td>
          </tr>
          <tr>
            <td><strong style="color:#0284c7;">[1] Bleu</strong></td>
            <td><strong>Poudre de lait entier 26 %</strong></td>
            <td>2,5 %</td>
            <td><strong>70 g</strong></td>
            <td>350 g</td>
            <td>Fixateur de moelleux au cœur.</td>
          </tr>
          <tr>
            <td><strong style="color:#0284c7;">[1] Bleu</strong></td>
            <td><strong>Sel fin d'atelier</strong></td>
            <td>1,8 %</td>
            <td><strong>50 g</strong></td>
            <td>250 g</td>
            <td>Ténacité du réseau protéique.</td>
          </tr>
          <tr>
            <td><strong style="color:#0284c7;">[1] Bleu</strong></td>
            <td><strong>Vinaigre blanc d'alcool 8°</strong></td>
            <td>0,5 %</td>
            <td><strong>15 g</strong></td>
            <td>75 g</td>
            <td>Tamponne le pH à 5,1.</td>
          </tr>
          <tr>
            <td><strong style="color:#ea580c;">[2] Ambre</strong></td>
            <td><strong>Margarine Opal cuve (ou beurre)</strong></td>
            <td>14,9 %</td>
            <td><strong>410 g</strong></td>
            <td>2 050 g</td>
            <td>Incorporer au passage en V2.</td>
          </tr>
          <tr class="total-row">
            <td colspan="2">DÉTREMPE CRYO PAR BAC PANEO</td>
            <td>181,8 %</td>
            <td>5 000 g pile</td>
            <td>25 000 g pile</td>
            <td>Pâton détrempe calibré (3 cm).</td>
          </tr>
          <tr>
            <td><strong style="color:#15803d;">[3] Vert</strong></td>
            <td><strong>Bloc Beurre Manié Sucré (Debic+Sucre)</strong></td>
            <td>138,9 %</td>
            <td><strong>3 820 g pile</strong></td>
            <td>19 100 g pile</td>
            <td>Plaque 40 × 30 cm étalonnée.</td>
          </tr>
          <tr class="total-row" style="background-color:#fed7aa;">
            <td colspan="2">PÂTON COMPLET PRÊT AU FAÇONNAGE</td>
            <td>320,7 %</td>
            <td>8 820 g pile</td>
            <td>44 100 g pile</td>
            <td>88 pièces indiv (100 g) / bac.</td>
          </tr>
        </tbody>
      </table>

      <div class="style3-section-title">2. Méthode Express de l'Enveloppe 40 × 30 cm (30 s / plaque)</div>
      <div class="style3-envelope-card">
        <strong>1. Peser 3 820 g pile</strong> de beurre manié issu du pétrin.<br/>
        <strong>2. Placer dans l'enveloppe sulfurisée 40 × 30 cm</strong> : donner 3 coups de rouleau fermes.<br/>
        <strong>3. Épaisseur calibrée 2,5 cm instantanée</strong> : zéro angle vide, zéro débordement, empilage direct sur grilles 60×40 (2 plaques par grille). Nuit à +4 °C.
      </div>

      <div class="style3-footer">
        <span>Laboratoire Tourage & Boulangerie • Gamme Bretagne & Terroir</span>
        <span>Page Gauche • Fiche N°07</span>
      </div>
    </div>
    """

    right_html = f"""
    <div class="style3-body style3-page panoramic-right">
      <div class="style3-header">
        <span class="style3-tag" style="background-color:#171717;">Conduite Machine & Cuisson Caramélisée</span>
        <h2 class="style3-title" style="font-size:14pt;">Tourage 9 Films, Façonnages & Grille Permanente</h2>
        <div class="style3-sub">Cellule Flash -35 °C • Remise en Œuvre Boutique • Four en Capsule Fermée</div>
      </div>

      <!-- Studio photo Kouign Amann -->
      <div class="style3-photo-frame">
        <img src="{img_kouign}" alt="Coupe Kouign-Amann Caramélisé"/>
      </div>

      <!-- SVG Kouign Tourage -->
      <div class="style3-section-title">1. Architecture des 9 Films & Découpe Duale</div>
      <div class="style3-vector-box" style="height:44mm; overflow:hidden;">
        {svg_kouign_tourage}
      </div>

      <!-- Baking specs under permanent grid -->
      <div class="style3-section-title">2. Barème Cuisson Moules Silicone sous Grille Métallique Permanente</div>
      <div class="style3-bake-grid">
        <div class="style3-bake-card">
          <h5>Format Individuel 100 g (Spirale)</h5>
          <p>
            • Moules Ø 80 mm chemisés cassonade.<br/>
            • <strong>1 min à 200 °C</strong> (flash absorption).<br/>
            • <strong>24 min à 175 °C sous grille permanente</strong>.<br/>
            • <strong style="color:#b91c1c;">Oura ouvert à fond à 20 min</strong>.<br/>
            • Durée totale : <strong>25 min chrono</strong>.
          </p>
        </div>
        <div class="style3-bake-card">
          <h5>Format Partage (400 g & 600 g)</h5>
          <p>
            • Moules Ø 20 cm (400 g) / Ø 24 cm (600 g).<br/>
            • <strong>1 min à 200 °C</strong> puis <strong>29 min à 175 °C</strong>.<br/>
            • <strong style="color:#b91c1c;">Oura ouvert à fond à 24 min</strong>.<br/>
            • Durée totale : <strong>30 min chrono</strong>.<br/>
            • Démoulage retournement miroir à tiède (4-6 min).
          </p>
        </div>
      </div>

      <div class="style3-footer">
        <span>Règle d'or : La grille reste posée pendant TOUTE la cuisson pour forcer le caramel miroir.</span>
        <span>Page Droite • Fiche N°07</span>
      </div>
    </div>
    """
    return left_html, right_html

# ==============================================================================
# MASTER COMPILER FUNCTION
# ==============================================================================
def compile_spread_pdf(left_html, right_html, css_custom, output_name, title):
    # 1. Generate A4 Portrait Double-Page PDF (2 sequential facing pages: Left then Right)
    html_a4 = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{title} (Pages A4 Face-à-Face)</title>
<style>
{COMMON_PRINT_CSS}
{css_custom}
</style>
</head>
<body>
  <div class="page page-left">
    {left_html}
  </div>
  <div class="page page-right">
    {right_html}
  </div>
</body>
</html>
"""
    html_a4_path = os.path.join(EXPORTS_DIR, f"{output_name}_A4_double_page.html")
    pdf_a4_path = os.path.join(EXPORTS_DIR, f"{output_name}_A4_double_page.pdf")
    with open(html_a4_path, 'w', encoding='utf-8') as f:
        f.write(html_a4)

    cmd_a4 = [
        'google-chrome',
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        f'--print-to-pdf={pdf_a4_path}',
        html_a4_path
    ]
    subprocess.run(cmd_a4, capture_output=True, text=True)

    # 2. Generate Panoramic A3 Spread PDF (Single A3 landscape page showing both pages side-by-side like an open book)
    html_panoramic = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{title} (Vue Panoramique Livre Ouvert A3)</title>
<style>
{COMMON_PRINT_CSS}
@page {{
  size: A3 landscape;
  margin: 0;
}}
{css_custom}
</style>
</head>
<body style="background-color:#ffffff;">
  <div class="panoramic-spread">
    {left_html}
    {right_html}
  </div>
</body>
</html>
"""
    html_pano_path = os.path.join(EXPORTS_DIR, f"{output_name}_A3_panoramique_livre_ouvert.html")
    pdf_pano_path = os.path.join(EXPORTS_DIR, f"{output_name}_A3_panoramique_livre_ouvert.pdf")
    with open(html_pano_path, 'w', encoding='utf-8') as f:
        f.write(html_panoramic)

    cmd_pano = [
        'google-chrome',
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        f'--print-to-pdf={pdf_pano_path}',
        html_pano_path
    ]
    subprocess.run(cmd_pano, capture_output=True, text=True)

    print(f"[OK] {output_name} :")
    if os.path.exists(pdf_a4_path):
        print(f"  -> A4 Portrait Face-à-Face : {os.path.basename(pdf_a4_path)} ({os.path.getsize(pdf_a4_path):,} octets)")
    if os.path.exists(pdf_pano_path):
        print(f"  -> A3 Panoramique Livre Ouvert : {os.path.basename(pdf_pano_path)} ({os.path.getsize(pdf_pano_path):,} octets)")

def build_master_cahier(l1, r1, l2, r2, l3, r3):
    cover_html = """
    <div class="page" style="background-color:#0f172a; color:#ffffff; display:flex; flex-direction:column; justify-content:space-between; padding:25mm 20mm; text-align:center;">
      <div style="border-bottom:2px solid #b45309; padding-bottom:12px;">
        <div style="font-family:'Cinzel', serif; font-size:12pt; letter-spacing:4px; text-transform:uppercase; color:#f59e0b; margin-bottom:6px;">Manufacture & Haute Meunerie</div>
        <div style="font-size:9pt; color:#94a3b8; letter-spacing:2px; text-transform:uppercase;">Unité de Recherche & Production de Tourage</div>
      </div>

      <div style="margin: 30mm 0;">
        <div style="font-family:'Cinzel', serif; font-size:10pt; letter-spacing:3px; color:#38bdf8; text-transform:uppercase; margin-bottom:10px;">Référentiel Technique Officiel</div>
        <h1 style="font-family:'Cinzel', serif; font-size:26pt; font-weight:900; letter-spacing:1px; line-height:1.2; color:#ffffff; margin-bottom:15px; text-transform:uppercase;">
          GRAND CAHIER DE RECETTES D'ATELIER
        </h1>
        <div style="width:80px; height:3px; background-color:#b45309; margin:0 auto 15px auto;"></div>
        <p style="font-size:11pt; color:#cbd5e1; max-width:140mm; margin:0 auto; line-height:1.5;">
          Architecture Documentaire à Double Page • Formulations Meunières 100 % en Grammes • Guides Visuels Vectoriels & Standards Photographiques d'Excellence
        </p>
      </div>

      <div style="background-color:#1e293b; border:1px solid #334155; border-radius:6px; padding:12px 20px; text-align:left; font-size:8.5pt; color:#94a3b8; line-height:1.6;">
        <strong style="color:#ffffff; font-size:9pt; display:block; margin-bottom:4px; text-transform:uppercase; letter-spacing:1px;">Sommaire des Maquettes Présentées en Double Page :</strong>
        • <strong>Double Page 01 (Style A • Prestige Grand Livre) :</strong> Croissant Pur Beurre PAC (Architecture 12 Films)<br/>
        • <strong>Double Page 02 (Style B • Précision Industrielle Suisse) :</strong> Pain au Chocolat (Équerrage 16 Films & Polyline)<br/>
        • <strong>Double Page 03 (Style C • Atelier Contemporain & Cuivre) :</strong> Kouign-Amann Traditionnel (Beurre Manié au Ratio d'Or)
      </div>

      <div style="font-size:8pt; color:#64748b; border-top:1px solid #334155; padding-top:10px;">
        Laboratoire Tourage & Boulangerie • Édition 2026 • Reliure d'Atelier A4 & Plastification 125 µm
      </div>
    </div>
    """

    master_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Grand Cahier de Recettes d'Atelier - Édition Double Page</title>
<style>
{COMMON_PRINT_CSS}
{STYLE_1_CSS}
{STYLE_2_CSS}
{STYLE_3_CSS}
</style>
</head>
<body>
  <!-- Cover Page -->
  {cover_html}

  <!-- Spread 1 (Style 1) -->
  <div class="page page-left">{l1}</div>
  <div class="page page-right">{r1}</div>

  <!-- Spread 2 (Style 2) -->
  <div class="page page-left">{l2}</div>
  <div class="page page-right">{r2}</div>

  <!-- Spread 3 (Style 3) -->
  <div class="page page-left">{l3}</div>
  <div class="page page-right">{r3}</div>
</body>
</html>
"""
    master_html_path = os.path.join(EXPORTS_DIR, "Grand_Cahier_Recettes_Atelier_Prestige_Master.html")
    master_pdf_path = os.path.join(EXPORTS_DIR, "Grand_Cahier_Recettes_Atelier_Prestige_Master.pdf")
    with open(master_html_path, 'w', encoding='utf-8') as f:
        f.write(master_html)

    cmd_master = [
        'google-chrome',
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        f'--print-to-pdf={master_pdf_path}',
        master_html_path
    ]
    subprocess.run(cmd_master, capture_output=True, text=True)
    if os.path.exists(master_pdf_path):
        print(f"[OK MASTER] Cahier Complet Généré : {os.path.basename(master_pdf_path)} ({os.path.getsize(master_pdf_path):,} octets)")

def build_all():
    print("=== GÉNÉRATION DES MAQUETTES DE STYLE DOUBLE-PAGE A4 ===")

    # 1. Style 1 : Grand Livre d'Art Culinaire
    l1, r1 = generate_style_1_html()
    compile_spread_pdf(l1, r1, STYLE_1_CSS, "Maquette_Style_1_Prestige_Grand_Livre_Croissant", "Maquette Style 1 - Édition Grand Livre d'Art (Croissant Pur Beurre PAC)")

    # 2. Style 2 : Laboratoire Industriel & Signalétique Suisse
    l2, r2 = generate_style_2_html()
    compile_spread_pdf(l2, r2, STYLE_2_CSS, "Maquette_Style_2_Industriel_Suisse_Pain_Chocolat", "Maquette Style 2 - Laboratoire Industriel Suisse (Pain au Chocolat 16 Films)")

    # 3. Style 3 : Atelier Contemporain & Matière Brute
    l3, r3 = generate_style_3_html()
    compile_spread_pdf(l3, r3, STYLE_3_CSS, "Maquette_Style_3_Contemporain_Cuivre_Kouign_Amann", "Maquette Style 3 - Atelier Contemporain (Kouign-Amann au Ratio d'Or)")

    # 4. Master Book Compilation (Grand Cahier Complet réunissant les 3 styles avec Couverture de Prestige)
    build_master_cahier(l1, r1, l2, r2, l3, r3)

if __name__ == '__main__':
    build_all()
