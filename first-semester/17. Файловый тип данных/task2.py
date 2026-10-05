# Текстовый файл может содержать данные следующего типа записанные через соответствующий разделить:
# • название пункта назначения рейса;
# • номер рейса;
# • тип самолета.
# Написать программу, выполняющую следующие действия:
# 1. ввод с клавиатуры данных и запись их в файл;
# 2. вывод на экран информации о рейсе, номер которого введен с клавиатуры, если таких рейсов нет, вывести соответствующее сообщение

import csv
import random

# Списки для генерации случайных данных (для дополнительного задания)
DESTINATIONS = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань", 
               "Сочи", "Владивосток", "Калининград", "Краснодар", "Минеральные Воды"]
AIRCRAFT_TYPES = ["Boeing 737", "Airbus A320", "Boeing 777", "Airbus A330", "Sukhoi Superjet",
                 "Ил-96", "Ту-204", "Embraer E-Jet", "Bombardier CRJ", "ATR 72"]

def create_file():
    """
    Создание нового CSV файла с заголовками
    """
    filename = input("Введите имя файла (например: flights.csv): ")
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Записываем заголовки столбцов
            writer.writerow(['destination', 'flight_number', 'aircraft_type'])
        print(f"Файл '{filename}' успешно создан!")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")

def input_data():
    """
    Ввод данных с клавиатуры и запись/дозапись в файл
    """
    filename = input("Введите имя файла для записи данных: ")
    
    try:
        # Проверяем существование файла
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                pass
        except FileNotFoundError:
            print("Файл не найден! Создайте файл сначала.")
            return
        
        # Ввод данных
        destination = input("Введите пункт назначения: ")
        flight_number = input("Введите номер рейса: ")
        aircraft_type = input("Введите тип самолета: ")
        
        # Запись данных в файл
        with open(filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([destination, flight_number, aircraft_type])
        
        print("Данные успешно записаны в файл!")
        
    except Exception as e:
        print(f"Ошибка при записи данных: {e}")

def display_all_data():
    """
    Вывод всех данных из файла на экран
    """
    filename = input("Введите имя файла для чтения: ")
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            print("Все данные из файла:\n")
            
            # Пропускаем заголовок
            headers = next(reader, None)
            if headers:
                print(f"{'Пункт назначения':<20} {'Номер рейса':<12} {'Тип самолета':<15}")
                print("-" * 50)
            
            data_exists = False
            for row in reader:
                if len(row) >= 3:
                    print(f"{row[0]:<20} {row[1]:<12} {row[2]:<15}")
                    data_exists = True
            
            if not data_exists:
                print("Файл пуст или не содержит данных.")
                
    except FileNotFoundError:
        print("Файл не найден!")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

def search_flight_by_number():
    """
    Поиск информации о рейсе по номеру
    """
    filename = input("Введите имя файла для поиска: ")
    search_number = input("Введите номер рейса для поиска: ")
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            # Пропускаем заголовок
            next(reader, None)
            
            found_flights = []
            for row in reader:
                if len(row) >= 2 and row[1] == search_number:
                    found_flights.append(row)
            
            # Вывод результатов поиска
            if found_flights:
                print(f"\nНайдено {len(found_flights)} рейс(ов) с номером {search_number}:")
                print("="*50)
                print(f"{'Пункт назначения':<20} {'Номер рейса':<12} {'Тип самолета':<15}")
                print("-" * 50)
                for flight in found_flights:
                    print(f"{flight[0]:<20} {flight[1]:<12} {flight[2]:<15}")
            else:
                print(f"\nРейсов с номером {search_number} не найдено.")
                
    except FileNotFoundError:
        print("Файл не найден!")
    except Exception as e:
        print(f"Ошибка при поиске: {e}")

def generate_random_data():
    """
    Генерация случайных данных (дополнительное задание)
    """
    filename = input("Введите имя файла для генерации данных: ")
    num = int(input("Введите количество записей для генерации: "))
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Записываем заголовки
            writer.writerow(['destination', 'flight_number', 'aircraft_type'])
            
            # Генерируем случайные записи
            for i in range(num):
                destination = random.choice(DESTINATIONS)
                flight_number = f"SU{random.randint(1000, 9999)}"
                aircraft_type = random.choice(AIRCRAFT_TYPES)
                writer.writerow([destination, flight_number, aircraft_type])
        
        print(f"Сгенерировано {num} случайных записей в файл '{filename}'!")
        
    except Exception as e:
        print(f"Ошибка при генерации данных: {e}")

def main():
    """
    Главная функция программы с меню
    """
    print("Программа для работы с данными о рейсах")
    print("=" * 40)
    
    while True:
        # Вывод меню
        print("\nМеню:")
        print("1. Создать файл")
        print("2. Ввести данные")
        print("3. Вывести все данные")
        print("4. Найти рейс по номеру")
        print("5. Сгенерировать случайные данные")
        print("6. Выйти из программы")
        
        choice = input("\nВыберите пункт меню (1-6): ")
        
        if choice == '1':
            create_file()
        elif choice == '2':
            input_data()
        elif choice == '3':
            display_all_data()
        elif choice == '4':
            search_flight_by_number()
        elif choice == '5':
            generate_random_data()
        elif choice == '6':
            print("Выход из программы")
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите пункт от 1 до 6.")

main()
