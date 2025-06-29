
def build_lp_components(ingredients, cp_min, tdn_min, total_weight):
    prices = [ing.price for ing in ingredients]
    cp_values = [ing.cp for ing in ingredients]
    tdn_values = [ing.tdn for ing in ingredients]

    c = prices
    A_ub = [[-cp for cp in cp_values], [-tdn for tdn in tdn_values]]
    b_ub = [-cp_min, -tdn_min]
    A_eq = [[1 for _ in ingredients]]
    b_eq = [total_weight]

    return c, A_ub, b_ub, A_eq, b_eq
