import pandas as pd
from models.ingredient import Ingredient


def main():
    df = pd.read_csv("data/ingredients.csv", sep=';', engine='python')
    df.columns = df.columns.str.strip()

    selected = ["Elephant Grass", "Soybean Meal", "Rice Husk Bran", "Wheat Pollard"]
    # Filter the DataFrame
    df_selected = df[df["Ingredients"].isin(selected)]

    ingredients = []
    for _, row in df_selected.iterrows():
        ing = Ingredient(row["Ingredients"], row["CP %"], row["TDN %"], row["Price (In Indonesia rupiah per kg)"])
        ingredients.append(ing)

    cp_per_kg = []
    tdn_per_kg = []
    prices = []
    for ing in ingredients:
        cp_per_kg.append(ing.cp)
        tdn_per_kg.append(ing.tdn)
        prices.append(ing.price)
    
    cp_min = 16.0
    tdn_min = 70.0
    total_weight = 1.0

    c = prices

    A_ub = [
        [-cp for cp in cp_per_kg],   # CP constraint
        [-tdn for tdn in tdn_per_kg] # TDN constraint
    ]
    b_ub = [-cp_min, -tdn_min]

    A_eq = [[1 for _ in ingredients]]
    b_eq = [total_weight]
    

if __name__ == "__main__":
    main()

