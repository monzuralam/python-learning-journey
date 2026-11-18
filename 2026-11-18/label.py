import matplotlib.pyplot as plt
import numpy as np

x = np.array([10, 20, 30, 40, 50])
y = np.array([10, 15, 12, 17, 14])

plt.plot(x, y)

# font style
f1 = {'font':'serif', 'color':'royalblue', 'size': '20'}
f2 = {'font':'serif', 'color':'green', 'size': '10'}

# title position: loc = left|center(default)|right

plt.title('Sports watch data', fontdict = f1, loc = 'left')
plt.xlabel("Average Pulse", fontdict = f2)
plt.ylabel("Calorie Burnage", fontdict = f2)

plt.show()