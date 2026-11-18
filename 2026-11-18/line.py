import matplotlib.pyplot as plt
import numpy as np

y = np.array([10, 20, 30, 40, 50, 60])
z = np.array([15, 5, 25, 15, 35, 25])

# Linestyle shorthand: ls
# dotted can be write as shorthand :
# color shorthand: c
# linewidth
plt.plot(y, linestyle = 'dotted', color = 'blue', linewidth = 10)
plt.plot(z, ls = '--', c = 'pink', lw = 4)
plt.show()