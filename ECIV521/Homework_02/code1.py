## section 1: importing libraries
import numpy as np
import matplotlib.pyplot as plt





## section 2: reading the input
# we don't have a specific input in this code, so we carry on with next section







## section 3: Doing the calculations
# defining the function from the homework text
def f(x):
    return (np.arcsin(np.sin(2 * np.pi * x)) + np.arccos(np.cos(2 * np.pi * x))) / (2 * np.pi)


# Generate x values as multiples of pi from -3π to 3π to keep consistent with the plot in the homework pdf file
x_vals = np.linspace(-3, 3, 600)  # Changed from -2,2 to -3,3 and 600 points
y_vals = f(x_vals) # Calculate y values using the function we defined earlier








## section 4: Plotting the results
# Create the plot using matplotlib library
plt.figure(figsize=(10, 5))  
plt.plot(x_vals * np.pi, y_vals) # changing the x lables to be multiples of pi


# modifying x-axis ticks to show multiples of π from -3π to 3π
pi_ticks = np.arange(-3, 4, 1)  # Changed to go from -3 to 3
pi_labels = [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$']  # Added -3π and 3π labels
plt.xticks(pi_ticks * np.pi, pi_labels)


# fixing laabels and grid
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x)")
plt.legend()
plt.grid()
plt.show()