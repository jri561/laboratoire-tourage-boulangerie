#!/usr/bin/env python3
"""
Calculateur de Fournée & Balance Thermique (TB)
Laboratoire R&D Tourage, Boulangerie & Viennoiserie

Standard Usine PLF Semi-Industrielle :
- Coupage Meunier 70 % Gruau T45 / 30 % T65 Tradition (sans E300)
- Cryoprotection : Trimoline 3,5 %, Levure Or 4,2 %, S500 Kimo Short 2,0 %
- Calibrage : 8,00 kg net de détrempe / bac Paneo (galette 3 cm) + 2,00 kg beurre tourage = 10,00 kg pâton touré
"""

import sys
import argparse

def calculer_glace_eau(tb_cible, t_ambiant, t_farine, echauffement_petrin, hydratation_kg):
    """
    Calcule la température théorique de l'eau nécessaire et la masse de glace paillette
    si l'eau requise est sous 3 °C.
    Chaleur latente de fusion de la glace : ~80 kcal/kg (ou ~334 kJ/kg).
    Formule pratique de boulangerie :
    T_eau_theorique = TB_cible - (T_ambiant + T_farine + echauffement_petrin)
    """
    t_eau_theorique = tb_cible - (t_ambiant + t_farine + echauffement_petrin)
    
    if t_eau_theorique >= 3.0:
        return {
            "t_eau_theorique": round(t_eau_theorique, 1),
            "eau_liquide_kg": round(hydratation_kg, 2),
            "glace_kg": 0.0,
            "remarque": f"Eau de coulage à {round(t_eau_theorique, 1)} °C sans glace requise."
        }
    
    # Si T_eau_theorique < 3 °C, il faut substituer une fraction par de la glace paillette.
    manque_froid = max(0.0, 4.0 - t_eau_theorique)
    glace_kg = (hydratation_kg * manque_froid) / 84.0
    glace_kg = min(glace_kg, hydratation_kg * 0.40) # Plafond de sécurité à 40% de l'eau totale
    eau_liquide_kg = hydratation_kg - glace_kg

    return {
        "t_eau_theorique": round(t_eau_theorique, 1),
        "eau_liquide_kg": round(eau_liquide_kg, 2),
        "glace_kg": round(glace_kg, 2),
        "remarque": f"Alerte thermique ! Eau théorique à {round(t_eau_theorique, 1)} °C requiert de la glace paillette."
    }

