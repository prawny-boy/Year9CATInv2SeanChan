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

middle_of_target = width/2
r = middle_of_target/5 # there are 5 rings so half the image / 5 to get r (radius of smallest ring)

above_10 = 0
under_10 = 0
# Draw blue dots around the image by editing pixel values to blue.
for i in range(5000):
	# Randomly select a number within the range of the width of the image.
    rand_x = random.randint(0,width-1)
	# Randomly select a number within the height of the image.
    rand_y = random.randint(0,height-1)

    distance = ((rand_x-middle_of_target)**2 + (rand_y-middle_of_target)**2)**0.5 # finds the absolute distance from center using pythagoras

    if distance < r*3: # third ring
        above_10 += 1
        pixels[rand_x,rand_y] = (0,0,255)
    else: # fourth ring and others/not above 10
        under_10 += 1
        pixels[rand_x,rand_y] = (255,0,0)    

# Show image with the edits.
img.show()
print(f"Chance scoring 10 or more: {above_10/(above_10 + under_10)}")
