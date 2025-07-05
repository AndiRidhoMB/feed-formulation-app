import csv

def export_result_txt(filename, ingredients, result, total_cost):
    with open(filename, "w") as f:
        f.write("Optimal Feed Mix:\n\n")
        f.write(f"{'Ingredient':<20} {'Weight (kg)':>12} {'Price/kg':>10} {'Cost':>10}\n")
        f.write("-" * 55 + "\n")
        for ing, weight in zip(ingredients, result.x):
            cost = weight * ing.price
            f.write(f"{ing.name:<20} {weight:>12.4f} {ing.price:>10,.0f} {cost:>10,.0f}\n")
        f.write("-" * 55 + "\n")
        f.write(f"{'Total Cost':<42} {total_cost:>10,.0f} Rupiah\n")


def export_result_csv(filename, ingredients, result, total_cost):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Ingredient", "Weight (kg)", "Price/kg", "Cost"])
        for ing, weight in zip(ingredients, result.x):
            cost = weight * ing.price
            writer.writerow([ing.name, f"{weight:.4f}", f"{ing.price}", f"{int(cost)}"])
        writer.writerow(["", "", "Total Cost", f"{int(total_cost)} Rupiah"])
