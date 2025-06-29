from utils.data_loader import load_selected_ingredients
from utils.optimizer_input import build_lp_components


def main():
    selected = ["Elephant Grass", "Soybean Meal", "Rice Husk Bran", "Wheat Pollard"]
    cp_min = 16.0
    tdn_min = 70.0
    total_weight = 1.0

    ingredients = load_selected_ingredients("data/ingredients.csv", selected)
    c, A_ub, b_ub, A_eq, b_eq = build_lp_components(ingredients, cp_min, tdn_min, total_weight)


if __name__ == "__main__":
    main()
