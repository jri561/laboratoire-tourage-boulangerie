#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur PDF « Atelier Direct » — Cahier de Recettes & Fiches Opérateurs
Format A4 portrait strict (210 × 297 mm) en double-page face-à-face.
Aucune photo, aucune illustration, aucun schéma SVG.
"""

import os
import re
import html
import subprocess

BASE_DIR = "/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie"
FICHES_DIR = os.path.join(BASE_DIR, "recettes/fiches_atelier_operateurs")
EXPORT_DIR = os.path.join(BASE_DIR, "exports_pdf")

CSS_BASE = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}

body {
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #0f172a;
    background-color: #ffffff;
    font-size: 8.6pt;
    line-height: 1.32;
    margin: 0;
    padding: 0;
    font-variant-numeric: tabular-nums;
    font-feature-settings: "tnum" 1;
}

.page-sheet {
    width: 100%;
    height: 267mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
    break-after: page;
    overflow: hidden;
}

.page-sheet:last-child {
    page-break-after: auto;
    break-after: auto;
}

.page-content {
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    gap: 3.5px;
}

.page-sheet.dense .topbar {
    padding: 2.2mm 4mm;
    margin-bottom: 1mm;
}

.page-sheet.dense .topbar-title {
    font-size: 11pt;
}

.page-sheet.dense .sec-title {
    font-size: 8.8pt;
    margin: 2px 0 1.5px 0;
}

/* === COUVERTURE SOMBRE === */
.cover-sheet {
    width: 210mm;
    height: 296.5mm;
    background-color: #0f172a;
    color: #ffffff;
    padding: 20mm 18mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
    break-after: page;
    overflow: hidden;
}

.cover-kicker {
    font-size: 9pt;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #60a5fa;
    margin-bottom: 6mm;
}

.cover-title {
    font-size: 30pt;
    font-weight: 800;
    line-height: 1.08;
    letter-spacing: -0.02em;
    margin: 0 0 5mm 0;
    color: #ffffff;
}

.cover-subtitle {
    font-size: 11.5pt;
    font-weight: 500;
    color: #cbd5e1;
    margin: 0 0 10mm 0;
    max-width: 155mm;
}

.cover-accent-bar {
    width: 28mm;
    height: 1.6mm;
    background-color: #60a5fa;
    margin-bottom: 10mm;
}

.cover-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4.5mm;
}

.cover-card {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 4px;
    padding: 4.5mm 5mm;
}

.cover-card-num {
    font-size: 8pt;
    font-weight: 800;
    color: #60a5fa;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1.5mm;
}

.cover-card-title {
    font-size: 11pt;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 1.5mm;
}

.cover-card-desc {
    font-size: 8.5pt;
    color: #cbd5e1;
    line-height: 1.35;
}

.cover-footer {
    border-top: 1px solid #334155;
    padding-top: 4mm;
    display: flex;
    justify-content: space-between;
    font-size: 8.5pt;
    color: #94a3b8;
    font-weight: 600;
}

/* === BANDEAU TOPBAR === */
.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 3.2mm 4.5mm;
    border-radius: 3px;
    margin-bottom: 2mm;
}

.topbar-left {
    background-color: #0f172a;
}

.topbar-right {
    background-color: #1e293b;
}

.topbar-title-wrap {
    display: flex;
    flex-direction: column;
}

.topbar-title {
    font-size: 12.5pt;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.01em;
    line-height: 1.15;
}

.topbar-sub {
    font-size: 7.8pt;
    font-weight: 500;
    color: #cbd5e1;
    margin-top: 1px;
}

.topbar-badge {
    font-size: 7.8pt;
    font-weight: 800;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #ffffff;
    padding: 1.6mm 3.2mm;
    border-radius: 2px;
    white-space: nowrap;
}

.badge-blue {
    background-color: #2563eb;
}

.badge-green {
    background-color: #16a34a;
}

/* === TITRES DE SECTION === */
.sec-title {
    font-size: 9.8pt;
    font-weight: 800;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: #0f172a;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 1.5px;
    margin: 4px 0 3px 0;
}

/* === PAVÉS 3 COLONNES (PARAMÈTRES CLÉS) === */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2.5mm;
    margin: 2px 0 4px 0;
}

.kpi-box {
    background-color: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 3px;
    padding: 2.4mm 2.5mm;
    text-align: center;
}

.kpi-val {
    font-size: 13pt;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.15;
    font-variant-numeric: tabular-nums;
}

.kpi-lbl {
    font-size: 7pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #64748b;
    margin-top: 1mm;
}

/* === TABLEAUX DE DONNÉES === */
.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2px 0 4px 0;
    font-size: 8.4pt;
    font-variant-numeric: tabular-nums;
}

.data-table th {
    text-align: left;
    font-size: 7.4pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    color: #0f172a;
    border-bottom: 2px solid #0f172a;
    padding: 3px 5px;
}

.data-table th.num,
.data-table td.num {
    text-align: right;
    font-weight: 700;
}

.data-table td.num {
    white-space: nowrap;
}

.data-table.wide {
    font-size: 7.4pt;
}

.data-table.wide th {
    font-size: 6.5pt;
    padding: 2px 3px;
}

.data-table.wide td {
    padding: 2px 3px;
}

.data-table.wide td.num {
    white-space: normal;
}

.data-table td {
    padding: 3.2px 5px;
    border-bottom: 1px solid #e2e8f0;
    color: #0f172a;
    vertical-align: middle;
}

.data-table tr.row-subtotal td {
    background-color: #f1f5f9;
    font-weight: 700;
    color: #334155;
    border-top: 1px solid #cbd5e1;
    border-bottom: 1px solid #cbd5e1;
}

.data-table tr.row-total td {
    background-color: #eff6ff;
    font-weight: 800;
    font-size: 9pt;
    color: #0f172a;
    border-top: 1.5px solid #2563eb;
    border-bottom: 1.5px solid #2563eb;
}

.data-table tr.row-total td.num {
    font-size: 9.6pt;
    color: #1d4ed8;
}

.data-table.compact {
    font-size: 7.6pt;
}

.data-table.compact th {
    font-size: 6.9pt;
    padding: 2px 4px;
}

.data-table.compact td {
    padding: 2px 4px;
}

.data-table.compact tr.row-total td {
    font-size: 8.2pt;
}

.data-table.ultra-compact {
    font-size: 6.7pt;
    line-height: 1.12;
    margin: 1px 0 2px 0;
}

.data-table.ultra-compact th {
    font-size: 6.2pt;
    padding: 1.4px 3px;
}

.data-table.ultra-compact td {
    padding: 1.3px 3px;
}

.data-table.ultra-compact tr.row-total td {
    font-size: 7.1pt;
}

.data-table.ultra-compact tr.row-total td.num {
    font-size: 7.4pt;
}

/* === PASTILLES D'ORDRE (2.4 mm) === */
.dot {
    display: inline-block;
    width: 2.4mm;
    height: 2.4mm;
    border-radius: 50%;
    vertical-align: middle;
    margin-right: 3px;
}
.dot-blue { background-color: #2563eb; }
.dot-amber { background-color: #d97706; }
.dot-green { background-color: #16a34a; }

/* === CARTES D'ÉTAPES (GRILLE 2 COLONNES) === */
.steps-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2.5mm;
    margin: 2px 0 4px 0;
}

.step-card {
    border: 1px solid #cbd5e1;
    border-radius: 3px;
    padding: 2.5mm 3mm;
    background-color: #ffffff;
}

.step-card-title {
    font-size: 8.5pt;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 1mm;
    display: block;
}

.step-card-body {
    font-size: 8pt;
    color: #334155;
    line-height: 1.3;
}

/* === LISTES SOBRES & PARAGRAPHES === */
.clean-list {
    margin: 1px 0 3px 14px;
    padding: 0;
    font-size: 8.1pt;
    color: #1e293b;
}
.clean-list li {
    margin-bottom: 1.5px;
}
.note-line {
    font-size: 7.9pt;
    color: #475569;
    margin: 1px 0 2px 0;
}

/* === ENCADRÉ ALERTE CRITIQUE === */
.alert-critical {
    background-color: #fef2f2;
    border: 1px solid #ef4444;
    border-radius: 3px;
    color: #991b1b;
    font-size: 8.2pt;
    font-weight: 800;
    text-transform: uppercase;
    text-align: center;
    padding: 2.5mm 4mm;
    margin-top: auto;
    letter-spacing: 0.02em;
}

/* === PIED DE PAGE DISCRET === */
.page-footer {
    border-top: 1px solid #cbd5e1;
    padding-top: 1.8mm;
    margin-top: 2mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.5pt;
    color: #64748b;
    font-weight: 600;
}
"""

