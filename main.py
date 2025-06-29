from utils.data_loader import load_selected_ingredients
from utils.optimizer_input import build_lp_components
from scipy.optimize import linprog



def main():
    selected = ["Elephant Grass", "Soybean Meal", "Rice Husk Bran", "Wheat Pollard"]
    cp_min = 16.0
    tdn_min = 70.0
    total_weight = 1.0

    ingredients = load_selected_ingredients("data/ingredients.csv", selected)
    c, A_ub, b_ub, A_eq, b_eq = build_lp_components(ingredients, cp_min, tdn_min, total_weight)

    result = linprog(
    c=c,
    A_ub=A_ub,
    b_ub=b_ub,
    A_eq=A_eq,
    b_eq=b_eq,
    bounds=[(0, None)] * len(c),  # [(0, None)] is a tuple range: it means from 0 up to infinity. * len(c) repeats that same range once for each ingredient.
    method="highs"
    )

    if result.success is False:
        print("Optimization failed:", result.message)
    else:
        print("\nOptimal Feed Mix:\n")
        print(f"{'Ingredient':<20} {'Weight (kg)':>12} {'Price/kg':>10} {'Cost':>10}")
        print("-" * 55)

        total_cost = 0
        for ing, weight in zip(ingredients, result.x):
            cost = weight * ing.price
            total_cost += cost
            print(f"{ing.name:<20} {weight:>12.4f} {ing.price:>10,.0f} {cost:>10,.0f}")

        print("-" * 55)
        print(f"{'Total Cost':<42} {total_cost:>10,.0f} Rupiah\n")



if __name__ == "__main__":
    main()
