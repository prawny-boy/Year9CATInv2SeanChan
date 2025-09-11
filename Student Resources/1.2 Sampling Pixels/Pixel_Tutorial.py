# Import the appropriate libraries.
from PIL import Image, ImageDraw
import random

# .open("") - lets computer know which image you will load
img = Image.open("sample.png")  # Replace with your file path
img = img.convert("RGB")  # Ensures it’s in RGB mode

# load the image into your program's memory.
pixels = img.load()

# Show the image without edits.
img.show()

# Access pixel values
width, height = img.size

# Draw blue dots around the image by editing pixel values to blue.
for ii in range(5000):

	# The image is represented as a 2-Dimensional Array where each value 
	# is a triple (R,G,B).  The First number R, represents the redness of
	# a pixel, the second G the greenness and the third B the blueness.
	# These values can be between 0 and 255 inclusive.

	# Randomly select a number within the range of the width of the image.
	rand_x = random.randint(0,width-1)
	# Randomly select a number within the height of the image.
	rand_y = random.randint(0,height-1)

	# Mark the selected value
	pixels[rand_x,rand_y] = (0,0,255)

# Show image with the edits.
img.show()

