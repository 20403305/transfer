import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1,1,5)
y = x+1
plt.xlim((-1,6))
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.plot(x,y,'ob-')
plt.show()