CSS_BOOK_MARGINS = """
@page {
    size: A4 portrait;
    margin: 15mm 14mm 14mm 18mm;
}
@page :first {
    margin: 0;
}
@page :left {
    margin: 15mm 18mm 14mm 14mm;
}
@page :right {
    margin: 15mm 14mm 14mm 18mm;
}
"""

CSS_SHEET_MARGINS = """
@page {
    size: A4 portrait;
    margin: 15mm 14mm 14mm 18mm;
}
@page :first {
    margin: 15mm 18mm 14mm 14mm;
}
@page :left {
    margin: 15mm 18mm 14mm 14mm;
}
@page :right {
    margin: 15mm 14mm 14mm 18mm;
}
"""


def clean_inline(text: str) -> str:
    """Formate le Markdown inline (gras, italique, code) en HTML propre."""
    text = html.escape(text)
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.*?)`', r'\1', text)
    text = text.replace('$\\rightarrow$', '→').replace('$\\ge$', '≥').replace('$\\le$', '≤').replace('$\\pm$', '±')
    text = re.sub(r'\$([^$]+)\$', r'\1', text)
    return text


def is_numeric_cell(raw: str) -> bool:
    s = re.sub(r'[*`]', '', raw).strip()
    if re.match(r'^(\+?\s*[0-9]|~[0-9]|—|-|PM$)', s):
        return True
    if any(u in s for u in (' g', ' kg', ' pcs', ' p.', ' min', ' °C', ' mm', ' cm')):
        if re.search(r'\d', s) and len(s) < 28:
            return True
    return False


