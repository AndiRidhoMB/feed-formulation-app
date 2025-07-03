import pandas as pd

def get_user_selected_ingredients(filepath):
    # Load the full ingredient list
    df = pd.read_csv(filepath, sep=';', engine='python')
    df.columns = df.columns.str.strip()

    # Create a list of ingredient names
    ingredient_names = df["Ingredients"].tolist()

    # Print numbered list for user to select
    print("Available ingredients:")
    for idx, name in enumerate(ingredient_names, start=1):
        print(f"{idx}. {name}")

    # User input
    while True:
        user_input = input("\nSelect ingredients by their number (e.g., 1,3,5):\n")

        if len(user_input) < 5:
            print("⚠️ Please select at least 3 ingredients.")
            continue

        if "," not in user_input:
            print("⚠️ Invalid format. Use commas to separate numbers (e.g., 1,3,5).")
            continue

        selected_indices = [i.strip() for i in user_input.split(",")]

        if not all(i.isdigit() for i in selected_indices):
            print("⚠️ Input must contain only numbers.")
            continue

        selected_indices = [int(i) for i in selected_indices]

        if len(selected_indices) < 3:
            print("⚠️ You must select at least 3 ingredients.")
            continue

        if any(i < 1 or i > len(ingredient_names) for i in selected_indices):
            print(f"⚠️ Numbers must be between 1 and {len(ingredient_names)}.")
            continue

        break  # All checks passed

    selected_ingredients = [ingredient_names[i - 1] for i in selected_indices]
    return selected_ingredients


def get_user_nutrient_requirements():
    while True:
        try:
            cp_min = float(input("Enter minimum CP% (e.g., 16.0): "))
            tdn_min = float(input("Enter minimum TDN% (e.g., 70.0): "))
            total_weight = float(input("Enter total feed weight in kg (e.g., 1.0): "))
            return cp_min, tdn_min, total_weight
        except ValueError:
            print("Invalid input. Please enter numeric values.")


