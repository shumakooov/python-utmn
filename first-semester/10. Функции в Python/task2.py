# Выведите значение функции на экран в заданном диапазоне с заданным шагом.
# Если фунеция в данной точке не вычисляется выдать соответствующее сообщение.
# Вычисление каждой функции в условии реализовать с помощью отдельной функции. Вывод
# значения функции на экран реализовать с помощью универсальной функции fprint(x, y).
# Основную функцию реализоватькак функцию процедурного типа. Значение функции выводить с двумя знаками
# после запятой. Функции должны иметь независимый интерфейс.
# img/1.10.2.png

import math

def fprint(x, y):
    """Универсальная функция для вывода значения функции"""
    print(f"x = {x:.2f}, y = {y:.2f}")


def func1(x):
    return 1 / math.cos(math.sin(x - 2))

def func2(x):
    return 2 * (5 ** x) - 4 * math.log(x ** 2, 8)

def func3(x):
    argument = x ** 3 - 2 * x + 3
    return math.cos(argument) / math.sin(argument)

def main_function(x, step):
    try:
        if 5 <= x < 9:
            y = func1(x)
        elif 9 <= x < 17:
            y = func2(x)
        elif 17 <= x <= 22:
            y = func3(x)
        else:
            print(f"x = {x:.2f} - точка вне диапазона определения функции")
            return
        
        fprint(x, y)
        
    except ValueError as e:
        print(f"x = {x:.2f} - ошибка вычисления: {e}")
    except ZeroDivisionError:
        print(f"x = {x:.2f} - деление на ноль")
    except Exception as e:
        print(f"x = {x:.2f} - непредвиденная ошибка: {e}")

def calculate_function_range(start, end, step):
    print(f"Вычисление функции в диапазоне [{start}, {end}] с шагом {step}")
    print("-" * 40)
    
    x = start
    while x <= end:
        main_function(x, step)
        x += step


start_x = 0
end_x = 22
step_size = 0.5

calculate_function_range(start_x, end_x, step_size)
