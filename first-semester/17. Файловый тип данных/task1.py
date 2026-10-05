# Реализовать постановку задачи и реализацию функции: ввода, вывода данных на экран, функции main() с меню.

def read_file(filename):
    """
    Чтение содержимого файла и возврат данных
    """
    try:
        file = open(filename, 'r')
        return file
    except FileNotFoundError:
        return "Ошибка: Файл не найден"
    except PermissionError:
        return "Ошибка: Нет прав доступа к файлу"
    except Exception as e:
        return f"Ошибка при чтении файла: {e}"

def display_file_content(file):
    """
    Вывод содержимого файла на экран
    """
    print("СОДЕРЖИМОЕ ФАЙЛА:")
    print(file.read())


def main():
    """
    Основная функция с меню управления
    """
    current_file = None
    
    while True:
        print("МЕНЮ УПРАВЛЕНИЯ ФАЙЛАМИ")
        print("1. Открыть файл")
        print("2. Показать содержимое файла")
        print("3. Выйти из программы")
        
        if current_file:
            print(f"Текущий файл: {current_file}")
        
        choice = input("Выберите действие (1-3): ")
        
        if choice == '1':
            # Открытие существующего файла
            filename = input("Введите имя файла для открытия: ")
            current_file = read_file(filename)
            print(f"Файл '{filename}' успешно открыт")
        
        elif choice == '2':
            # Показать содержимое текущего файла
            if current_file:
                display_file_content(current_file)
            else:
                print("Файл не открыт. Сначала откройте или создайте файл.")
        
        elif choice == '3':
            # Выход
            print("Выход из программы")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 3.")

main()
