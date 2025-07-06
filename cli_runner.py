"""
📦 Terminal Version of Feed Formulation App
--------------------------------------------------
This is the CLI version of the Feed Formulation App.
For GUI version, run:
    streamlit run app.py
"""

from utils.data_loader import load_selected_ingredients
from utils.optimizer_input import build_lp_components
from utils.input_handler import get_user_selected_ingredients, get_user_nutrient_requirements
from utils.output_exporter import export_result_txt, export_result_csv
from scipy.optimize import linprog


def main():
    print("📦 Feed Formulation App (Terminal Version)\n")

    selected = get_user_selected_ingredients("data/ingredients.csv")
    cp_min, tdn_min, total_weight = get_user_nutrient_requirements()

    min_weight = total_weight * 0.01
    max_weight = total_weight * 0.7

    ingredients = load_selected_ingredients("data/ingredients.csv", selected)

    max_cp = max(ing.cp for ing in ingredients)
    max_tdn = max(ing.tdn for ing in ingredients)
    print(f"\n⚠️  Based on selected ingredients:")
    print(f"- Max CP%: {max_cp:.2f}%")
    print(f"- Max TDN%: {max_tdn:.2f}%\n")

    if cp_min > max_cp or tdn_min > max_tdn:
        print("❌ Nutrient requirement exceeds what's achievable with selected ingredients.")
        return

    c, A_ub, b_ub, A_eq, b_eq = build_lp_components(ingredients, cp_min, tdn_min, total_weight)

    result = linprog(
        c=c,
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=[(min_weight, max_weight)] * len(c),
        method="highs"
    )

    if not result.success:
        print("❌ Optimization failed:", result.message)
        return

    # Output results
    print("\n✅ Optimal Feed Mix:\n")
    print(f"{'Ingredient':<20} {'Weight (kg)':>12} {'Price/kg':>10} {'Cost':>10}")
    print("-" * 55)

    total_cost = 0
    for ing, weight in zip(ingredients, result.x):
        cost = weight * ing.price
        total_cost += cost
        print(f"{ing.name:<20} {weight:>12.4f} {ing.price:>10,.0f} {cost:>10,.0f}")

    print("-" * 55)
    print(f"{'Total Cost':<42} {total_cost:>10,.0f} Rupiah\n")

    # Export
    export = input("Export result? (y/n): ").strip().lower()
    if export == 'y':
        format_choice = input("Format: (1) TXT, (2) CSV: ").strip()
        file_path = input("Save to (e.g., output/result.txt): ").strip()

        if format_choice == '1':
            export_result_txt(file_path, ingredients, result, total_cost)
        elif format_choice == '2':
            export_result_csv(file_path, ingredients, result, total_cost)
        else:
            print("❌ Invalid format. Export skipped.")
            return

        print(f"✅ Result exported to '{file_path}'\n")


if __name__ == "__main__":
    main()
