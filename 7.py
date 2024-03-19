import seaborn as sns
import matplotlib.pyplot as plt


# tips = sns.load_dataset("Book1")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [12, 13, 41, 65, 74, 26, 9, 5, 44]



sns.set(style="whitegrid")

# Create a scatter plot using Seaborn
sns.scatterplot(x=x, y=y)


# sns.despine()  
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Scatter Plot of Total Bill vs Tip")

# Show the plot
plt.show()
