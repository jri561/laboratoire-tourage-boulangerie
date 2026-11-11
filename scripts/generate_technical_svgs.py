import os

def create_svg_tourage_12_films(filepath):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 260" width="100%" height="100%" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <linearGradient id="gradPate" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#fef3c7"/>
      <stop offset="100%" stop-color="#fde68a"/>
    </linearGradient>
    <linearGradient id="gradBeurre" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="960" height="260" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>

  <!-- Step 1: Enchâssement -->
  <g transform="translate(20, 20)">
    <rect width="165" height="220" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="165" height="28" rx="6" fill="#0f172a"/>
    <text x="82" y="19" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">1. ENCHÂSSEMENT</text>
    
    <!-- Détrempe + Beurre centré -->
    <rect x="18" y="55" width="129" height="60" rx="4" fill="url(#gradPate)" stroke="#d97706" stroke-width="1.5"/>
    <rect x="43" y="65" width="79" height="40" rx="2" fill="url(#gradBeurre)" stroke="#b45309" stroke-width="1"/>
    <text x="82" y="89" fill="#78350f" font-size="10" font-weight="700" text-anchor="middle">BEURRE 2 000 g</text>
    
    <!-- Arrows folding -->
    <path d="M 22 50 Q 50 35 70 58" fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="3,2"/>
    <polygon points="70,58 64,52 69,50" fill="#2563eb"/>
    <path d="M 143 50 Q 115 35 95 58" fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="3,2"/>
    <polygon points="95,58 96,50 101,52" fill="#2563eb"/>

    <text x="82" y="145" fill="#334155" font-size="10" font-weight="600" text-anchor="middle">Enveloppe à plat</text>
    <text x="82" y="160" fill="#64748b" font-size="9" text-anchor="middle">Bord à bord (sans chevauchement)</text>
    
    <rect x="25" y="180" width="115" height="26" rx="4" fill="#eff6ff" stroke="#93c5fd" stroke-width="1"/>
    <text x="82" y="197" fill="#1e40af" font-size="10" font-weight="700" text-anchor="middle">1 FILM DE BEURRE</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <g transform="translate(192, 120)">
    <path d="M 0 0 L 15 0" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>
    <polygon points="15,-4 22,0 15,4" fill="#94a3b8"/>
  </g>

  <!-- Step 2: 1er Tour Double -->
  <g transform="translate(220, 20)">
    <rect width="185" height="220" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="185" height="28" rx="6" fill="#0369a1"/>
    <text x="92" y="19" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">2. TOUR DOUBLE (4 PLIS)</text>

    <!-- Laminoir allongé -->
    <text x="92" y="48" fill="#0284c7" font-size="9" font-weight="700" text-anchor="middle">Allonger à 85 – 90 cm (ép. 8 mm)</text>
    
    <!-- Schéma pliage portefeuille -->
    <g transform="translate(18, 62)">
      <!-- Base layer -->
      <path d="M 5 35 L 45 35 L 45 15 L 75 15" fill="none" stroke="#d97706" stroke-width="4" stroke-linecap="round"/>
      <path d="M 145 35 L 105 35 L 105 15 L 75 15" fill="none" stroke="#d97706" stroke-width="4" stroke-linecap="round"/>
      <!-- Inner butter line representation -->
      <line x1="8" y1="31" x2="42" y2="31" stroke="#f59e0b" stroke-width="2"/>
      <line x1="142" y1="31" x2="108" y2="31" stroke="#f59e0b" stroke-width="2"/>
      <!-- Center fold indicator -->
      <circle cx="75" cy="15" r="3" fill="#dc2626"/>
      <text x="75" y="8" fill="#dc2626" font-size="8" font-weight="700" text-anchor="middle">Pliage asymétrique</text>
    </g>

    <!-- Folded layers graphic -->
    <g transform="translate(30, 115)">
      <rect x="0" y="0" width="125" height="24" rx="3" fill="url(#gradPate)" stroke="#b45309" stroke-width="1"/>
      <line x1="4" y1="6" x2="121" y2="6" stroke="#d97706" stroke-width="1.8"/>
      <line x1="4" y1="12" x2="121" y2="12" stroke="#d97706" stroke-width="1.8"/>
      <line x1="4" y1="18" x2="121" y2="18" stroke="#d97706" stroke-width="1.8"/>
    </g>

    <text x="92" y="160" fill="#334155" font-size="10" font-weight="600" text-anchor="middle">Portefeuille (pli 1/3 + 2/3)</text>
    
    <rect x="25" y="180" width="135" height="26" rx="4" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="1"/>
    <text x="92" y="197" fill="#0369a1" font-size="10" font-weight="700" text-anchor="middle">4 FILMS DE BEURRE</text>
  </g>

  <!-- Arrow 2 -> Repos -->
  <g transform="translate(412, 120)">
    <polygon points="10,-4 17,0 10,4" fill="#94a3b8"/>
  </g>

  <!-- Step 3: Détente Froid -->
  <g transform="translate(435, 20)">
    <rect width="115" height="220" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="115" height="28" rx="6" fill="#475569"/>
    <text x="57" y="19" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">3. DÉTENTE</text>

    <!-- Thermometer / Clock Icon -->
    <circle cx="57" cy="75" r="24" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2"/>
    <path d="M 57 60 L 57 75 L 67 75" fill="none" stroke="#0284c7" stroke-width="2.5" stroke-linecap="round"/>
    
    <text x="57" y="125" fill="#0f172a" font-size="13" font-weight="800" text-anchor="middle">15 – 20 min</text>
    <text x="57" y="143" fill="#2563eb" font-size="11" font-weight="700" text-anchor="middle">+2 °C / +4 °C</text>
    <text x="57" y="162" fill="#64748b" font-size="9" text-anchor="middle">Sous plastique étanche</text>
    
    <rect x="12" y="180" width="91" height="26" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
    <text x="57" y="197" fill="#475569" font-size="9.5" font-weight="700" text-anchor="middle">Relaxation gluten</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <g transform="translate(557, 120)">
    <polygon points="10,-4 17,0 10,4" fill="#94a3b8"/>
  </g>

  <!-- Step 4: 2e Tour Simple -->
  <g transform="translate(580, 20)">
    <rect width="185" height="220" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="185" height="28" rx="6" fill="#0284c7"/>
    <text x="92" y="19" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">4. TOUR SIMPLE (3 PLIS)</text>

    <text x="92" y="48" fill="#0284c7" font-size="9" font-weight="700" text-anchor="middle">Pivot 90° • Allonger à 65 cm</text>

    <!-- Schéma pliage simple 3 plis -->
    <g transform="translate(25, 62)">
      <path d="M 5 35 L 90 35 L 90 22 L 45 22 L 45 9 L 135 9" fill="none" stroke="#d97706" stroke-width="4" stroke-linecap="round"/>
      <line x1="8" y1="31" x2="87" y2="31" stroke="#f59e0b" stroke-width="2"/>
      <line x1="87" y1="18" x2="48" y2="18" stroke="#f59e0b" stroke-width="2"/>
      <line x1="48" y1="5" x2="132" y2="5" stroke="#f59e0b" stroke-width="2"/>
    </g>

    <g transform="translate(30, 115)">
      <rect x="0" y="0" width="125" height="24" rx="3" fill="url(#gradPate)" stroke="#b45309" stroke-width="1"/>
      <!-- Multi layers -->
      <line x1="4" y1="3" x2="121" y2="3" stroke="#d97706" stroke-width="1"/>
      <line x1="4" y1="6" x2="121" y2="6" stroke="#d97706" stroke-width="1"/>
      <line x1="4" y1="9" x2="121" y2="9" stroke="#d97706" stroke-width="1"/>
      <line x1="4" y1="12" x2="121" y2="12" stroke="#d97706" stroke-width="1"/>
      <line x1="4" y1="15" x2="121" y2="15" stroke="#d97706" stroke-width="1"/>
      <line x1="4" y1="18" x2="121" y2="18" stroke="#d97706" stroke-width="1"/>
      <line x1="4" y1="21" x2="121" y2="21" stroke="#d97706" stroke-width="1"/>
    </g>

    <text x="92" y="160" fill="#334155" font-size="10" font-weight="600" text-anchor="middle">Pliage en 3 (4 films × 3 = 12)</text>
    
    <rect x="25" y="180" width="135" height="26" rx="4" fill="#fef3c7" stroke="#f59e0b" stroke-width="1"/>
    <text x="92" y="197" fill="#b45309" font-size="10" font-weight="800" text-anchor="middle">12 FILMS DE BEURRE</text>
  </g>

  <!-- Arrow 4 -> 5 -->
  <g transform="translate(772, 120)">
    <polygon points="10,-4 17,0 10,4" fill="#94a3b8"/>
  </g>

  <!-- Step 5: Drossage & Repos Final -->
  <g transform="translate(795, 20)">
    <rect width="145" height="220" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="145" height="28" rx="6" fill="#16a34a"/>
    <text x="72" y="19" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">5. DROSSAGE & DÉTENTE</text>

    <!-- Knife cut illustration -->
    <g transform="translate(25, 48)">
      <rect x="10" y="10" width="75" height="50" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
      <!-- Cut lines on borders -->
      <line x1="10" y1="10" x2="10" y2="60" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="3,2"/>
      <line x1="85" y1="10" x2="85" y2="60" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="3,2"/>
      <line x1="10" y1="10" x2="85" y2="10" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="3,2"/>
      <line x1="10" y1="60" x2="85" y2="60" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="3,2"/>
    </g>

    <text x="72" y="125" fill="#dc2626" font-size="10" font-weight="700" text-anchor="middle">Rogner les 4 chants</text>
    <text x="72" y="140" fill="#64748b" font-size="9" text-anchor="middle">Coupe 5 mm (libère tension)</text>
    <text x="72" y="160" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">Détente : 45 min</text>
    
    <rect x="12" y="180" width="121" height="26" rx="4" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
    <text x="72" y="197" fill="#15803d" font-size="10" font-weight="800" text-anchor="middle">PRÊT AU FAÇONNAGE</text>
  </g>
