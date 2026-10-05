#Реализовать постановку задачи и реализацию функции: ввода массива, вывод массива на экран, редактирование i-элемента массива, функции main() с меню.

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


def show_menu():
    """Функция для отображения меню"""
    print("=== МЕНЮ РАБОТЫ С МАССИВОМ===")
    print("1. Ввод массива")
    print("2. Вывод массива")
    print("3. Редактирование элемента")
    print("4. Выход")

def main():
    """Основная функция с меню управления"""
    arr = []
    
    print("Программа для работы с массивом")
    
    while True:
        show_menu()
        
        choice = input("Выберите пункт меню (1-4): ")
        
        if choice == '1':
            arr = input_array()
        
        elif choice == '2':
            print_array(arr)
        
        elif choice == '3':
            arr = edit_element(arr)
        
        elif choice == '4':
            print("Выход из программы")
            break
        
        else:
            print("Неверный выбор! Выберите пункт от 1 до 4.")

main()
