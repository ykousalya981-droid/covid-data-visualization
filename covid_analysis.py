import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("STARTED")

# Load dataset
df = pd.read_csv('data/covid19tests.csv')

print("DATA LOADED")

# Clean numeric columns
df['tests'] = pd.to_numeric(df['tests'].astype(str).str.replace(',', ''), errors='coerce')
df['positive'] = pd.to_numeric(df['positive'], errors='coerce')

# Remove missing values
df = df.dropna(subset=['tests', 'positive'])

print("Rows after cleaning:", len(df))

# ===============================
# 📊 Top 10 Countries (Bar Chart)
# ===============================
top = df.sort_values('tests', ascending=False).head(10)

plt.figure(figsize=(12,6))
plt.bar(top['country'], top['tests'])
plt.title("Top 10 Countries by COVID Tests")
plt.xlabel("Country")
plt.ylabel("Tests")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add values
for i, v in enumerate(top['tests']):
    plt.text(i, v, str(int(v)), ha='center', va='bottom')

plt.tight_layout()
plt.show()

# ===============================
# 🥧 Pie Chart
# ===============================
plt.figure(figsize=(7,7))
plt.pie(top['tests'], labels=top['country'], autopct='%1.1f%%')
plt.title("Test Distribution (Top 10 Countries)")
plt.show()

# =====================================
# 📈 Scatter Plot + Trend Line
# =====================================
plt.figure(figsize=(8,5))
plt.scatter(df['tests'], df['positive'])

# Trend line
z = np.polyfit(df['tests'], df['positive'], 1)
p = np.poly1d(z)
plt.plot(df['tests'], p(df['tests']))

plt.title("Tests vs Positive Cases")
plt.xlabel("Tests")
plt.ylabel("Positive Cases")
plt.grid(alpha=0.5)

plt.show()


plt.figure(figsize=(6,5))
plt.title("India vs USA - Positive Cases")
plt.ylabel("Positive Cases")
plt.show()

print("DONE")