</svg>
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"[OK] Généré : {filepath}")


def create_svg_faconnage_croissant(filepath):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 260" width="100%" height="100%" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <!-- Background -->
  <rect width="960" height="260" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>

  <!-- Panel 1: Laminage & Découpe de la bande -->
  <g transform="translate(20, 20)">
    <rect width="445" height="220" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="445" height="28" rx="6" fill="#0f172a"/>
    <text x="222" y="19" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">ABAISSE & GÉOMÉTRIE DES TRIANGLES (CROISSOMAT SCM50)</text>

    <!-- Calibres bande -->
    <g transform="translate(20, 45)">
      <!-- Fond bande de pâte -->
      <rect x="30" y="20" width="350" height="90" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
      
      <!-- Triangles découpe -->
      <polygon points="30,110 80,20 130,110" fill="#fde68a" stroke="#b45309" stroke-width="1.5"/>
      <polygon points="130,110 180,20 230,110" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
      <polygon points="230,110 280,20 330,110" fill="#fde68a" stroke="#b45309" stroke-width="1.5"/>
      
      <!-- Lignes de coupe inverses (chutes nulles) -->
      <line x1="80" y1="20" x2="130" y2="110" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="2,2"/>
      <line x1="180" y1="20" x2="230" y2="110" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="2,2"/>
      <line x1="280" y1="20" x2="330" y2="110" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="2,2"/>

      <!-- Cotations Largeur bande -->
      <line x1="15" y1="20" x2="15" y2="110" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="10" y1="20" x2="20" y2="20" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="10" y1="110" x2="20" y2="110" stroke="#0284c7" stroke-width="1.5"/>
      <text x="8" y="70" fill="#0284c7" font-size="9" font-weight="700" text-anchor="end" transform="rotate(-90 8 70)">400 mm</text>

      <!-- Cotations Base triangle -->
      <line x1="30" y1="120" x2="130" y2="120" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="30" y1="115" x2="30" y2="125" stroke="#0284c7" stroke-width="1.5"/>
      <line x1="130" y1="115" x2="130" y2="125" stroke="#0284c7" stroke-width="1.5"/>
      <text x="80" y="133" fill="#0284c7" font-size="9" font-weight="700" text-anchor="middle">Base : 100 mm</text>

      <!-- Cotation Hauteur -->
      <line x1="80" y1="20" x2="80" y2="110" stroke="#475569" stroke-width="1" stroke-dasharray="2,2"/>
      <text x="85" y="65" fill="#475569" font-size="8.5" font-weight="600">H : 250 mm</text>

      <!-- Poids / Epaisseur Badge -->
      <rect x="235" y="30" width="135" height="36" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="1.2"/>
      <text x="302" y="45" fill="#0f172a" font-size="9.5" font-weight="800" text-anchor="middle">ÉPAISSEUR : 3,5 mm</text>
      <text x="302" y="58" fill="#0284c7" font-size="9" font-weight="700" text-anchor="middle">Poids cru : 77 g ± 2 g</text>
    </g>

    <!-- Repère Farinage inversé -->
    <rect x="20" y="180" width="405" height="26" rx="4" fill="#fef2f2" stroke="#f87171" stroke-width="1"/>
    <text x="222" y="197" fill="#b91c1c" font-size="9.5" font-weight="700" text-anchor="middle">⚠️ FARINAGE INVERSÉ STRICT : Face farinée contre le tapis • Face vierge dessus</text>
  </g>

  <!-- Panel 2: Enroulement, Réglages SCM50 & Calage Clé -->
  <g transform="translate(485, 20)">
    <rect width="455" height="220" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="455" height="28" rx="6" fill="#0369a1"/>
    <text x="227" y="19" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">ENROULEMENT SOUPLE & CALAGE DE LA CLÉ À 6 HEURES</text>

    <!-- SCM50 Manettes Settings -->
    <g transform="translate(20, 42)">
      <!-- Knob 1 -->
      <rect x="0" y="0" width="125" height="52" rx="4" fill="#ffffff" stroke="#93c5fd" stroke-width="1"/>
      <text x="62" y="14" fill="#1e40af" font-size="8.5" font-weight="700" text-anchor="middle">ENTRÉE AMONT (DROITE)</text>
      <text x="62" y="32" fill="#0284c7" font-size="13" font-weight="900" text-anchor="middle">2,2 à 2,5</text>
      <text x="62" y="45" fill="#64748b" font-size="7.5" text-anchor="middle">Amorce sans écraser</text>

      <!-- Knob 2 -->
      <rect x="140" y="0" width="125" height="52" rx="4" fill="#ffffff" stroke="#86efac" stroke-width="1"/>
      <text x="202" y="14" fill="#15803d" font-size="8.5" font-weight="700" text-anchor="middle">SORTIE AVAL (GAUCHE)</text>
      <text x="202" y="32" fill="#16a34a" font-size="13" font-weight="900" text-anchor="middle">3,0 à 3,2</text>
      <text x="202" y="45" fill="#64748b" font-size="7.5" text-anchor="middle">Dégage rouleau 30 mm</text>

      <!-- Knob 3 -->
      <rect x="280" y="0" width="125" height="52" rx="4" fill="#ffffff" stroke="#fcd34d" stroke-width="1"/>
      <text x="342" y="14" fill="#b45309" font-size="8.5" font-weight="700" text-anchor="middle">CAMBRURE (INFÉRIEURE)</text>
      <text x="342" y="32" fill="#d97706" font-size="13" font-weight="900" text-anchor="middle">7,5 à 8,0</text>
      <text x="342" y="45" fill="#64748b" font-size="7.5" text-anchor="middle">3,5 spires souples</text>
    </g>

    <!-- Croissant Roll & Spire diagram -->
    <g transform="translate(30, 106)">
      <!-- Cross section croissant rolled -->
      <ellipse cx="65" cy="38" rx="45" ry="28" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
      <ellipse cx="65" cy="38" rx="30" ry="18" fill="none" stroke="#b45309" stroke-width="1.8"/>
      <ellipse cx="65" cy="38" rx="15" ry="9" fill="none" stroke="#b45309" stroke-width="1.8"/>
      <!-- Small hole center -->
      <ellipse cx="65" cy="38" rx="6" ry="3.5" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
      
      <!-- Callout "Petit jour visible" -->
      <text x="65" y="10" fill="#0284c7" font-size="8.5" font-weight="700" text-anchor="middle">PETIT JOUR AU CŒUR</text>
      <line x1="65" y1="13" x2="65" y2="33" stroke="#0284c7" stroke-width="1.2" stroke-dasharray="2,2"/>

      <!-- Clé à 6 heures -->
      <path d="M 65 66 L 65 78" stroke="#dc2626" stroke-width="2" marker-end="url(#arrow)"/>
      <polygon points="65,78 61,72 69,72" fill="#dc2626"/>
      <text x="65" y="88" fill="#dc2626" font-size="9" font-weight="800" text-anchor="middle">CLÉ À 6 HEURES EN DESSOUS</text>

      <!-- Text explanation -->
      <g transform="translate(145, 12)">
        <text x="0" y="12" fill="#0f172a" font-size="10" font-weight="700">• 3,5 à 4 spires régulières</text>
        <text x="0" y="27" fill="#334155" font-size="9">• Ne jamais serrer le roulage : la pâte doit respirer.</text>
        <text x="0" y="42" fill="#334155" font-size="9">• Couchage sur plaque 600×400 : 15 pcs (3 rangées de 5).</text>
        <text x="0" y="57" fill="#15803d" font-size="9" font-weight="700">• La clé bloquée sous le croissant évite le déroulage à la pousse.</text>
      </g>
    </g>
  </g>
