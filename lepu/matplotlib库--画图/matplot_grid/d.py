import numpy as np
import matplotlib.pyplot as plt
 
# The Data
x = [1, 2, 3, 4, 5,6, 7, 8, 9, 10, 11]
y = [234, 124,368, 343,456,234, 124,368, 343, 343,456]
 
# Create the figure and axes objects
fig, ax = plt.subplots(1, figsize=(8, 6))
fig.suptitle('Example Of Plot With Major and Minor Grid Lines')
 
# Plot the data
ax.plot(x,y)
 
new_ticks = np.linspace(0,60,7)
plt.xticks(new_ticks)

# Show the major grid lines with dark grey lines
plt.grid(b=True, which='major', color='#666666', linestyle='-')
 

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
# plt.xlim((1,5))
 
plt.show()