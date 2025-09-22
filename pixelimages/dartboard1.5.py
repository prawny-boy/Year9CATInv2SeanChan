# Blue: (59,163,234) 
# • Gold: (247,188,43) 
# • Green: (138,219,138) 
# • Peach (238,193,165): 
# • Red: (237,49,25)
# Import the appropriate libraries.
from PIL import Image, ImageDraw
import random

# .open("") - lets computer know which image you will load
img = Image.open("pixelimages\\dartboard2.png")  # Replace with your file path
img = img.convert("RGB")  # Ensures it’s in RGB mode

# load the image into your program's memory.
pixels = img.load()

# Show the image without edits.
img.show()

# Access pixel values
width, height = img.size

number_of_pixels = {
    (59, 163, 234): 0, #blue
    (247, 188, 43): 0, #gold
    (138, 219, 138): 0, #green
    (238, 193, 165): 0, #peach
    (237, 49, 25): 0, #red
}
trials = 5000
# Draw blue dots around the image by editing pixel values to blue.
for i in range(trials):
	# Randomly select a number within the range of the width of the image.
    rand_x = random.randint(0,width-1)
	# Randomly select a number within the height of the image.
    rand_y = random.randint(0,height-1)

    for colour in number_of_pixels.keys():
        if pixels[rand_x, rand_y] == colour:
            number_of_pixels[colour] += 1
            pixels[rand_x,rand_y] = (0,0,0) 
    else:
        print(f"Colour was not found. Colour {pixels[rand_x, rand_y]}")

# Show image with the edits.
img.show()
print("----APPROXIMATE RATIO OF EACH COLOUR----")
for colour, amount in number_of_pixels.items():
    print(f"{colour}: {amount/trials}")
