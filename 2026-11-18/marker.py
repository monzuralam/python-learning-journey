import matplotlib.pyplot as plt
import numpy as np

y = np.array([10, 5, 15, 10, 20, 15, 30, 25])

plt.plot(y, marker = 'D') # marker style: o * . , x X + P s d D p h H v  ^ > < 1 2 3 4 | _
plt.show()

# Format String ( fmt ) 
plt.plot(y, 'o:g') # marker|line|color 
# line: : (dot), - (solid), -- (dashed), -. (dashed/dotted)
# color: r(red), g(green), b(blue), c(cyan), m(magenta), y(yellow), k(black), w(white)
plt.show()

# markersize | ms
plt.plot(y, marker = 'x', markersize = 30)
plt.show()