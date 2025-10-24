# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import joblib # optional if saving models

# Step 1: Load dataset
df = pd.read_csv(r"C:\Users\PSVCS01\Desktop\FDS\Using Data.csv")

# Step 2: Display first few rows
print("\n--- Head ---")
print(df.head())

# Step 3: Frequency count of Glucose
print("\n--- Value Counts of Glucose ---")
print(df['Glucose'].value_counts())

# Step 4: Descriptive statistics
print("\n--- Describe ---")
print(df.describe())

print("\n--- Mean ---")
print(df.mean())

print("\n--- Median ---")
print(df.median())

print("\n--- Mode ---")
print(df.mode().iloc[0])

print("\n--- Variance ---")
print(df.var())

print("\n--- Standard Deviation ---")
print(df.std())

print("\n--- Skewness ---")
print(df.skew())

print("\n--- Kurtosis ---")
print(df.kurtosis())

# Step 5: Correlation Matrix
corr = df.corr()
print("\n--- Correlation Matrix ---")
print(corr)

# Heatmap of correlation
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="plasma", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Step 6: Outcome Distribution
sns.countplot(x="Outcome", data=df)
plt.title("Diabetes Outcome Distribution (0 = Non-diabetic, 1 = Diabetic)")
plt.show()

# Step 7: % of diabetic vs non-diabetic
Out1 = len(df[df['Outcome'] == 1])
Out0 = len(df[df['Outcome'] == 0])
Total = Out1 + Out0
print(f"\n% Non-Diabetic: {Out0/Total*100:.2f}%")
print(f"% Diabetic: {Out1/Total*100:.2f}%")

# Step 8: Triangular correlation heatmap
plt.figure(dpi=120, figsize=(5,4))
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, cmap="plasma", fmt=".2f")
plt.title("Correlation Heatmap (Triangular)")
plt.xticks(rotation=90)
plt.yticks(rotation=0)
