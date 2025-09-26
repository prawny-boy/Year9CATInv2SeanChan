# Import the appropriate libraries.
from PIL import Image, ImageDraw
import random
from matplotlib import pyplot as plt

# .open("") - lets computer know which image you will load
img = Image.open("Part4\\0.5_2.png")  # Replace with your file path
img = img.convert("RGB")  # Ensures it’s in RGB mode

# load the image into your program's memory.
pixels = img.load()

# Access pixel values
width, height = img.size

trials_until_red = []

for _ in range(20000):
    rand_x = width-1
    rand_y = height-1
    trials = 0
    while pixels[rand_x,rand_y] != (255, 0, 0):
        # Randomly select a number within the range of the width of the image.
        rand_x = random.randint(0,width-1)
        # Randomly select a number within the height of the image.
        rand_y = random.randint(0,height-1)
        trials += 1
    trials_until_red.append(trials)

# save to output file
with open("Part4\\output.py", "w") as file:
    file.writelines("output="+str(trials_until_red))
print("Saved results to output.txt")

# show table
plt.hist(trials_until_red, bins=range(int(min(trials_until_red)), int(max(trials_until_red) + 2)), align='left',
         edgecolor='none') 
plt.title('Distribution of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()