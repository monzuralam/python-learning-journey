import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 5, 7, 9])
y = np.array([10, 15, 20, 25, 30 ])

plt.plot(x, y, 'o')
plt.show()

# default m plot
n = np.array([20, 15, 25, 20, 30, 25, 35])
plt.plot(n)
plt.show()