import random
import matplotlib.pyplot as plt

def f1(x):
    return 1/2*x+1

def f2(x):
    return (x-2)**2+0.5

def separate_coordinates(coordinate_list):
    x_vals = []
    y_vals = []

    for coordinate in coordinate_list:
        x_vals.append(coordinate[0])
        y_vals.append(coordinate[1])

    return x_vals,y_vals

# Set up domain and range
x_min, x_max = 0, 4
y_min, y_max = 0, 3
# Set the number of random coordinates you want to generate.
N = 10000

# Generate random (x, y) points over 20×20 square
random_coordinates = []

for i in range(N):
    x_rand = random.uniform(x_min, x_max)
    y_rand = random.uniform(y_min, y_max)
    random_coordinate = (x_rand,y_rand)
    random_coordinates.append(random_coordinate)

# Determine which points are under or over the curve
inside_area_coordinates = []
outside_area_coordinates = []

for coordinate in random_coordinates:
    # Calculate the function value for the x value of this coordiante

    if coordinate[1] <= f1(coordinate[0]) and coordinate[1] >= f2(coordinate[0]):
        inside_area_coordinates.append(coordinate)
    else:
        outside_area_coordinates.append(coordinate)

# Estimate area under the curve
# First calculate the area of the plane
area_box = (x_max - x_min) * (y_max - y_min)
# Take your ratio
area_estimate = (len(inside_area_coordinates) / N) * area_box

# Output results
print(f"Monte Carlo Estimate: {area_estimate:.5f}")

# Generating coordinates for y=10
# Plot your function for comparison - this is the black line in the picture.
function_coordinates = []
function_coordinates2 = []
for i in range(101):
    function_x = (x_min+(x_max-x_min))/100*i
    function_y = f1(function_x)

    function_coordinate = (function_x,function_y)
    function_coordinates.append(function_coordinate)

    function_x2 = (x_min+(x_max-x_min))/100*i
    function_y2 = f2(function_x2)

    function_coordinate2 = (function_x2,function_y2)
    function_coordinates2.append(function_coordinate2)

# Plotting
plt.figure(figsize=(6,6))

# Plot the coordinates that correspond to our function, y=10
# First, matplotlib takes the x and y values separately, so these need to be separated and 
# given to plt.plot separately.
function_coordinate_x_vals, function_coordinate_y_vals = separate_coordinates(function_coordinates)
plt.plot(function_coordinate_x_vals, function_coordinate_y_vals, color='black', label='y = f1(x)')
function_coordinate_x_vals, function_coordinate_y_vals = separate_coordinates(function_coordinates2)
plt.plot(function_coordinate_x_vals, function_coordinate_y_vals, color='black', label='y = f2(x)')

# Plot the coordinates above the function.
over_coordinate_x_vals, over_coordinate_y_vals = separate_coordinates(outside_area_coordinates)
plt.scatter(over_coordinate_x_vals, over_coordinate_y_vals, color='red', s=1, label='Above curve')

# Plot the coordinates below the function.
under_coordinate_x_vals, under_coordinate_y_vals = separate_coordinates(inside_area_coordinates)
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
