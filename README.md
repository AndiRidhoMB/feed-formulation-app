# 🐄 Feed Formulation App
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Built with Pandas](https://img.shields.io/badge/pandas-powered-lightgrey.svg)](https://pandas.pydata.org/)
[![Optimization Engine](https://img.shields.io/badge/solver-scipy.optimize-orange)](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)

A terminal-based Python application for livestock feed formulation. This app helps users select feed ingredients and calculate the **optimal feed mix** that satisfies **minimum nutrient requirements** (Crude Protein and Total Digestible Nutrients) at the **lowest cost**, using **linear programming**.

---

## 🚀 Features

- ✅ Choose feed ingredients from a CSV file
- ✅ Input minimum CP% and TDN% requirements
- ✅ Specify total feed weight (kg)
- ✅ Automatically calculates the cheapest feed mix using `scipy.optimize.linprog`
- ✅ Ensures all selected ingredients are utilized
- ✅ Clean, readable result formatting
- 🔜 Future plans: Export results to CSV / GUI interface

---

## 🧱 Project Structure
feed-formulation-app/
│
├── data/
│ └── ingredients.csv
│
├── models/
│ └── ingredient.py # Ingredient class definition
│
├── utils/
│ ├── data_loader.py # Load and filter ingredient data
│ ├── input_handler.py # Handle user input (ingredients + nutrients)
│ └── optimizer_input.py # Build optimization matrices
│
├── main.py # Main script to run the app
├── requirements.txt # Python dependencies
└── README.md # You're here!


---

## 📦 Requirements

Install all required dependencies using:
pip install -r requirements.txt

Dependencies include:
pandas
scipy
(Other modules like os, sys, etc. are built-in to Python.)


## ▶️ How to Use
Run the app:
python main.py

Step-by-step flow:
✅ View a list of available ingredients (from ingredients.csv)

🧠 Select ingredients by entering their numbers (e.g., 2, 5, 7)

🧪 Enter nutrient requirements:

Minimum CP%

Minimum TDN%

Total feed weight in kilograms

📊 Get the optimal feed mix based on your inputs


## 📄 Data File Format
Your ingredients.csv must be in ;-separated format with columns like:
Ingredients;DM;CP %;TDN %;Price (In Indonesia rupiah per kg)
Rice Husk Bran;89.3;13.8;81.0;300
Wheat Pollard;88.1;13.2;86.0;4000
Soybean Meal;87.6;46.9;83.2;6500
...

Important:
Ensure column headers are clean (no extra spaces).
You can update or add new ingredients to this file.

## 📌 Notes
The total feed weight must be in kg.

The optimization ensures that the feed:

Meets or exceeds CP% and TDN% targets

Uses only the ingredients you selected

Minimizes total cost

The program prevents solutions that use 0 kg of all but one ingredient.


