import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv("book1.csv")

# Histogram
plt.hist(data["km"], bins=5, color="blue", edgecolor="black")
plt.xlabel("km")
plt.ylabel("days")
plt.title("Histogram Plot")
plt.yticks()
plt.show()

# Pie Chart
plt.pie(data["Percentages"], labels=data["Labels"], autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart")
plt.show()


# Bar Plot
plt.bar(data["Category"], data["Values"])
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Bar Plot")
plt.show()

# Scatter Plot
plt.scatter(data["X"], data["Y"])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.show()
