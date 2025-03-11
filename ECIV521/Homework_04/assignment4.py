import numpy as np

# Channel parameters
length = 1500  # channel length in meters
b = 10  # bed width in meters
m = 0.5  # side slope (horizontal:vertical)
n = 0.016  # Manning's coefficient
S0 = 0.00020  # bed slope (20 cm/km)
num_reaches = 10
dx = length / num_reaches  # spatial step
g = 9.81  # gravitational acceleration

# Initial conditions
y = np.array([2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.57, 2.46, 2.19, 0.97])
v = np.array([1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.48, 1.70, 2.09, 3.94])

# Calculate areas
def calculate_area(y):
    return (b + m * y) * y

# Calculate time step based on CFL condition
def calculate_time_step():
    celerity = np.sqrt(g * y)
    max_val = np.max(np.abs(v) + celerity)
    dt_max = dx / max_val
    return 0.8 * dt_max  # Using 80% of max for stability

# Apply Lax diffusive scheme
def lax_diffusive_scheme(dt):
    y_new = np.copy(y)
    v_new = np.copy(v)
    
    # Calculate discharges
    A = np.array([calculate_area(yi) for yi in y])
    Q = A * v
    
    # Update internal points
    for i in range(1, len(y)-1):
        # Continuity equation
        y_new[i] = 0.5 * (y[i+1] + y[i-1]) - 0.5 * (dt/dx) * (Q[i+1] - Q[i-1])
        
        # Momentum equation
        v_new[i] = 0.5 * (v[i+1] + v[i-1]) - 0.5 * (dt/dx) * (
            v[i+1]**2 - v[i-1]**2 + g * (y[i+1] - y[i-1])
        )
    
    return y_new, v_new

# Calculate appropriate time step
dt = calculate_time_step()
print(f"Time step: {dt:.2f} seconds")

# Perform one step of Lax scheme
y_next, v_next = lax_diffusive_scheme(dt)

# Print results for sections 7, 8, and 9 (indices 6, 7, and 8)
print("\nWater depths at next time step:")
print(f"Section 7: {y_next[6]:.4f} m")
print(f"Section 8: {y_next[7]:.4f} m")
print(f"Section 9: {y_next[8]:.4f} m")