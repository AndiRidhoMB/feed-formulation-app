from utils.data_loader import load_selected_ingredients
from utils.optimizer_input import build_lp_components
from utils.input_handler import get_user_selected_ingredients, get_user_nutrient_requirements
from scipy.optimize import linprog
from utils.output_exporter import export_result_txt, export_result_csv



def main():
    while True:
        # Step 1: User selects ingredients
        selected = get_user_selected_ingredients("data/ingredients.csv")

        # Step 2: User sets nutrient requirements
        cp_min, tdn_min, total_weight = get_user_nutrient_requirements()
        min_weight = total_weight * 0.01  # 1% of total weight
        max_weight = total_weight * 0.7   # 70% max



        # Step 3: Load selected ingredient data
        ingredients = load_selected_ingredients("data/ingredients.csv", selected)

        # Step 4: Nutrient feasibility check
        max_cp = max(ing.cp for ing in ingredients)
        max_tdn = max(ing.tdn for ing in ingredients)
        print(f"\n⚠️  Based on your selected ingredients:")
        print(f"- Max possible CP%: {max_cp:.2f}%")
        print(f"- Max possible TDN%: {max_tdn:.2f}%\n")

        if cp_min > max_cp or tdn_min > max_tdn:
            print("❌ Your nutrient requirement exceeds what's possible with selected ingredients.")
            print("Please choose different ingredients or lower your requirement.\n")
            retry = input("Do you want to try again? (y/n): ").strip().lower()
            if retry != 'y':
                print("Exiting program.")
                return
            continue

        # Step 5: Build LP components and solve
        c, A_ub, b_ub, A_eq, b_eq = build_lp_components(ingredients, cp_min, tdn_min, total_weight)

        result = linprog(
            c=c,
            A_ub=A_ub,
            b_ub=b_ub,
            A_eq=A_eq,
            b_eq=b_eq,
            bounds = [(min_weight, max_weight)] * len(c),  # use at least 1% of total for each ingredient
            method="highs"
        )

        if not result.success:
            print("❌ Optimization failed:", result.message)
            retry = input("Do you want to try again? (y/n): ").strip().lower()
            if retry == 'y':
                continue
            print("Exiting program.")
            return

        # Step 6: Display Results
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
        break  # Exit after successful run

    # Ask user if they want to export
    export = input("Would you like to export the result? (y/n): ").strip().lower()
    if export == 'y':
        format_choice = input("Choose format: (1) TXT, (2) CSV): ").strip()
        file_path = input("Enter file name or full path (e.g., output/result.txt): ").strip()

        if format_choice == '1':
            export_result_txt(file_path, ingredients, result, total_cost)
            print(f"✅ Exported to '{file_path}'\n")
        elif format_choice == '2':
            export_result_csv(file_path, ingredients, result, total_cost)
            print(f"✅ Exported to '{file_path}'\n")
        else:
            print("❌ Invalid format. Export skipped.\n")



if __name__ == "__main__":
    main()
