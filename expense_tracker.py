# expense_tracker.py

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("expenses.csv", parse_dates=["Date"])

# Extract month and year
df["Month"] = df["Date"].dt.to_period("M")

# Total spent per category
total_by_category = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
print("\nTotal Spending by Category:")
print(total_by_category)

# Monthly spending trend
monthly_trend = df.groupby(["Month"])["Amount"].sum()

# Plot: Pie chart of total spending by category
plt.figure(figsize=(8, 8))
total_by_category.plot.pie(autopct="%1.1f%%", startangle=140)
plt.title("Spending Breakdown by Category")
plt.ylabel("")
plt.tight_layout()
plt.savefig("spending_pie_chart.png")
plt.show()

# Plot: Monthly trend line chart
plt.figure(figsize=(10, 5))
monthly_trend.plot(marker='o')
plt.title("Total Monthly Spending")
plt.xlabel("Month")
plt.ylabel("Amount (€)")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_spending_trend.png")
plt.show()

print("\nCharts saved as 'spending_pie_chart.png' and 'monthly_spending_trend.png'")
