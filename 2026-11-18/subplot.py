import matplotlib.pyplot as plt
import numpy as np

# plot 1
a = np.array([10, 20, 30, 40, 50])
b = np.array([10, 15, 12, 17, 14])

plt.subplot(1, 2, 1)
plt.plot(a, b)
plt.title('Plot 1')
plt.xlabel('x label')
plt.ylabel('y label')

# plot 2
c = np.array([10, 15, 20])
d = np.array([60, 79, 80])

plt.subplot(1, 2, 2)
plt.plot(c, d)
plt.title('Plot 2')
plt.xlabel('x label')
plt.ylabel('y label')

# show
plt.show()



