# img/2.16-17.2.png

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.log(x) - x + 1.8

x = np.linspace(0.1, 5, 1000)
y1 = np.log(x)
y2 = x - 1.8

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x, y1, label='ln(x)')
plt.plot(x, y2, label='x - 1.8')
plt.grid()
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, f(x), label='f(x) = ln(x) - x + 1.8')
plt.grid()
plt.legend()
plt.axhline(0, color='black')

plt.show()

f_vals = f(x)
for i in range(len(x) - 1):
    if f_vals[i] * f_vals[i+1] < 0:
        a = x[i]
        b = x[i+1]
        print(f"Интервал: [{a}, {b}]")
        break

eps = 0.0001

while (b - a) / 2 > eps:
    c = (a + b) / 2
    if f(a) * f(c) <= 0:
        b = c
    else:
        a = c

x_root = (a + b) / 2

print(f"Корень: x = {x_root}")
print(f"f(x) = {f(x_root)}")
