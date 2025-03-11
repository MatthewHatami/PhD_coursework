import numpy as np
import matplotlib.pyplot as plt

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
y_initial = np.array([2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.63, 2.57, 2.46, 2.19, 0.97])
v_initial = np.array([1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.48, 1.70, 2.09, 3.94])

def calculate_area(y):
    """Calculate cross-sectional area for trapezoidal channel"""
    return (b + m * y) * y

def calculate_wetted_perimeter(y):
    """Calculate wetted perimeter for trapezoidal channel"""
    return b + 2 * y * np.sqrt(1 + m**2)

def calculate_hydraulic_radius(y):
    """Calculate hydraulic radius"""
    return calculate_area(y) / calculate_wetted_perimeter(y)

def calculate_discharge(y, v):
    """Calculate discharge Q = A*V"""
    return calculate_area(y) * v

def calculate_celerity(y):
    """Calculate wave celerity c = sqrt(g*y)"""
    return np.sqrt(g * y)

def calculate_time_step(y, v):
    """Calculate appropriate time step based on CFL condition"""
    celerity = calculate_celerity(y)
    max_velocity_plus_celerity = np.max(np.abs(v) + celerity)
    dt_max = dx / max_velocity_plus_celerity
    return 0.8 * dt_max  # Using 80% of max for stability

def lax_diffusive_scheme(y, v, dt):
    """Apply Lax diffusive scheme to update y and v"""
    n_points = len(y)
    A = np.array([calculate_area(yi) for yi in y])
    Q = A * v
    
    # New arrays for updated values
    y_new = np.zeros_like(y)
    v_new = np.zeros_like(v)
    
    # Apply Lax scheme for internal points
    for i in range(1, n_points-1):
        # Continuity equation
        y_new[i] = 0.5 * (y[i+1] + y[i-1]) - 0.5 * (dt/dx) * (Q[i+1] - Q[i-1])
        
        # Momentum equation
        v_new[i] = 0.5 * (v[i+1] + v[i-1]) - 0.5 * (dt/dx) * (
            v[i+1]**2 - v[i-1]**2 + g * (y[i+1] - y[i-1])
        )
    
    # Boundary conditions
    y_new[0] = y[0]  # Constant head reservoir
    v_new[0] = v[0]  # Assuming constant velocity at inlet
    
    # Downstream boundary (simplified)
    y_new[-1] = y[-1]
    v_new[-1] = v[-1]
    
    return y_new, v_new

# Calculate appropriate time step
dt = calculate_time_step(y_initial, v_initial)
print(f"Calculated time step: {dt:.2f} seconds")

# Perform one step of Lax scheme
y_next, v_next = lax_diffusive_scheme(y_initial, v_initial, dt)

# Print results for sections 7, 8, and 9 (indices 6, 7, and 8)
print("\nWater depths at next time step:")
print(f"Section 7: {y_next[6]:.4f} m")
print(f"Section 8: {y_next[7]:.4f} m")
print(f"Section 9: {y_next[8]:.4f} m")

# Additional diagnostic information
print("\nDetailed calculations:")
for i in range(6, 9):  # Sections 7, 8, 9
    area_before = calculate_area(y_initial[i])
    area_after = calculate_area(y_next[i])
    discharge_before = calculate_discharge(y_initial[i], v_initial[i])
    discharge_after = calculate_discharge(y_next[i], v_next[i])
    
    print(f"\nSection {i+1} (index {i}):")
    print(f"  Initial depth: {y_initial[i]:.4f} m")
    print(f"  Initial velocity: {v_initial[i]:.4f} m/s")
    print(f"  Initial area: {area_before:.4f} m²")
    print(f"  Initial discharge: {discharge_before:.4f} m³/s")
    print(f"  New depth: {y_next[i]:.4f} m")
    print(f"  New velocity: {v_next[i]:.4f} m/s")
    print(f"  New area: {area_after:.4f} m²")
    print(f"  New discharge: {discharge_after:.4f} m³/s")

# Visualize the results
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(range(1, len(y_initial)+1), y_initial, 'bo-', label='Initial depth')
plt.plot(range(1, len(y_next)+1), y_next, 'ro-', label='Next time step depth')
plt.grid(True)
plt.xlabel('Section number')
plt.ylabel('Water depth (m)')
plt.legend()
plt.title('Water depth profile')

plt.subplot(2, 1, 2)
plt.plot(range(1, len(v_initial)+1), v_initial, 'bo-', label='Initial velocity')
plt.plot(range(1, len(v_next)+1), v_next, 'ro-', label='Next time step velocity')
plt.grid(True)
plt.xlabel('Section number')
plt.ylabel('Velocity (m/s)')
plt.legend()
plt.title('Velocity profile')

plt.tight_layout()
plt.show()