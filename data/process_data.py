import pandas as pd
import os

# Read all CSV files in this folder
files = [f for f in os.listdir(".") if f.endswith(".csv")]

data = []

for file in files:
    df = pd.read_csv(file)
    data.append(df)

# Combine all data into one table
combined = pd.concat(data)

# Keep only Pink Morsels
pink = combined[combined["product"] == "Pink Morsels"]

# Create Sales column
pink["Sales"] = pink["quantity"] * pink["price"]

# Keep required columns only
final = pink[["Sales", "date", "region"]]
final.columns = ["Sales", "Date", "Region"]

# Save final CSV
final.to_csv("formatted_sales_data.csv", index=False)

print("Done! New file created.")
