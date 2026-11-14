#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur des 3 Maquettes de Design pour le Cahier de Production Boulangerie.
Double-page A4 (Page Gauche = Pesée & Lancement, Page Droite = Conduite & Cuisson)
sur la Fiche 01 (Recette Maîtresse PLF Commune).
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
# MAQUETTE A : CHRONO LABO (Cockpit de production, gros chiffres, blocs phases)
# ==============================================================================
HTML_MAQUETTE_A = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Maquette A - Chrono Labo</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
@page { size: A4 portrait; margin: 12mm 12mm 12mm 14mm; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
body { font-family: "Inter", sans-serif; color: #09090b; margin: 0; font-size: 9pt; line-height: 1.3; font-variant-numeric: tabular-nums; }
.sheet { height: 272mm; display: flex; flex-direction: column; justify-content: space-between; page-break-after: always; overflow: hidden; }
.sheet:last-child { page-break-after: auto; }

/* Header Cockpit */
.cockpit-head { display: flex; justify-content: space-between; align-items: stretch; border-bottom: 3px solid #09090b; padding-bottom: 3mm; margin-bottom: 3.5mm; }
.ch-left { display: flex; flex-direction: column; justify-content: center; }
.ch-kicker { font-size: 7.5pt; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase; color: #2563eb; margin-bottom: 1mm; }
.ch-title { font-size: 20pt; font-weight: 900; letter-spacing: -0.02em; line-height: 1.05; margin: 0; }
.ch-sub { font-size: 8.5pt; color: #52525b; font-weight: 600; margin-top: 1.5mm; }
.ch-badge { background: #09090b; color: #fff; padding: 3mm 5mm; border-radius: 4px; display: flex; flex-direction: column; justify-content: center; align-items: flex-end; min-width: 44mm; }
.ch-badge-top { font-size: 7pt; font-weight: 700; color: #93c5fd; text-transform: uppercase; letter-spacing: 0.08em; }
.ch-badge-main { font-size: 13pt; font-weight: 900; margin-top: 0.5mm; }

/* Barre de lancement 4 tuiles */
.launch-bar { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2.5mm; margin-bottom: 4mm; }
.l-tile { background: #f4f4f5; border-left: 3.5px solid #2563eb; padding: 2.5mm 3mm; border-radius: 2px; }
.l-tile.amber { border-left-color: #d97706; }
.l-tile.green { border-left-color: #16a34a; }
.l-tile.dark { border-left-color: #09090b; background: #e4e4e7; }
.l-val { font-size: 14pt; font-weight: 900; color: #09090b; line-height: 1.1; }
.l-lbl { font-size: 6.8pt; font-weight: 700; text-transform: uppercase; color: #52525b; margin-top: 1mm; letter-spacing: 0.04em; }

/* Tableau de pesée orienté balance */
.pesee-table { width: 100%; border-collapse: collapse; }
.pesee-table th { font-size: 7.2pt; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; color: #52525b; border-bottom: 2px solid #09090b; padding: 2mm 2mm; text-align: left; }
.pesee-table th.num { text-align: right; }
.pesee-table th.main-col { color: #1d4ed8; font-size: 8pt; background: #eff6ff; }
.pesee-table td { padding: 2.1mm 2mm; border-bottom: 1px solid #e4e4e7; font-size: 9pt; vertical-align: middle; }
.pesee-table td.chk { width: 7mm; text-align: center; font-size: 11pt; color: #a1a1aa; }
.pesee-table td.ing { font-weight: 600; color: #18181b; }
.pesee-table td.ing small { font-weight: 500; color: #71717a; font-size: 7.8pt; }
.pesee-table td.main-qty { text-align: right; font-size: 12pt; font-weight: 900; color: #09090b; background: #eff6ff; padding-right: 3mm; }
.pesee-table td.sub-qty { text-align: right; font-size: 9pt; font-weight: 600; color: #52525b; }

.phase-band td { background: #18181b; color: #ffffff; font-size: 7.8pt; font-weight: 800; letter-spacing: 0.06em; text-transform: uppercase; padding: 1.6mm 2.5mm; border: none; }
.phase-band.p1 td { background: #1e40af; }
.phase-band.p2 td { background: #b45309; }
.phase-band.p3 td { background: #15803d; }

.row-stot td { background: #f4f4f5; font-weight: 800; border-top: 1.5px solid #a1a1aa; border-bottom: 1.5px solid #a1a1aa; }
.row-stot td.main-qty { background: #dbeafe; font-size: 12pt; color: #1e3a8a; }
.row-tot td { background: #09090b; color: #ffffff; font-weight: 900; font-size: 10pt; padding: 2.8mm 2mm; }
.row-tot td.main-qty { background: #2563eb; color: #ffffff; font-size: 13.5pt; }
.row-tot td.sub-qty { color: #e4e4e7; font-weight: 800; }

/* Page droite : Timeline chrono */
.timeline { display: flex; flex-direction: column; gap: 3.5mm; flex: 1; }
.tl-block { border: 1.5px solid #d4d4d8; border-radius: 5px; overflow: hidden; }
.tl-head { background: #18181b; color: #ffffff; padding: 2mm 3.5mm; display: flex; justify-content: space-between; align-items: center; }
.tl-head.blue { background: #1e40af; }
.tl-head.green { background: #15803d; }
.tl-head-title { font-size: 10pt; font-weight: 800; letter-spacing: 0.03em; text-transform: uppercase; }
.tl-head-kpi { font-size: 8.5pt; font-weight: 800; background: rgba(255,255,255,0.18); padding: 0.8mm 2.5mm; border-radius: 3px; }
.tl-rows { display: flex; flex-direction: column; }
.tl-row { display: grid; grid-template-columns: 36mm 1fr; border-bottom: 1px solid #e4e4e7; }
.tl-row:last-child { border-bottom: none; }
.tl-metric { background: #f8fafc; padding: 2.5mm 3mm; border-right: 1px solid #e4e4e7; display: flex; flex-direction: column; justify-content: center; }
.tl-m-val { font-size: 12pt; font-weight: 900; color: #09090b; line-height: 1.1; }
.tl-m-lbl { font-size: 7pt; font-weight: 700; text-transform: uppercase; color: #64748b; margin-top: 0.5mm; }
.tl-action { padding: 2.5mm 3.5mm; display: flex; flex-direction: column; justify-content: center; font-size: 8.8pt; color: #27272a; }
.tl-action strong.step-name { color: #09090b; font-size: 9.2pt; display: block; margin-bottom: 0.5mm; }

.alert-banner { background: #dc2626; color: #ffffff; padding: 2.8mm 4mm; border-radius: 4px; font-weight: 900; font-size: 8.8pt; text-align: center; text-transform: uppercase; letter-spacing: 0.03em; margin-top: 2mm; }
.foot { display: flex; justify-content: space-between; font-size: 7.5pt; font-weight: 700; color: #71717a; border-top: 1px solid #d4d4d8; padding-top: 2mm; margin-top: 2mm; }
</style>
</head>
<body>
<!-- PAGE GAUCHE -->
<div class="sheet">
  <div>
    <div class="cockpit-head">
      <div class="ch-left">
        <div class="ch-kicker">PÔLE 1 • PÂTE LEVÉE FEUILLETÉE • MAQUETTE A « CHRONO LABO »</div>
        <h1 class="ch-title">PLF COMMUNE — PESÉE</h1>
        <div class="ch-sub">Codes V-PLF-01 à 07 • Tourage unifié 1D + 1S (12 films de beurre)</div>
      </div>
      <div class="ch-badge">
        <span class="ch-badge-top">FORMAT STANDARD</span>
        <span class="ch-badge-main">1 BAC = 10 KG</span>
      </div>
    </div>

    <div class="launch-bar">
      <div class="l-tile"><div class="l-val">8 000 g</div><div class="l-lbl">Détrempe / Bac Paneo</div></div>
      <div class="l-tile amber"><div class="l-val">2 000 g</div><div class="l-lbl">1 Plaque Debic 82%</div></div>
      <div class="l-tile green"><div class="l-val">20–21 °C</div><div class="l-lbl">Sortie Pétrin Cible</div></div>
      <div class="l-tile dark"><div class="l-val">3 cm</div><div class="l-lbl">Pré-laminage Bac</div></div>
    </div>

    <table class="pesee-table">
      <thead>
        <tr>
          <th style="width:7mm"></th>
          <th>Ingrédient à peser</th>
          <th class="num main-col">1 BAC (10 kg)</th>
          <th class="num">10 BACS (100 kg)</th>
          <th class="num">20 BACS (200 kg)</th>
        </tr>
      </thead>
      <tbody>
        <tr class="phase-band p1"><td colspan="5">1 • DÉTREMPAGE CUVE V1 (FRASAGE 5 MIN)</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Farine Gruau Rouge T45</td><td class="main-qty">3 130 g</td><td class="sub-qty">31 300 g</td><td class="sub-qty">62 600 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Farine T65 Tradition pure</td><td class="main-qty">1 340 g</td><td class="sub-qty">13 400 g</td><td class="sub-qty">26 800 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Eau glacée (+1 °C) / Glace écaille</td><td class="main-qty">2 015 g</td><td class="sub-qty">20 150 g</td><td class="sub-qty">40 300 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Sucre cristal blanc</td><td class="main-qty">394 g</td><td class="sub-qty">3 940 g</td><td class="sub-qty">7 880 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Trimoline <small>(sucre inverti)</small></td><td class="main-qty">157 g</td><td class="sub-qty">1 570 g</td><td class="sub-qty">3 140 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Levure fraîche L'Hirondelle Or</td><td class="main-qty">188 g</td><td class="sub-qty">1 880 g</td><td class="sub-qty">3 760 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Poudre de lait entier 26 % MG</td><td class="main-qty">180 g</td><td class="sub-qty">1 800 g</td><td class="sub-qty">3 600 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Améliorant S500 Kimo Short</td><td class="main-qty">90 g</td><td class="sub-qty">900 g</td><td class="sub-qty">1 800 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Sel fin d'atelier</td><td class="main-qty">90 g</td><td class="sub-qty">900 g</td><td class="sub-qty">1 800 g</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Vinaigre blanc d'alcool 8°</td><td class="main-qty">36 g</td><td class="sub-qty">360 g</td><td class="sub-qty">720 g</td></tr>

        <tr class="phase-band p2"><td colspan="5">2 • INCORPORATION CUVE V2 (4 MIN 30 À 5 MIN MAX)</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Margarine OPAL cuve <small>(morceaux 500 g)</small></td><td class="main-qty">380 g</td><td class="sub-qty">3 800 g</td><td class="sub-qty">7 600 g</td></tr>
        <tr class="row-stot"><td></td><td>SOUS-TOTAL DÉTREMPE NETTE</td><td class="main-qty">8 000 g</td><td class="sub-qty">80 000 g</td><td class="sub-qty">160 000 g</td></tr>

        <tr class="phase-band p3"><td colspan="5">3 • TOURAGE J+1 (ENCHÂSSEMENT PORTEFEUILLE)</td></tr>
        <tr><td class="chk">☐</td><td class="ing">Beurre Debic Croissant 82 % <small>(12–14 °C)</small></td><td class="main-qty">2 000 g</td><td class="sub-qty">20 000 g</td><td class="sub-qty">40 000 g</td></tr>
        <tr class="row-tot"><td></td><td>POIDS TOTAL PÂTON TOURÉ</td><td class="main-qty">10 000 g</td><td class="sub-qty">100 000 g</td><td class="sub-qty">200 000 g</td></tr>
      </tbody>
    </table>
  </div>
  <div class="foot"><span>01 — RECETTE MAÎTRESSE PLF COMMUNE • POSTE DE PESÉE</span><span>PAGE 4 / 37</span></div>
</div>

<!-- PAGE DROITE -->
<div class="sheet">
  <div style="display:flex; flex-direction:column; flex:1;">
    <div class="cockpit-head">
      <div class="ch-left">
        <div class="ch-kicker" style="color:#16a34a;">CONDUITE MACHINE • TOURAGE • CIRCUIT PAC</div>
        <h1 class="ch-title">PLF COMMUNE — CONDUITE</h1>
        <div class="ch-sub">Séquence chronologique de J-1 (Pétrin) à Expédition Boutiques</div>
      </div>
      <div class="ch-badge" style="background:#15803d;">
        <span class="ch-badge-top" style="color:#dcfce7;">CIRCUIT PAC</span>
        <span class="ch-badge-main">J-1 → J → BOUTIQUE</span>
      </div>
    </div>

    <div class="timeline">
      <div class="tl-block">
        <div class="tl-head blue"><span class="tl-head-title">1. Pétrissage &amp; Blocage J-1</span><span class="tl-head-kpi">SORTIE 20–21 °C</span></div>
        <div class="tl-rows">
          <div class="tl-row">
            <div class="tl-metric"><span class="tl-m-val">5 min V1</span><span class="tl-m-lbl">Frasage</span></div>
            <div class="tl-action"><strong class="step-name">Mélange base [1]</strong>Verser tous les ingrédients [1] dans le pétrin spirale. Tourner 5 min en 1re vitesse.</div>
          </div>
          <div class="tl-row">
            <div class="tl-metric"><span class="tl-m-val">4'30–5' V2</span><span class="tl-m-lbl">Décollement net</span></div>
            <div class="tl-action"><strong class="step-name">Incorporation OPAL [2]</strong>Passer en V2 avec la margarine OPAL en dés de 500 g. Stopper dès décollement net (sans chercher le voile).</div>
          </div>
          <div class="tl-row">
            <div class="tl-metric"><span class="tl-m-val">35 min / -35°C</span><span class="tl-m-lbl">Puis 0/+1,5 °C</span></div>
            <div class="tl-action"><strong class="step-name">Bacs Paneo &amp; Pointage Nuit</strong>Diviser en bacs de <strong>8 000 g pile</strong>, étaler à 3 cm. Flash -35 °C (cœur &lt; 6 °C), puis 12–15 h à 0/+1,5 °C.</div>
          </div>
        </div>
      </div>

      <div class="tl-block">
        <div class="tl-head"><span class="tl-head-title">2. Tourage Unifié (1D + 1S)</span><span class="tl-head-kpi">12 FILMS BEURRE</span></div>
        <div class="tl-rows">
          <div class="tl-row">
            <div class="tl-metric"><span class="tl-m-val">12–14 °C</span><span class="tl-m-lbl">Beurre Debic</span></div>
            <div class="tl-action"><strong class="step-name">Enchâssement Portefeuille</strong>Détrempe froide (+2/+4 °C) + plaque 2 000 g Debic à 12–14 °C. Fermer bord à bord sans chevauchement.</div>
          </div>
          <div class="tl-row">
            <div class="tl-metric"><span class="tl-m-val">1D + 1S</span><span class="tl-m-lbl">Sans pause</span></div>
            <div class="tl-action"><strong class="step-name">Enchaîner Tour Double + Tour Simple</strong>Allonger, plier en 4, pivoter 90°, allonger, plier en 3. Parer les 4 chants au couteau.</div>
          </div>
          <div class="tl-row">
            <div class="tl-metric"><span class="tl-m-val">45 min +2 °C</span><span class="tl-m-lbl">Détente filmée</span></div>
            <div class="tl-action"><strong class="step-name">Repos avant abaisse</strong>Filmer hermétiquement et laisser détendre 45 min à +2 °C avant laminage final.</div>
          </div>
        </div>
      </div>

      <div class="tl-block">
        <div class="tl-head green"><span class="tl-head-title">3. Abaisse &amp; Double Congélation PAC</span><span class="tl-head-kpi">SONDE -10 °C</span></div>
        <div class="tl-rows">
          <div class="tl-row">
            <div class="tl-metric"><span class="tl-m-val">≥ 60 sec</span><span class="tl-m-lbl">Décompression</span></div>
            <div class="tl-action"><strong class="step-name">Polyline &amp; Détente Tapis</strong>Dérouler face farinée en dessous (dessus nu pour soudure). Laisser flotter ≥ 60 s avant coupe.</div>
          </div>
          <div class="tl-row">
            <div class="tl-metric"><span class="tl-m-val">70–75 % vol</span><span class="tl-m-lbl">2h15–2h30 étuve</span></div>
            <div class="tl-action"><strong class="step-name">Stock 1 Cru → Étuve → Stock 2 PAC</strong>Stock 1 : flash -35 °C → -18 °C. PAC : décongélation +2/+4 °C (10–12 h) → étuve 25–26 °C / 75–80 % HR → ressuyage 15 min +4 °C → dorure pistolet 1,5 bar → flash -35 °C (arrêt -10 °C cœur).</div>
          </div>
        </div>
      </div>
    </div>

    <div class="alert-banner">CRITIQUE PAC : NE JAMAIS DÉPASSER 75 % DE POUSSE EN ÉTUVE — ARRÊT FLASH STRICT À -10 °C SONDE CŒUR</div>
  </div>
  <div class="foot"><span>01 — RECETTE MAÎTRESSE PLF COMMUNE • CONDUITE &amp; CUISSON</span><span>PAGE 5 / 37</span></div>
</div>
</body>
</html>"""


# ==============================================================================
# MAQUETTE B : POSTE & COULEUR (3 Seaux séparés, Onglet latéral, Flux 4 colonnes)
# ==============================================================================
HTML_MAQUETTE_B = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Maquette B - Poste & Couleur</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800&family=JetBrains+Mono:wght@600;800&display=swap');
@page { size: A4 portrait; margin: 11mm 12mm 11mm 14mm; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
body { font-family: "DM Sans", sans-serif; color: #0f172a; margin: 0; font-size: 8.6pt; line-height: 1.3; font-variant-numeric: tabular-nums; }
.sheet { height: 274mm; display: flex; gap: 4mm; page-break-after: always; overflow: hidden; }
.sheet:last-child { page-break-after: auto; }

/* Onglet latéral vertical */
.side-rail { width: 10mm; border-radius: 4px; background: #1d4ed8; color: #ffffff; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.side-rail.green { background: #047857; }
.side-rail span { writing-mode: vertical-rl; transform: rotate(180deg); font-size: 8.5pt; font-weight: 800; letter-spacing: 0.18em; text-transform: uppercase; white-space: nowrap; }

.main-col { flex: 1; display: flex; flex-direction: column; justify-content: space-between; }

/* Header */
.b-head { display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 2px solid #cbd5e1; padding-bottom: 2.5mm; margin-bottom: 3.5mm; }
.b-num { font-family: "JetBrains Mono", monospace; font-size: 9pt; font-weight: 800; color: #1d4ed8; }
.b-title { font-size: 18pt; font-weight: 800; letter-spacing: -0.02em; margin: 0.5mm 0 0 0; line-height: 1.05; }
.b-meta { font-size: 8pt; color: #475569; margin-top: 1mm; }
.b-pill { background: #eff6ff; border: 1.5px solid #1d4ed8; color: #1e40af; padding: 1.8mm 3.5mm; border-radius: 99px; font-weight: 800; font-size: 8.5pt; white-space: nowrap; }

/* 3 Blocs-Seaux séparés */
.bucket { border: 1.5px solid #cbd5e1; border-radius: 5px; margin-bottom: 3mm; overflow: hidden; }
.bucket.blue { border-color: #93c5fd; }
.bucket.amber { border-color: #fcd34d; }
.bucket.green { border-color: #6ee7b7; }
.bucket-head { padding: 1.8mm 3mm; font-size: 8pt; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; display: flex; justify-content: space-between; }
.bucket.blue .bucket-head { background: #dbeafe; color: #1e3a8a; }
.bucket.amber .bucket-head { background: #fef3c7; color: #92400e; }
.bucket.green .bucket-head { background: #d1fae5; color: #065f46; }

.b-tbl { width: 100%; border-collapse: collapse; }
.b-tbl th { font-size: 6.8pt; text-transform: uppercase; color: #64748b; padding: 1.5mm 2.5mm; text-align: left; border-bottom: 1px solid #e2e8f0; background: #f8fafc; }
.b-tbl th.r, .b-tbl td.r { text-align: right; }
.b-tbl td { padding: 1.7mm 2.5mm; border-bottom: 1px solid #f1f5f9; font-size: 8.8pt; }
.b-tbl tr:nth-child(even) td { background: #fafafa; }
.b-tbl td.qty1 { font-family: "JetBrains Mono", monospace; font-weight: 800; font-size: 10.5pt; color: #0f172a; text-align: right; background: #f8fafc !important; }
.b-tbl td.qty2 { font-family: "JetBrains Mono", monospace; font-weight: 600; font-size: 8.5pt; color: #475569; text-align: right; }

.total-strip { background: #0f172a; color: #ffffff; border-radius: 5px; padding: 2.8mm 4mm; display: flex; justify-content: space-between; align-items: center; }
.ts-lbl { font-size: 9pt; font-weight: 800; text-transform: uppercase; letter-spacing: 0.04em; }
.ts-vals { display: flex; gap: 6mm; font-family: "JetBrains Mono", monospace; }
.ts-v { text-align: right; }
.ts-v small { display: block; font-size: 6.5pt; color: #94a3b8; font-family: "DM Sans", sans-serif; }
.ts-v strong { font-size: 12pt; color: #60a5fa; }

/* Page droite : Modules asymétriques */
.mod-2col { display: grid; grid-template-columns: 1fr 1fr; gap: 3.5mm; margin-bottom: 3.5mm; }
.mod-box { border: 1.5px solid #cbd5e1; border-radius: 5px; padding: 3mm; background: #ffffff; }
.mod-title { font-size: 8.8pt; font-weight: 800; text-transform: uppercase; color: #047857; border-bottom: 2px solid #047857; padding-bottom: 1.2mm; margin-bottom: 2.5mm; display: flex; justify-content: space-between; }
.mod-step { margin-bottom: 2.2mm; }
.mod-step:last-child { margin-bottom: 0; }
.mod-step-h { font-weight: 800; font-size: 8.6pt; color: #0f172a; }
.mod-step-p { font-size: 8.2pt; color: #334155; margin-top: 0.4mm; }
.tag-val { display: inline-block; background: #f1f5f9; border: 1px solid #cbd5e1; font-family: "JetBrains Mono", monospace; font-weight: 800; font-size: 7.8pt; padding: 0.2mm 1.5mm; border-radius: 3px; color: #0f172a; }

/* Flux horizontal 4 étapes */
.flow-box { border: 1.5px solid #cbd5e1; border-radius: 5px; padding: 3mm; background: #f8fafc; margin-bottom: 3.5mm; }
.flow-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2.5mm; margin-top: 2mm; }
.flow-card { background: #ffffff; border: 1px solid #cbd5e1; border-top: 3px solid #047857; border-radius: 4px; padding: 2.5mm; }
.flow-num { font-family: "JetBrains Mono", monospace; font-size: 11pt; font-weight: 800; color: #047857; }
.flow-t { font-weight: 800; font-size: 8.4pt; margin: 1mm 0; color: #0f172a; }
.flow-d { font-size: 7.8pt; color: #475569; line-height: 1.28; }

.b-alert { background: #fef2f2; border: 2px solid #ef4444; border-left-width: 6px; border-radius: 4px; padding: 2.8mm 3.5mm; color: #991b1b; font-weight: 800; font-size: 8.3pt; }
.b-foot { display: flex; justify-content: space-between; font-size: 7.4pt; color: #64748b; font-weight: 700; margin-top: 2mm; }
</style>
</head>
<body>
<!-- PAGE GAUCHE -->
<div class="sheet">
  <div class="side-rail"><span>POSTE DE PESÉE • BAC PAR BAC</span></div>
  <div class="main-col">
    <div>
      <div class="b-head">
        <div>
          <div class="b-num">FICHE 01 • MAQUETTE B « POSTE &amp; COULEUR »</div>
          <h1 class="b-title">Pâte Levée Feuilletée Commune</h1>
          <div class="b-meta">Codes V-PLF-01 à 07 • Répartition physique en 3 préparations distinctes</div>
        </div>
        <div class="b-pill">1 BAC = 10 KG TOURÉ</div>
      </div>

      <div class="bucket blue">
        <div class="bucket-head"><span>BAC / CUVE 1 — FRASAGE V1 (5 MIN)</span><span>À PESER ENSEMBLE</span></div>
        <table class="b-tbl">
          <thead><tr><th>Ingrédient</th><th class="r">1 Bac</th><th class="r">10 Bacs</th><th class="r">20 Bacs</th></tr></thead>
          <tbody>
            <tr><td>Farine Gruau Rouge T45</td><td class="qty1">3 130 g</td><td class="qty2">31 300 g</td><td class="qty2">62 600 g</td></tr>
            <tr><td>Farine T65 Tradition pure</td><td class="qty1">1 340 g</td><td class="qty2">13 400 g</td><td class="qty2">26 800 g</td></tr>
            <tr><td>Eau glacée (+1 °C) / Glace écaille</td><td class="qty1">2 015 g</td><td class="qty2">20 150 g</td><td class="qty2">40 300 g</td></tr>
            <tr><td>Sucre cristal blanc</td><td class="qty1">394 g</td><td class="qty2">3 940 g</td><td class="qty2">7 880 g</td></tr>
            <tr><td>Trimoline (sucre inverti)</td><td class="qty1">157 g</td><td class="qty2">1 570 g</td><td class="qty2">3 140 g</td></tr>
            <tr><td>Levure fraîche L'Hirondelle Or</td><td class="qty1">188 g</td><td class="qty2">1 880 g</td><td class="qty2">3 760 g</td></tr>
            <tr><td>Poudre de lait entier 26 % MG</td><td class="qty1">180 g</td><td class="qty2">1 800 g</td><td class="qty2">3 600 g</td></tr>
            <tr><td>Améliorant S500 Kimo Short</td><td class="qty1">90 g</td><td class="qty2">900 g</td><td class="qty2">1 800 g</td></tr>
            <tr><td>Sel fin d'atelier</td><td class="qty1">90 g</td><td class="qty2">900 g</td><td class="qty2">1 800 g</td></tr>
            <tr><td>Vinaigre blanc d'alcool 8°</td><td class="qty1">36 g</td><td class="qty2">360 g</td><td class="qty2">720 g</td></tr>
          </tbody>
        </table>
      </div>

      <div class="bucket amber">
        <div class="bucket-head"><span>BAC 2 — AJOUT PÉTRISSAGE V2 (4'30–5')</span><span>MORCEAUX 500 G</span></div>
        <table class="b-tbl">
          <tbody>
            <tr><td>Margarine OPAL cuve</td><td class="qty1">380 g</td><td class="qty2">3 800 g</td><td class="qty2">7 600 g</td></tr>
            <tr><td><strong>Sous-total Détrempe nette / bac Paneo</strong></td><td class="qty1" style="color:#b45309;">8 000 g</td><td class="qty2"><strong>80 000 g</strong></td><td class="qty2"><strong>160 000 g</strong></td></tr>
          </tbody>
        </table>
      </div>

      <div class="bucket green">
        <div class="bucket-head"><span>POSTE LAMINOIR — TOURAGE J+1 (1D + 1S)</span><span>12–14 °C</span></div>
        <table class="b-tbl">
          <tbody>
            <tr><td>Beurre Debic Croissant 82 % (1 plaque)</td><td class="qty1">2 000 g</td><td class="qty2">20 000 g</td><td class="qty2">40 000 g</td></tr>
          </tbody>
        </table>
      </div>

      <div class="total-strip">
        <span class="ts-lbl">Masse Totale Pâton Touré Net</span>
        <div class="ts-vals">
          <div class="ts-v"><small>1 BAC</small><strong>10 000 g</strong></div>
          <div class="ts-v"><small>10 BACS</small><strong>100 000 g</strong></div>
          <div class="ts-v"><small>20 BACS</small><strong>200 000 g</strong></div>
        </div>
      </div>
    </div>
    <div class="b-foot"><span>PLF COMMUNE • POSTE DE PESÉE</span><span>4 / 37</span></div>
  </div>
</div>

<!-- PAGE DROITE -->
<div class="sheet">
  <div class="side-rail green"><span>CONDUITE MACHINE &amp; CIRCUIT PAC</span></div>
  <div class="main-col">
    <div>
      <div class="b-head">
        <div>
          <div class="b-num" style="color:#047857;">FICHE 01 • CONDUITE OPÉRATOIRE</div>
          <h1 class="b-title">Pétrissage, Tourage &amp; Circuit PAC</h1>
          <div class="b-meta">Lecture par poste : Pétrin (J-1) → Laminoir (J) → Étuve &amp; Cellule Flash</div>
        </div>
        <div class="b-pill" style="border-color:#047857; color:#065f46; background:#ecfdf5;">SORTIE 20–21 °C</div>
      </div>

      <div class="mod-2col">
        <div class="mod-box">
          <div class="mod-title"><span>A. Pétrissage J-1</span><span>PÉTRIN SPIRALE</span></div>
          <div class="mod-step"><div class="mod-step-h">1. Frasage <span class="tag-val">5 min V1</span></div><div class="mod-step-p">Tous les ingrédients du Bac 1 dans la cuve.</div></div>
          <div class="mod-step"><div class="mod-step-h">2. Pétrissage <span class="tag-val">4'30–5' V2</span></div><div class="mod-step-p">Ajouter OPAL (morceaux 500 g). Stopper au 1er décollement net des parois (zéro voile étiré).</div></div>
          <div class="mod-step"><div class="mod-step-h">3. Bacs Paneo <span class="tag-val">8 000 g / 3 cm</span></div><div class="mod-step-p">Diviser immédiatement et pré-laminer à 3 cm.</div></div>
          <div class="mod-step"><div class="mod-step-h">4. Refroidissement <span class="tag-val">-35 °C 35 min</span></div><div class="mod-step-p">Cœur &lt; 6 °C, puis pointage 12–15 h à 0/+1,5 °C.</div></div>
        </div>

        <div class="mod-box">
          <div class="mod-title"><span>B. Tourage J (1D + 1S)</span><span>LAMINOIR</span></div>
          <div class="mod-step"><div class="mod-step-h">1. Enchâssement <span class="tag-val">+2/+4 °C vs 12–14 °C</span></div><div class="mod-step-p">Détrempe froide, beurre Debic 2 000 g souple. Fermer portefeuille bord à bord.</div></div>
          <div class="mod-step"><div class="mod-step-h">2. 1er Tour Double <span class="tag-val">Pliage en 4</span></div><div class="mod-step-p">Allonger, plier en 4 (portefeuille), pivoter 90°.</div></div>
          <div class="mod-step"><div class="mod-step-h">3. 2e Tour Simple <span class="tag-val">Pliage en 3</span></div><div class="mod-step-p">Allonger dans le nouveau sens, plier en 3 (12 films).</div></div>
          <div class="mod-step"><div class="mod-step-h">4. Drossage &amp; Détente <span class="tag-val">45 min +2 °C</span></div><div class="mod-step-p">Couper les 4 chants fermés au couteau, filmer.</div></div>
        </div>
      </div>

      <div class="flow-box">
        <div class="mod-title" style="margin-bottom:1.5mm;"><span>C. Flux Abaisse → Double Congélation PAC</span><span>POLYLINE / ÉTUVE / FLASH</span></div>
        <div class="flow-grid">
          <div class="flow-card"><div class="flow-num">01</div><div class="flow-t">Déroulage Polyline</div><div class="flow-d">Côté fariné sur tapis, face supérieure <strong>nue sans farine</strong> (soudure). Flotter <strong>≥ 60 s</strong> avant coupe.</div></div>
          <div class="flow-card"><div class="flow-num">02</div><div class="flow-t">Stock 1 (Cru)</div><div class="flow-d">Plaquer serré. Flash <strong>-35 °C (35–40 min)</strong>, puis caisses étanches à <strong>-18 °C</strong>.</div></div>
          <div class="flow-card"><div class="flow-num">03</div><div class="flow-t">Décong. &amp; Étuve</div><div class="flow-d">Nuit +2/+4 °C (10–12 h). Étuve <strong>25–26 °C / 75–80 % HR</strong> 2h15–2h30 (<strong>arrêt 70–75 % vol</strong>).</div></div>
          <div class="flow-card"><div class="flow-num">04</div><div class="flow-t">Dorure &amp; Stock 2</div><div class="flow-d">Ressuyage 15' (+4 °C), Dorure Végétale pistolet (1,5 bar), flash <strong>-35 °C → sonde -10 °C</strong>.</div></div>
        </div>
      </div>

      <div class="b-alert">POINT DE RUPTURE CRITIQUE : NE JAMAIS SUR-PÉTRIR EN V2 (VOILE INTERDIT) • ARRÊT STRICT DE L'ÉTUVE À 70–75 % DU VOLUME • SONDE FLASH STRICTEMENT À -10 °C AVANT MISE EN CAISSE -18 °C.</div>
    </div>
    <div class="b-foot"><span>PLF COMMUNE • CONDUITE &amp; CIRCUIT PAC</span><span>5 / 37</span></div>
  </div>
</div>
</body>
</html>"""


# ==============================================================================
# MAQUETTE C : ARTISAN ÉDITORIAL (Chaleureux, Aéré, Mémo Express + Liste d'actions)
# ==============================================================================
HTML_MAQUETTE_C = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Maquette C - Artisan Editorial</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
@page { size: A4 portrait; margin: 13mm 14mm 13mm 16mm; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
body { font-family: "Inter", sans-serif; color: #1c1917; background: #ffffff; margin: 0; font-size: 8.8pt; line-height: 1.38; font-variant-numeric: tabular-nums; }
.sheet { height: 270mm; display: flex; flex-direction: column; justify-content: space-between; page-break-after: always; overflow: hidden; }
.sheet:last-child { page-break-after: auto; }

/* Header Éditorial chaud */
.ed-head { border-bottom: 2px solid #b45309; padding-bottom: 3mm; margin-bottom: 4.5mm; display: flex; justify-content: space-between; align-items: flex-end; }
.ed-kicker { font-size: 7.5pt; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #b45309; margin-bottom: 1mm; }
.ed-title { font-size: 19pt; font-weight: 800; color: #1c1917; letter-spacing: -0.02em; margin: 0; line-height: 1.08; }
.ed-tag { background: #fef3c7; color: #92400e; border: 1px solid #f59e0b; padding: 1.5mm 3.5mm; border-radius: 3px; font-size: 8pt; font-weight: 800; letter-spacing: 0.04em; }

/* Layout 2 colonnes Page Gauche : Mémo Express + Pesée */
.ed-split { display: grid; grid-template-columns: 44mm 1fr; gap: 5mm; align-items: start; }
.memo-box { background: #faf8f5; border: 1px solid #e7e5e4; border-top: 3px solid #b45309; border-radius: 4px; padding: 3mm; }
.memo-h { font-size: 7.5pt; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; color: #b45309; margin-bottom: 2.5mm; }
.memo-item { border-bottom: 1px dashed #d6d3d1; padding: 2mm 0; }
.memo-item:last-child { border-bottom: none; padding-bottom: 0; }
.memo-v { font-size: 12.5pt; font-weight: 800; color: #1c1917; line-height: 1.1; }
.memo-l { font-size: 7pt; color: #78716c; font-weight: 600; text-transform: uppercase; margin-top: 0.5mm; }

/* Tableau aéré */
.ed-tbl { width: 100%; border-collapse: collapse; }
.ed-tbl th { font-size: 7pt; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; color: #78716c; border-bottom: 1.5px solid #1c1917; padding: 1.8mm 2mm; text-align: left; }
.ed-tbl th.r, .ed-tbl td.r { text-align: right; }
.ed-tbl td { padding: 2.1mm 2mm; border-bottom: 1px solid #f5f5f4; font-size: 8.6pt; }
.ed-tbl td.w1 { text-align: right; font-weight: 800; font-size: 10.5pt; color: #1c1917; background: #faf8f5; }
.ed-tbl td.w2 { text-align: right; font-weight: 600; color: #57534e; }
.ed-sec td { padding-top: 3mm; font-size: 7.4pt; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; color: #b45309; border-bottom: 1px solid #fed7aa; background: #fffbeb; }
.ed-stot td { background: #f5f5f4; font-weight: 700; border-top: 1px solid #d6d3d1; border-bottom: 1px solid #d6d3d1; }
.ed-tot td { background: #1c1917; color: #ffffff; font-weight: 800; font-size: 9.5pt; padding: 2.5mm 2mm; }
.ed-tot td.w1 { background: #b45309; color: #ffffff; font-size: 11.5pt; }

/* Page droite : Chapitres aérés numérotés */
.chap { margin-bottom: 4.5mm; }
.chap-head { display: flex; align-items: baseline; gap: 3mm; border-bottom: 1px solid #e7e5e4; padding-bottom: 1.5mm; margin-bottom: 2.5mm; }
.chap-num { font-size: 15pt; font-weight: 800; color: #b45309; line-height: 1; }
.chap-title { font-size: 10.5pt; font-weight: 800; text-transform: uppercase; letter-spacing: 0.03em; color: #1c1917; }
.chap-sub { margin-left: auto; font-size: 7.8pt; font-weight: 700; color: #15803d; background: #f0fdf4; padding: 0.6mm 2.2mm; border-radius: 3px; border: 1px solid #bbf7d0; }

.act-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 2mm; }
.act-list li { display: grid; grid-template-columns: 32mm 1fr; gap: 3mm; background: #faf8f5; padding: 2mm 3mm; border-radius: 3px; border-left: 2.5px solid #d6d3d1; }
.act-list li.key { border-left-color: #b45309; }
.act-k { font-weight: 800; font-size: 8.2pt; color: #1c1917; }
.act-v { font-size: 8.4pt; color: #44403c; }

.gold-rule { background: #fffbeb; border: 1px solid #f59e0b; border-left: 4px solid #b45309; border-radius: 4px; padding: 3mm 4mm; margin-top: auto; }
.gold-rule-h { font-size: 7.5pt; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; color: #b45309; margin-bottom: 1mm; }
.gold-rule-p { font-size: 8.6pt; font-weight: 700; color: #78350f; margin: 0; }

.ed-foot { display: flex; justify-content: space-between; font-size: 7.5pt; color: #78716c; border-top: 1px solid #e7e5e4; padding-top: 2mm; margin-top: 3mm; }
</style>
</head>
<body>
<!-- PAGE GAUCHE -->
<div class="sheet">
  <div>
    <div class="ed-head">
      <div>
        <div class="ed-kicker">FICHE 01 • MAQUETTE C « ARTISAN ÉDITORIAL »</div>
        <h1 class="ed-title">Pâte Levée Feuilletée Commune</h1>
      </div>
      <div class="ed-tag">POSTE DE PESÉE</div>
    </div>

    <div class="ed-split">
      <div class="memo-box">
        <div class="memo-h">Mémo Express</div>
        <div class="memo-item"><div class="memo-v">8 000 g</div><div class="memo-l">Détrempe / Bac Paneo</div></div>
        <div class="memo-item"><div class="memo-v">2 000 g</div><div class="memo-l">Beurre Debic / Bac</div></div>
        <div class="memo-item"><div class="memo-v">20–21 °C</div><div class="memo-l">Sortie Pétrin Cible</div></div>
        <div class="memo-item"><div class="memo-v">1D + 1S</div><div class="memo-l">Tourage (12 films)</div></div>
        <div class="memo-item"><div class="memo-v">-10 °C</div><div class="memo-l">Sonde cœur fin PAC</div></div>
      </div>

      <table class="ed-tbl">
        <thead>
          <tr><th>Ingrédient</th><th class="r">1 Bac (10 kg)</th><th class="r">10 Bacs</th><th class="r">20 Bacs</th></tr>
        </thead>
        <tbody>
          <tr class="ed-sec"><td colspan="4">Phase 1 • Base Cuve V1 (5 min)</td></tr>
          <tr><td>Farine Gruau Rouge T45</td><td class="w1">3 130 g</td><td class="w2">31 300 g</td><td class="w2">62 600 g</td></tr>
          <tr><td>Farine T65 Tradition pure</td><td class="w1">1 340 g</td><td class="w2">13 400 g</td><td class="w2">26 800 g</td></tr>
          <tr><td>Eau glacée (+1 °C) / Glace écaille</td><td class="w1">2 015 g</td><td class="w2">20 150 g</td><td class="w2">40 300 g</td></tr>
          <tr><td>Sucre cristal blanc</td><td class="w1">394 g</td><td class="w2">3 940 g</td><td class="w2">7 880 g</td></tr>
          <tr><td>Trimoline (sucre inverti)</td><td class="w1">157 g</td><td class="w2">1 570 g</td><td class="w2">3 140 g</td></tr>
          <tr><td>Levure fraîche L'Hirondelle Or</td><td class="w1">188 g</td><td class="w2">1 880 g</td><td class="w2">3 760 g</td></tr>
          <tr><td>Poudre de lait entier 26 % MG</td><td class="w1">180 g</td><td class="w2">1 800 g</td><td class="w2">3 600 g</td></tr>
          <tr><td>Améliorant S500 Kimo Short</td><td class="w1">90 g</td><td class="w2">900 g</td><td class="w2">1 800 g</td></tr>
          <tr><td>Sel fin d'atelier</td><td class="w1">90 g</td><td class="w2">900 g</td><td class="w2">1 800 g</td></tr>
          <tr><td>Vinaigre blanc d'alcool 8°</td><td class="w1">36 g</td><td class="w2">360 g</td><td class="w2">720 g</td></tr>
          <tr class="ed-sec"><td colspan="4">Phase 2 • Ajout Cuve V2 (4'30–5')</td></tr>
          <tr><td>Margarine OPAL cuve (dés 500 g)</td><td class="w1">380 g</td><td class="w2">3 800 g</td><td class="w2">7 600 g</td></tr>
          <tr class="ed-stot"><td>Sous-total Détrempe Nette</td><td class="w1">8 000 g</td><td class="w2">80 000 g</td><td class="w2">160 000 g</td></tr>
          <tr class="ed-sec"><td colspan="4">Phase 3 • Tourage J+1</td></tr>
          <tr><td>Beurre Debic Croissant 82 %</td><td class="w1">2 000 g</td><td class="w2">20 000 g</td><td class="w2">40 000 g</td></tr>
          <tr class="ed-tot"><td>TOTAL PÂTON TOURÉ</td><td class="w1">10 000 g</td><td class="w2" style="color:#e7e5e4;">100 000 g</td><td class="w2" style="color:#e7e5e4;">200 000 g</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="ed-foot"><span>Cahier de Production • Pôle 1 PLF</span><span>Page 4 / 37</span></div>
</div>

<!-- PAGE DROITE -->
<div class="sheet">
  <div style="display:flex; flex-direction:column; flex:1;">
    <div class="ed-head">
      <div>
        <div class="ed-kicker">FICHE 01 • CONDUITE &amp; TOURAGE</div>
        <h1 class="ed-title">Méthode Opératoire &amp; Circuit PAC</h1>
      </div>
      <div class="ed-tag" style="background:#f0fdf4; color:#15803d; border-color:#86efac;">CONDUITE &amp; CUISSON</div>
    </div>

    <div class="chap">
      <div class="chap-head"><span class="chap-num">01</span><span class="chap-title">Pétrissage &amp; Refroidissement J-1</span><span class="chap-sub">Sortie 20–21 °C</span></div>
      <ul class="act-list">
        <li class="key"><span class="act-k">Frasage (5 min V1)</span><span class="act-v">Verser tous les ingrédients [1] dans le pétrin spirale. Tourner 5 min en 1re vitesse.</span></li>
        <li class="key"><span class="act-k">Pétrissage (V2)</span><span class="act-v">Passer en V2 avec l'OPAL (morceaux 500 g). Pétrir <strong>4 min 30 à 5 min max</strong> : stopper au 1er décollement net (ne pas chercher le voile).</span></li>
        <li><span class="act-k">Bacs Paneo</span><span class="act-v">Diviser en bacs de <strong>8 000 g pile</strong>, pré-laminer en galette uniforme de <strong>3 cm</strong>.</span></li>
        <li><span class="act-k">Blocage &amp; Nuit</span><span class="act-v">Cellule flash <strong>-35 °C (30–35 min, cœur &lt; 6 °C)</strong>, puis chambre froide <strong>0/+1,5 °C pendant 12–15 h</strong>.</span></li>
      </ul>
    </div>

    <div class="chap">
      <div class="chap-head"><span class="chap-num">02</span><span class="chap-title">Tourage Unifié (1D + 1S)</span><span class="chap-sub">12 films de beurre</span></div>
      <ul class="act-list">
        <li class="key"><span class="act-k">Enchâssement</span><span class="act-v">Détrempe à <strong>+2/+4 °C</strong>, plaque Debic 2 000 g à <strong>12–14 °C</strong>. Enfermer portefeuille sans chevauchement.</span></li>
        <li><span class="act-k">Tour Double + Simple</span><span class="act-v">Enchaîner 1 Tour Double (pliage en 4, quart de tour) puis 1 Tour Simple (pliage en 3).</span></li>
        <li><span class="act-k">Drossage &amp; Détente</span><span class="act-v">Parer les 4 chants fermés au couteau, filmer et détendre <strong>45 min à +2 °C</strong> avant abaisse.</span></li>
      </ul>
    </div>

    <div class="chap">
      <div class="chap-head"><span class="chap-num">03</span><span class="chap-title">Abaisse &amp; Circuit Double Congélation PAC</span><span class="chap-sub">Sonde -10 °C</span></div>
      <ul class="act-list">
        <li><span class="act-k">Polyline</span><span class="act-v">Dérouler face farinée dessous, dessus <strong>nu sans farine</strong> (soudure). Flotter <strong>≥ 60 s</strong> avant coupe.</span></li>
        <li><span class="act-k">Stock 1 (Cru)</span><span class="act-v">Plaquer serré, flash <strong>-35 °C (35–40 min)</strong>, stocker en caisses étanches à <strong>-18 °C</strong>.</span></li>
        <li class="key"><span class="act-k">Pousse &amp; Stock 2</span><span class="act-v">Décongélation nuit (+2/+4 °C, 10–12 h) → étuve <strong>25–26 °C / 75–80 % HR</strong> 2h15–2h30 (<strong>arrêt 70–75 % volume</strong>) → ressuyage 15 min +4 °C → Dorure Végétale pistolet (1,5 bar) → flash <strong>-35 °C (arrêt -10 °C cœur)</strong> → caisses -18 °C.</span></li>
      </ul>
    </div>

    <div class="gold-rule">
      <div class="gold-rule-h">Règle d'Or Atelier — Points de Rupture</div>
      <p class="gold-rule-p">Zéro voile au pétrin • Zéro farine sur le dessus au déroulage • Arrêt étuve à 75 % max • Sonde flash à -10 °C strict.</p>
    </div>
  </div>
  <div class="ed-foot"><span>Cahier de Production • Pôle 1 PLF</span><span>Page 5 / 37</span></div>
</div>
</body>
</html>"""


if __name__ == "__main__":
    compile_pdf(HTML_MAQUETTE_A, "Maquette_A_Chrono_Labo")
    compile_pdf(HTML_MAQUETTE_B, "Maquette_B_Poste_Couleur")
    compile_pdf(HTML_MAQUETTE_C, "Maquette_C_Artisan_Editorial")
