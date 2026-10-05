# Реализовать постановку задачи и реализацию функции: ввода, вывода данных на экран, удаление кортежа, функции main() с меню.

def input_data():
    """Ввод кортежа"""
    tuples_dict = {}
    
    print("\n=== ВВОД ДАННЫХ ===")
    
    try:
        num_tuples = int(input("Введите количество кортежей"))
        for i in range(num_tuples):
            name = input(f"Введите имя для кортежа {i+1}: ")
            elements = input(f"Введите элементы кортежа '{name}' через пробел: ").split()
            tuples_dict[name] = tuple(elements)
    except ValueError:
        print("Ошибка ввода!")
    
    return tuples_dict

def display_data(tuples_dict):
    """Вывод данных на экран"""
    print("\n=== ВЫВОД ДАННЫХ ===")
    
    print("\nКОРТЕЖИ:")
    for name, data in tuples_dict.items():
        print(f"  {name}: {data}")

def delete_tuple(tuples_dict):
    """Удаление кортежа по имени"""
    print("\n=== УДАЛЕНИЕ КОРТЕЖА ===")
    
    if not tuples_dict:
        print("Нет кортежей для удаления!")
        return tuples_dict
    
    name = input("Введите имя кортежа для удаления: ")
    
    if name in tuples_dict:
        tuples_dict.pop(name)
        print(f"Кортеж '{name}' удален")
    else:
        print(f"Кортеж '{name}' не найден!")
    
    return tuples_dict

def main():
    """Главная функция с меню"""
    tuples_dict = {}
    
    while True:
        print("\n1. Ввод данных")
        print("2. Вывод данных")
        print("3. Удаление кортежа")
        print("4. Выход")
        
        choice = input("Выберите действие (1-4): ")
        
        if choice == '1':
            tuples_dict = input_data()
        elif choice == '2':
            display_data(tuples_dict)
        elif choice == '3':
            tuples_dict = delete_tuple(tuples_dict)
        elif choice == '4':
            print("Выход!")
            break
        else:
            print("Неверный выбор!")

main()
