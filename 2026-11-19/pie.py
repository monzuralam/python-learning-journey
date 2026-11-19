import matplotlib.pyplot as plt
import numpy as np

x = np.array([10, 23, 15, 30])
mylabels = ['A', 'B', 'C', 'D']
myexplode = [0.2, 0, 0, 0]

plt.pie(x, labels = mylabels, explode = myexplode, startangle = 90, shadow = True)
plt.legend(title = 'Hello World')

plt.show()