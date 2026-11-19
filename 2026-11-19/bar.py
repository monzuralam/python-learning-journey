import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([10, 12, 15, 20])

plt.bar(x, y)

plt.show()

# horizontal bar
plt.barh(x, y)

plt.show()