</svg>
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"[OK] Généré : {filepath}")


def create_svg_pain_chocolat_geometrie(filepath):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 260" width="100%" height="100%" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="960" height="260" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>

  <!-- Left: Tourage 16 Films & Coupe Polyline -->
  <g transform="translate(20, 20)">
    <rect width="445" height="220" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="445" height="28" rx="6" fill="#0f172a"/>
    <text x="222" y="19" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">TOURAGE 16 FILMS (2 DOUBLES) & DÉCOUPE POLYLINE</text>

    <!-- Schéma 2 Tours Doubles -->
    <g transform="translate(25, 45)">
      <rect x="0" y="0" width="180" height="60" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="1.2"/>
      <text x="90" y="18" fill="#0369a1" font-size="9.5" font-weight="700" text-anchor="middle">1ER DOUBLE (4 FILMS)</text>
      <text x="90" y="34" fill="#64748b" font-size="8.5" text-anchor="middle">Allongement 90 cm • Portefeuille</text>
      <text x="90" y="48" fill="#0284c7" font-size="9" font-weight="700" text-anchor="middle">Détente 15 min à +2 °C</text>

      <path d="M 188 30 L 208 30" stroke="#94a3b8" stroke-width="2"/>
      <polygon points="208,26 216,30 208,34" fill="#94a3b8"/>

      <rect x="222" y="0" width="180" height="60" rx="4" fill="#ffffff" stroke="#16a34a" stroke-width="1.2"/>
      <text x="312" y="18" fill="#15803d" font-size="9.5" font-weight="700" text-anchor="middle">2E DOUBLE (16 FILMS)</text>
      <text x="312" y="34" fill="#64748b" font-size="8.5" text-anchor="middle">Pivot 90° • Allongement 90 cm</text>
      <text x="312" y="48" fill="#15803d" font-size="9" font-weight="800" text-anchor="middle">16 FILMS RÉGULIERS</text>
    </g>

    <!-- Cotes rectangle -->
    <g transform="translate(25, 120)">
      <rect x="20" y="10" width="140" height="80" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
      <text x="90" y="45" fill="#78350f" font-size="11" font-weight="800" text-anchor="middle">85 mm × 140 mm</text>
      <text x="90" y="60" fill="#b45309" font-size="9" font-weight="600" text-anchor="middle">Poids cru : 78 g ± 2 g</text>
      
      <!-- Cotations -->
      <text x="90" y="6" fill="#0284c7" font-size="8.5" font-weight="700" text-anchor="middle">Largeur : 85 mm</text>
      <text x="175" y="55" fill="#0284c7" font-size="8.5" font-weight="700" text-anchor="start">Longueur 140 mm</text>

      <g transform="translate(200, 15)">
        <text x="0" y="12" fill="#0f172a" font-size="10" font-weight="700">Calibrage Ligne Polyline :</text>
        <text x="0" y="27" fill="#334155" font-size="9">• Épaisseur finale bande : 3,8 mm</text>
        <text x="0" y="42" fill="#334155" font-size="9">• Largeur bande : 425 mm (5 rangées de 85 mm)</text>
        <text x="0" y="57" fill="#dc2626" font-size="9" font-weight="700">• Équerrage parfait = zéro chute d'angle</text>
      </g>
    </g>
  </g>

  <!-- Right: Pliage avec 2 barres de chocolat & Clé -->
  <g transform="translate(485, 20)">
    <rect width="455" height="220" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="455" height="28" rx="6" fill="#0369a1"/>
    <text x="227" y="19" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">DISPOSITION DES 2 BÂTONS DE CHOCOLAT & CLÉ</text>

    <!-- Step by step folding of Pain Chocolat -->
    <g transform="translate(20, 45)">
      <!-- Unfolded strip with 2 bars -->
      <g transform="translate(0, 0)">
        <rect x="0" y="10" width="190" height="45" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
        <!-- Bar 1 -->
        <rect x="25" y="14" width="8" height="37" rx="1.5" fill="#3b0764" stroke="#1e1b4b" stroke-width="1"/>
        <text x="29" y="8" fill="#3b0764" font-size="7.5" font-weight="700" text-anchor="middle">Barre 1</text>
        <!-- Bar 2 -->
        <rect x="100" y="14" width="8" height="37" rx="1.5" fill="#3b0764" stroke="#1e1b4b" stroke-width="1"/>
        <text x="104" y="8" fill="#3b0764" font-size="7.5" font-weight="700" text-anchor="middle">Barre 2</text>
        <!-- Arrow fold 1 -->
        <path d="M 5 32 Q 25 15 45 32" fill="none" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="2,2"/>
        <!-- Arrow fold 2 -->
        <path d="M 185 32 Q 130 5 80 32" fill="none" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="2,2"/>
      </g>

      <!-- Finished folded cross section -->
      <g transform="translate(240, 5)">
        <rect x="10" y="5" width="165" height="65" rx="8" fill="#fde68a" stroke="#b45309" stroke-width="2"/>
        <!-- 2 chocolate sticks inside -->
        <rect x="35" y="24" width="22" height="22" rx="3" fill="#3b0764" stroke="#000000" stroke-width="1.5"/>
        <text x="46" y="38" fill="#ffffff" font-size="8" font-weight="800" text-anchor="middle">CHOC</text>
        <rect x="115" y="24" width="22" height="22" rx="3" fill="#3b0764" stroke="#000000" stroke-width="1.5"/>
        <text x="126" y="38" fill="#ffffff" font-size="8" font-weight="800" text-anchor="middle">CHOC</text>

        <!-- Arrow Clé dessous -->
        <path d="M 86 73 L 86 85" stroke="#dc2626" stroke-width="2"/>
        <polygon points="86,85 82,79 90,79" fill="#dc2626"/>
        <text x="86" y="96" fill="#dc2626" font-size="8.5" font-weight="800" text-anchor="middle">CLÉ BIEN À PLAT DESSOUS</text>
      </g>

      <!-- Specifications callouts -->
      <g transform="translate(10, 110)">
        <rect x="0" y="0" width="405" height="50" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
        <text x="15" y="16" fill="#0f172a" font-size="9" font-weight="700">• Bâtons de chocolat 44 % :</text>
        <text x="160" y="16" fill="#334155" font-size="9">Longueur 80 mm • 5,5 g pièce (11 g total par pièce).</text>
        <text x="15" y="31" fill="#0f172a" font-size="9" font-weight="700">• Règle de soudure :</text>
        <text x="160" y="31" fill="#334155" font-size="9">Ne pas trop étirer le rabat final ; presser légèrement à plat.</text>
        <text x="15" y="44" fill="#15803d" font-size="9" font-weight="700">• Disposition plaque 600×400 :</text>
        <text x="160" y="44" fill="#15803d" font-size="9">16 pièces (4 rangées de 4) en quinconce.</text>
      </g>
    </g>
  </g>
