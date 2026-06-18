import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas

# Read data
df = pd.read_csv("sales.csv")

# Calculate total sales
total_sales = df["Sales"].sum()

# Create chart
plt.figure(figsize=(8,5))
plt.plot(df["Date"], df["Sales"], marker="o")
plt.title("Weekly Sales Report")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.savefig("sales_chart.png")
plt.close()

# Create PDF
pdf = canvas.Canvas("Weekly_Report.pdf")

pdf.drawString(100,750,"Weekly Sales Report")
pdf.drawString(100,720,f"Total Sales: {total_sales}")

pdf.drawImage(
    "sales_chart.png",
    50,
    400,
    width=450,
    height=250
)

pdf.save()

print("PDF Report Created Successfully!")