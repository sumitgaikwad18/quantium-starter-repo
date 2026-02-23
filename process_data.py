import pandas as pd
import os

# Correct folder where CSV files exist
data_folder = "data"

files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

data = []

for file in files:
    df = pd.read_csv(os.path.join(data_folder, file))
    data.append(df)

# Combine all CSVs
combined = pd.concat(data)

# Keep only Pink Morsels
pink = combined[combined["product"] == "Pink Morsels"]

# Create Sales column
pink["Sales"] = pink["quantity"] * pink["price"]

# Keep needed columns
final = pink[["Sales", "date", "region"]]
final.columns = ["Sales", "Date", "Region"]

# Save output in main folder
final.to_csv("formatted_sales_data.csv", index=False)

print("Done! File created successfully.")
