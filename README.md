# 🐄 Feed Formulation App
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Built with Pandas](https://img.shields.io/badge/pandas-powered-lightgrey.svg)](https://pandas.pydata.org/)
[![Optimization Engine](https://img.shields.io/badge/solver-scipy.optimize-orange)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)

A feed formulation tool for livestock, built in Python.  
The app calculates the **cheapest optimal feed mix** using linear programming, ensuring **minimum crude protein (CP%) and total digestible nutrients (TDN%)** are met — either via a **terminal interface** or a **Streamlit-based GUI**.

---

## 🚀 Features

- ✅ Choose feed ingredients from a CSV file
- ✅ Input minimum CP%, TDN%, and feed weight
- ✅ Automatically calculates the lowest-cost feed formula using `scipy.optimize.linprog`
- ✅ Ensures all selected ingredients are used at **minimum 1%** of total feed
- ✅ Warns if nutrient targets exceed the potential of selected ingredients
- ✅ Clean output formatting
- ✅ Export results to **TXT** or **CSV**
- ✅ Streamlit GUI for easier interaction
- 🔄 Terminal (CLI) alternative for minimal setup

---

## 🧱 Project Structure

```
feed-formulation-app/
│
├── data/
│   └── ingredients.csv
│
├── models/
│   └── ingredient.py            # Ingredient class definition
│
├── utils/
│   ├── data_loader.py           # Load and filter ingredient data
│   ├── input_handler.py         # Handle user input (ingredients + nutrients)
│   ├── optimizer_input.py       # Build optimization matrices
│   └── output_exporter.py       # Export to TXT/CSV
│
├── app.py                       # ✅ Streamlit GUI interface
├── cli_runner.py                # 🖥 Terminal-based version
├── requirements.txt             # Dependency list
└── README.md                    # You're here!
```

---

## 📦 Requirements

Install all dependencies:

```bash
pip install -r requirements.txt
```

Includes:
- `numpy`
- `pandas`
- `scipy`
- `streamlit`

Other standard libraries (e.g., `os`, `sys`) are built into Python.

---

## ▶️ How to Use

### 🔷 Option 1: Run with Streamlit (GUI)

```bash
streamlit run app.py
```

Features:
- ✅ Select ingredients via checkboxes
- ✅ Enter nutrient requirements interactively
- ✅ View optimized feed results in a clean table
- ✅ Export to `.csv` or `.txt`

### 🔷 Option 2: Use the Terminal (CLI)

```bash
python cli_runner.py
```

Step-by-step:

1. View all available ingredients from the `ingredients.csv`
2. Select by entering numbers (e.g., `2, 5, 7`)
3. Enter:
   - Minimum CP%
   - Minimum TDN%
   - Total feed weight (kg)
4. View optimized feed mix
5. Optionally export as `.txt` or `.csv`

---

## 📄 Data File Format

Your `ingredients.csv` must be `;`-separated and contain these headers:

```csv
Ingredients;DM;CP %;TDN %;Price (In Indonesia rupiah per kg)
Rice Husk Bran;89.3;13.8;81.0;300
Wheat Pollard;88.1;13.2;86.0;4000
Soybean Meal;87.6;46.9;83.2;6500
...
```

⚠️ Tips:
- Clean header names (no extra spaces)
- Add/modify rows as needed

---

## 📌 Notes

- Total feed weight is in **kg**
- Nutrient constraints are **minimums**
- Each ingredient is required to contribute at least **1% of total feed**
- If your nutrient requirement is **too high**, the program will notify you
- Optimization uses the `highs` method in `scipy.optimize.linprog`

---

## 📤 Export Options

After solving:

- `.txt`: Plain text summary (easy to read/share)
- `.csv`: Spreadsheet-compatible format (for Excel, Google Sheets)

You'll be prompted to:
- Choose format
- Enter file name or path (e.g., `output/formula.txt`)