</svg>
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"[OK] Généré : {filepath}")


def create_svg_bareme_cuisson_oura(filepath):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 220" width="100%" height="100%" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="960" height="220" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>

  <!-- Header -->
  <rect x="0" y="0" width="960" height="28" rx="6" fill="#0f172a"/>
  <text x="480" y="19" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">CHRONOLOGIE THERMIQUE D'ATELIER & DÉVERROUILLAGE D'OURA</text>

  <!-- Timeline graph -->
  <g transform="translate(60, 45)">
    <!-- Axes -->
    <line x1="50" y1="120" x2="800" y2="120" stroke="#94a3b8" stroke-width="2"/>
    <line x1="50" y1="10" x2="50" y2="120" stroke="#94a3b8" stroke-width="2"/>

    <!-- Y labels (Temperatures) -->
    <text x="40" y="123" fill="#64748b" font-size="9" text-anchor="end">0 °C</text>
    <text x="40" y="70" fill="#64748b" font-size="9" text-anchor="end">100 °C</text>
    <text x="40" y="25" fill="#0284c7" font-size="9.5" font-weight="700" text-anchor="end">175 °C</text>

    <!-- Temperature curve -->
    <path d="M 50 25 L 120 40 L 150 25 L 630 25 L 750 35 L 800 120" fill="none" stroke="#ea580c" stroke-width="3"/>
    
    <!-- Phase 1: Enfournement + Buée -->
    <circle cx="120" cy="40" r="4" fill="#0284c7"/>
    <text x="120" y="15" fill="#0284c7" font-size="8.5" font-weight="700" text-anchor="middle">Enfournement</text>
    <rect x="90" y="52" width="70" height="22" rx="3" fill="#eff6ff" stroke="#93c5fd" stroke-width="1"/>
    <text x="125" y="66" fill="#1d4ed8" font-size="8.5" font-weight="700" text-anchor="middle">BUÉE : 3 s</text>
    <line x1="120" y1="44" x2="120" y2="52" stroke="#0284c7" stroke-width="1"/>

    <!-- Phase 2: Ovenspring & Développement -->
    <rect x="230" y="50" width="180" height="34" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <text x="320" y="64" fill="#0f172a" font-size="8.5" font-weight="700" text-anchor="middle">OVENSPRING & EXPANSION GAZ</text>
    <text x="320" y="77" fill="#64748b" font-size="7.5" text-anchor="middle">Four fermé hermétique • Ébullition beurre</text>

    <!-- Phase 3: OUVERTURE OURA (CRITIQUE) -->
    <line x1="630" y1="15" x2="630" y2="120" stroke="#dc2626" stroke-width="2" stroke-dasharray="3,2"/>
    <circle cx="630" cy="25" r="5" fill="#dc2626"/>
    
    <rect x="550" y="45" width="160" height="42" rx="4" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
    <text x="630" y="59" fill="#991b1b" font-size="9" font-weight="800" text-anchor="middle">OUVERTURE D'OURA : 14 min</text>
    <text x="630" y="71" fill="#b91c1c" font-size="8" font-weight="600" text-anchor="middle">Évacuation de l'humidité</text>
    <text x="630" y="82" fill="#7f1d1d" font-size="7.5" text-anchor="middle">Indispensable pour croustillance durable</text>

    <!-- Phase 4: Sortie & Ressuage -->
    <circle cx="750" cy="35" r="4" fill="#16a34a"/>
    <rect x="715" y="52" width="75" height="32" rx="3" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
    <text x="752" y="65" fill="#15803d" font-size="8.5" font-weight="700" text-anchor="middle">SORTIE FOUR</text>
    <text x="752" y="78" fill="#166534" font-size="8" font-weight="700" text-anchor="middle">17 min pile</text>

    <!-- Timeline X marks -->
    <line x1="50" y1="120" x2="50" y2="125" stroke="#94a3b8" stroke-width="1"/>
    <text x="50" y="137" fill="#64748b" font-size="8.5" text-anchor="middle">0 min</text>

    <line x1="200" y1="120" x2="200" y2="125" stroke="#94a3b8" stroke-width="1"/>
    <text x="200" y="137" fill="#64748b" font-size="8.5" text-anchor="middle">5 min</text>

    <line x1="420" y1="120" x2="420" y2="125" stroke="#94a3b8" stroke-width="1"/>
    <text x="420" y="137" fill="#64748b" font-size="8.5" text-anchor="middle">10 min</text>

    <line x1="630" y1="120" x2="630" y2="125" stroke="#dc2626" stroke-width="1.5"/>
    <text x="630" y="137" fill="#dc2626" font-size="9" font-weight="800" text-anchor="middle">14 min (Oura)</text>

    <line x1="750" y1="120" x2="750" y2="125" stroke="#16a34a" stroke-width="1.5"/>
    <text x="750" y="137" fill="#15803d" font-size="9" font-weight="800" text-anchor="middle">17 min (Fin)</text>
  </g>
