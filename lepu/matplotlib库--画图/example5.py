import matplotlib.pyplot as plt



plt.plot([23, 456, 676, 89, 906, 34, 2345])
plt.yscale('log')

plt.grid(b=True, which='major', color='b', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')

plt.show()
