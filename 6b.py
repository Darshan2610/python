import matplotlib.pyplot as plt


def formatted_linear_plot():
    # Sample data
    x = [1, 2, 3, 4, 5, 6]
    y = [3, 7, 9, 11, 14, 18]
    plt.plot(
        x, y, marker="h", linestyle="-", color="b", label="Linear Function: y = 2x"
    )
    # Adding labels and title
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Formatted Linear Plot Example")
    plt.legend()
    plt.grid(True)  # Add a grid for better readability
    plt.show()


# Call the function to generate the formatted linear plot
formatted_linear_plot()
