import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

f = plt.figure(figsize=(4,4))
ax = f.add_subplot(111)

ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(10))

majc ="#3182bd"
minc ="#deebf7"

ax.xaxis.grid(True,'minor',color=minc, ls='-', lw=0.2)
ax.yaxis.grid(True,'minor',color=minc, ls='-', lw=0.2)
ax.xaxis.grid(True,'major',color=majc, ls='-')
ax.yaxis.grid(True,'major',color=majc,ls ='-')
ax.set_axisbelow(True)

x = np.linspace(0, 30, 100)
ax.plot(x, x, 'r-', lw=0.7)
plt.show()

# [line.set_zorder(3) for line in ax.lines]
# plt.savefig('test.pdf')