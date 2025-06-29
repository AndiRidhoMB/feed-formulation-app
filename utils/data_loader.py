import pandas as pd
from models.ingredient import Ingredient


def load_selected_ingredients(filepath, selected_names):
    df = pd.read_csv(filepath, sep=';', engine='python')
    df.columns = df.columns.str.strip()
    df_selected = df[df["Ingredients"].isin(selected_names)]

    ingredients = []
    for _, row in df_selected.iterrows():
        ing = Ingredient(row["Ingredients"], row["CP %"], row["TDN %"], row["Price (In Indonesia rupiah per kg)"])
        ingredients.append(ing)

    return ingredients
