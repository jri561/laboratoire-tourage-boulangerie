import os
import re
import html
import subprocess

CSS_PRINT = """
@page {
    size: A4 portrait;
    margin: 12mm 10mm 12mm 10mm;
    @bottom-right {
        content: counter(page);
    }
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #0f172a;
    background-color: #ffffff;
    font-size: 11pt;
    line-height: 1.35;
    margin: 0;
    padding: 0;
}

.page-break {
    page-break-before: always;
    break-before: page;
}

.doc-header {
    border-bottom: 2px solid #0284c7;
    padding-bottom: 6px;
    margin-bottom: 12px;
}

.doc-title {
    font-size: 16pt;
    font-weight: 800;
    color: #0369a1;
    margin: 0 0 4px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.doc-meta {
    font-size: 9pt;
    color: #475569;
    font-weight: 600;
    margin: 0;
}

.section-title {
    font-size: 12pt;
    font-weight: 700;
    color: #0f172a;
    background-color: #f1f5f9;
    padding: 4px 8px;
    border-left: 4px solid #0284c7;
    margin: 12px 0 6px 0;
    text-transform: uppercase;
}

.sub-title {
    font-size: 10.5pt;
    font-weight: 700;
    color: #1e293b;
    margin: 8px 0 4px 0;
}

.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0 12px 0;
    font-size: 9.5pt;
}

.data-table th {
    background-color: #0f172a;
    color: #ffffff;
    font-weight: 700;
    text-align: left;
    padding: 6px 8px;
    border: 1px solid #0f172a;
}

.data-table td {
    padding: 5px 8px;
    border: 1px solid #cbd5e1;
    color: #1e293b;
}

.data-table tr:nth-child(even) {
    background-color: #f8fafc;
}

.callout-box {
    background-color: #f0fdf4;
    border-left: 4px solid #16a34a;
    padding: 6px 10px;
    margin: 6px 0;
    font-size: 9.5pt;
    color: #166534;
    font-weight: 500;
}

.alert-box {
    background-color: #fef2f2;
    border-left: 4px solid #dc2626;
    padding: 6px 10px;
    margin: 6px 0;
    font-size: 9.5pt;
    color: #991b1b;
}

.step-item {
    padding: 4px 0;
    font-size: 10pt;
}

.para {
    margin: 4px 0;
    font-size: 10pt;
}

.action-list {
    margin: 4px 0 8px 18px;
    padding: 0;
    font-size: 9.5pt;
}

.action-list li {
    margin-bottom: 2px;
}

.divider {
    border: 0;
    height: 1px;
    background: #e2e8f0;
    margin: 10px 0;
}
"""