def format_phase_dot(raw: str) -> str:
    s = re.sub(r'[*`\[\]]', '', raw).strip().upper()
    if s in ('1', 'A', '1 A', '1 B'):
        return f'<span class="dot dot-blue"></span>{clean_inline(raw)}'
    if s in ('2', 'B', 'C'):
        return f'<span class="dot dot-amber"></span>{clean_inline(raw)}'
    if s in ('3', '4', 'D', 'OPTION', '4 A', '4 B', '3 B', 'DÉCOR', 'FOURRAGE'):
        return f'<span class="dot dot-green"></span>{clean_inline(raw)}'
    return clean_inline(raw)


def render_table(table_lines: list[str], force_ultra_compact: bool = False) -> str:
    if len(table_lines) < 2:
        return ""
    headers = [p.strip() for p in table_lines[0].strip('|').split('|')]
    rows = []
    for ln in table_lines[2:]:
        cells = [p.strip() for p in ln.strip('|').split('|')]
        if cells:
            rows.append(cells)

    # Détection des colonnes numériques
    num_cols = set()
    for c_idx in range(len(headers)):
        if c_idx == 0:
            continue
        matches = sum(1 for r in rows if c_idx < len(r) and is_numeric_cell(r[c_idx]))
        if rows and matches >= max(1, len(rows) // 2):
            num_cols.add(c_idx)

    # Mode compact automatique si > 15 lignes, ultra-compact si page dense, wide si >= 5 colonnes
    classes = ["data-table"]
    if force_ultra_compact:
        classes.append("ultra-compact")
    elif len(rows) > 15:
        classes.append("compact")
    if len(headers) >= 5:
        classes.append("wide")
    out = [f'<table class="{" ".join(classes)}"><thead><tr>']
    for c_idx, h in enumerate(headers):
        cls = ' class="num"' if c_idx in num_cols else ''
        out.append(f'<th{cls}>{clean_inline(h)}</th>')
    out.append('</tr></thead><tbody>')

    has_phase_col = headers and headers[0].strip().lower() in ('phase', 'étape', 'bloc')

    for r in rows:
        lbl_upper = (r[0] + " " + (r[1] if len(r) > 1 else "")).upper()
        tr_cls = ""
        if "SOUS-TOTAL" in lbl_upper or "SOUS-BLOC" in lbl_upper or "S-TOT" in lbl_upper:
            tr_cls = ' class="row-subtotal"'
        elif "TOTAL" in r[0].upper() or "MASSE" in r[0].upper():
            tr_cls = ' class="row-total"'

        out.append(f'<tr{tr_cls}>')
        for c_idx in range(len(headers)):
            val = r[c_idx] if c_idx < len(r) else ""
            cls = ' class="num"' if c_idx in num_cols else ''
            if c_idx == 0 and has_phase_col and not tr_cls:
                cell_html = format_phase_dot(val)
            else:
                cell_html = clean_inline(val)
            out.append(f'<td{cls}>{cell_html}</td>')
        out.append('</tr>')
    out.append('</tbody></table>')
    return "\n".join(out)


def render_kpi_from_table(table_lines: list[str]) -> str:
    """Transforme un tableau Repères Flash (<= 3 lignes) en grille 3 colonnes de pavés."""
    rows = []
    for ln in table_lines[2:]:
        cells = [p.strip() for p in ln.strip('|').split('|')]
        if len(cells) >= 2:
            rows.append(cells)
    if not rows:
        return ""
    out = ['<div class="kpi-grid">']
    for r in rows[:3]:
        lbl = clean_inline(r[0])
        val = clean_inline(r[1])
        out.append(f'<div class="kpi-box"><div class="kpi-val">{val}</div><div class="kpi-lbl">{lbl}</div></div>')
    out.append('</div>')
    return "\n".join(out)


def render_page_body(md_block: str, is_right: bool) -> tuple[str, str]:
    """Convertit une demi-fiche Markdown (gauche ou droite) en HTML structuré."""
    lines = md_block.strip().splitlines()
    blocks = []
    alert_html = ""
    sec_num = 0
    i = 0
    step_cards = []

    def flush_steps():
        nonlocal step_cards
        if step_cards:
            blocks.append('<div class="steps-grid">' + "".join(step_cards) + '</div>')
            step_cards = []

    while i < len(lines):
        s = lines[i].strip()
        if not s or s == '---' or s.startswith('## PAGE '):
            i += 1
            continue

        # Titre de section
        if s.startswith('### ') or s.startswith('#### '):
            flush_steps()
            title = s.lstrip('#').strip()
            # Repères Flash -> converti en pavés KPI 3 colonnes
            if "repères flash" in title.lower():
                j = i + 1
                while j < len(lines) and not lines[j].strip().startswith('|'):
                    j += 1
                tbl = []
                while j < len(lines) and lines[j].strip().startswith('|'):
                    tbl.append(lines[j].strip())
                    j += 1
                if tbl:
                    blocks.append(render_kpi_from_table(tbl))
                    i = j
                    continue
            sec_num += 1
            if not re.match(r'^\d+\.', title):
                title = f"{sec_num}. {title}"
            blocks.append(f'<div class="sec-title">{clean_inline(title)}</div>')
            i += 1
            continue

        # Tableaux
        if s.startswith('|'):
            flush_steps()
            tbl = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                tbl.append(lines[i].strip())
                i += 1
            blocks.append(render_table(tbl))
            continue

        # Cartes d'étapes numérotées (1. **Titre :** texte)
        m_step = re.match(r'^(\d+)\.\s+\*\*(.*?)\*\*\s*(.*)$', s)
        if m_step and is_right:
            num, stitle, sbody = m_step.groups()
            stitle = stitle.rstrip(':').strip()
            sbody = sbody.lstrip(':').strip()
            # Rassembler éventuelles sous-puces rattachées à cette étape
            sub_bullets = []
            j = i + 1
            while j < len(lines) and (lines[j].startswith('   -') or lines[j].startswith('   *')):
                sub_bullets.append(clean_inline(lines[j].strip()[2:].strip()))
                j += 1
            if sub_bullets:
                sbody = (sbody + " " if sbody else "") + " • ".join(sub_bullets)
                i = j
            else:
                i += 1
            step_cards.append(
                f'<div class="step-card">'
                f'<span class="step-card-title">{num}. {clean_inline(stitle)}</span>'
                f'<div class="step-card-body">{clean_inline(sbody)}</div>'
                f'</div>'
            )
            continue

        # Listes à puces
        if s.startswith('- ') or s.startswith('* '):
            flush_steps()
            items = []
            while i < len(lines) and (lines[i].strip().startswith('- ') or lines[i].strip().startswith('* ')):
                txt = lines[i].strip()[2:].strip()
                if is_right and ("INTERDICTION" in txt.upper() or "OURA" in txt.upper() and "FERMÉ" in txt.upper() and "STRICTEMENT" in txt.upper()):
                    alert_html = f'<div class="alert-critical">{clean_inline(txt)}</div>'
                else:
                    items.append(f'<li>{clean_inline(txt)}</li>')
                i += 1
            if items:
                blocks.append('<ul class="clean-list">' + "".join(items) + '</ul>')
            continue

        # Callout / Alerte
        if s.startswith('> '):
            flush_steps()
            q_lines = []
            while i < len(lines) and lines[i].strip().startswith('> '):
                q_lines.append(lines[i].strip()[2:].strip())
                i += 1
            q_text = " ".join(q_lines)
            if is_right or "INTERDIT" in q_text.upper() or "ATTENTION" in q_text.upper():
                alert_html = f'<div class="alert-critical">{clean_inline(q_text)}</div>'
            else:
                blocks.append(f'<p class="note-line">{clean_inline(q_text)}</p>')
            continue

        # Note italique
        flush_steps()
        blocks.append(f'<p class="note-line">{clean_inline(s)}</p>')
        i += 1

    flush_steps()
    return "\n".join(blocks), alert_html


def parse_fiche_pages(md_path: str, page_start: int, total_pages: int) -> list[str]:
    text = open(md_path, encoding='utf-8').read()
    lines = text.splitlines()

    # Extraire titre H1 et ligne meta
    title = ""
    meta = ""
    body_lines = []
    for idx, ln in enumerate(lines):
        if idx == 0 and ln.startswith('# '):
            title = ln[2:].strip()
        elif idx <= 2 and ln.startswith('**'):
            meta = ln.strip()
        else:
            body_lines.append(ln)

    body_text = "\n".join(body_lines)
    parts = body_text.split('<!-- PAGE_BREAK -->')
    left_md = parts[0] if len(parts) > 0 else ""
    right_md = parts[1] if len(parts) > 1 else ""

    left_html, left_alert = render_page_body(left_md, is_right=False)
    right_html, right_alert = render_page_body(right_md, is_right=True)

    # Extraire numéro de fiche pour libellé pied de page
    fname = os.path.basename(md_path)
    section_label = title

    page_left = f"""
    <div class="page-sheet">
      <div class="page-content">
        <div class="topbar topbar-left">
          <div class="topbar-title-wrap">
            <div class="topbar-title">{clean_inline(title)}</div>
            <div class="topbar-sub">{clean_inline(meta)}</div>
          </div>
          <div class="topbar-badge badge-blue">POSTE DE PESÉE</div>
        </div>
        {left_html}
        {left_alert}
      </div>
      <footer class="page-footer">
        <span>{clean_inline(section_label)}</span>
        <span>{page_start} / {total_pages}</span>
      </footer>
    </div>
    """

    page_right = f"""
    <div class="page-sheet">
      <div class="page-content">
        <div class="topbar topbar-right">
          <div class="topbar-title-wrap">
            <div class="topbar-title">{clean_inline(title)}</div>
            <div class="topbar-sub">{clean_inline(meta)}</div>
          </div>
          <div class="topbar-badge badge-green">CONDUITE &amp; CUISSON</div>
        </div>
        {right_html}
        {right_alert}
      </div>
      <footer class="page-footer">
        <span>{clean_inline(section_label)}</span>
        <span>{page_start + 1} / {total_pages}</span>
      </footer>
    </div>
    """
    return [page_left, page_right]


def build_cover_html() -> str:
    return """
    <div class="cover-sheet">
      <div>
        <div class="cover-kicker">LABORATOIRE DE TOURAGE &amp; BOULANGERIE • EDITION ATELIER DIRECT</div>
        <h1 class="cover-title">CAHIER DE PRODUCTION<br>&amp; FICHES D'ATELIER</h1>
        <div class="cover-accent-bar"></div>
        <p class="cover-subtitle">Référentiel opérationnel de pesée, façonnage, double congélation PAC et cuisson. Document structuré en double-page A4 pour lecture directe au poste de travail.</p>

        <div class="cover-grid">
          <div class="cover-card">
            <div class="cover-card-num">PÔLE 1 • FICHES 01 – 02</div>
            <div class="cover-card-title">Pâte Levée Feuilletée (PLF)</div>
            <div class="cover-card-desc">Détrempe commune, tourage unifié 1D + 1S (12 films) et 7 façonnages sur Rondo Polyline &amp; Croissomat SCM50.</div>
          </div>
          <div class="cover-card">
            <div class="cover-card-num">PÔLE 2 • FICHES 03 – 04</div>
            <div class="cover-card-title">Pains Viennois &amp; Brioches PAC</div>
            <div class="cover-card-desc">Méthode directe Soft'r / Kimo : Pains Viennois 280 g &amp; 140 g, Petites Brioches au Sucre 75 g.</div>
          </div>
          <div class="cover-card">
            <div class="cover-card-num">PÔLE 3 • FICHE 05</div>
            <div class="cover-card-title">Kouign-Amann Breton</div>
            <div class="cover-card-desc">Beurre manié sucré au Ratio d'Or (3 820 g/bac), individuels 100 g &amp; partage 400/600 g en octogone.</div>
          </div>
          <div class="cover-card">
            <div class="cover-card-num">PÔLE 4 • FICHES 06 – 07</div>
            <div class="cover-card-title">Feuilletage Inversé &amp; Épiphanie</div>
            <div class="cover-card-desc">Feuilletage 48 strates (OPAL en détrempe), Frangipane 80/20, Pommes Topfil &amp; Trio Poire-Nutolade.</div>
          </div>
          <div class="cover-card">
            <div class="cover-card-num">PÔLE 5 • FICHES 08 – 13</div>
            <div class="cover-card-title">Biscuiterie &amp; Gâteaux de Voyage</div>
            <div class="cover-card-desc">Cookies coupe-fil 80 g, Muffins pilon 120 g, Brownie &amp; Brookie en cadres 56×36 cm, Cakes &amp; Nantais.</div>
          </div>
          <div class="cover-card">
            <div class="cover-card-num">PÔLE 6 • FICHES 14 – 17</div>
            <div class="cover-card-title">Girocrêpes, Traiteur &amp; Cuissons</div>
            <div class="cover-card-desc">Crêpes froment, Galettes blé noir, Quiches individuelles IQF, Dorures, Sirop 44°B et barèmes généraux.</div>
          </div>
        </div>
      </div>

      <div class="cover-footer">
        <span>CONFORME PRODUCTION QUOTIDIENNE • IMPRESSION RECTO-VERSO RELIURE CENTRALE</span>
        <span>37 PAGES • DOUBLE-PAGE A4</span>
      </div>
    </div>
    """


def build_sommaire_pages(total_pages: int) -> list[str]:
    p2 = f"""
    <div class="page-sheet">
      <div class="page-content">
        <div class="topbar topbar-left">
          <div class="topbar-title-wrap">
            <div class="topbar-title">SOMMAIRE GÉNÉRAL — PÔLES 1 À 4</div>
            <div class="topbar-sub">Index des fiches Viennoiserie, Kouign-Amann, Feuilletage &amp; Galettes</div>
          </div>
          <div class="topbar-badge badge-blue">PAGES 4 – 17</div>
        </div>

        <div class="sec-title">1. Index des Fiches Pôles 1 à 4</div>
        <table class="data-table">
          <thead><tr><th>Fiche</th><th>Pôle</th><th>Désignation Atelier</th><th class="num">Pages</th></tr></thead>
          <tbody>
            <tr><td><strong>01</strong></td><td>Pôle 1 • PLF</td><td><strong>Recette Maîtresse PLF Commune (1D + 1S &amp; PAC)</strong></td><td class="num">4 – 5</td></tr>
            <tr><td><strong>02</strong></td><td>Pôle 1 • PLF</td><td><strong>Annexe Façonnages, Calibres &amp; Garnitures PLF (7 produits)</strong></td><td class="num">6 – 7</td></tr>
            <tr><td><strong>03</strong></td><td>Pôle 2 • Pâtes Levées</td><td><strong>Pains Viennois Nature (280 g) &amp; Pépites Chocolat (140 g) PAC</strong></td><td class="num">8 – 9</td></tr>
            <tr><td><strong>04</strong></td><td>Pôle 2 • Pâtes Levées</td><td><strong>Petite Brioche Individuelle au Sucre PAC (75 g)</strong></td><td class="num">10 – 11</td></tr>
            <tr><td><strong>05</strong></td><td>Pôle 3 • Breton</td><td><strong>Kouign-Amann Individuel (100 g) &amp; Partage (400 / 600 g)</strong></td><td class="num">12 – 13</td></tr>
            <tr><td><strong>06</strong></td><td>Pôle 4 • Feuilletage</td><td><strong>Feuilletage Inversé Universel (48 Strates) &amp; Plaques Pâtisserie</strong></td><td class="num">14 – 15</td></tr>
            <tr><td><strong>07</strong></td><td>Pôle 4 • Épiphanie</td><td><strong>Galettes des Rois : Frangipane 80/20, Pommes &amp; Poire-Nutolade</strong></td><td class="num">16 – 17</td></tr>
          </tbody>
        </table>

        <div class="sec-title">2. Tolérances de Pesée &amp; Températures de Base</div>
        <div class="kpi-grid">
          <div class="kpi-box"><div class="kpi-val">± 1 g</div><div class="kpi-lbl">Levure, Sel, S500, Vinaigre</div></div>
          <div class="kpi-box"><div class="kpi-val">20–21 °C</div><div class="kpi-lbl">Sortie Pétrin PLF / Viennois</div></div>
          <div class="kpi-box"><div class="kpi-val">-10 °C</div><div class="kpi-lbl">Sonde Cœur Blocage PAC</div></div>
        </div>
        <ul class="clean-list">
          <li><strong>Farines, sucres, graisses &amp; liquides :</strong> tolérance ± 5 g ; bacs Paneo divisés pile au gramme près.</li>
          <li><strong>Pastilles d'ordre dans les tableaux :</strong> <span class="dot dot-blue"></span>Phase 1 (Frasage / Base) • <span class="dot dot-amber"></span>Phase 2 (Matière grasse cuve / Émulsion) • <span class="dot dot-green"></span>Phase 3–4 (Tourage / Poudres / Options).</li>
        </ul>
      </div>
      <footer class="page-footer">
        <span>SOMMAIRE GÉNÉRAL • PÔLES 1 À 4</span>
        <span>2 / {total_pages}</span>
      </footer>
    </div>
    """

    p3 = f"""
    <div class="page-sheet">
      <div class="page-content">
        <div class="topbar topbar-right">
          <div class="topbar-title-wrap">
            <div class="topbar-title">SOMMAIRE GÉNÉRAL — PÔLES 5 À 6</div>
            <div class="topbar-sub">Index des fiches Biscuiterie, Gâteaux de Voyage, Girocrêpes, Traiteur &amp; Finitions</div>
          </div>
          <div class="topbar-badge badge-green">PAGES 18 – 37</div>
        </div>

        <div class="sec-title">1. Index des Fiches Pôles 5 à 6</div>
        <table class="data-table">
          <thead><tr><th>Fiche</th><th>Pôle</th><th>Désignation Atelier</th><th class="num">Pages</th></tr></thead>
          <tbody>
            <tr><td><strong>08</strong></td><td>Pôle 5 • Biscuiterie</td><td><strong>Cookies Classique &amp; Chocolat-Noisette (Coupe-Fil 80 g)</strong></td><td class="num">18 – 19</td></tr>
            <tr><td><strong>09</strong></td><td>Pôle 5 • Biscuiterie</td><td><strong>Muffins Pépites/Cœur Nutolade &amp; Noisette (Doseuse 120 g)</strong></td><td class="num">20 – 21</td></tr>
            <tr><td><strong>10</strong></td><td>Pôle 5 • Biscuiterie</td><td><strong>Brownie Fondant Chocolat, Trimoline &amp; Cerneaux de Noix</strong></td><td class="num">22 – 23</td></tr>
            <tr><td><strong>11</strong></td><td>Pôle 5 • Biscuiterie</td><td><strong>Brookie Double Couche en Cadres 56×36 cm (30 Parts 115 g)</strong></td><td class="num">24 – 25</td></tr>
            <tr><td><strong>12</strong></td><td>Pôle 5 • Biscuiterie</td><td><strong>Cakes de Voyage (Mix Golden, Citron Pavot &amp; Marbré)</strong></td><td class="num">26 – 27</td></tr>
            <tr><td><strong>13</strong></td><td>Pôle 5 • Biscuiterie</td><td><strong>Gâteau Nantais OPAL &amp; Glaçage Rhum-Gélatine</strong></td><td class="num">28 – 29</td></tr>
            <tr><td><strong>14</strong></td><td>Pôle 6 • Girocrêpes</td><td><strong>Crêpes de Froment sur Carrousel Girocrêpes</strong></td><td class="num">30 – 31</td></tr>
            <tr><td><strong>15</strong></td><td>Pôle 6 • Girocrêpes</td><td><strong>Galettes de Blé Noir (Sarrasin) sur Carrousel Girocrêpes</strong></td><td class="num">32 – 33</td></tr>
            <tr><td><strong>16</strong></td><td>Pôle 6 • Traiteur</td><td><strong>Quiches Traiteur (Lorraine, Chèvre-Épinards IQF, Poireaux)</strong></td><td class="num">34 – 35</td></tr>
            <tr><td><strong>17</strong></td><td>Pôle 6 • Finitions</td><td><strong>Dorures, Sirop de Lustrage 44° Brix &amp; Barèmes Cuissons</strong></td><td class="num">36 – 37</td></tr>
          </tbody>
        </table>

        <div class="sec-title">2. Règles Sanitaires &amp; Chaîne du Froid</div>
        <div class="steps-grid">
          <div class="step-card"><span class="step-card-title">Légumes IQF (Quiches)</span><div class="step-card-body">Enfourner directement congelés sans jamais décongeler au préalable.</div></div>
          <div class="step-card"><span class="step-card-title">Refroidissement Traiteur</span><div class="step-card-body">Descente en cellule sous +10 °C à cœur en moins de 2 heures.</div></div>
          <div class="step-card"><span class="step-card-title">Dorure Pinceau (+4 °C)</span><div class="step-card-body">Conservation maximale 48 h datée. Filtration chinois étamine 0,5 mm.</div></div>
          <div class="step-card"><span class="step-card-title">Allergènes &amp; Étiquetage</span><div class="step-card-body">Identifier chaque bac/caisse : gluten, œufs, lait, fruits à coque, sarrasin.</div></div>
        </div>

        <div class="alert-critical">CHAÎNE DU FROID STRICTE : STOCKAGE NÉGATIF À -18 °C EN CAISSES ÉTANCHES APRÈS BLOCAGE FLASH -35 °C</div>
      </div>
      <footer class="page-footer">
        <span>SOMMAIRE GÉNÉRAL • PÔLES 5 À 6</span>
        <span>3 / {total_pages}</span>
      </footer>
    </div>
    """
    return [p2, p3]


def compile_html_to_pdf(body_html: str, css_margins: str, out_name: str, title: str):
    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>{CSS_BASE}\n{css_margins}</style>
</head>
<body>
{body_html}
</body>
</html>"""
    html_out = os.path.join(EXPORT_DIR, f"{out_name}.html")
    pdf_out = os.path.join(EXPORT_DIR, f"{out_name}.pdf")
    with open(html_out, "w", encoding="utf-8") as f:
        f.write(full_html)
    cmd = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_out}",
        html_out,
    ]
    subprocess.run(cmd, capture_output=True, text=True, check=True)
    if os.path.exists(pdf_out):
        print(f"  [PDF OK] {out_name}.pdf ({os.path.getsize(pdf_out):,} octets)")
    return pdf_out


def build_pdf():
    os.makedirs(EXPORT_DIR, exist_ok=True)
    print("=== GÉNÉRATION DES PDFS « ATELIER DIRECT » ===")

    fiches_ordered = [
        ("01-recette-maitresse-plf-commune.md", "01_Recette_Maitresse_PLF_Commune", "Fiche 01 - Recette Maîtresse PLF Commune"),
        ("02-annexe-faconnages-et-calibres-plf.md", "02_Annexe_Faconnages_Calibres_PLF", "Fiche 02 - Façonnages & Calibres PLF"),
        ("03-fiche-atelier-pain-viennois-nature-et-chocolat-pac.md", "03_Pain_Viennois_Nature_Chocolat_PAC", "Fiche 03 - Pains Viennois PAC"),
        ("04-fiche-atelier-petite-brioche-sucre-pac.md", "04_Petite_Brioche_Sucre_PAC", "Fiche 04 - Petite Brioche au Sucre PAC"),
        ("05-fiche-atelier-kouign-amann.md", "05_Kouign_Amann_Individuel_Partage", "Fiche 05 - Kouign-Amann"),
        ("06-fiche-atelier-feuilletage-inverse-universel.md", "06_Feuilletage_Inverse_Universel", "Fiche 06 - Feuilletage Inversé"),
        ("07-fiche-atelier-galettes-rois-epiphanie-gamme.md", "07_Galettes_Rois_Epiphanie_Gamme", "Fiche 07 - Galettes des Rois Épiphanie"),
        ("08-fiche-atelier-cookies-classique-noisette.md", "08_Cookies_Classique_Noisette", "Fiche 08 - Cookies Coupe-Fil 80 g"),
        ("09-fiche-atelier-muffins-gamme-atelier.md", "09_Muffins_Gamme_Atelier", "Fiche 09 - Muffins Gamme Atelier"),
        ("10-fiche-atelier-brownie-fondant-chocolat.md", "10_Brownie_Fondant_Noix", "Fiche 10 - Brownie Cadres 56x36"),
        ("11-fiche-atelier-brookie-cadres-60x40.md", "11_Brookie_Cadres_56x36", "Fiche 11 - Brookie Cadres 56x36"),
        ("12-fiche-atelier-cakes-de-voyage.md", "12_Cakes_de_Voyage_Mix", "Fiche 12 - Cakes de Voyage"),
        ("13-fiche-atelier-gateau-nantais.md", "13_Gateau_Nantais_OPAL", "Fiche 13 - Gâteau Nantais"),
        ("14-fiche-atelier-crepes-froment-girocrepes.md", "14_Crepes_Froment_Girocrepes", "Fiche 14 - Crêpes Froment Girocrêpes"),
        ("15-fiche-atelier-galettes-ble-noir-girocrepes.md", "15_Galettes_Ble_Noir_Girocrepes", "Fiche 15 - Galettes Blé Noir Girocrêpes"),
        ("16-fiche-atelier-quiches-traiteur.md", "16_Quiches_Traiteur", "Fiche 16 - Quiches Traiteur"),
        ("17-fiche-atelier-dorures-sirops-et-cuissons.md", "17_Dorures_Sirops_Et_Cuissons", "Fiche 17 - Dorures, Sirops & Cuissons"),
    ]

    total_book_pages = 1 + 2 + 2 * len(fiches_ordered)  # 37 pages
    book_chunks = [build_cover_html()] + build_sommaire_pages(total_book_pages)
    cur_page = 4
    for md_name, _, _ in fiches_ordered:
        fpath = os.path.join(FICHES_DIR, md_name)
        book_chunks.extend(parse_fiche_pages(fpath, cur_page, total_book_pages))
        cur_page += 2

    book_html = "\n".join(book_chunks)
    compile_html_to_pdf(book_html, CSS_BOOK_MARGINS, "Cahier_Recettes_Complet_Labo", "Cahier de Production Atelier Direct")
    compile_html_to_pdf(book_html, CSS_BOOK_MARGINS, "cahier_atelier_equipe", "Cahier d'Atelier Équipe - Atelier Direct")

    # PDFs individuels (2 pages strictes par fiche)
    for md_name, out_name, title in fiches_ordered:
        fpath = os.path.join(FICHES_DIR, md_name)
        pages = parse_fiche_pages(fpath, 1, 2)
        compile_html_to_pdf("\n".join(pages), CSS_SHEET_MARGINS, out_name, title)

    # Regroupement historique PLF 01-02 si utilisé par scripts annexes
    plf_pages = parse_fiche_pages(os.path.join(FICHES_DIR, "01-recette-maitresse-plf-commune.md"), 1, 4)
    plf_pages += parse_fiche_pages(os.path.join(FICHES_DIR, "02-annexe-faconnages-et-calibres-plf.md"), 3, 4)
    compile_html_to_pdf("\n".join(plf_pages), CSS_SHEET_MARGINS, "01_02_PLF_Commune_Et_Faconnages", "Fiches 01-02 - PLF Commune & Façonnages")

    print("=> Génération terminée avec succès.")


if __name__ == "__main__":
    build_pdf()
