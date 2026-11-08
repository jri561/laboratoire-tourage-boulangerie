import json
import subprocess
from pathlib import Path
import pypdf

OUTPUT_DIR = Path("Cahier_Recettes_Atelier")
SOURCES_DIR = OUTPUT_DIR / "_sources_html"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
SOURCES_DIR.mkdir(parents=True, exist_ok=True)

# Styles CSS universels d'atelier adaptés à l'insertion sous pochette plastique
CSS_STYLE = """
@page {
  size: A4 portrait;
  margin: 6mm 7mm 6mm 7mm;
}
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
body {
  width: 100%;
  color: #0f172a;
  background: #ffffff;
  font-size: 10.5px;
  line-height: 1.35;
}
.header {
  border-bottom: 2.5px solid #0f172a;
  padding-bottom: 5px;
  margin-bottom: 7px;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}
.header-titles .supertitle {
  font-size: 9.5px;
  font-weight: 700;
  color: #64748b;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}
.header-titles h1 {
  font-size: 17px;
  font-weight: 800;
  color: #0f172a;
  letter-spacing: -0.3px;
  line-height: 1.15;
}
.header-titles .subtitle {
  font-size: 10.5px;
  font-weight: 600;
  color: #334155;
  margin-top: 1px;
}
.badge-code {
  background: #0f172a;
  color: #ffffff;
  padding: 4px 9px;
  border-radius: 4px;
  font-weight: 800;
  font-size: 11px;
  text-align: right;
  white-space: nowrap;
}
.flash-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 5px;
  margin-bottom: 7px;
}
.flash-cell {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-left: 3.5px solid #0284c7;
  padding: 4px 7px;
  border-radius: 3px;
}
.flash-cell.alert-cell {
  border-left-color: #dc2626;
  background: #fff5f5;
}
.flash-cell.amber-cell {
  border-left-color: #d97706;
  background: #fffbeb;
}
.flash-cell.green-cell {
  border-left-color: #16a34a;
  background: #f0fdf4;
}
.flash-label {
  font-size: 8.5px;
  font-weight: 700;
  color: #475569;
  text-transform: uppercase;
  margin-bottom: 1px;
}
.flash-val {
  font-size: 11.5px;
  font-weight: 800;
  color: #0f172a;
}
.alert-box {
  background: #fff7ed;
  border: 1.2px solid #ea580c;
  border-left: 4.5px solid #ea580c;
  padding: 5px 8px;
  border-radius: 4px;
  margin-bottom: 7px;
  font-size: 9.5px;
  color: #7c2d12;
}
.alert-box.danger {
  background: #fef2f2;
  border-color: #dc2626;
  border-left-color: #dc2626;
  color: #7f1d1d;
}
.alert-title {
  font-weight: 800;
  text-transform: uppercase;
  font-size: 9.5px;
  margin-bottom: 1px;
  display: flex;
  align-items: center;
  gap: 4px;
}
.section-title {
  font-size: 11px;
  font-weight: 800;
  color: #0f172a;
  text-transform: uppercase;
  border-left: 3px solid #0284c7;
  padding-left: 5px;
  margin: 6px 0 4px 0;
  letter-spacing: 0.2px;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 6px;
  font-size: 9.5px;
}
th {
  background: #1e293b;
  color: #ffffff;
  padding: 4px 5px;
  text-align: left;
  font-size: 9px;
  font-weight: 700;
  text-transform: uppercase;
  border: 1px solid #1e293b;
}
th.num, td.num {
  text-align: right;
}
td {
  padding: 3.5px 5px;
  border: 1px solid #cbd5e1;
  font-weight: 600;
  color: #0f172a;
}
tr:nth-child(even) td {
  background-color: #f1f5f9;
}
tr.total-row td {
  background: #e2e8f0;
  font-weight: 800;
  color: #0f172a;
  border-top: 1.5px solid #0f172a;
}
.highlight-val {
  font-weight: 800;
  color: #0369a1;
}
.two-cols {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-bottom: 5px;
}
.col-card {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 4px;
  padding: 5px 7px;
}
.col-card-title {
  font-weight: 800;
  font-size: 10px;
  color: #0f172a;
  margin-bottom: 3px;
  text-transform: uppercase;
  border-bottom: 1px solid #e2e8f0;
  padding-bottom: 2px;
}
.steps-list {
  list-style: none;
  font-size: 9.5px;
}
.steps-list li {
  position: relative;
  padding-left: 14px;
  margin-bottom: 3.5px;
}
.steps-list li::before {
  content: "▪";
  position: absolute;
  left: 3px;
  color: #0284c7;
  font-weight: 800;
}
.step-num {
  font-weight: 800;
  color: #0f172a;
}
.footer {
  border-top: 1px solid #cbd5e1;
  padding-top: 3px;
  margin-top: 5px;
  display: flex;
  justify-content: space-between;
  font-size: 8.5px;
  color: #64748b;
  font-weight: 600;
}
"""

print("Base setup ready.")
