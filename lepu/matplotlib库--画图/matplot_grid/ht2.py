import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, MaxNLocator,FormatStrFormatter,
                               AutoMinorLocator)
# The Data
x = [1, 2, 3, 4, 5,6, 7, 8, 9, 10, 11]
y = [234, 124,368, 343,456,234, 124,368, 343, 343,456]
 
# Create the figure and axes objects
fig, ax = plt.subplots(1, figsize=(8, 6))
# fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)
fig.suptitle('Example Of Plot With Major and Minor Grid Lines')
 
# Plot the data
ax.plot(x,y)

# new_ticks = np.linspace(0,60,7)
new_ticks = np.linspace(0,1440,25)
# new_ticks = np.linspace(-10,1430,25)
plt.xticks(new_ticks)
# plt.xlim(0,60)
# Show the major grid lines with dark grey lines



ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='r')

plt.grid(b=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

# ax.xaxis.set_minor_formatter(FormatStrFormatter('%d'))

plt.minorticks_on()

ax.xaxis.set_major_locator(MultipleLocator(120))
ax.xaxis.set_major_formatter(FormatStrFormatter('good%d'))
ax.xaxis.set_minor_locator(AutoMinorLocator(n = 5))
# plt.xlim((1,5))
 
plt.show()