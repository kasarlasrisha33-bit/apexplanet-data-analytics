import pandas as pd

# Load data
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

# Data cleaning
df.drop_duplicates(inplace=True)

# KPI calculations
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# Export KPIs
kpi = pd.DataFrame({
    "Metric": ["Total Sales", "Total Profit"],
    "Value": [total_sales, total_profit]
})

kpi.to_excel("kpi_report.xlsx", index=False)

print("Automation completed successfully!")
