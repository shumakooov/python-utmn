# img/2.7-8.1.png

def only_positive_even_sum(a, b):
    if not isinstance(a, int):
        raise TypeError("Параметр должен быть целым числом")
    if not isinstance(b, int):
        raise TypeError("Параметр должен быть целым числом")
    
    if a <= 0 or a % 2 != 0:
        raise ValueError("Параметр должен быть положительным чётным числом")
    if b <= 0 or b % 2 != 0:
        raise ValueError("Параметр должен быть положительным чётным числом")
    
    return a + b
