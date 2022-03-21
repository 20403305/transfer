from matplotlib import pyplot as plt
import numpy as np


def sinplot():
    """Example plot we'll use throughout."""
    fig, ax = plt.subplots()
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        ax.plot(x, np.sin(x + i * .5) * (7 - i))
    return ax

ax = sinplot()
# Show the major grid and style it slightly.
ax.grid(which='major', color='#DDDDDD', linewidth=0.8)
# Show the minor grid as well. Style it in very light gray as a thin,
# dotted line.
ax.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=0.5)
# Make the minor ticks and gridlines show.
ax.minorticks_on()

plt.show()