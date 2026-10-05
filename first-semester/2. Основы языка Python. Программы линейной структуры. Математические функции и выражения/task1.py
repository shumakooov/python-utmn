# Вычислить значение функции f(x) = abs(sin((1+sqrt3(x))/x)).
# Значение переменной x вводится с клавиатуры.

import math
x = float(input("Введите значение x -> "))
f=abs(math.sin((1+math.pow(x,1/3))/x))
print(f)