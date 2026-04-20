import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("COVID-19 Data Analysis Dashboard")

# Load dataset
df = pd.read_csv('data/covid19tests.csv')

# Clean data
df['tests'] = pd.to_numeric(df['tests'].astype(str).str.replace(',', ''), errors='coerce')
df['positive'] = pd.to_numeric(df['positive'], errors='coerce')
df = df.dropna(subset=['tests', 'positive'])

st.write("Dataset Loaded Successfully ✅")
st.dataframe(df.head())

# Top 10 countries
top = df.sort_values('tests', ascending=False).head(10)

# =====================
# 📊 Bar Chart
# =====================
st.subheader("Top 10 Countries by Tests")

fig1, ax1 = plt.subplots()
ax1.bar(top['country'], top['tests'])
plt.xticks(rotation=45)
st.pyplot(fig1)

# =====================
# 🥧 Pie Chart
# =====================
st.subheader("Test Distribution")

fig2, ax2 = plt.subplots()
ax2.pie(top['tests'], labels=top['country'], autopct='%1.1f%%')
st.pyplot(fig2)

# =====================
# 📈 Scatter Plot
# =====================
st.subheader("Tests vs Positive Cases")

fig3, ax3 = plt.subplots()
ax3.scatter(df['tests'], df['positive'])

z = np.polyfit(df['tests'], df['positive'], 1)
p = np.poly1d(z)
ax3.plot(df['tests'], p(df['tests']))

st.pyplot(fig3)

# =====================
# 🌍 Comparison
# =====================
st.subheader("India vs USA Comparison")

compare = df[df['country'].isin(['India', 'United States'])]

fig4, ax4 = plt.subplots()
ax4.bar(compare['country'], compare['positive'])
st.pyplot(fig4)