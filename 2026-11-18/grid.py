import matplotlib.pyplot as plt
import numpy as np

x = np.array([10, 20, 30, 40, 50])
y = np.array([10, 15, 12, 17, 14])

plt.plot(x, y, linestyle='--',  marker="h", ms = 20)

f1 = {"family": "serif", "color": "red", "size": "25"}

plt.title("Sports Data", fontdict=f1)
plt.xlabel("xlabel")
plt.ylabel("ylabel")

# grid layout
# axis = x, y( default x, y)
# color
# linestyle
# linewidth
plt.grid(c="green", linestyle="--", linewidth=1)

plt.show()
