import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and a grid of subplots
fig, axs = plt.subplots(2, 1)  # 2 rows, 1 column

# Plot data on the first subplot
axs[0].plot(x, y1, color="blue")
axs[0].set_title("Plot of sin(x)")

# Plot data on the second subplot
axs[1].plot(x, y2, color="red")
axs[1].set_title("Plot of cos(x)")

# Show the plot
plt.tight_layout()
plt.show()
