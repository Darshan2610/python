import matplotlib.pyplot as plt 

def linear_plot():
# Sample data
    x = [1, 2, 3, 4, 5]
    y = [3, 7, 9, 11, 14]
    # Plotting the data
    plt.plot(x, y, label='Linear Function: y = 2x')


    # Adding labels and title 
    plt.xlabel('X-axis') 
    plt.ylabel('Y-axis') 
    plt.title('Linear Plot Example') 
    plt.legend()
    plt.show()


# Call the function to generate the plot
linear_plot()
