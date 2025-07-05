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
- ✅ Ensures all selected ingredients are used at **minimum 1%** of the total feed
- ✅ Warns user if nutrient targets exceed possible maximums based on selected ingredients
- ✅ Clean, readable output in the terminal
- ✅ Option to export results to **TXT** or **CSV**
- 🔜 Future: GUI with Streamlit or Tkinter

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
│ ├── optimizer_input.py # Build optimization matrices
│ └── output_exporter.py # Export results to .txt or .csv
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

Step-by-step:
✅ View a list of available ingredients from ingredients.csv

📋 Select ingredients by entering their numbers (e.g., 2,5,7)

🧪 Enter nutrient requirements:

Minimum CP%

Minimum TDN%

Total feed weight (in kg)

⚠️ If your requirements exceed what’s possible, you’ll be notified

🧠 Get the optimal feed mix that meets requirements at the lowest cost

📤 Optionally, export the result as .txt or .csv


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
Total feed weight is in kg

Feed optimization:

Must meet or exceed CP% and TDN% targets

Uses only your selected ingredients

Each ingredient must contribute at least 1% of total feed

Goal is to minimize total cost

The app will notify you if your nutrient targets are not feasible with your selection


## 📤 Export Options

After generating results, you’ll be prompted to export:

.txt: Plain text summary

.csv: Spreadsheet-friendly output

Simply choose the format and provide a file name or path (e.g., output/result.txt or output/formula.csv).
