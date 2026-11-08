#!/usr/bin/env python3
"""
Calculateur de Fournée & Balance Thermique (TB)
Laboratoire R&D Tourage, Boulangerie & Viennoiserie

Permet de :
1. Calculer les pesées exactes d'une recette en fonction du nombre de bacs (calibrage 8,00 kg net / bac).
2. Calculer la Température de Base (TB) et la répartition Eau froide / Glace paillette.
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
    
    # Si T_eau_theorique < 3 °C, il faut substituer une partie par de la glace paillette.
    # Équivalence frigorifique : 1 kg de glace paillette à 0 °C apporte environ 80 kcal de froid.
    # Formule d'atelier : Glace (kg) = Eau_totale * (4 - T_eau_theorique) / (80 + 4)
    manque_froid = max(0.0, 4.0 - t_eau_theorique)
    glace_kg = (hydratation_kg * manque_froid) / 84.0
    glace_kg = min(glace_kg, hydratation_kg * 0.40) # Plafond à 40% de l'eau totale max
    eau_liquide_kg = hydratation_kg - glace_kg

    return {
        "t_eau_theorique": round(t_eau_theorique, 1),
        "eau_liquide_kg": round(eau_liquide_kg, 2),
        "glace_kg": round(glace_kg, 2),
        "remarque": f"Alerte thermique ! Eau théorique à {round(t_eau_theorique, 1)} °C requiert de la glace paillette."
    }

def main():
    parser = argparse.ArgumentParser(description="Calculateur d'atelier PLF — Laboratoire Tourage & Boulangerie")
    parser.add_argument("--bacs", type=int, default=1, help="Nombre de bacs de détrempe (ex: 1, 10, 20)")
    parser.add_argument("--t-piece", type=float, default=22.0, help="Température ambiante du labo (°C)")
    parser.add_argument("--t-farine", type=float, default=20.0, help="Température de la farine (°C)")
    parser.add_argument("--petrin-delta", type=float, default=12.0, help="Échauffement mécanique pétrin spirale (°C)")
    parser.add_argument("--tb", type=float, default=52.0, help="Température de base visée (50 à 52 °C pour sortie 18–20 °C)")
    
    args = parser.parse_args()

    # Formule normalisée d'atelier PLF PAC :
    # 1 bac = 4 400 g farine Gruau T45 pour 8 000 g détrempe et 2 000 g beurre tourage (Total 10 kg pâton)
    coef = args.bacs
    farine_kg = coef * 4.400
    eau_totale_kg = coef * 1.950
    sucre_kg = coef * 0.400
    poudre_lait_kg = coef * 0.180
    trimoline_kg = coef * 0.160
    kimo_short_kg = coef * 0.130
    sel_kg = coef * 0.090
    vinaigre_kg = coef * 0.040
    levure_or_kg = coef * 0.250
    margarine_opale_kg = coef * 0.400
    
    detrempe_totale_kg = (farine_kg + eau_totale_kg + sucre_kg + poudre_lait_kg +
                          trimoline_kg + kimo_short_kg + sel_kg + vinaigre_kg +
                          levure_or_kg + margarine_opale_kg)
    
    beurre_tourage_kg = coef * 2.000
    paton_toure_total_kg = detrempe_totale_kg + beurre_tourage_kg

    bilan_froid = calculer_glace_eau(
        tb_cible=args.tb,
        t_ambiant=args.t_piece,
        t_farine=args.t_farine,
        echauffement_petrin=args.petrin_delta,
        hydratation_kg=eau_totale_kg
    )

    print("=" * 70)
    print(f"LABORATOIRE TOURAGE & BOULANGERIE : FEUILLE DE PESÉE — {args.bacs} BAC(S)")
    print(f"Procédé : PLF Prêt-à-Cuire (PAC) — Pâtons de 8,00 kg net / bac")
    print("=" * 70)
    print("PHASE 1 • CUVE FRASAGE V1 (14 min) :")
    print(f"  - Farine de Gruau T45 (100,0 %)       : {farine_kg:7.2f} kg ({farine_kg*1000:6.0f} g)")
    print(f"  - Eau totale calculée (44,32 %)       : {eau_totale_kg:7.2f} kg ({eau_totale_kg*1000:6.0f} g)")
    print(f"      > Dont Eau liquide (+1 °C)        : {bilan_froid['eau_liquide_kg']:7.2f} kg")
    print(f"      > Dont Glace paillette            : {bilan_froid['glace_kg']:7.2f} kg")
    print(f"  - Sucre semoule (9,09 %)              : {sucre_kg:7.2f} kg ({sucre_kg*1000:6.0f} g)")
    print(f"  - Poudre de lait entier 26% (4,09 %)  : {poudre_lait_kg:7.2f} kg ({poudre_lait_kg*1000:6.0f} g)")
    print(f"  - Trimoline / Inverti (3,64 %)        : {trimoline_kg:7.2f} kg ({trimoline_kg*1000:6.0f} g)")
    print(f"  - Améliorant Kimo Short (2,95 %)      : {kimo_short_kg:7.2f} kg ({kimo_short_kg*1000:6.0f} g)")
    print(f"  - Sel fin d'atelier (2,05 %)          : {sel_kg:7.2f} kg ({sel_kg*1000:6.0f} g) [Isolé]")
    print(f"  - Vinaigre d'alcool blanc (0,91 %)    : {vinaigre_kg:7.2f} kg ({vinaigre_kg*1000:6.0f} g)")
    print(f"  - Levure fraîche Or (5,68 %)          : {levure_or_kg:7.2f} kg ({levure_or_kg*1000:6.0f} g)")
    print("-" * 70)
    print("PHASE 2 • INCORPORATION V2 (2 min) :")
    print(f"  - Margarine OPALE (9,09 %)            : {margarine_opale_kg:7.2f} kg ({margarine_opale_kg*1000:6.0f} g)")
    print("-" * 70)
    print(f"SOUS-TOTAL DÉTREMPE ({args.bacs} bacs x 8,00 kg) : {detrempe_totale_kg:7.2f} kg")
    print("-" * 70)
    print("PHASE 3 • TOURAGE (2 TOURS DOUBLES AU LAMINOIR) :")
    print(f"  - Beurre sec tourage 84% (Plaques 2kg): {beurre_tourage_kg:7.2f} kg ({args.bacs} plaque(s))")
    print("=" * 70)
    print(f"POIDS TOTAL PÂTON TOURÉ                 : {paton_toure_total_kg:7.2f} kg ({paton_toure_total_kg/args.bacs:.1f} kg / bac)")
    croissants_75g = int(paton_toure_total_kg / 0.075 * 0.98) # Rendement net avec 2% de chutes
    print(f"Rendement estimé (~75 g cru net)        : ~{croissants_75g} croissants")
    print(f"Diagnostic Thermique : {bilan_froid['remarque']}")
    print("=" * 70)

if __name__ == "__main__":
    main()
