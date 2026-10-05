# img/2.18-19.1.png

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (1 - np.cos(x)) / ((x - np.sin(x)) ** 2)

x_plot = np.linspace(np.pi, 2*np.pi, 1000)
y_plot = f(x_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot)
plt.grid()
plt.title('График подынтегральной функции на интервале [π, 2π]')
plt.show()

def rectangle_method(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a + h/2, b - h/2, n)
    return h * np.sum(f(x))

a = np.pi
b = 2 * np.pi
eps = 0.00001

n = 100000
I = rectangle_method(f, a, b, n)

print(f"Результат: I = {I}")
