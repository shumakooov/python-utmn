# Вычислить углы треугольника, зная его стороны. Стороны треугольника вводятся с клавиатуры.

import math
a = float(input("Введите сторону a -> "))
b = float(input("Введите сторону b -> "))
c = float(input("Введите сторону c -> "))
cos_a = ((math.pow(b,2) + math.pow(c,2) - math.pow(a,2)) / (2*b*c))
cos_b = ((math.pow(c,2) + math.pow(a,2) - math.pow(b,2)) / (2*a*c))
cos_c = ((math.pow(a,2) + math.pow(b,2) - math.pow(c,2)) / (2*a*b))
angle_a = math.degrees(math.acos(cos_a))
angle_b = math.degrees(math.acos(cos_b))
angle_c = math.degrees(math.acos(cos_c))
print(angle_a, angle_b, angle_c)
