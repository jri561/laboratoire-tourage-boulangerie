#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur des 3 Maquettes finales (Mix AC-1 / AC-2 / AC-3).
Toutes en tableau pleine largeur + Mémo Express en haut + Code couleur strict relié
entre les phases du tableau (gauche) et les instructions (droite) :
  - Phase 1 (Base / V1)       = Bleu (#1e40af)
  - Phase 2 (Ajout V2 / Tour) = Ambre (#b45309)
  - Phase 3 (Tourage / PAC)   = Vert (#15803d)
"""

import os
import subprocess

BASE_DIR = "/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie"
EXPORT_DIR = os.path.join(BASE_DIR, "exports_pdf")


def compile_pdf(html_str: str, out_name: str):
    os.makedirs(EXPORT_DIR, exist_ok=True)
    html_path = os.path.join(EXPORT_DIR, f"{out_name}.html")
    pdf_path = os.path.join(EXPORT_DIR, f"{out_name}.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_str)
    subprocess.run(
        [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            html_path,
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    print(f"[OK] {pdf_path} ({os.path.getsize(pdf_path):,} octets)")


# ==============================================================================
# MAQUETTE 1 : CHRONO UNIFIÉ
# En-tête sobre + Mémo Express 5 tuiles + Tableau pleine largeur (bandeaux pleins)
# Page droite : Pastilles 01/02/03 & barres couleur strictement reliées au tableau
# ==============================================================================
HTML_M1 = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Maquette 1 - Chrono Unifie</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
@page { size: A4 portrait; margin: 12mm 13mm 12mm 15mm; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
body { font-family: "Inter", sans-serif; color: #1c1917; background: #ffffff; margin: 0; font-size: 9pt; line-height: 1.32; font-variant-numeric: tabular-nums; }
.sheet { height: 272mm; display: flex; flex-direction: column; justify-content: space-between; page-break-after: always; overflow: hidden; }
.sheet:last-child { page-break-after: auto; }

.head { display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 2.5px solid #1c1917; padding-bottom: 2.5mm; margin-bottom: 3.5mm; }
.kicker { font-size: 7.5pt; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase; color: #b45309; margin-bottom: 0.8mm; }
.title { font-size: 19pt; font-weight: 900; letter-spacing: -0.02em; line-height: 1.05; margin: 0; }
.sub { font-size: 8.3pt; color: #57534e; font-weight: 500; margin-top: 1mm; }
.pill { background: #1e40af; color: #ffffff; padding: 2mm 4mm; border-radius: 4px; font-weight: 900; font-size: 8.8pt; white-space: nowrap; }
.pill.green { background: #15803d; }

/* Mémo Express 5 tuiles */
.memo-strip { display: grid; grid-template-columns: repeat(5, 1fr); gap: 2mm; margin-bottom: 4mm; }
.m-card { background: #faf8f5; border: 1px solid #e7e5e4; border-top: 3.5px solid #1e40af; border-radius: 3px; padding: 2mm 2.5mm; }
.m-card.amber { border-top-color: #b45309; }
.m-card.green { border-top-color: #15803d; }
.m-v { font-size: 13.5pt; font-weight: 900; color: #1c1917; line-height: 1.08; }
.m-l { font-size: 6.5pt; font-weight: 700; text-transform: uppercase; color: #78716c; margin-top: 0.8mm; }

/* Tableau pleine largeur */
.tbl { width: 100%; border-collapse: collapse; }
.tbl th { font-size: 7.2pt; font-weight: 800; text-transform: uppercase; letter-spacing: 0.04em; color: #57534e; border-bottom: 2px solid #1c1917; padding: 1.8mm 2mm; text-align: left; }
.tbl th.num { text-align: right; }
.tbl th.main { background: #eff6ff; color: #1e3a8a; font-size: 8pt; }
.tbl td { padding: 2mm 2mm; border-bottom: 1px solid #f0ede8; font-size: 9pt; vertical-align: middle; }
.tbl td.chk { width: 7mm; text-align: center; font-size: 11pt; color: #a8a29e; }
.tbl td.ing { font-weight: 600; }
.tbl td.ing small { font-weight: 500; color: #78716c; font-size: 7.8pt; }
.tbl td.q1 { text-align: right; font-size: 12pt; font-weight: 900; color: #0f172a; background: #eff6ff; padding-right: 3mm; }
.tbl td.q2 { text-align: right; font-size: 9pt; font-weight: 600; color: #57534e; }

.p-band td { font-size: 7.8pt; font-weight: 800; letter-spacing: 0.06em; text-transform: uppercase; padding: 1.6mm 2.5mm; color: #ffffff; border: none; }
.p-band.p1 td { background: #1e40af; }
.p-band.p2 td { background: #b45309; }
.p-band.p3 td { background: #15803d; }

.r-stot td { background: #f5f5f4; font-weight: 800; border-top: 1.5px solid #a8a29e; border-bottom: 1.5px solid #a8a29e; }
.r-stot td.q1 { background: #dbeafe; color: #1e3a8a; font-size: 12pt; }
.r-tot td { background: #1c1917; color: #ffffff; font-weight: 900; font-size: 10pt; padding: 2.5mm 2mm; }
.r-tot td.q1 { background: #1e40af; color: #ffffff; font-size: 13.5pt; }
.r-tot td.q2 { color: #e7e5e4; }

/* Page droite : Pastilles couleur reliées */
.sec { margin-bottom: 4mm; }
.sec-h { display: flex; align-items: center; gap: 2.5mm; border-bottom: 1.5px solid #e7e5e4; padding-bottom: 1.5mm; margin-bottom: 2mm; }
.sec-num { color: #ffffff; font-size: 10pt; font-weight: 900; padding: 0.8mm 2.5mm; border-radius: 3px; }
.sec-num.p1 { background: #1e40af; }
.sec-num.p2 { background: #b45309; }
.sec-num.p3 { background: #15803d; }
.sec-t { font-size: 10.5pt; font-weight: 800; text-transform: uppercase; color: #1c1917; }
.sec-k { margin-left: auto; font-size: 8pt; font-weight: 800; background: #faf8f5; border: 1px solid #d6d3d1; padding: 0.6mm 2.5mm; border-radius: 3px; color: #1c1917; }

.step-rows { display: flex; flex-direction: column; gap: 1.5mm; }
.s-row { display: grid; grid-template-columns: 35mm 1fr; border: 1px solid #e7e5e4; border-left: 3.5px solid #1e40af; border-radius: 3px; overflow: hidden; background: #ffffff; }
.s-row.p2 { border-left-color: #b45309; }
.s-row.p3 { border-left-color: #15803d; }
.s-left { background: #faf8f5; border-right: 1px solid #e7e5e4; padding: 2mm 2.5mm; display: flex; flex-direction: column; justify-content: center; }
.s-val { font-size: 11.5pt; font-weight: 900; color: #1c1917; line-height: 1.1; }
.s-lbl { font-size: 6.8pt; font-weight: 700; text-transform: uppercase; color: #78716c; margin-top: 0.5mm; }
.s-right { padding: 2mm 3mm; display: flex; flex-direction: column; justify-content: center; font-size: 8.6pt; color: #44403c; }
.s-right strong.st { color: #1c1917; font-size: 9pt; display: block; margin-bottom: 0.4mm; }

.rule-box { background: #fef2f2; border: 1.5px solid #ef4444; border-left: 5px solid #dc2626; border-radius: 4px; padding: 2.5mm 3.5mm; margin-top: auto; }
.rule-h { font-size: 7.5pt; font-weight: 900; text-transform: uppercase; letter-spacing: 0.06em; color: #dc2626; margin-bottom: 0.5mm; }
.rule-p { font-size: 8.6pt; font-weight: 800; color: #7f1d1d; margin: 0; }
.foot { display: flex; justify-content: space-between; font-size: 7.5pt; font-weight: 700; color: #78716c; border-top: 1px solid #e7e5e4; padding-top: 2mm; margin-top: 2mm; }
</style>
</head>
<body>
<div class="sheet">
  <div>
    <div class="head">
      <div>
        <div class="kicker">FICHE 01 • MAQUETTE 1 « CHRONO UNIFIÉ »</div>
        <h1 class="title">Pâte Levée Feuilletée Commune</h1>
        <div class="sub">Codes V-PLF-01 à 07 • Couleurs Phases Tableau = Couleurs Instructions</div>
      </div>
      <div class="pill">PESÉE • 1 BAC = 10 KG</div>
    </div>

    <div class="memo-strip">
      <div class="m-card"><div class="m-v">8 000 g</div><div class="m-l">Détrempe / Bac</div></div>
      <div class="m-card amber"><div class="m-v">2 000 g</div><div class="m-l">Debic 82%</div></div>
      <div class="m-card"><div class="m-v">20–21 °C</div><div class="m-l">Sortie Pétrin</div></div>
      <div class="m-card amber"><div class="m-v">1D + 1S</div><div class="m-l">Tourage (12f)</div></div>
      <div class="m-card green"><div class="m-v">-10 °C</div><div class="m-l">Sonde Fin PAC</div></div>
    </div>

    <table class="tbl">
      <thead>
        <tr><th style="width:7mm"></th><th>Ingrédient à peser</th><th class="num main">1 BAC (10 kg)</th><th class="num">10 BACS (100 kg)</th><th class="num">20 BACS (200 kg)</th></tr>
      </thead>
      <tbody>
        <tr class="p-band p1"><td colspan="5">01 • DÉTREMPAGE CUVE V1 (FRASAGE 5 MIN)</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Farine Gruau Rouge T45</td><td class="q1">3 130 g</td><td class="q2">31 300 g</td><td class="q2">62 600 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Farine T65 Tradition pure</td><td class="q1">1 340 g</td><td class="q2">13 400 g</td><td class="q2">26 800 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Eau glacée (+1 °C) / Glace écaille</td><td class="q1">2 015 g</td><td class="q2">20 150 g</td><td class="q2">40 300 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Sucre cristal blanc</td><td class="q1">394 g</td><td class="q2">3 940 g</td><td class="q2">7 880 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Trimoline <small>(sucre inverti)</small></td><td class="q1">157 g</td><td class="q2">1 570 g</td><td class="q2">3 140 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Levure fraîche L'Hirondelle Or</td><td class="q1">188 g</td><td class="q2">1 880 g</td><td class="q2">3 760 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Poudre de lait entier 26 % MG</td><td class="q1">180 g</td><td class="q2">1 800 g</td><td class="q2">3 600 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Améliorant S500 Kimo Short</td><td class="q1">90 g</td><td class="q2">900 g</td><td class="q2">1 800 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Sel fin d'atelier</td><td class="q1">90 g</td><td class="q2">900 g</td><td class="q2">1 800 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Vinaigre blanc d'alcool 8°</td><td class="q1">36 g</td><td class="q2">360 g</td><td class="q2">720 g</td></tr>

        <tr class="p-band p2"><td colspan="5">02 • INCORPORATION CUVE V2 (4 MIN 30 À 5 MIN MAX)</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Margarine OPAL cuve <small>(dés 500 g)</small></td><td class="q1">380 g</td><td class="q2">3 800 g</td><td class="q2">7 600 g</td></tr>
        <tr class="r-stot"><td></td><td>SOUS-TOTAL DÉTREMPE NETTE</td><td class="q1">8 000 g</td><td class="q2">80 000 g</td><td class="q2">160 000 g</td></tr>

        <tr class="p-band p3"><td colspan="5">03 • TOURAGE J+1 &amp; CIRCUIT PAC</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Beurre Debic Croissant 82 % <small>(12–14 °C)</small></td><td class="q1">2 000 g</td><td class="q2">20 000 g</td><td class="q2">40 000 g</td></tr>
        <tr class="r-tot"><td></td><td>POIDS TOTAL PÂTON TOURÉ</td><td class="q1">10 000 g</td><td class="q2">100 000 g</td><td class="q2">200 000 g</td></tr>
      </tbody>
    </table>
  </div>
  <div class="foot"><span>01 — RECETTE MAÎTRESSE PLF COMMUNE • POSTE DE PESÉE</span><span>PAGE 4 / 37</span></div>
</div>

<div class="sheet">
  <div style="display:flex; flex-direction:column; flex:1;">
    <div class="head">
      <div>
        <div class="kicker" style="color:#15803d;">FICHE 01 • CONDUITE MACHINE &amp; CIRCUIT PAC</div>
        <h1 class="title">Méthode Opératoire &amp; Tourage</h1>
        <div class="sub">Repères couleur 01 / 02 / 03 alignés sur la feuille de pesée</div>
      </div>
      <div class="pill green">CONDUITE &amp; PAC</div>
    </div>

    <div class="sec">
      <div class="sec-h"><span class="sec-num p1">01</span><span class="sec-t">Détrempe, Pétrissage &amp; Blocage J-1</span><span class="sec-k">Sortie 20–21 °C</span></div>
      <div class="step-rows">
        <div class="s-row"><div class="s-left"><span class="s-val">5 min V1</span><span class="s-lbl">Frasage</span></div><div class="s-right"><strong class="st">Mélange cuve V1 (bloc bleu)</strong>Verser tous les ingrédients 01 dans le pétrin spirale. Tourner 5 min en 1re vitesse.</div></div>
        <div class="s-row p2"><div class="s-left"><span class="s-val">4'30–5' V2</span><span class="s-lbl">Ajout V2 (ambre)</span></div><div class="s-right"><strong class="st">Incorporation OPAL (bloc ambre)</strong>Passer en V2 avec l'OPAL (dés 500 g). Stopper dès décollement net (zéro voile étiré).</div></div>
        <div class="s-row"><div class="s-left"><span class="s-val">35' / -35 °C</span><span class="s-lbl">Puis 0/+1,5 °C</span></div><div class="s-right"><strong class="st">Bacs Paneo &amp; Pointage Nuit</strong>Diviser en bacs de <strong>8 000 g pile</strong> (3 cm). Flash -35 °C (cœur &lt; 6 °C), puis 12–15 h au froid.</div></div>
      </div>
    </div>

    <div class="sec">
      <div class="sec-h"><span class="sec-num p2">02</span><span class="sec-t">Tourage Unifié (1D + 1S)</span><span class="sec-k">12 films de beurre</span></div>
      <div class="step-rows">
        <div class="s-row p2"><div class="s-left"><span class="s-val">12–14 °C</span><span class="s-lbl">Beurre Debic</span></div><div class="s-right"><strong class="st">Enchâssement Portefeuille</strong>Détrempe à +2/+4 °C + plaque 2 000 g Debic. Enfermer bord à bord sans chevauchement.</div></div>
        <div class="s-row p2"><div class="s-left"><span class="s-val">1D + 1S</span><span class="s-lbl">Enchaînés</span></div><div class="s-right"><strong class="st">Tour Double + Tour Simple</strong>Allonger, plier en 4, pivoter 90°, allonger, plier en 3. Parer les 4 chants au couteau.</div></div>
        <div class="s-row p2"><div class="s-left"><span class="s-val">45 min +2 °C</span><span class="s-lbl">Détente filmée</span></div><div class="s-right"><strong class="st">Repos avant abaisse</strong>Filmer hermétiquement et détendre 45 min à +2 °C avant laminage final.</div></div>
      </div>
    </div>

    <div class="sec">
      <div class="sec-h"><span class="sec-num p3">03</span><span class="sec-t">Abaisse &amp; Double Congélation PAC</span><span class="sec-k">Sonde -10 °C</span></div>
      <div class="step-rows">
        <div class="s-row p3"><div class="s-left"><span class="s-val">≥ 60 sec</span><span class="s-lbl">Tapis Polyline</span></div><div class="s-right"><strong class="st">Déroulage &amp; Décompression</strong>Côté fariné dessous, dessus <strong>nu sans farine</strong> (soudure). Flotter ≥ 60 s avant coupe.</div></div>
        <div class="s-row p3"><div class="s-left"><span class="s-val">70–75 % vol</span><span class="s-lbl">Étuve 2h15–30</span></div><div class="s-right"><strong class="st">Stock 1 Cru → Étuve → Stock 2 PAC</strong>Stock 1 : flash -35 °C → -18 °C. PAC : nuit +2/+4 °C → étuve 25–26 °C / 75–80 % HR → ressuyage 15' (+4 °C) → Dorure Végétale pistolet (1,5 bar) → flash -35 °C (arrêt -10 °C cœur).</div></div>
      </div>
    </div>

    <div class="rule-box">
      <div class="rule-h">Règle d'Or Atelier — Points de Rupture</div>
      <p class="rule-p">Zéro voile au pétrin • Zéro farine dessus au déroulage • Arrêt étuve ≤ 75 % • Sonde flash stricte à -10 °C.</p>
    </div>
  </div>
  <div class="foot"><span>01 — RECETTE MAÎTRESSE PLF COMMUNE • CONDUITE &amp; CUISSON</span><span>PAGE 5 / 37</span></div>
</div>
</body>
</html>"""


# ==============================================================================
# MAQUETTE 2 : LABO CONTRASTE (Bandeau sombre + Double Mémo + Blocs ouverts)
# ==============================================================================
HTML_M2 = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Maquette 2 - Labo Contraste</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
@page { size: A4 portrait; margin: 12mm 13mm 12mm 15mm; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
body { font-family: "Inter", sans-serif; color: #0f172a; background: #ffffff; margin: 0; font-size: 9pt; line-height: 1.32; font-variant-numeric: tabular-nums; }
.sheet { height: 272mm; display: flex; flex-direction: column; justify-content: space-between; page-break-after: always; overflow: hidden; }
.sheet:last-child { page-break-after: auto; }

/* Bandeau sombre haut */
.dark-head { background: #0f172a; color: #ffffff; padding: 3.2mm 4.5mm; border-radius: 4px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 3.5mm; }
.dh-k { font-size: 7.2pt; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase; color: #fbbf24; }
.dh-t { font-size: 16.5pt; font-weight: 900; margin: 0.5mm 0 0 0; line-height: 1.08; }
.dh-b { background: #2563eb; color: #ffffff; padding: 1.8mm 3.5mm; border-radius: 3px; font-size: 8.5pt; font-weight: 900; text-transform: uppercase; white-space: nowrap; }
.dh-b.green { background: #16a34a; }

/* Double Mémo Express */
.dual-memo { display: grid; grid-template-columns: 1fr 1.45fr; gap: 3mm; margin-bottom: 3.5mm; }
.dm-box { background: #faf8f5; border: 1px solid #d6d3d1; border-radius: 4px; padding: 2.2mm 3mm; }
.dm-h { font-size: 6.8pt; font-weight: 900; text-transform: uppercase; letter-spacing: 0.08em; color: #b45309; margin-bottom: 1.5mm; }
.dm-items { display: flex; justify-content: space-between; gap: 2mm; }
.dm-i strong { display: block; font-size: 13pt; font-weight: 900; color: #0f172a; line-height: 1.05; }
.dm-i span { font-size: 6.6pt; font-weight: 700; text-transform: uppercase; color: #64748b; }

/* Tableau pleine largeur avec bordure gauche couleur par phase */
.tbl { width: 100%; border-collapse: collapse; }
.tbl th { font-size: 7.2pt; font-weight: 800; text-transform: uppercase; color: #475569; border-bottom: 2px solid #0f172a; padding: 1.8mm 2mm; text-align: left; }
.tbl th.num { text-align: right; }
.tbl th.main { color: #0f172a; background: #fef3c7; font-size: 8pt; }
.tbl td { padding: 2mm 2mm; border-bottom: 1px solid #e7e5e4; font-size: 9pt; vertical-align: middle; }
.tbl tr:nth-child(even) td { background: #fcfbf9; }
.tbl td.chk { width: 7mm; text-align: center; font-size: 11pt; color: #94a3b8; }
.tbl td.ing { font-weight: 600; }
.tbl td.ing small { color: #64748b; font-weight: 500; font-size: 7.8pt; }
.tbl td.q1 { text-align: right; font-size: 12pt; font-weight: 900; color: #0f172a; background: #fffbeb !important; border-left: 2px solid #f59e0b; border-right: 2px solid #f59e0b; padding-right: 3mm; }
.tbl td.q2 { text-align: right; font-size: 9pt; font-weight: 600; color: #475569; }

.ph td { font-size: 7.8pt; font-weight: 900; text-transform: uppercase; letter-spacing: 0.05em; padding: 1.6mm 2.5mm; background: #f1f5f9 !important; border-top: 1.5px solid #0f172a; border-bottom: 1px solid #cbd5e1; }
.ph.p1 td { border-left: 5px solid #1e40af; color: #1e3a8a; background: #eff6ff !important; }
.ph.p2 td { border-left: 5px solid #b45309; color: #92400e; background: #fffbeb !important; }
.ph.p3 td { border-left: 5px solid #15803d; color: #166534; background: #f0fdf4 !important; }

.st td { background: #f1f5f9 !important; font-weight: 800; border-top: 1.5px solid #94a3b8; border-bottom: 1.5px solid #94a3b8; }
.st td.q1 { background: #fde68a !important; font-size: 12pt; }
.tt td { background: #0f172a !important; color: #ffffff; font-weight: 900; font-size: 10pt; padding: 2.5mm 2mm; }
.tt td.q1 { background: #b45309 !important; color: #ffffff; font-size: 13.5pt; border-color: #b45309; }
.tt td.q2 { color: #cbd5e1; }

/* Page Droite : Blocs ouverts bordure épaisse exactement mêmes couleurs */
.open-sec { border-left: 5px solid #1e40af; padding-left: 3.5mm; margin-bottom: 4.5mm; }
.open-sec.p2 { border-left-color: #b45309; }
.open-sec.p3 { border-left-color: #15803d; }
.os-head { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 2mm; border-bottom: 1px solid #e2e8f0; padding-bottom: 1mm; }
.os-title { font-size: 10.8pt; font-weight: 900; text-transform: uppercase; color: #0f172a; }
.os-title span.tag1 { color: #1e40af; margin-right: 1.5mm; }
.os-title span.tag2 { color: #b45309; margin-right: 1.5mm; }
.os-title span.tag3 { color: #15803d; margin-right: 1.5mm; }
.os-badge { font-size: 8.2pt; font-weight: 800; color: #0f172a; background: #f1f5f9; padding: 0.5mm 2.5mm; border-radius: 3px; }

.os-grid { display: flex; flex-direction: column; gap: 2.2mm; }
.os-line { display: grid; grid-template-columns: 38mm 1fr; gap: 3mm; align-items: baseline; }
.os-key { font-size: 11pt; font-weight: 900; color: #0f172a; }
.os-key small { display: block; font-size: 7.2pt; font-weight: 700; color: #64748b; text-transform: uppercase; }
.os-val { font-size: 8.8pt; color: #334155; }

.dual-foot-box { display: grid; grid-template-columns: 1.3fr 1fr; gap: 3mm; margin-top: auto; }
.dfb-red { background: #fef2f2; border: 1.5px solid #ef4444; border-radius: 4px; padding: 2.5mm 3mm; color: #991b1b; font-size: 8.2pt; font-weight: 800; }
.dfb-gold { background: #fffbeb; border: 1.5px solid #f59e0b; border-radius: 4px; padding: 2.5mm 3mm; color: #78350f; font-size: 8.2pt; font-weight: 700; }
.dfb-h { font-size: 7pt; font-weight: 900; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 0.8mm; }
.foot { display: flex; justify-content: space-between; font-size: 7.5pt; font-weight: 700; color: #64748b; border-top: 1px solid #cbd5e1; padding-top: 2mm; margin-top: 2mm; }
</style>
</head>
<body>
<div class="sheet">
  <div>
    <div class="dark-head">
      <div>
        <div class="dh-k">FICHE 01 • MAQUETTE 2 « LABO CONTRASTE »</div>
        <h1 class="dh-t">Pâte Levée Feuilletée Commune</h1>
      </div>
      <div class="dh-b">PESÉE • 1 BAC = 10 KG</div>
    </div>

    <div class="dual-memo">
      <div class="dm-box">
        <div class="dm-h">Mémo Calibres</div>
        <div class="dm-items">
          <div class="dm-i"><strong>8 000 g</strong><span>Détrempe / Bac</span></div>
          <div class="dm-i"><strong>2 000 g</strong><span>Debic 82%</span></div>
        </div>
      </div>
      <div class="dm-box">
        <div class="dm-h">Mémo Express Process</div>
        <div class="dm-items">
          <div class="dm-i"><strong>20–21 °C</strong><span>Sortie Pétrin</span></div>
          <div class="dm-i"><strong>1D + 1S</strong><span>Tourage (12f)</span></div>
          <div class="dm-i"><strong>-10 °C</strong><span>Sonde Fin PAC</span></div>
        </div>
      </div>
    </div>

    <table class="tbl">
      <thead>
        <tr><th style="width:7mm"></th><th>Ingrédient à peser</th><th class="num main">1 BAC (10 kg)</th><th class="num">10 BACS (100 kg)</th><th class="num">20 BACS (200 kg)</th></tr>
      </thead>
      <tbody>
        <tr class="ph p1"><td colspan="5">01 • Détrempage Cuve V1 (Frasage 5 min)</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Farine Gruau Rouge T45</td><td class="q1">3 130 g</td><td class="q2">31 300 g</td><td class="q2">62 600 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Farine T65 Tradition pure</td><td class="q1">1 340 g</td><td class="q2">13 400 g</td><td class="q2">26 800 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Eau glacée (+1 °C) / Glace écaille</td><td class="q1">2 015 g</td><td class="q2">20 150 g</td><td class="q2">40 300 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Sucre cristal blanc</td><td class="q1">394 g</td><td class="q2">3 940 g</td><td class="q2">7 880 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Trimoline <small>(sucre inverti)</small></td><td class="q1">157 g</td><td class="q2">1 570 g</td><td class="q2">3 140 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Levure fraîche L'Hirondelle Or</td><td class="q1">188 g</td><td class="q2">1 880 g</td><td class="q2">3 760 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Poudre de lait entier 26 % MG</td><td class="q1">180 g</td><td class="q2">1 800 g</td><td class="q2">3 600 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Améliorant S500 Kimo Short</td><td class="q1">90 g</td><td class="q2">900 g</td><td class="q2">1 800 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Sel fin d'atelier</td><td class="q1">90 g</td><td class="q2">900 g</td><td class="q2">1 800 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Vinaigre blanc d'alcool 8°</td><td class="q1">36 g</td><td class="q2">360 g</td><td class="q2">720 g</td></tr>

        <tr class="ph p2"><td colspan="5">02 • Incorporation Cuve V2 (4 min 30 à 5 min max)</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Margarine OPAL cuve <small>(dés 500 g)</small></td><td class="q1">380 g</td><td class="q2">3 800 g</td><td class="q2">7 600 g</td></tr>
        <tr class="st"><td></td><td>SOUS-TOTAL DÉTREMPE NETTE</td><td class="q1">8 000 g</td><td class="q2">80 000 g</td><td class="q2">160 000 g</td></tr>

        <tr class="ph p3"><td colspan="5">03 • Tourage J+1 &amp; Circuit PAC</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Beurre Debic Croissant 82 % <small>(12–14 °C)</small></td><td class="q1">2 000 g</td><td class="q2">20 000 g</td><td class="q2">40 000 g</td></tr>
        <tr class="tt"><td></td><td>POIDS TOTAL PÂTON TOURÉ</td><td class="q1">10 000 g</td><td class="q2">100 000 g</td><td class="q2">200 000 g</td></tr>
      </tbody>
    </table>
  </div>
  <div class="foot"><span>01 — RECETTE MAÎTRESSE PLF COMMUNE • POSTE DE PESÉE</span><span>PAGE 4 / 37</span></div>
</div>

<div class="sheet">
  <div style="display:flex; flex-direction:column; flex:1;">
    <div class="dark-head">
      <div>
        <div class="dh-k" style="color:#86efac;">FICHE 01 • CONDUITE &amp; CIRCUIT PAC</div>
        <h1 class="dh-t">Conduite Machine &amp; Tourage</h1>
      </div>
      <div class="dh-b green">CONDUITE &amp; PAC</div>
    </div>

    <div class="open-sec">
      <div class="os-head"><div class="os-title"><span class="tag1">01</span> Pétrissage &amp; Refroidissement J-1</div><div class="os-badge">Sortie 20–21 °C</div></div>
      <div class="os-grid">
        <div class="os-line"><div class="os-key">5 min V1<small>Frasage (Bleu)</small></div><div class="os-val">Verser tous les ingrédients du bloc 01 dans le pétrin spirale. Tourner 5 min en 1re vitesse.</div></div>
        <div class="os-line"><div class="os-key" style="color:#b45309;">4'30–5' V2<small>Ajout OPAL (Ambre)</small></div><div class="os-val">Passer en V2 avec l'OPAL (dés 500 g). Stopper au 1er décollement net (zéro voile étiré).</div></div>
        <div class="os-line"><div class="os-key">35' / -35 °C<small>Bacs &amp; Pointage</small></div><div class="os-val">Diviser en bacs de <strong>8 000 g pile</strong> (3 cm). Flash -35 °C (cœur &lt; 6 °C), puis 12–15 h à 0/+1,5 °C.</div></div>
      </div>
    </div>

    <div class="open-sec p2">
      <div class="os-head"><div class="os-title"><span class="tag2">02</span> Tourage Unifié (1D + 1S)</div><div class="os-badge">12 films de beurre</div></div>
      <div class="os-grid">
        <div class="os-line"><div class="os-key">12–14 °C<small>Enchâssement</small></div><div class="os-val">Détrempe à +2/+4 °C + plaque Debic 2 000 g à 12–14 °C. Fermer portefeuille bord à bord.</div></div>
        <div class="os-line"><div class="os-key">1D + 1S<small>Enchaînés</small></div><div class="os-val">Allonger, plier en 4 (Tour Double), pivoter 90°, allonger, plier en 3 (Tour Simple).</div></div>
        <div class="os-line"><div class="os-key">45 min +2 °C<small>Drossage &amp; Détente</small></div><div class="os-val">Couper/parer les 4 chants fermés au couteau, filmer et laisser détendre 45 min avant abaisse.</div></div>
      </div>
    </div>

    <div class="open-sec p3">
      <div class="os-head"><div class="os-title"><span class="tag3">03</span> Abaisse &amp; Double Congélation PAC</div><div class="os-badge">Sonde -10 °C</div></div>
      <div class="os-grid">
        <div class="os-line"><div class="os-key">≥ 60 sec<small>Tapis Polyline</small></div><div class="os-val">Dérouler face farinée dessous, dessus <strong>nu sans farine</strong> (soudure). Flotter ≥ 60 s avant coupe.</div></div>
        <div class="os-line"><div class="os-key">35–40' / -35 °C<small>Stock 1 (Cru)</small></div><div class="os-val">Plaquer serré, passer en cellule flash -35 °C, puis stocker en caisses étanches à -18 °C.</div></div>
        <div class="os-line"><div class="os-key">70–75 % vol<small>Étuve &amp; Stock 2</small></div><div class="os-val">Nuit +2/+4 °C (10–12 h) → étuve <strong>25–26 °C / 75–80 % HR</strong> (2h15–2h30) → ressuyage 15' (+4 °C) → Dorure Végétale pistolet (1,5 bar) → flash -35 °C (arrêt -10 °C cœur) → -18 °C.</div></div>
      </div>
    </div>

    <div class="dual-foot-box">
      <div class="dfb-red"><div class="dfb-h">Interdictions Strictes</div>Zéro voile au pétrin • Zéro farine dessus au déroulage • Arrêt étuve ≤ 75 % volume.</div>
      <div class="dfb-gold"><div class="dfb-h">Contrôle Qualité</div>Sonde cœur -10 °C exact en fin de flash PAC avant mise en caisses -18 °C.</div>
    </div>
  </div>
  <div class="foot"><span>01 — RECETTE MAÎTRESSE PLF COMMUNE • CONDUITE &amp; CUISSON</span><span>PAGE 5 / 37</span></div>
</div>
</body>
</html>"""


# ==============================================================================
# MAQUETTE 3 : ÉDITION MAÎTRE TOURIER
# Mémo Express en barre haute 2 blocs + Pastilles numérotées dans le tableau
# Page droite : Bandeaux fins colorés + Cartes crème aérées avec gros badge à gauche
# ==============================================================================
HTML_M3 = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Maquette 3 - Edition Maitre Tourier</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
@page { size: A4 portrait; margin: 12mm 13mm 12mm 15mm; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
body { font-family: "Inter", sans-serif; color: #1c1917; background: #ffffff; margin: 0; font-size: 9pt; line-height: 1.32; font-variant-numeric: tabular-nums; }
.sheet { height: 272mm; display: flex; flex-direction: column; justify-content: space-between; page-break-after: always; overflow: hidden; }
.sheet:last-child { page-break-after: auto; }

.head { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #b45309; padding-bottom: 2.5mm; margin-bottom: 3.5mm; }
.kicker { font-size: 7.5pt; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase; color: #b45309; }
.title { font-size: 18.5pt; font-weight: 900; letter-spacing: -0.02em; margin: 0.5mm 0 0 0; line-height: 1.05; }
.tag { border: 1.5px solid #1e40af; color: #1e40af; background: #eff6ff; padding: 1.5mm 3.5mm; border-radius: 3px; font-weight: 900; font-size: 8.5pt; white-space: nowrap; }
.tag.green { border-color: #15803d; color: #15803d; background: #f0fdf4; }

/* Mémo Express barre haute compacte 6 valeurs */
.memo-bar { display: grid; grid-template-columns: repeat(6, 1fr); background: #faf8f5; border: 1px solid #d6d3d1; border-radius: 4px; margin-bottom: 4mm; overflow: hidden; }
.mb-cell { padding: 2mm 2.2mm; border-right: 1px solid #e7e5e4; text-align: center; }
.mb-cell:last-child { border-right: none; }
.mb-v { font-size: 12.5pt; font-weight: 900; color: #1c1917; line-height: 1.08; }
.mb-l { font-size: 6.2pt; font-weight: 700; text-transform: uppercase; color: #78716c; margin-top: 0.6mm; }

/* Tableau avec pastilles phase 1 / 2 / 3 */
.tbl { width: 100%; border-collapse: collapse; }
.tbl th { font-size: 7.2pt; font-weight: 800; text-transform: uppercase; color: #78716c; border-bottom: 2px solid #1c1917; padding: 1.8mm 2mm; text-align: left; }
.tbl th.num { text-align: right; }
.tbl th.main { color: #1e3a8a; background: #eff6ff; font-size: 8pt; }
.tbl td { padding: 2mm 2mm; border-bottom: 1px solid #f0ede8; font-size: 9pt; vertical-align: middle; }
.tbl td.chk { width: 7mm; text-align: center; font-size: 11pt; color: #a8a29e; }
.tbl td.ing { font-weight: 600; }
.tbl td.ing small { color: #78716c; font-weight: 500; font-size: 7.8pt; }
.tbl td.q1 { text-align: right; font-size: 12.2pt; font-weight: 900; color: #0f172a; background: #eff6ff; padding-right: 3mm; }
.tbl td.q2 { text-align: right; font-size: 9pt; font-weight: 600; color: #57534e; }

.sub-hdr td { padding: 2.2mm 2mm 1.5mm 2mm; font-size: 8pt; font-weight: 900; text-transform: uppercase; letter-spacing: 0.04em; border-bottom: 1.5px solid #d6d3d1; background: #faf8f5; }
.pill-n { display: inline-block; color: #ffffff; padding: 0.4mm 2mm; border-radius: 3px; margin-right: 2mm; font-size: 7.5pt; }
.pn1 { background: #1e40af; }
.pn2 { background: #b45309; }
.pn3 { background: #15803d; }

.st td { background: #f5f5f4; font-weight: 800; border-top: 1.5px solid #a8a29e; border-bottom: 1.5px solid #a8a29e; }
.st td.q1 { background: #dbeafe; color: #1e3a8a; font-size: 12.2pt; }
.tt td { background: #1c1917; color: #ffffff; font-weight: 900; font-size: 10pt; padding: 2.5mm 2mm; }
.tt td.q1 { background: #1e40af; color: #ffffff; font-size: 13.5pt; }
.tt td.q2 { color: #e7e5e4; }

/* Page droite : Bandeaux fins colorés + Cartes crème */
.chap { margin-bottom: 4mm; }
.chap-bar { display: flex; align-items: center; justify-content: space-between; padding: 1.4mm 3mm; border-radius: 3px; color: #ffffff; margin-bottom: 2mm; }
.cb1 { background: #1e40af; }
.cb2 { background: #b45309; }
.cb3 { background: #15803d; }
.cb-t { font-size: 9.5pt; font-weight: 900; text-transform: uppercase; letter-spacing: 0.04em; }
.cb-k { font-size: 8pt; font-weight: 800; background: rgba(255,255,255,0.2); padding: 0.4mm 2mm; border-radius: 2px; }

.c-list { display: flex; flex-direction: column; gap: 1.5mm; }
.c-card { display: grid; grid-template-columns: 35mm 1fr; gap: 3mm; align-items: center; background: #faf8f5; border: 1px solid #e7e5e4; border-radius: 4px; padding: 2mm 3mm; }
.c-metric { background: #ffffff; border: 1px solid #d6d3d1; border-radius: 3px; padding: 1.4mm 2mm; text-align: center; }
.c-metric strong { display: block; font-size: 11pt; font-weight: 900; color: #1c1917; line-height: 1.1; }
.c-metric span { font-size: 6.5pt; font-weight: 700; text-transform: uppercase; color: #78716c; }
.c-body { font-size: 8.6pt; color: #44403c; }
.c-body strong.ct { color: #1c1917; }

.alert { background: #dc2626; color: #ffffff; padding: 2.5mm 4mm; border-radius: 4px; font-weight: 900; font-size: 8.6pt; text-align: center; text-transform: uppercase; margin-top: auto; }
.foot { display: flex; justify-content: space-between; font-size: 7.5pt; font-weight: 700; color: #78716c; border-top: 1px solid #e7e5e4; padding-top: 2mm; margin-top: 2mm; }
</style>
</head>
<body>
<div class="sheet">
  <div>
    <div class="head">
      <div>
        <div class="kicker">FICHE 01 • MAQUETTE 3 « ÉDITION MAÎTRE TOURIER »</div>
        <h1 class="title">Pâte Levée Feuilletée Commune</h1>
      </div>
      <div class="tag">PESÉE • 1 BAC = 10 KG</div>
    </div>

    <div class="memo-bar">
      <div class="mb-cell"><div class="mb-v">8 000 g</div><div class="mb-l">Détrempe / Bac</div></div>
      <div class="mb-cell"><div class="mb-v">2 000 g</div><div class="mb-l">Debic 82%</div></div>
      <div class="mb-cell"><div class="mb-v">20–21 °C</div><div class="mb-l">Sortie Pétrin</div></div>
      <div class="mb-cell"><div class="mb-v">3 cm</div><div class="mb-l">Pré-laminage</div></div>
      <div class="mb-cell"><div class="mb-v">1D + 1S</div><div class="mb-l">Tourage (12f)</div></div>
      <div class="mb-cell"><div class="mb-v">-10 °C</div><div class="mb-l">Sonde Fin PAC</div></div>
    </div>

    <table class="tbl">
      <thead>
        <tr><th style="width:7mm"></th><th>Ingrédient à peser</th><th class="num main">1 BAC (10 kg)</th><th class="num">10 BACS (100 kg)</th><th class="num">20 BACS (200 kg)</th></tr>
      </thead>
      <tbody>
        <tr class="sub-hdr"><td colspan="5"><span class="pill-n pn1">PHASE 1</span>Détrempage Cuve V1 (Frasage 5 min)</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Farine Gruau Rouge T45</td><td class="q1">3 130 g</td><td class="q2">31 300 g</td><td class="q2">62 600 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Farine T65 Tradition pure</td><td class="q1">1 340 g</td><td class="q2">13 400 g</td><td class="q2">26 800 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Eau glacée (+1 °C) / Glace écaille</td><td class="q1">2 015 g</td><td class="q2">20 150 g</td><td class="q2">40 300 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Sucre cristal blanc</td><td class="q1">394 g</td><td class="q2">3 940 g</td><td class="q2">7 880 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Trimoline <small>(sucre inverti)</small></td><td class="q1">157 g</td><td class="q2">1 570 g</td><td class="q2">3 140 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Levure fraîche L'Hirondelle Or</td><td class="q1">188 g</td><td class="q2">1 880 g</td><td class="q2">3 760 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Poudre de lait entier 26 % MG</td><td class="q1">180 g</td><td class="q2">1 800 g</td><td class="q2">3 600 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Améliorant S500 Kimo Short</td><td class="q1">90 g</td><td class="q2">900 g</td><td class="q2">1 800 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Sel fin d'atelier</td><td class="q1">90 g</td><td class="q2">900 g</td><td class="q2">1 800 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Vinaigre blanc d'alcool 8°</td><td class="q1">36 g</td><td class="q2">360 g</td><td class="q2">720 g</td></tr>

        <tr class="sub-hdr"><td colspan="5"><span class="pill-n pn2">PHASE 2</span>Incorporation Cuve V2 (4 min 30 à 5 min max)</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Margarine OPAL cuve <small>(dés 500 g)</small></td><td class="q1">380 g</td><td class="q2">3 800 g</td><td class="q2">7 600 g</td></tr>
        <tr class="st"><td></td><td>SOUS-TOTAL DÉTREMPE NETTE</td><td class="q1">8 000 g</td><td class="q2">80 000 g</td><td class="q2">160 000 g</td></tr>

        <tr class="sub-hdr"><td colspan="5"><span class="pill-n pn3">PHASE 3</span>Tourage J+1 &amp; Circuit PAC</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Beurre Debic Croissant 82 % <small>(12–14 °C)</small></td><td class="q1">2 000 g</td><td class="q2">20 000 g</td><td class="q2">40 000 g</td></tr>
        <tr class="tt"><td></td><td>POIDS TOTAL PÂTON TOURÉ</td><td class="q1">10 000 g</td><td class="q2">100 000 g</td><td class="q2">200 000 g</td></tr>
      </tbody>
    </table>
  </div>
  <div class="foot"><span>01 — RECETTE MAÎTRESSE PLF COMMUNE • POSTE DE PESÉE</span><span>PAGE 4 / 37</span></div>
</div>

<div class="sheet">
  <div style="display:flex; flex-direction:column; flex:1;">
    <div class="head">
      <div>
        <div class="kicker" style="color:#15803d;">FICHE 01 • CONDUITE MACHINE &amp; CIRCUIT PAC</div>
        <h1 class="title">Méthode Opératoire &amp; Tourage</h1>
      </div>
      <div class="tag green">CONDUITE &amp; PAC</div>
    </div>

    <div class="chap">
      <div class="chap-bar cb1"><span class="cb-t">PHASE 1 • Pétrissage &amp; Refroidissement J-1</span><span class="cb-k">SORTIE 20–21 °C</span></div>
      <div class="c-list">
        <div class="c-card"><div class="c-metric"><strong>5 min V1</strong><span>Frasage</span></div><div class="c-body"><strong class="ct">Base Phase 1 :</strong> Verser tous les ingrédients du bloc bleu dans le pétrin spirale. Tourner 5 min en 1re vitesse.</div></div>
        <div class="c-card"><div class="c-metric" style="border-color:#b45309;"><strong style="color:#b45309;">4'30–5' V2</strong><span>Phase 2 OPAL</span></div><div class="c-body"><strong class="ct">Incorporation OPAL :</strong> Passer en V2 avec l'OPAL (dés 500 g). Stopper au 1er décollement net (zéro voile).</div></div>
        <div class="c-card"><div class="c-metric"><strong>35' / -35 °C</strong><span>Puis 0/+1,5 °C</span></div><div class="c-body"><strong class="ct">Bacs &amp; Nuit :</strong> Diviser en bacs de <strong>8 000 g</strong> (3 cm). Flash -35 °C (cœur &lt; 6 °C), puis 12–15 h au froid.</div></div>
      </div>
    </div>

    <div class="chap">
      <div class="chap-bar cb2"><span class="cb-t">PHASE 2 • Tourage Unifié (1D + 1S)</span><span class="cb-k">12 FILMS BEURRE</span></div>
      <div class="c-list">
        <div class="c-card"><div class="c-metric"><strong>12–14 °C</strong><span>Beurre Debic</span></div><div class="c-body"><strong class="ct">Enchâssement :</strong> Détrempe à +2/+4 °C + plaque Debic 2 000 g. Fermer portefeuille bord à bord.</div></div>
        <div class="c-card"><div class="c-metric"><strong>1D + 1S</strong><span>Enchaînés</span></div><div class="c-body"><strong class="ct">Tours :</strong> Allonger, plier en 4 (Tour Double), pivoter 90°, allonger, plier en 3 (Tour Simple).</div></div>
        <div class="c-card"><div class="c-metric"><strong>45 min +2 °C</strong><span>Détente filmée</span></div><div class="c-body"><strong class="ct">Drossage :</strong> Parer les 4 chants fermés au couteau, filmer et laisser détendre 45 min avant abaisse.</div></div>
      </div>
    </div>

    <div class="chap">
      <div class="chap-bar cb3"><span class="cb-t">PHASE 3 • Abaisse &amp; Circuit Double Congélation PAC</span><span class="cb-k">SONDE -10 °C</span></div>
      <div class="c-list">
        <div class="c-card"><div class="c-metric"><strong>≥ 60 sec</strong><span>Tapis Polyline</span></div><div class="c-body"><strong class="ct">Déroulage :</strong> Côté fariné dessous, dessus <strong>nu sans farine</strong> (soudure). Flotter ≥ 60 s avant coupe.</div></div>
        <div class="c-card"><div class="c-metric"><strong>70–75 % vol</strong><span>Étuve 2h15–30</span></div><div class="c-body"><strong class="ct">Stock 1 → Stock 2 PAC :</strong> Stock 1 flash -35 °C → -18 °C. PAC : nuit +2/+4 °C → étuve 25–26 °C / 75–80 % HR → ressuyage 15' (+4 °C) → Dorure Végétale pistolet (1,5 bar) → flash -35 °C (arrêt -10 °C cœur).</div></div>
      </div>
    </div>

    <div class="alert">CRITIQUE : ZÉRO VOILE AU PÉTRIN • ZÉRO FARINE DESSUS • ARRÊT ÉTUVE 75 % MAX • SONDE -10 °C STRICT</div>
  </div>
  <div class="foot"><span>01 — RECETTE MAÎTRESSE PLF COMMUNE • CONDUITE &amp; CUISSON</span><span>PAGE 5 / 37</span></div>
</div>
</body>
</html>"""


if __name__ == "__main__":
    compile_pdf(HTML_M1, "Maquette_V3_1_Chrono_Unifie")
    compile_pdf(HTML_M2, "Maquette_V3_2_Labo_Contraste")
    compile_pdf(HTML_M3, "Maquette_V3_3_Maitre_Tourier")
