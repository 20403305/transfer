import matplotlib.pyplot as plt
import numpy as np


# x = np.array([1,2,3])
# 和linspace 不能同时出现，会画出两个图
# plt.figure(figsize=(10,5))


x = np.linspace(0,60,5)
y = x+1

new_ticks = np.linspace(0,60,3)
plt.xticks(new_ticks)
# 查看范围
# plt.xlim((1,60))
plt.grid(which='major', color='#f31d1d', linewidth=0.8)
plt.grid(which='minor', color='#eb7575', linestyle=':', linewidth=0.5, alpha=0.5)

plt.minorticks_on()


plt.plot(x,y,"ob-")

plt.show()