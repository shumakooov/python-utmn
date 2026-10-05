# Вычислить и вывести на экран значение функции F, где a, b, c, x -
# действительные числа. Значения a, b, c и x вводятся пользователем. Функция F вычисляется по формуле:
# img/1.3.1.png

import math
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
x = int(input("Введите число x: "))
if x < 0 and b != 0:
    F = (x**(1/3) if x >= 0 else -(-x)**(1/3)) + b
    F = F / a
elif x > 0 and b > 0:
    F = (x**2 - math.sin(a - 2)) / (3*x - b*c)
else:
    F = math.log(x) / c
print("F =", F)
