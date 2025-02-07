# import libraries we need
import numpy as np
import matplotlib.pyplot as plt


# defining the range for x
x = np.linspace(0, 10, 100)

# defining the functions
y1 = np.sinh(x)
y2 = np.cosh(x)
y3 = np.tanh(x)


## plotting the functions
# making a figure with 2 subplots
plt.figure(figsize=(8, 6))

# filling the first subplot
plt.subplot(2,1,1)
plt.plot(x, y1, label="y1 = sinh(x)")
plt.plot(x, y2, label="y2 = cosh(x)")
plt.plot(x, y3, label="y3 = tanh(x)")
plt.xlim(-10, 10)
plt.legend()
plt.title("Functions over full range (-10 to 10)")


# filling the second subplot
plt.subplot(2, 1, 2)
plt.plot(x[(x >= -2.5) & (x <= 2.5)], y1[(x >= -2.5) & (x <= 2.5)], label="sinh(x)")
plt.plot(x[(x >= -2.5) & (x <= 2.5)], y2[(x >= -2.5) & (x <= 2.5)], label="cosh(x)")
plt.plot(x[(x >= -2.5) & (x <= 2.5)], y3[(x >= -2.5) & (x <= 2.5)], label="tanh(x)")

plt.xlim(-2.5, 2.5)
plt.legend()
plt.title("functions over limited range of -2.5 to 2.5")


# saving the layout as a PDf file
plt.tight_layout()
plt.savefig("exercise2_plot.pdf")
plt.show()