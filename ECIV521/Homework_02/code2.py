## section 1: importing the libraries we will use later
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from numpy import pi







## section 2: Doing the calculations
# Define the function sinx/x with special handling for x=0
def f(x):
    return np.where(np.abs(x) < 1e-10, 1.0, np.sin(x)/x)  # the notation is like: np.where(condition, value if true, value if false)

# Trapezoidal method using vector notation
def trapezoidal(f, a, b, n):
    h = (b - a) / n                  # this is the step size
    x = np.linspace(a, b, n+1)       # this is the array of x values
    y = f(x)
    return h * (0.5 * y[0] + 0.5 * y[-1] + np.sum(y[1:-1])) # this is the trapezoidal rule formula



# Midpoint method using vector notation
def midpoint(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a + h/2, b - h/2, n)  # Midpoints of each interval
    y = f(x)
    return h * np.sum(y)


# Calculate the exact value using scipy's quad
exact_value, _ = quad(f, 0, pi)
print(f"Exact value: {exact_value:.10f}")







## section 3: Evaluating and comparing the results from the two methods
# Test with different numbers of intervals
n_values = [5, 10, 25, 50, 75, 100]
trap_results = [] # this will store the results of the trapezoidal method
mid_results = []  # this will store the results of the midpoint method
trap_errors = []  # this will store the errors of the trapezoidal method
mid_errors = []   # this will store the errors of the midpoint method




# now we loop over different values of n and calculate the results and erros for each method
for n in n_values:
    trap_result = trapezoidal(f, 0, pi, n) # compute the integral using trapezoidal method
    mid_result = midpoint(f, 0, pi, n)     # compute the integral using midpoint method
    
    trap_error = abs(trap_result - exact_value) # computing error for trapezoidal 
    mid_error = abs(mid_result - exact_value)   # computing error for midpoint 
    
    trap_results.append(trap_result)   # storing the results
    mid_results.append(mid_result)     # storing the results
    trap_errors.append(trap_error)     # storing the errors
    mid_errors.append(mid_error)       # storing the errors
    
    # print the results to the console as well
    print(f"\nIntervals (n): {n}")
    print(f"Trapezoidal result: {trap_result:.10f}, Error: {trap_error:.10e}")
    print(f"Midpoint result: {mid_result:.10f}, Error: {mid_error:.10e}")







# section 4: Plotting the results
# Create a single plot for method comparison
plt.figure(figsize=(10, 6))
plt.plot(n_values, [r - exact_value for r in trap_results], 'o-', label='Trapezoidal Error')
plt.plot(n_values, [r - exact_value for r in mid_results], 's-', label='Midpoint Error')
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.xlabel('Number of intervals (n)')
plt.ylabel('Error (Method - Exact)')
plt.legend()
plt.grid(True)
plt.title('Comparison of Errors')
plt.tight_layout()

# Save the plot as a PDF file
plt.savefig('numerical_integration_comparison.pdf')
plt.show()

