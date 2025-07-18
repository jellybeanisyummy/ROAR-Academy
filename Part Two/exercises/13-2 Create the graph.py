from matplotlib import pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# display 2 functions on the same graph
func1 = lambda x: 2*x
func2 = lambda x: -3*x + 10

# Generate x values for the x-axis
x_values = np.arange(1.0, 3.1, 0.5)

#generate x values for the functions
x_values1 = np.arange(1.0, 2.1, 0.5)
x_values2 = np.arange(2.0, 3.1, 0.5)

# generate y values for the y-axis
y_values = np.arange(1.0, 4.1, 0.5)

# Plot the functions
ax.plot(x_values1, func1(x_values1),  color='blue')
ax.plot(x_values2, func2(x_values2), color='blue')

# Set the x and y axis with correct labels
ax.set_xlim(1.0, 3.0)
ax.set_ylim(1.0, 4.0)
ax.set_xticks(x_values)
ax.set_yticks(y_values)
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")

# Set the title of the graph
ax.set_title("Sample Graph!")

plt.show()
