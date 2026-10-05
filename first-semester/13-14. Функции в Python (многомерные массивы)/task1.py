# Реализовать постановку задачи и реализацию функции: ввода массива, вывод
# массива на экран, редактирование i,j -элемента массива, функции main() с меню.

def input_array():
    """Ввод многомерного массива"""
    num_dimensions = int(input("Введите количество измерений массива: "))
    if num_dimensions <= 0:
        print("Количество измерений должно быть положительным числом!")
        return None, None
    
    dimensions = []
    for i in range(num_dimensions):
        size = int(input(f"Введите размер {i+1}-го измерения: "))
        if size <= 0:
            print("Размер измерения должен быть положительным числом!")
            return None, None
        dimensions.append(size)
    
    print("\nВведите элементы массива:")
    array = create_array(dimensions, 0)
    print("Массив успешно создан!")
    return array, dimensions

def create_array(dimensions, level):
    """Рекурсивное создание многомерного массива"""
    if len(dimensions) == 1:
        arr = []
        for i in range(dimensions[0]):
            while True:
                try:
                    value = float(input(f"Элемент [{i}]: "))
                    arr.append(value)
                    break
                except ValueError:
                    print("Ошибка: введите число!")
        return arr

    arr = []
    for i in range(dimensions[0]):
        print(f"Уровень {level+1}, элемент [{i}]:")
        arr.append(create_array(dimensions[1:], level + 1))
    return arr


def display_array(array):
    """Вывод массива на экран"""
    if array is None:
        print("Массив не создан! Сначала создайте массив.")
        return
    
    print("\n" + "="*50)
    print("Многомерный массив:")
    print("="*50)
    print_array(array, 0)
    print("="*50)

def print_array(arr, level):
    """Рекурсивный вывод массива с отступами"""
    indent = "  " * level
    
    if isinstance(arr, list) and len(arr) > 0 and isinstance(arr[0], list):
        for i, subarr in enumerate(arr):
            print(f"{indent}Измерение {level+1}, индекс {i}:")
            print_array(subarr, level + 1)
    else:
        print(f"{indent}{arr}")


def edit_element(array, dimensions):
    """Редактирование элемента по индексам"""
    if array is None:
        print("Массив не создан! Сначала создайте массив.")
        return array
    
    try:
        indices = []
        for i in range(len(dimensions)):
            idx = int(input(f"Введите {i+1}-й индекс: "))
            if idx < 0 or idx >= dimensions[i]:
                print(f"Ошибка: индекс должен быть в диапазоне [0, {dimensions[i]-1}]")
                return array
            indices.append(idx)
        
        new_value = float(input("Введите новое значение: "))
        
        set_element(array, indices, 0, new_value)
        print("Элемент успешно изменен!")
        return array
        
    except ValueError:
        print("Ошибка: введите целое число для индексов и число для значения!")
        return array

def set_element(arr, indices, level, value):
    """Рекурсивная установка значения элемента"""
    if level == len(indices) - 1:
        arr[indices[level]] = value
    else:
        set_element(arr[indices[level]], indices, level + 1, value)


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
            current_array, current_dimensions = input_array()
        
        elif choice == '2':
            display_array(current_array)
        
        elif choice == '3':
            current_array = edit_element(current_array, current_dimensions)
        
        elif choice == '4':
            print("Выход из программы")
            break
        
        else:
            print("Неверный выбор! Выберите пункт от 1 до 4.")

main()
