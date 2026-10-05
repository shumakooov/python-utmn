# img/1.10.3.png

import math

def g(a, b):
    """
    Вычисление функции g(a, b) = (a² - b²)/(2ab - a - b) + (a + b)·√(|a + b|/2)
    """
    numerator = a**2 - b**2
    denominator = 2 * a * b - a - b
    
    first_term = numerator / denominator
    
    sum_ab = a + b
    second_term = sum_ab * math.sqrt(abs(sum_ab) / 2)
    
    return first_term + second_term

s = 1
t = 2
print(f"Результат функции 1: {g(1.2,s) + g(t,s) - g(2*s-1, s*t)}\n")

def f(u, v, t):
    if u > 1:
        return v * u * t
    elif u >= 0:
        return u + t + v
    else:
        return v - t - u

x = 1
y = 5
print(f"Результат функции 2: {f(math.sin(x) + math.cos(y), x + y, 2) + f(x * y, math.sin(x), math.cos(y)) + f(math.sin(x)**2, x - y**2, y - x**2)}\n")

def F(u, t):
    if u > 0 and t > 0:
        return u**2 + t**2
    elif u <= 0 and t <= 0:
        return u + t**2
    elif u > 0 and t <= 0:
        return u - t
    else:
        return u + t

a = 6
b = 4
print(f"Результат функции 3: {F(a, b) + F(a**2, b**2) + F(a**2 - 1, b) + F(a - b, b)}\n")

def sum_sin(x):
    return sum(math.sin(x_i) for x_i in x)

def sum_cos(y):
    return sum(math.cos(y_i) for y_i in y)

def sum_abs(x):
    return sum(abs(x_i) for x_i in x)

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
y = [40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
numerator = sum_sin(x) + sum_cos(y)
denominator = sum_abs(x)
print(f"Результат функции 4: {numerator / denominator}")
