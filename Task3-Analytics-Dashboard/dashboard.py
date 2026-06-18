import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "Department": ["Sales", "Marketing", "HR", "Finance"],
    "Value": [400, 300, 200, 100]
}

df = pd.DataFrame(data)

# Bar Chart
plt.figure(figsize=(6,4))
plt.bar(df["Department"], df["Value"])
plt.title("Department Performance")
plt.savefig("bar_chart.png")
plt.close()

# Pie Chart
plt.figure(figsize=(6,4))
plt.pie(
    df["Value"],
    labels=df["Department"],
    autopct="%1.1f%%"
)
plt.title("Department Distribution")
plt.savefig("pie_chart.png")
plt.close()

print("Dashboard charts created successfully!")