from Part4.output import output
from matplotlib import pyplot as plt

new_output = []
while len(output) != 0:
    new_output.append(sum(output[:20])/20)
    output = output[20:]

plt.hist(new_output, bins="auto", align='left',
         edgecolor='none') 
plt.title('Distribution of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()