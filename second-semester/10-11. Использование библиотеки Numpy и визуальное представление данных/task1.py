# img/2.10-11.1.png

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)

y1 = 5 / (1 + 2 * x**3)
y2 = np.exp(-3 * x)
y3 = np.sin(3 * x**2)
y4 = np.cos(5 + 6 * x**2) / (2 ** (- 4 * x))

plt.figure(figsize=(10, 6))

plt.plot(x, y1, label='5 / (1 + 2 * x**3)')
plt.plot(x, y2, label='np.exp(-3 * x)$')
plt.plot(x, y3, label='np.sin(3 * x**2)')
plt.plot(x, y4, label='np.cos(5 + 6 * x**2) / (2 ** (- 4 * x))')

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='-')

plt.ylim(-10, 10)

plt.show()
