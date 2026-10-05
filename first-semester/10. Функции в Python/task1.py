# Написать функцию для вычисления значения:
# 1) Вычислить высоту треугольника, зная две стороны треугольника и угол между ними.
# 2) Вычислить углы треугольника, зная его стороны.
# 3) Вычислить сторону треугольника, зная две другие стороны и угол между ними.
# 4) Вычислить площадь ромба, зная длину стороны и угол.
# 5) Вычислить объем шара, вписанного в куб со стороной а.
# Функции должны иметь независимый интерфейс.

import math

def triangle_height(side1, side2, angle):
    """Вычислить высоту треугольника, зная две стороны треугольника и угол между ними."""
    angle_rad = math.radians(angle)
    height = side2 * math.sin(angle_rad)
    return height

def triangle_angles(side_a, side_b, side_c):
    """Вычислить углы треугольника, зная его стороны."""
    if (side_a + side_b <= side_c or 
        side_a + side_c <= side_b or 
        side_b + side_c <= side_a):
        raise ValueError("Треугольник с такими сторонами не существует")
    
    cos_A = (side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)
    angle_A = math.degrees(math.acos(cos_A))
    
    cos_B = (side_a**2 + side_c**2 - side_b**2) / (2 * side_a * side_c)
    angle_B = math.degrees(math.acos(cos_B))
    
    angle_C = 180 - angle_A - angle_B
    
    return angle_A, angle_B, angle_C

def triangle_side(side1, side2, angle):
    """Вычислить сторону треугольника, зная две другие стороны и угол между ними."""
    angle_rad = math.radians(angle)

    side3 = math.sqrt(side1**2 + side2**2 - 2 * side1 * side2 * math.cos(angle_rad))
    return side3

def rhombus_area(side, angle):
    """ Вычислить площадь ромба, зная длину стороны и угол."""
    angle_rad = math.radians(angle)

    area = side**2 * math.sin(angle_rad)
    return area

def sphere_volume_in_cube(side_a):
    """Вычислить объем шара, вписанного в куб со стороной a."""
    radius = side_a / 2
    volume = (4/3) * math.pi * radius**3
    return volume


height = triangle_height(5, 6, 30)
print(f"1) Высота треугольника со сторонами 5 и 6 и углом 30: {height}")

angles = triangle_angles(3, 4, 5)
print(f"2) Углы треугольника со сторонами 3, 4, 5: {angles[0]}, {angles[1]}, {angles[2]}")

side = triangle_side(3, 4, 90)
print(f"3) Третья сторона треугольника со сторонами 3, 4 и углом 90: {side}")

area = rhombus_area(5, 60)
print(f"4) Площадь ромба со стороной 5 и углом 60: {area}")

volume = sphere_volume_in_cube(10)
print(f"5) Объем шара, вписанного в куб со стороной 10: {volume}")
