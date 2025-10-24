# Import required packages
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.stats import norm

# Step 1: Load Dataset
df = pd.read_csv(r"C:\Users\PSVCS01\Desktop\FDS\Plotting functions.csv")

# -------------------- Normal Curve --------------------
mean = df['time_in_hospital'].mean()
std = df['time_in_hospital'].std()
x_axis = np.arange(1, 10, 0.01)

plt.figure()
plt.plot(x_axis, norm.pdf(x_axis, mean, std))
plt.title('Normal Distribution Curve - time_in_hospital')
plt.show()

# -------------------- Density and Contour Plots --------------------
df.time_in_hospital.plot.density(color='green')
plt.title('Density plot for time_in_hospital')
plt.show()

df.num_lab_procedures.plot.density(color='green')
plt.title('Density Plot for num_lab_procedures')
plt.show()

df.num_medications.plot.density(color='green')
plt.title('Density Plot for num_medications')
plt.show()

df.number_emergency.plot.kde(color='green')
plt.title('KDE-Density plot for number_emergency')
plt.show()

# Contour plot


def func(x, y):
    return np.sin(x) ** 2 + np.cos(y) ** 2


x = np.linspace(0, 10, 50)
y = np.linspace(0, 10, 50)
X, Y = np.meshgrid(x, y)
Z = func(X, Y)

plt.figure()
plt.contour(X, Y, Z, cmap='gist_rainbow_r')
plt.title('Rectangular Contour Plot')
plt.show()

# -------------------- Correlation and Scatter Plot --------------------
plt.figure(figsize=(20, 10))
# Select numeric columns only
numeric_df = df.select_dtypes(include=[np.number])
sb.heatmap(numeric_df.corr(), cmap="YlGnBu", annot=True)
plt.title('Correlation Heatmap')
plt.show()


# -------------------- Histograms --------------------
df.hist(figsize=(12, 12), layout=(5, 5))
plt.show()

sb.distplot(df['num_lab_procedures'], kde=False)
plt.title('Histogram for num_lab_procedures')
plt.show()

# -------------------- 3D Plot --------------------

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x = df['number_emergency']
y = df['number_inpatient']
z = df['number_outpatient']

ax.plot3D(x, y, z, 'green')
ax.set_title('3D line plot diabetes dataset')
plt.show()
