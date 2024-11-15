import numpy as np
import matplotlib.pyplot as plt

# Create points for the circle
theta = np.linspace(0, 2*np.pi, 100)
radius = 1
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Create the plot
plt.figure(figsize=(6,6))
plt.plot(x, y)
plt.axis('equal')  # Make sure the circle looks round
plt.grid(True)
plt.title('Circle with radius 1')
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()