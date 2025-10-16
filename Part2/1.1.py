# Import the appropriate libraries.
from PIL import Image, ImageDraw
from print_functions import *
import random

# .open("") - lets computer know which image you will load
img = Image.open("Part2\\bolt.png")  # Replace with your file path
img = img.convert("RGB")  # Ensures it’s in RGB mode

# load the image into your program's memory.
pixels = img.load()

# Show the image without edits.
img.show()

# Access pixel values
width, height = img.size

inside_bolt = 0
outside_bolt = 0
# Draw blue dots around the image by editing pixel values to blue.
for i in range(5000):
	# Randomly select a number within the range of the width of the image.
    rand_x = random.randint(0,width-1)
	# Randomly select a number within the height of the image.
    rand_y = random.randint(0,height-1)
    print(pixels[rand_x,rand_y])
    if pixels[rand_x,rand_y] == (255,255,54) or pixels[rand_x,rand_y] == (0,0,255):
        inside_bolt += 1
        pixels[rand_x,rand_y] = (0,0,255)
    else:
        outside_bolt += 1
        pixels[rand_x,rand_y] = (255,0,0)

# Show image with the edits.
img.show()
print_title("Results")
print("Space taken by bolt:")
print(f"Percentage: {inside_bolt/(outside_bolt+inside_bolt)*100}%")
print(f"Ratio: {inside_bolt/(outside_bolt+inside_bolt)}")
print(f"Amount of Pixels: {round(inside_bolt/(outside_bolt+inside_bolt)*(width*height))} out of {(width*height)} pixels")