def main():
    parser = argparse.ArgumentParser(description="Calculateur d'Atelier PLF Semi-Industrielle (40 Bacs / Jour)")
    parser.add_argument("--bacs", type=int, default=1, help="Nombre de bacs Paneo (1 à 20 bacs, défaut: 1)")
    parser.add_argument("--t-piece", type=float, default=22.0, help="Température ambiante du laboratoire (°C)")
    parser.add_argument("--t-farine", type=float, default=20.0, help="Température de la farine (°C)")
    parser.add_argument("--petrin-delta", type=float, default=12.0, help="Échauffement pétrin spirale plein volume (°C)")
    parser.add_argument("--tb", type=float, default=52.0, help="Température de base visée (50 à 52 °C pour sortie 20–21 °C)")
    
    args = parser.parse_args()

    # Formule Étalon Atelier :
    # 20 bacs = 89,50 kg farine totale (62,65 kg Gruau + 26,85 kg T65 Trad) -> 160 kg détrempe
    coef = args.bacs / 20.0
    gruau_t45_kg = coef * 62.650
    trad_t65_kg = coef * 26.850
    farine_totale_kg = gruau_t45_kg + trad_t65_kg

    eau_totale_kg = coef * 40.275
    sucre_kg = coef * 7.875
    trimoline_kg = coef * 3.130
    levure_or_kg = coef * 3.760
    poudre_lait_kg = coef * 3.580
    kimo_short_kg = coef * 1.790
    sel_kg = coef * 1.790
    vinaigre_kg = coef * 0.715
    mg_cuve_kg = coef * 7.605

    detrempe_totale_kg = (farine_totale_kg + eau_totale_kg + sucre_kg + trimoline_kg +
                          levure_or_kg + poudre_lait_kg + kimo_short_kg + sel_kg +
                          vinaigre_kg + mg_cuve_kg)

    beurre_tourage_kg = args.bacs * 2.000
    paton_toure_total_kg = detrempe_totale_kg + beurre_tourage_kg

    bilan_froid = calculer_glace_eau(
        tb_cible=args.tb,
        t_ambiant=args.t_piece,
        t_farine=args.t_farine,
        echauffement_petrin=args.petrin_delta,
        hydratation_kg=eau_totale_kg
    )

    print("=" * 72)
    print(f"LABORATOIRE TOURAGE & BOULANGERIE : FEUILLE DE PESÉE — {args.bacs} BAC(S) PANEO")
    print(f"Standard Étalon : PLF PAC Semi-Industrielle (1 Bac = 8,00 kg net / galette 3 cm)")
    print("=" * 72)
    print("PHASE 1 • CUVE FRASAGE V1 (5 min lente) :")
    print(f"  - Farine de Gruau T45 (70,0 % / W>330)   : {gruau_t45_kg:7.2f} kg ({gruau_t45_kg*1000:6.0f} g)")
    print(f"  - Farine T65 Tradition pure (30,0 %)    : {trad_t65_kg:7.2f} kg ({trad_t65_kg*1000:6.0f} g) [Zéro E300]")
    print(f"  >>> TOTAL FARINE (100,0 %)              : {farine_totale_kg:7.2f} kg ({farine_totale_kg*1000:6.0f} g)")
    print(f"  - Eau totale calculée (45,0 %)          : {eau_totale_kg:7.2f} kg ({eau_totale_kg*1000:6.0f} g)")
    print(f"      > Dont Eau liquide (+1 °C)          : {bilan_froid['eau_liquide_kg']:7.2f} kg")
    print(f"      > Dont Glace paillette              : {bilan_froid['glace_kg']:7.2f} kg")
    print(f"  - Sucre cristal semoule (8,8 %)         : {sucre_kg:7.2f} kg ({sucre_kg*1000:6.0f} g)")
    print(f"  - Trimoline / Sucre inverti (3,5 %)     : {trimoline_kg:7.2f} kg ({trimoline_kg*1000:6.0f} g)")
    print(f"  - Levure fraîche L'Hirondelle Or (4,2 %): {levure_or_kg:7.2f} kg ({levure_or_kg*1000:6.0f} g) [Osmotolérante]")
    print(f"  - Poudre de lait entier 26% MG (4,0 %)  : {poudre_lait_kg:7.2f} kg ({poudre_lait_kg*1000:6.0f} g)")
    print(f"  - Améliorant S500 Kimo Short (2,0 %)    : {kimo_short_kg:7.2f} kg ({kimo_short_kg*1000:6.0f} g) [Plafonné]")
    print(f"  - Sel fin d'atelier (2,0 %)             : {sel_kg:7.2f} kg ({sel_kg*1000:6.0f} g) [Balance isolée]")
    print(f"  - Vinaigre blanc d'alcool 8° (0,8 %)    : {vinaigre_kg:7.2f} kg ({vinaigre_kg*1000:6.0f} g) [Anti-PPO]")
    print("-" * 72)
    print("PHASE 2 • INCORPORATION V2 (4 min 30 à 5 min rapide) :")
    print(f"  - Matière grasse cuve (8,5 %)           : {mg_cuve_kg:7.2f} kg ({mg_cuve_kg*1000:6.0f} g)")
    print("-" * 72)
    print(f"SOUS-TOTAL DÉTREMPE ({args.bacs} bac(s) x 8,00 kg)   : {detrempe_totale_kg:7.2f} kg")
    print("-" * 72)
    print("PHASE 3 • TOURAGE (RONDO COMPAS : 1 TOUR DOUBLE + 1 TOUR SIMPLE) :")
    print(f"  - Beurre sec tourage 84% (Plaques 2 kg) : {beurre_tourage_kg:7.2f} kg ({args.bacs} plaque(s) de 2 kg)")
    print("=" * 72)
    print(f"POIDS TOTAL PÂTON TOURÉ (12 films / 25-30 µm)  : {paton_toure_total_kg:7.2f} kg ({paton_toure_total_kg/args.bacs:.2f} kg / bac)")
    croissants = int((paton_toure_total_kg * 0.98) / 0.075)
    pains_choc = int((paton_toure_total_kg * 0.98) / 0.075) # 75 g de pâte crue par pièce
    boites_160 = round(pains_choc / 160.0, 1)
    chocolat_kg = pains_choc * 0.010

    pains_raisins = int((paton_toure_total_kg * 0.98) / 0.055) # 55 g de pâte crue par pièce
    creme_raisins_kg = pains_raisins * 0.020
    poudre_creme_raisins_kg = creme_raisins_kg * 0.259
    eau_creme_raisins_kg = creme_raisins_kg * 0.741
    raisins_kg = pains_raisins * 0.015

    pains_suisses = int((paton_toure_total_kg * 0.98) / 0.070) # 70 g de pâte crue par pièce
    creme_suisse_kg = pains_suisses * 0.035
    poudre_creme_suisse_kg = creme_suisse_kg * 0.259
    pepites_kg = pains_suisses * 0.015

    oranais = int((paton_toure_total_kg * 0.98) / 0.060) # 60 g de pâte crue par pièce
    creme_oranais_kg = oranais * 0.025
    oreillons_nb = oranais * 2
    abricots_kg = oranais * 0.015

    cinnamon_rolls = int((paton_toure_total_kg * 0.98) / 0.055) # 55 g de pâte crue par pièce
    appareil_cannelle_kg = cinnamon_rolls * 0.020
    beurre_cannelle_kg = appareil_cannelle_kg * 0.40
    cassonade_kg = appareil_cannelle_kg * 0.50
    cannelle_kg = appareil_cannelle_kg * 0.10

    cruffins = int((paton_toure_total_kg * 0.98) / 0.080) # 80 g de pâte crue par pièce

    print("-" * 72)
    print("RENDEMENTS D'ATELIER ESTIMÉS SI PRODUCTION DÉDIÉE (après parage 2 %) :")
    print(f"  > 1. CROISSANTS D'EXCELLENCE (75 g cru) : ~{croissants} pièces")
    print(f"  > 2. PAINS AU CHOCOLAT 1 BARRE (85 g brut : 75 g pâte + 10 g barre 160) :")
    print(f"      - Quantité produite              : ~{pains_choc} pains au chocolat")
    print(f"      - Besoin en barres calibre 160    : ~{pains_choc} barres ({chocolat_kg:.2f} kg) | ~{boites_160} boîte(s)")
    print(f"  > 3. PAINS AUX RAISINS ESCARGOTS (90 g brut : 55 g pâte + 20 g crème + 15 g raisins) :")
    print(f"      - Quantité produite              : ~{pains_raisins} escargots")
    print(f"      - Crème pâtissière à froid       : {creme_raisins_kg:6.2f} kg ({poudre_creme_raisins_kg:.2f} kg poudre)")
    print(f"      - Raisins secs bruts (non trempés): {raisins_kg:6.2f} kg")
    print(f"  > 4. PAINS SUISSES (120 g brut : 70 g pâte + 35 g crème + 15 g pépites) :")
    print(f"      - Quantité produite              : ~{pains_suisses} pièces")
    print(f"      - Crème pâtissière à froid       : {creme_suisse_kg:6.2f} kg ({poudre_creme_suisse_kg:.2f} kg poudre)")
    print(f"      - Pépites chocolat 50 %          : {pepites_kg:6.2f} kg")
    print(f"  > 5. ORANAIS AUX ABRICOTS (100 g brut : 60 g pâte + 25 g crème + 15 g abricots) :")
    print(f"      - Quantité produite              : ~{oranais} pièces")
    print(f"      - Crème pâtissière à froid       : {creme_oranais_kg:6.2f} kg")
    print(f"      - Demi-oreillons égouttés        : ~{oreillons_nb} oreillons ({abricots_kg:6.2f} kg)")
    print(f"  > 6. CINNAMON ROLLS FEUILLETÉS (75 g brut : 55 g pâte + 20 g appareil cannelle) :")
    print(f"      - Quantité produite en caissettes: ~{cinnamon_rolls} pièces")
    print(f"      - Appareil Beurre/Cannelle/Cass. : {appareil_cannelle_kg:6.2f} kg (Beurre: {beurre_cannelle_kg:.2f}kg, Cassonade: {cassonade_kg:.2f}kg, Cannelle: {cannelle_kg:.2f}kg)")
    print(f"  > 7. CRUFFINS ATELIER (80 g brut de pâte tourée) :")
    print(f"      - Quantité produite en alvéoles  : ~{cruffins} cruffins")
    print("-" * 72)
    print(f"Diagnostic Thermique : {bilan_froid['remarque']}")
    print("=" * 72)

if __name__ == "__main__":
    main()
