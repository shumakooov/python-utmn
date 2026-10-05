# 2. Дан одномерный массив, состоящий из N целочисленных элементов.
# 2.1. Заполнить массив случайными числами.
# 2.2. Вычислить сумму отрицательных элементов массива кратных 7.
# 2.3. Вывести положительные, четные элементы на экран.
# 2.4. Отсортировать массив методом вставки и вывести отсортированный массив на экран.

# 3. Дан одномерный массив, состоящий из N вещественных элементов.
# 3.1. Ввести массив с клавиатуры.
# 3.2. Вычислить среднее арифметическое отрицательных элементов массива.
# 3.3. Вывести положительные элементы на экран в обратном порядке.
# 3.4. Отсортировать массив методом «пузырька» и вывести отсортированный массив на экран.

# 4. Дан одномерный массив, состоящий из N целочисленных элементов.
# 4.1. Ввести массив с клавиатуры.
# 4.2. Вычислить сумму элементов массива кратных 8 с нечетными индексами.
# 4.3. Вывести положительные элементы на экран.
# 4.4. Отсортировать массив методом вставки и вывести отсортированный массив на экран.

import random

def input_array():
    """Функция для ввода массива с клавиатуры"""
    print("\n=== Ввод массива ===")
    
    while True:
        try:
            n = int(input("Введите количество элементов массива: "))
            if n <= 0:
                print("Количество элементов должно быть положительным числом!")
                continue
            break
        except ValueError:
            print("Ошибка! Введите целое число.")
    
    arr = []
    print("Введите элементы массива:")
    for i in range(n):
        while True:
            try:
                element = float(input(f"Элемент [{i}]: "))
                arr.append(element)
                break
            except ValueError:
                print("Ошибка! Введите число.")
    
    print("Массив успешно создан!")
    return arr

def random_input_array():
    """Функция для заполнения массива случайными числами"""
    while True:
        try:
            n = int(input("Введите количество элементов массива: "))
            if n <= 0:
                print("Количество элементов должно быть положительным числом!")
                continue
            break
        except ValueError:
            print("Ошибка! Введите целое число.")

    arr = [random.randint(-100, 100) for _ in range(n)]

    print("Массив успешно создан!")
    return arr


def print_array(arr):
    """Функция для вывода массива на экран"""
    if not arr:
        print("Массив пуст!")
        return
    
    print("\n=== Вывод массива ===")
    print("Индекс\tЗначение")
    print("-" * 20)
    for i, value in enumerate(arr):
        print(f"{i}\t{value}")


def edit_element(arr):
    """Функция для редактирования i-го элемента массива"""
    if not arr:
        print("Массив пуст! Сначала создайте массив.")
        return arr
    
    print_array(arr)
    
    while True:
        try:
            index = int(input(f"\nВведите индекс элемента для редактирования (0-{len(arr)-1}): "))
            if 0 <= index < len(arr):
                break
            else:
                print(f"Индекс должен быть в диапазоне от 0 до {len(arr)-1}!")
        except ValueError:
            print("Ошибка! Введите целое число.")
    
    while True:
        try:
            new_value = float(input(f"Введите новое значение для элемента [{index}]: "))
            break
        except ValueError:
            print("Ошибка! Введите число.")
    
    old_value = arr[index]
    arr[index] = new_value
    print(f"Элемент [{index}] изменен: {old_value} -> {new_value}")
    
    return arr


def task_2():
    # 2.1. Заполнить массив случайными числами
    arr = random_input_array()

    # 2.2. Вычислить сумму отрицательных элементов массива кратных 7
    sum_negative_multiple_7 = 0
    for num in arr:
        if num < 0 and num % 7 == 0:
            sum_negative_multiple_7 += num
    
    print(f"Сумма отрицательных элементов кратных 7: {sum_negative_multiple_7}\n")
    
    # 2.3. Вывести положительные, четные элементы на экран
    positive_even = [num for num in arr if num > 0 and num % 2 == 0]
    print("Положительные четные элементы:")
    print(f"{positive_even}\n")
    
    # 2.4. Отсортировать массив методом вставки и вывести на экран
    array = arr.copy()
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    
    sorted_arr = array
    print("Отсортированный массив (метод вставки):")
    print(sorted_arr)


def task_3():
    # 3.1. Ввести массив с клавиатуры
    arr = input_array()

    # 3.2. Вычислить среднее арифметическое отрицательных элементов массива
    negative_elements = []
    
    for num in arr:
        if num < 0:
            negative_elements.append(num)
    
    if negative_elements:
        average_negative = sum(negative_elements) / len(negative_elements)
        print(f"Среднее арифметическое отрицательных элементов: {average_negative:.2f}\n")
    else:
        print("Отрицательных элементов не найдено")
        average_negative = 0
    
    # 3.3. Вывести положительные элементы на экран в обратном порядке
    positive_elements = []
    
    for num in arr:
        if num > 0:
            positive_elements.append(num)
    
    if positive_elements:
        # Выводим в обратном порядке
        reversed_positive = positive_elements[::-1]
        print("Положительные элементы (в обратном порядке):", reversed_positive)
    else:
        print("Положительных элементов не найдено")
    
    # 3.4. Отсортировать массив методом «пузырька»
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - 1 - i):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
    
        if not swapped:
            break
    
    print("Отсортированный массив:")
    print(sorted_arr)


def task_4():
    # 4.1. Ввести массив с клавиатуры
    arr = input_array()

     # 4.2. Вычислить сумму элементов массива кратных 8 с нечетными индексам
    
    sum_multiple_8_odd_index = 0
    
    for i in range(len(arr)):
        if i % 2 == 1 and arr[i] % 8 == 0:
            sum_multiple_8_odd_index += arr[i]
    
    if sum_multiple_8_odd_index > 0:
        print(f"Сумма элементов массива кратных 8 с нечетными индексами: {sum_multiple_8_odd_index}")
    else:
        print("Элементов кратных 8 с нечетными индексами не найдено")
    
    # 4.3. Вывести положительные элементы на экран

    positive_elements = []
    for num in arr:
        if num > 0:
            positive_elements.append(num)
    
    if positive_elements:
        print("Положительные элементы:", positive_elements)
    else:
        print("Положительных элементов не найдено")
    
    # 4.4. Отсортировать массив методом вставки
    
    # Создаем копию для сортировки
    sorted_arr = arr.copy()
    
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key

    print("Отсортированный массив методом вставки:")
    print(sorted_arr)


def show_menu():
    """Функция для отображения меню"""
    print("=== МЕНЮ РАБОТЫ С МАССИВОМ===")
    print("1. Вывод массива")
    print("2. Редактирование элемента")
    print("3. Задача 2")
    print("4. Задача 3")
    print("5. Задача 4")
    print("6. Выход")

def main():
    """Основная функция с меню управления"""
    arr = []
    
    print("Программа для работы с массивом")
    
    while True:
        show_menu()
        
        choice = input("Выберите пункт меню (1-6): ")
        
        if choice == '1':
            print_array(arr)
        
        elif choice == '2':
            arr = edit_element(arr)
        
        elif choice == '3':
            arr = task_2()
        
        elif choice == '4':
            arr = task_3()
        
        elif choice == '5':
            arr = task_4()
        
        elif choice == '6':
            print("Выход из программы")
            break
        
        else:
            print("Неверный выбор! Выберите пункт от 1 до 6.")

main()
