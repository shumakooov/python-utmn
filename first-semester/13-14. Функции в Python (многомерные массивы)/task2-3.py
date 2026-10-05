# 2. Дан двухмерный массив, состоящий из N, M целочисленных элементов.
# 2.1. Вычислить среднее арифметическое четных элементов двухмерного массива.
# 2.2. Для элементов массива, находящихся в четных строках и нечетных столбцах найти максимальный элемент среди элементов кратных 3, и вывести на экран все элементы массива большие найденного максимального и их индексы.

# 3. Дан двухмерный массив, состоящий из N, M целочисленных элементов.
# 3.1. Вычислить сумму нечетных элементов двухмерного массива.
# 3.2. Для элементов массива, находящихся в нечетных строках и четных столбцах вычислить среднее арифметическое положительных элементов и вывести на экран все элементы массива, больше найденного среднего арифметического и их индексы.

import random

def initialize_array(n, m, min_val=1, max_val=100):
    """
    Инициализация двумерного массива случайными числами
    n - количество строк
    m - количество столбцов
    min_val, max_val - диапазон случайных чисел
    """
    return [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]

def print_array(arr):
    """Вывод массива на экран"""
    print("\nДвумерный массив:")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(f"{arr[i][j]:4}", end="")
        print()

def edit_element(arr):
    """Редактирование элемента массива по индексам i, j"""
    try:
        i = int(input("Введите номер строки i: "))
        j = int(input("Введите номер столбца j: "))
        new_value = int(input("Введите новое значение: "))
        
        if 0 <= i < len(arr) and 0 <= j < len(arr[0]):
            arr[i][j] = new_value
            print(f"Элемент [{i}][{j}] изменен на {new_value}")
        else:
            print("Ошибка: неверные индексы")
    except ValueError:
        print("Ошибка: введите целые числа")

def task1_1(arr):
    """
    Задание 1.1: Вычисление среднего арифметического четных элементов
    Возвращает кортеж (результат, успех_выполнения)
    """
    even_elements = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] % 2 == 0:  # проверка на четность
                even_elements.append(arr[i][j])
    
    if len(even_elements) > 0:
        # Вычисление среднего арифметического без использования стандартных функций
        total = 0
        for num in even_elements:
            total += num
        average = total / len(even_elements)
        return average, True
    else:
        return 0, False

def task1_2(arr):
    """Задание 1.2: Поиск максимального элемента и элементов больших его"""
    max_element = None
    
    # Поиск максимального элемента среди кратных 3 в четных строках и нечетных столбцах
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # Четные строки (индексация с 0) и нечетные столбцы
            if i % 2 == 0 and j % 2 == 1 and arr[i][j] % 3 == 0:
                if max_element is None or arr[i][j] > max_element:
                    max_element = arr[i][j]
    
    if max_element is not None:
        print(f"\nМаксимальный элемент кратный 3 в четных строках и нечетных столбцах: {max_element}")
        print("Элементы большие найденного максимального:")
        
        found = False
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] > max_element:
                    print(f"Элемент [{i}][{j}] = {arr[i][j]}")
                    found = True
        
        if not found:
            print("Элементов больших найденного максимального не найдено")
    else:
        print("Не найдено элементов кратных 3 в четных строках и нечетных столбцах")

def task2_1(arr):
    """
    Задание 2.1: Вычисление суммы нечетных элементов
    Возвращает кортеж (результат, успех_выполнения)
    """
    odd_elements = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] % 2 == 1:  # проверка на нечетность
                odd_elements.append(arr[i][j])
    
    if len(odd_elements) > 0:
        # Вычисление суммы без использования стандартных функций
        total = 0
        for num in odd_elements:
            total += num
        return total, True
    else:
        return 0, False

def task2_2(arr):
    """Задание 2.2: Вычисление среднего арифметического и поиск элементов больших его"""
    positive_elements = []
    
    # Сбор положительных элементов из нечетных строк и четных столбцов
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # Нечетные строки (индексация с 0) и четные столбцы
            if i % 2 == 1 and j % 2 == 0 and arr[i][j] > 0:
                positive_elements.append(arr[i][j])
    
    if len(positive_elements) > 0:
        # Вычисление среднего арифметического
        total = 0
        for num in positive_elements:
            total += num
        average = total / len(positive_elements)
        
        print(f"\nСреднее арифметическое положительных элементов в нечетных строках и четных столбцах: {average:.2f}")
        print("Элементы большие найденного среднего:")
        
        found = False
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] > average:
                    print(f"Элемент [{i}][{j}] = {arr[i][j]}")
                    found = True
        
        if not found:
            print("Элементов больших найденного среднего не найдено")
    else:
        print("Не найдено положительных элементов в нечетных строках и четных столбцах")

def main():
    """Основная функция программы"""
    # Инициализация массива
    N = 5  # количество строк
    M = 5  # количество столбцов
    arr = initialize_array(N, M)
    
    # Бесконечный цикл меню
    while True:
        print("\n" + "="*50)
        print("МЕНЮ:")
        print("1. Вывод массива на экран")
        print("2. Редактирование элемента массива")
        print("3. Задание 1.1 - Среднее арифметическое четных элементов")
        print("4. Задание 1.2 - Максимальный элемент и элементы большие его")
        print("5. Задание 2.1 - Сумма нечетных элементов")
        print("6. Задание 2.2 - Среднее арифметическое и элементы большие его")
        print("0. Выход")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            print_array(arr)
            
        elif choice == '2':
            edit_element(arr)
            
        elif choice == '3':
            result, success = task1_1(arr)
            if success:
                print(f"\nСреднее арифметическое четных элементов: {result:.2f}")
            else:
                print("Четные элементы не найдены")
                
        elif choice == '4':
            task1_2(arr)
            
        elif choice == '5':
            result, success = task2_1(arr)
            if success:
                print(f"\nСумма нечетных элементов: {result}")
            else:
                print("Нечетные элементы не найдены")
                
        elif choice == '6':
            task2_2(arr)
            
        elif choice == '0':
            print("Выход из программы")
            break
            
        else:
            print("Неверный выбор. Попробуйте снова.")


main()
