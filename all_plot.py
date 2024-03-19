import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
dt = pd.read_csv("rain.csv")
df = pd.read_csv("dataa.csv")

# Histogram
# plt.figure(figsize=(8, 6))
# plt.hist(dt['temp'], bins=7, color="skyblue", edgecolor="black")
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.grid(True)
# plt.show()

# Bar Plot
plt.figure(figsize=(8, 6))
plt.bar(df["Name"], df["Score"], color="green")
plt.title("Scores of Individuals")
plt.xlabel("Name")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(df["Height(cm)"], df["Weight(kg)"], color="red", marker="o")
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.show()

# Line Plot
plt.figure(figsize=(8, 6))
plt.plot(df["Name"], df["Age"], marker="o", linestyle="-", color="purple")
plt.title("Age of Individuals")
plt.xlabel("Name")
plt.ylabel("Age")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
