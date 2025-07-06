import streamlit as st
import pandas as pd
from utils.data_loader import load_selected_ingredients
from utils.optimizer_input import build_lp_components
from scipy.optimize import linprog
from models.ingredient import Ingredient
from io import StringIO

# Load all ingredient names
@st.cache_data
def load_all_ingredient_names(filepath):
    df = pd.read_csv(filepath, sep=';', engine='python')
    df.columns = df.columns.str.strip()
    return df['Ingredients'].tolist(), df

# Display optimization result
def display_result(ingredients, result, total_cost):
    st.subheader("✅ Optimal Feed Mix")
    table_data = []
    for ing, weight in zip(ingredients, result.x):
        cost = weight * ing.price
        table_data.append({
            "Ingredient": ing.name,
            "Weight (kg)": f"{weight:.4f}",
            "Price/kg (Rp)": f"{ing.price:,.0f}",
            "Cost (Rp)": f"{cost:,.0f}"
        })
    df_result = pd.DataFrame(table_data)
    st.table(df_result)
    st.success(f"💰 Total Cost: Rp {total_cost:,.0f}")
    return df_result

# Build ingredients from selected names
def get_selected_ingredients(df_all, selected_names):
    ingredients = []
    for _, row in df_all[df_all["Ingredients"].isin(selected_names)].iterrows():
        ing = Ingredient(row["Ingredients"], row["CP %"], row["TDN %"], row["Price (In Indonesia rupiah per kg)"])
        ingredients.append(ing)
    return ingredients

# Export as text
def generate_txt(df_result, total_cost):
    output = StringIO()
    output.write("Optimal Feed Mix:\n")
    output.write(df_result.to_string(index=False))
    output.write(f"\n\nTotal Cost: Rp {total_cost:,.0f}")
    return output.getvalue()

# --- Streamlit App ---
st.set_page_config(page_title="Feed Formulation Optimizer", layout="centered")
st.title("🐄 Feed Formulation App")
st.caption("Formulate optimal livestock feed based on cost and nutrient requirements")

# File & Ingredient Selection
filepath = "data/ingredients.csv"
ingredient_names, df_all = load_all_ingredient_names(filepath)
selected = st.multiselect("✅ Select Ingredients", ingredient_names)

if selected:
    st.markdown("### 🧪 Set Nutrient Requirements")
    cp_min = st.number_input("Minimum CP (%)", value=16.0)
    tdn_min = st.number_input("Minimum TDN (%)", value=70.0)
    total_weight = st.number_input("Total Feed Weight (kg)", value=1.0)

    ingredients = get_selected_ingredients(df_all, selected)
    max_cp = max(ing.cp for ing in ingredients)
    max_tdn = max(ing.tdn for ing in ingredients)

    st.info(f"Max possible CP%: {max_cp:.2f} | Max possible TDN%: {max_tdn:.2f}")

    if cp_min > max_cp or tdn_min > max_tdn:
        st.error("❌ Nutrient requirement exceeds the limit based on selected ingredients.")
        st.stop()

    c, A_ub, b_ub, A_eq, b_eq = build_lp_components(ingredients, cp_min, tdn_min, total_weight)
    min_weight = total_weight * 0.01  # 1% minimum per ingredient

    result = linprog(
        c=c,
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=[(min_weight, None)] * len(c),
        method="highs"
    )

    if result.success:
        total_cost = sum(weight * ing.price for ing, weight in zip(ingredients, result.x))
        df_result = display_result(ingredients, result, total_cost)

        # Export option
        st.markdown("### 💾 Export Result")
        format = st.selectbox("Choose format", ["TXT", "CSV"])
        filename = st.text_input("Enter file name", value="feed_result")

        if format == "TXT":
            txt_content = generate_txt(df_result, total_cost)
            st.download_button(
                label="📥 Download TXT",
                data=txt_content,
                file_name=f"{filename}.txt",
                mime="text/plain"
            )
        elif format == "CSV":
            csv_content = df_result.to_csv(index=False)
            st.download_button(
                label="📥 Download CSV",
                data=csv_content,
                file_name=f"{filename}.csv",
                mime="text/csv"
            )
    else:
        st.error(f"❌ Optimization failed: {result.message}")
else:
    st.warning("Please select at least one ingredient to get started.")
