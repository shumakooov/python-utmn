# 1. Дана строка, состоящая из групп нулей и единиц. Каждая группа отделяется от другой одним или несколькими пробелами. Найти количество групп с пятью символами.
# 2. Дана строка, состоящая из групп нулей и единиц. Каждая группа отделяется от другой одним или несколькими пробелами. Найти и вывести на экран самую короткую группу.
# 3. Дана строка, состоящая из букв, цифр, запятых, точек, знаков “+” и “-“. Выделить подстроку, которая соответствует записи целого числа (т.е. начинается со знака “+” или “-“ и внутри которой нет букв, запятых и точек).
# 4. Дана строка символов, состоящая из произвольных десятичных цифр, разделенных пробелами. Вывести на экран числа этой строки в порядке возрастания их значений.
# 5. Дана строка символов, состоящая из произвольного текста на английском языке, слова разделены пробелами. Вывести на экран слова этого текста в порядке, соответствующем латинскому алфавиту.

def task1():
    """
    Задача 1: Найти количество групп с пятью символами
    """
    test_string = "10101 111 00000 11 11111 000 1010101"
    # Разделяем строку на группы по пробелам
    groups = test_string.split()
    count = 0
    
    # Проходим по всем группам и считаем те, у которых длина 5
    for group in groups:
        if len(group) == 5:
            count += 1
    
    # Выводим результат
    print(f"Исходная строка: '{test_string}'")
    if count > 0:
        print(f"Найдено групп с пятью символами: {count}")
    else:
        print("Групп с пятью символами не найдено")
    
    return count

def task2():
    """
    Задача 2: Найти и вывести самую короткую группу
    """
    test_string = "10101 111 00000 11 11111 000 1010101"

    # Разделяем строку на группы по пробелам
    groups = test_string.split()
    
    # Если строка пустая или нет групп
    if not groups:
        return None
    
    # Находим группу с минимальной длиной
    shortest_group = min(groups, key=len)
    
    # Выводим результат
    print(f"\nИсходная строка: '{test_string}'")
    if shortest_group:
        print(f"Самая короткая группа: '{shortest_group}' (длина: {len(shortest_group)})")
    else:
        print("Группы не найдены")
    
    return shortest_group

def task3():
    """
    Задача 3: Выделить подстроку, соответствующую целому числу
    """
    test_string = "abc+123def-456ghi789.01jkl,123mno-"
    
    result = ""
    i = 0
    while i < len(test_string):
        # Если нашли знак + или -
        if test_string[i] in '+-':
            # Начинаем собирать число
            start = i
            i += 1  # переходим к символу после знака
            
            # Продолжаем пока идут цифры
            while i < len(test_string) and test_string[i].isdigit():
                i += 1
            
            # Проверяем, что после знака есть хотя бы одна цифра
            if i > start + 1:
                number = test_string[start:i]
                result = number
                break
        
        i += 1
    
    # Выводим результат
    print(f"\nИсходная строка: '{test_string}'")
    if result:
        print(f"Найдено целое число: '{result}'")
    else:
        print("Целые числа не найдены")
    
    return result

def task4():
    """
    Задача 4: Вывести числа строки в порядке возрастания
    """
    test_string = "45 12 89 3 67 23 1 99"

    # Разбиваем строку на числа по пробелам
    number_strings = test_string.split()
    numbers = []
    
    # Преобразуем строки в числа
    for num_str in number_strings:
        try:
            numbers.append(int(num_str))
        except ValueError:
            # Пропускаем нечисловые значения
            continue
    
    # Сортируем числа
    sorted_numbers = sorted(numbers)
    
    # Выводим результат
    print(f"\nИсходная строка: '{test_string}'")
    if sorted_numbers:
        print("Числа в порядке возрастания:", sorted_numbers)
    else:
        print("Числа не найдены")
    
    return sorted_numbers

def task5():
    """
    Задача 5: Вывести слова в порядке латинского алфавита
    """
    test_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

    # Разбиваем строку на слова по пробелам
    words = test_string.split()
    
    # Сортируем слова в алфавитном порядке (регистронезависимо)
    sorted_words = sorted(words, key=lambda x: x.lower())
    
    # Выводим результат
    print(f"\nИсходная строка: '{test_string}'")
    if sorted_words:
        print("Слова в алфавитном порядке:", sorted_words)
    else:
        print("Слова не найдены")
    
    return sorted_words

def main():
    """
    Главная функция, которая запускает все задачи
    """

    task1()
    task2()
    task3()
    task4()
    task5()

main()
