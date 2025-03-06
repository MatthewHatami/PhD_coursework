import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# Define the function to compute Taylor series approximation
def sin_compare(x, n):
    sin_approx = 0
    for i in range(n + 1):
        term = (-1) ** i * (x ** (2 * i + 1)) / np.math.factorial(2 * i + 1)
        sin_approx += term
    return sin_approx

# Create a linspace between -5 and 5
x = np.linspace(-5, 5, 50)
exact_sine = np.sin(x)

# Different values of m to try
M = [1, 3, 5, 7, 9, 11]

# Plot and compare
for m in M:
    approx_sine = [sin_compare(xi, m) for xi in x]
    plt.plot(x, approx_sine, label=f"m = {m}")

# Plot the exact sine function
plt.plot(x, exact_sine, label="Exact sine", color='black', linestyle='--')

# Add labels and a legend
plt.title('Sine Approximation')
plt.xlabel('x (radians)')
plt.ylabel('sin(x)')
plt.legend()
plt.grid()

# Show the plot
plt.show()
