# img/2.18-19.2.png

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x * np.sin(x)) / (x**2 + 3)

x_plot = np.linspace(0, 5, 1000)
y_plot = f(x_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot)

plt.fill_between(x_plot, y_plot, 0, 
                 where=(y_plot >= 0), 
                 color='blue', alpha=0.3)
plt.fill_between(x_plot, y_plot, 0, 
                 where=(y_plot < 0), 
                 color='red', alpha=0.3)

plt.grid()
plt.title('График функции f(x) = x·sin(x)/(x²+3) на интервале [0, 5]')
plt.show()

def trapezoid_method(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])

a = 0
b = 5
eps = 0.00001

n = 100000
I = trapezoid_method(f, a, b, n)

print(f"Площадь (интеграл): I = {I}")
