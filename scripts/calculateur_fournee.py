#!/usr/bin/env python3
"""
Calculateur de Fournée & Balance Thermique (TB)
Laboratoire R&D Tourage, Boulangerie & Viennoiserie

Permet de :
1. Calculer les pesées exactes d'une recette en fonction du nombre de bacs ou du poids total.
2. Calculer la Température de Base (TB) et la répartition Eau froide / Glace paillette.
"""

import sys
import argparse

def calculer_glace_eau(tb_cible, t_ambiant, t_farine, echauffement_petrin, hydratation_kg):
    """
    Calcule la température théorique de l'eau nécessaire et la masse de glace paillette
    si l'eau requise est sous 0°C.
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
    
    # Si T_eau_theorique < 3°C, il faut substituer une partie par de la glace paillette.
    # Règle d'équivalence thermique : 1 kg de glace paillette à 0°C refroidit comme
    # une chute d'environ 80°C répartie sur la masse d'eau.
    # Formule simplifiée d'atelier : Glace (kg) = Eau_totale * (4 - T_eau_theorique) / (80 + 4)
    manque_froid = max(0.0, 4.0 - t_eau_theorique)
    glace_kg = (hydratation_kg * manque_froid) / 84.0
    glace_kg = min(glace_kg, hydratation_kg * 0.40) # Plafond à 40% de l'hydratation max
    eau_liquide_kg = hydratation_kg - glace_kg

    return {
        "t_eau_theorique": round(t_eau_theorique, 1),
        "eau_liquide_kg": round(eau_liquide_kg, 2),
        "glace_kg": round(glace_kg, 2),
        "remarque": f"Alerte thermique ! Eau théorique à {round(t_eau_theorique, 1)} °C impossible sans glace."
    }

def main():
    parser = argparse.ArgumentParser(description="Calculateur d'atelier boulangerie")
    parser.add_argument("--bacs", type=int, default=1, help="Nombre de bacs de détrempe (ex: 1, 10, 20)")
    parser.add_argument("--t-piece", type=float, default=22.0, help="Température ambiante du labo (°C)")
    parser.add_argument("--t-farine", type=float, default=20.0, help="Température de la farine (°C)")
    parser.add_argument("--petrin-delta", type=float, default=12.0, help="Échauffement mécanique pétrin (°C)")
    parser.add_argument("--tb", type=float, default=54.0, help="Température de base visée")
    
    args = parser.parse_args()

    # Base PLF PAC 1 bac de 8 kg = ~4.74 kg de farine totale
    farine_totale_kg = args.bacs * 4.740
    eau_totale_kg = farine_totale_kg * 0.450

    bilan_froid = calculer_glace_eau(
        tb_cible=args.tb,
        t_ambiant=args.t_piece,
        t_farine=args.t_farine,
        echauffement_petrin=args.petrin_delta,
        hydratation_kg=eau_totale_kg
    )

    print("=" * 65)
    print(f"LABORATOIRE R&D : CALCUL DE FOURNÉE POUR {args.bacs} BAC(S)")
    print("=" * 65)
    print(f"Farine Totale (100 %) : {farine_totale_kg:.2f} kg")
    print(f"  - Gruau T45 (70 %)  : {farine_totale_kg * 0.70:.2f} kg")
    print(f"  - T65 Trad  (30 %)  : {farine_totale_kg * 0.30:.2f} kg")
    print("-" * 65)
    print("BILAN HYDRIQUE ET THERMIQUE :")
    print(f"Eau totale calculée (45 %) : {eau_totale_kg:.2f} kg")
    print(f"  > Eau liquide (+1 °C)    : {bilan_froid['eau_liquide_kg']} kg")
    print(f"  > Glace paillette        : {bilan_froid['glace_kg']} kg")
    print(f"Diagnostic : {bilan_froid['remarque']}")
    print("-" * 65)
    print(f"Beurre de tourage (25 % détrempe) : {args.bacs * 2.00:.2f} kg")
    print("=" * 65)

if __name__ == "__main__":
    main()