</svg>
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"[OK] Généré : {filepath}")

if __name__ == '__main__':
    base_dir = '/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie/docs/vectors'
    create_svg_tourage_12_films(os.path.join(base_dir, 'tourage_12_films_schema.svg'))
    create_svg_faconnage_croissant(os.path.join(base_dir, 'faconnage_croissant_geometrie.svg'))
    create_svg_pain_chocolat_geometrie(os.path.join(base_dir, 'faconnage_pain_chocolat_geometrie.svg'))
    create_svg_bareme_cuisson_oura(os.path.join(base_dir, 'bareme_cuisson_oura.svg'))

def create_svg_kouign_amann_tourage(filepath):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 260" width="100%" height="100%" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="960" height="260" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>

  <!-- Left: Beurre Manié au Ratio d'Or -->
  <g transform="translate(20, 20)">
    <rect width="445" height="220" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="445" height="28" rx="6" fill="#92400e"/>
    <text x="222" y="19" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">BEURRE MANIÉ SUCRÉ (RATIO D'OR 3 820 g) & ENCHÂSSEMENT</text>

    <!-- Composition bloc -->
    <g transform="translate(25, 45)">
      <rect x="0" y="0" width="395" height="65" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
      <text x="15" y="24" fill="#78350f" font-size="10" font-weight="800">Composition Plaque 40 × 30 cm (Épaisseur 2,5 cm) :</text>
      <text x="15" y="42" fill="#92400e" font-size="9.5">• Beurre tourage Debic 84 % froid (+4 °C) : <strong>2 000 g</strong> (52,4 %)</text>
      <text x="15" y="56" fill="#92400e" font-size="9.5">• Sucre extra-fin (≤ 200 µm) : <strong>1 800 g</strong> (47,1 %) + Fleur de sel Guérande : <strong>20 g</strong></text>
    </g>

    <!-- Enchâssement & T° -->
    <g transform="translate(25, 122)">
      <rect x="0" y="0" width="190" height="82" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
      <text x="95" y="18" fill="#0f172a" font-size="9" font-weight="700" text-anchor="middle">DÉTREMPE 5 000 g</text>
      <text x="95" y="34" fill="#2563eb" font-size="9" font-weight="800" text-anchor="middle">T° Pâte : +2 °C / +4 °C</text>
      <text x="95" y="50" fill="#64748b" font-size="8.5" text-anchor="middle">Galette 3 cm au bac Paneo</text>
      <text x="95" y="66" fill="#15803d" font-size="8.5" font-weight="700" text-anchor="middle">Zéro pointage en cuve</text>

      <path d="M 198 40 L 212 40" stroke="#94a3b8" stroke-width="2"/>
      <polygon points="212,36 220,40 212,44" fill="#94a3b8"/>

      <rect x="228" y="0" width="167" height="82" rx="4" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.2"/>
      <text x="311" y="18" fill="#78350f" font-size="9" font-weight="700" text-anchor="middle">BEURRE MANIÉ 3 820 g</text>
      <text x="311" y="34" fill="#b45309" font-size="9" font-weight="800" text-anchor="middle">T° Plaque : 12 °C – 14 °C</text>
      <text x="311" y="50" fill="#78350f" font-size="8.5" text-anchor="middle">Amalgame friction V1 (2 min)</text>
      <text x="311" y="66" fill="#b91c1c" font-size="8.5" font-weight="700" text-anchor="middle">Pâton total : 8 820 g net</text>
    </g>
  </g>

  <!-- Right: 2 Tours Simples = 9 Films & Façonnages -->
  <g transform="translate(485, 20)">
    <rect width="455" height="220" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="455" height="28" rx="6" fill="#b45309"/>
    <text x="227" y="19" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle" letter-spacing="0.5">2 TOURS SIMPLES (9 FILMS ÉPAIS) & FAÇONNAGES SANS FUITE</text>

    <!-- Tourage 2 simples -->
    <g transform="translate(20, 42)">
      <rect x="0" y="0" width="195" height="58" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="1"/>
      <text x="97" y="16" fill="#0369a1" font-size="9" font-weight="700" text-anchor="middle">1ER TOUR SIMPLE (10 mm)</text>
      <text x="97" y="32" fill="#64748b" font-size="8.5" text-anchor="middle">Pliage en 3 • Pas de fuite sucre</text>
      <text x="97" y="47" fill="#0284c7" font-size="8.5" font-weight="700" text-anchor="middle">Détente 15 min à +2 °C</text>

      <path d="M 203 29 L 217 29" stroke="#94a3b8" stroke-width="2"/>
      <polygon points="217,25 225,29 217,33" fill="#94a3b8"/>

      <rect x="230" y="0" width="185" height="58" rx="4" fill="#ffffff" stroke="#16a34a" stroke-width="1"/>
      <text x="322" y="16" fill="#15803d" font-size="9" font-weight="700" text-anchor="middle">2E TOUR SIMPLE (8 mm)</text>
      <text x="322" y="32" fill="#64748b" font-size="8.5" text-anchor="middle">Drossage 4 chants • Détente 30 min</text>
      <text x="322" y="47" fill="#15803d" font-size="8.5" font-weight="800" text-anchor="middle">9 FILMS CARAMÉLISANTS</text>
    </g>

    <!-- Dual Façonnage Specs -->
    <g transform="translate(20, 112)">
      <!-- Indiv 100g -->
      <rect x="0" y="0" width="200" height="92" rx="4" fill="#fffbeb" stroke="#fcd34d" stroke-width="1"/>
      <text x="100" y="16" fill="#92400e" font-size="9" font-weight="800" text-anchor="middle">INDIVIDUEL 100 g (88 pcs/bac)</text>
      <text x="12" y="34" fill="#78350f" font-size="8.5">• Abaisse : 4,0 mm bande 400 mm</text>
      <text x="12" y="49" fill="#78350f" font-size="8.5">• Roulage boudin + Flash 10 min</text>
      <text x="12" y="64" fill="#78350f" font-size="8.5">• Tronçonnage : <strong>100 g pile</strong></text>
      <text x="12" y="79" fill="#b45309" font-size="8.5" font-weight="700">• Moule silicone + lit cassonade</text>

      <!-- Partage 400/600g -->
      <rect x="215" y="0" width="200" height="92" rx="4" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
      <text x="315" y="16" fill="#166534" font-size="9" font-weight="800" text-anchor="middle">PARTAGE (400 g & 600 g)</text>
      <text x="227" y="34" fill="#14532d" font-size="8.5">• Abaisse : 5,0 mm régulière</text>
      <text x="227" y="49" fill="#14532d" font-size="8.5">• Découpe carrés (21×21 / 25×25 cm)</text>
      <text x="227" y="64" fill="#14532d" font-size="8.5">• 4 pointes rabattues (octogone)</text>
      <text x="227" y="79" fill="#15803d" font-size="8.5" font-weight="700">• Moules Ø 20 cm (400g) / Ø 24 cm (600g)</text>
    </g>
  </g>
</svg>"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"[OK] Généré : {filepath}")

create_svg_kouign_amann_tourage('/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie/docs/vectors/tourage_kouign_amann_schema.svg')
