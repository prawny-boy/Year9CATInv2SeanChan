# Import the appropriate libraries.
from PIL import Image, ImageDraw
import random

# .open("") - lets computer know which image you will load
img = Image.open("pixelimages\\dartboard1.png")  # Replace with your file path
img = img.convert("RGB")  # Ensures it’s in RGB mode

# load the image into your program's memory.
pixels = img.load()

# Show the image without edits.
img.show()

# Access pixel values
width, height = img.size

inside_dart_board = 0
outside_dart_board = 0
# Draw blue dots around the image by editing pixel values to blue.
for i in range(5000):
	# Randomly select a number within the range of the width of the image.
    rand_x = random.randint(0,width-1)
	# Randomly select a number within the height of the image.
    rand_y = random.randint(0,height-1)
    print(pixels[rand_x,rand_y])
    if pixels[rand_x,rand_y] == (255,255,255):
        outside_dart_board += 1
        pixels[rand_x,rand_y] = (255,0,0)
    else:
        inside_dart_board += 1
        pixels[rand_x,rand_y] = (0,0,255)

# Show image with the edits.
img.show()
print(f"Percentage space taken by dartboard: {inside_dart_board/(outside_dart_board+inside_dart_board)*100}%")
