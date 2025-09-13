import random
import matplotlib.pyplot as plt

def f(x):
    return 10  # Constant function y = 10

def separate_coordinates(coordinate_list):
    x_vals = []
    y_vals = []

    for coordinate in coordinate_list:
        x_vals.append(coordinate[0])
        y_vals.append(coordinate[1])

    return x_vals,y_vals

# Set up domain and range
x_min, x_max = 0, 20
y_min, y_max = 0, 20
# Set the number of random coordinates you want to generate.
N = 10000

# Generate random (x, y) points over 20×20 square
random_coordinates = []

for ii in range(N):
    x_rand = random.uniform(x_min, x_max)
    y_rand = random.uniform(y_min, y_max)
    random_coordinate = (x_rand,y_rand)
    random_coordinates.append(random_coordinate)

# Determine which points are under or over the curve
under_curve_coordinates = []
over_curve_coordinates = []

for coordinate in random_coordinates:
    # Calculate the function value for the x value of this coordiante

    if coordinate[1] <= f(coordinate[0]):
        under_curve_coordinates.append(coordinate)
    else:
        over_curve_coordinates.append(coordinate)

# Estimate area under the curve
# First calculate the area of the plane
area_box = (x_max - x_min) * (y_max - y_min)
# Take your ratio
area_estimate = (len(under_curve_coordinates) / N) * area_box
# Hard corded for comparison
exact_value = 10 * 20  # since the function is constant

# Output results
print(f"Monte Carlo Estimate: {area_estimate:.5f}")
print(f"Exact Value: {exact_value:.5f}")
print(f"Error: {abs(area_estimate - exact_value):.5f}")

# Generating coordinates for y=10
# Plot your function for comparison - this is the black line in the picture.
function_coordinates = []
for ii in range(101):
    function_x = (x_min+(x_max-x_min))/100*ii
    function_y = f(function_x)

    function_coordinate = (function_x,function_y)
    function_coordinates.append(function_coordinate)

# Plotting
plt.figure(figsize=(6,6))

# Plot the coordinates that correspond to our function, y=10
# First, matplotlib takes the x and y values separately, so these need to be separated and 
# given to plt.plot separately.
function_coordinate_x_vals, function_coordinate_y_vals = separate_coordinates(function_coordinates)
plt.plot(function_coordinate_x_vals, function_coordinate_y_vals, color='black', label='y = f(x)')

# Plot the coordinates above the function.
over_coordinate_x_vals, over_coordinate_y_vals = separate_coordinates(over_curve_coordinates)
plt.scatter(over_coordinate_x_vals, over_coordinate_y_vals, color='red', s=1, label='Above curve')

# Plot the coordinates below the function.
under_coordinate_x_vals, under_coordinate_y_vals = separate_coordinates(under_curve_coordinates)
plt.scatter(under_coordinate_x_vals, under_coordinate_y_vals, color='blue', s=1, label='Under curve')

# Setup the rest of the graph
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.legend()
plt.title("Monte Carlo Estimate of Area Under Curve")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