def parse_md_to_html_body(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    lines = md_text.split('\n')
    html_lines = []
    in_table = False
    in_list = False
    
    for line in lines:
        stripped = line.strip()
        
        # Headers
        if stripped.startswith('# '):
            if in_table: html_lines.append('</tbody></table>'); in_table = False
            if in_list: html_lines.append('</ul>'); in_list = False
            title = stripped[2:]
            html_lines.append(f'<div class="doc-header"><h1 class="doc-title">{html.escape(title)}</h1></div>')
            continue
        elif stripped.startswith('## '):
            if in_table: html_lines.append('</tbody></table>'); in_table = False
            if in_list: html_lines.append('</ul>'); in_list = False
            html_lines.append(f'<h2 class="section-title">{html.escape(stripped[3:])}</h2>')
            continue
        elif stripped.startswith('### '):
            if in_table: html_lines.append('</tbody></table>'); in_table = False
            if in_list: html_lines.append('</ul>'); in_list = False
            html_lines.append(f'<h3 class="sub-title">{html.escape(stripped[4:])}</h3>')
            continue
        elif stripped.startswith('---'):
            if in_table: html_lines.append('</tbody></table>'); in_table = False
            if in_list: html_lines.append('</ul>'); in_list = False
            html_lines.append('<hr class="divider"/>')
            continue
            
        # Tables
        if '|' in stripped and not stripped.startswith('```'):
            parts = [p.strip() for p in stripped.split('|')[1:-1]]
            if not parts:
                continue
            if all(re.match(r'^:?-+:?$', p) for p in parts):
                continue
            
            if not in_table:
                in_table = True
                html_lines.append('<table class="data-table">')
                th_cols = "".join(f'<th>{re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", p)}</th>' for p in parts)
                html_lines.append(f'<thead><tr>{th_cols}</tr></thead><tbody>')
            else:
                td_cols = "".join(f'<td>{re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", p)}</td>' for p in parts)
                html_lines.append(f'<tr>{td_cols}</tr>')
            continue
        else:
            if in_table:
                html_lines.append('</tbody></table>')
                in_table = False

        # Lists
        if stripped.startswith('* ') or stripped.startswith('- '):
            if not in_list:
                in_list = True
                html_lines.append('<ul class="action-list">')
            item_text = stripped[2:]
            item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
            html_lines.append(f'<li>{item_text}</li>')
            continue
        elif re.match(r'^\d+\.\s+', stripped):
            if in_list: html_lines.append('</ul>'); in_list = False
            item_text = re.sub(r'^\d+\.\s+', '', stripped)
            item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
            num = stripped.split()[0]
            html_lines.append(f'<div class="step-item"><strong>{num}</strong> {item_text}</div>')
            continue
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False

        # Callouts
        if stripped.startswith('> '):
            b_text = stripped[2:]
            b_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', b_text)
            html_lines.append(f'<div class="callout-box">{b_text}</div>')
            continue

        if stripped.startswith('```'):
            continue

        if stripped:
            p_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', stripped)
            html_lines.append(f'<p class="para">{p_text}</p>')

    if in_table: html_lines.append('</tbody></table>')
    if in_list: html_lines.append('</ul>')
    return '\n'.join(html_lines)

def generate_pdf_from_md_files(md_filenames, output_name, title, fiches_dir, export_dir):
    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>{CSS_PRINT}</style>
</head>
<body>
"""
    count = 0
    for fname in md_filenames:
        fpath = os.path.join(fiches_dir, fname)
        if os.path.exists(fpath):
            if count > 0:
                full_html += '<div class="page-break"></div>\n'
            full_html += parse_md_to_html_body(fpath)
            count += 1
            
    full_html += "</body></html>"
    
    html_out = os.path.join(export_dir, f"{output_name}.html")
    pdf_out = os.path.join(export_dir, f"{output_name}.pdf")
    
    with open(html_out, 'w', encoding='utf-8') as f:
        f.write(full_html)
        
    cmd = [
        'google-chrome',
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        f'--print-to-pdf={pdf_out}',
        html_out
    ]
    subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_out):
        print(f"  [PDF OK] {output_name}.pdf ({os.path.getsize(pdf_out):,} octets)")
        return pdf_out
    return None

def build_pdf():
    base_dir = '/home/toto/.gemini/antigravity/scratch/laboratoire-tourage-boulangerie'
    fiches_dir = os.path.join(base_dir, 'recettes/fiches_atelier_operateurs')
    export_dir = os.path.join(base_dir, 'exports_pdf')
    os.makedirs(export_dir, exist_ok=True)
    
    print("=== GÉNÉRATION DES PDFS D'ATELIER ET DU CAHIER COMPLET ===")
    
    # 1. Cahier complet équipe
    all_fiches = [
        '00-sommaire-classeur-atelier.md',
        '01-recette-maitresse-plf-commune.md',
        '02-annexe-faconnages-et-calibres-plf.md',
        '04-fiche-atelier-pain-viennois-nature-et-chocolat-pac.md',
        '05-fiche-atelier-petite-brioche-sucre-pac.md',
        '06-fiche-atelier-brioche-fine-nanterre.md',
        '07-fiche-atelier-kouign-amann.md',
        '08-fiche-atelier-feuilletage-inverse-universel.md',
        '09-fiche-atelier-galettes-rois-epiphanie-gamme.md',
        '03-annexe-baremes-generaux-cuisson.md'
    ]
    generate_pdf_from_md_files(all_fiches, 'cahier_atelier_equipe', "Cahier d'Atelier Équipe - Laboratoire Tourage & Boulangerie", fiches_dir, export_dir)
    generate_pdf_from_md_files(all_fiches, 'Cahier_Recettes_Complet_Labo', "Cahier de Recettes Complet - Laboratoire de Tourage", fiches_dir, export_dir)

    # 2. Fiches individuelles d'atelier
    fiches_map = [
        (['01-recette-maitresse-plf-commune.md', '02-annexe-faconnages-et-calibres-plf.md'], '06_PLF_Pret_A_Cuire_PAC', "Fiche Atelier 01-02 - Pâte Levée Feuilletée PAC"),
        (['07-fiche-atelier-kouign-amann.md'], '03_Kouign_Amann_Cru_Surgele', "Fiche Atelier 07 - Kouign-Amann"),
        (['07-fiche-atelier-kouign-amann.md'], '07_fiche_atelier_kouign_amann', "Fiche Atelier 07 - Kouign-Amann"),
        (['04-fiche-atelier-pain-viennois-nature-et-chocolat-pac.md'], '04_Viennoise_Nature_Chocolat_PAC', "Fiche Atelier 04 - Pain Viennois"),
        (['08-fiche-atelier-feuilletage-inverse-universel.md'], '05_Feuilletage_Inverse', "Fiche Atelier 08 - Feuilletage Inversé"),
        (['08-fiche-atelier-feuilletage-inverse-universel.md'], '08_fiche_atelier_feuilletage_inverse', "Fiche Atelier 08 - Feuilletage Inversé"),
        (['06-fiche-atelier-brioche-fine-nanterre.md'], '06_Brioche_Fine_Nanterre', "Fiche Atelier 06 - Brioche Fine Nanterre"),
        (['05-fiche-atelier-petite-brioche-sucre-pac.md'], '15_Brioches_Individuelles_Sucre_PAC', "Fiche Atelier 05 - Petite Brioche Individuelle Sucre"),
        (['09-fiche-atelier-galettes-rois-epiphanie-gamme.md'], '09_fiche_atelier_galettes_rois_epiphanie', "Fiche Atelier 09 - Galettes des Rois Épiphanie"),
        (['09-fiche-atelier-galettes-rois-epiphanie-gamme.md'], '10_Frangipane_Galette_Rois', "Fiche Atelier 09 - Galettes des Rois & Frangipane"),
        (['03-annexe-baremes-generaux-cuisson.md'], '16_Registre_General_Cuissons_Atelier', "Annexe 03 - Registre Général Cuissons Atelier"),
    ]

    for md_list, out_name, title in fiches_map:
        generate_pdf_from_md_files(md_list, out_name, title, fiches_dir, export_dir)

    print("=> Génération de tous les PDFs terminée avec succès.")

if __name__ == '__main__':
    build_pdf()
