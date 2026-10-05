# 1. Написать программу, которая считывает текст из файла и выводит его на экран, заменив цифры от 0 до 9 на слова «ноль», «один», ..., «девять», начиная каждое предложение с новой строки.
# 2. Дан текстовый файл. Создать символьный файл, содержащий все знаки препинания, встретившиеся в текстовом файле (в том же порядке).
# 3. Дана некоторая буква и текстовый файл. Создать файл, содержащий все слова из исходного файла, начинающиеся и оканчивающиеся этой буквой (как прописной, так и строчной). Знаки препинания, расположенные в начале и в конце слов, не учитывать. Если исходный файл не содержит подходящих слов, оставить результирующий файл пустым.
# 4. Дан текстовый файл, содержащий слова паразиты (ну, короче и т.п.) Удалить из текстового файла эти слова и создать новый файл без этих слов.
# 5. Даны два текстовых файла. Составить третий файл, состоящий из слов, которые встречаются и в первом файле и во втором.

import string

def task1_replace_digits():
    """
    Задача 1: Замена цифр на слова в тексте
    """
    filename = input("Введите имя файла для чтения: ")
    
    # Словарь для замены цифр на слова
    digit_words = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Заменяем цифры на слова
        for digit, word in digit_words.items():
            text = text.replace(digit, word)
        
        # Разбиваем текст на предложения и выводим каждое с новой строки
        sentences = []
        current_sentence = ""
        
        for char in text:
            current_sentence += char
            if char in '.!?…':
                sentences.append(current_sentence.strip())
                current_sentence = ""
        
        # Добавляем последнее предложение, если оно есть
        if current_sentence.strip():
            sentences.append(current_sentence.strip())
        
        print("\nТекст с замененными цифрами (каждое предложение с новой строки):")
        print("=" * 60)
        for sentence in sentences:
            if sentence:  # Проверяем, что предложение не пустое
                print(sentence)
        
        if not sentences:
            print("Файл не содержит предложений.")
            
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден!")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")

def task2_punctuation_marks():
    """
    Задача 2: Создание файла со знаками препинания из текста
    """
    input_filename = input("Введите имя исходного файла: ")
    output_filename = input("Введите имя файла для знаков препинания: ")
    
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Собираем все знаки препинания
        punctuation_marks = []
        for char in text:
            if char in string.punctuation + '—–«»„“' + string.whitespace:
                # string.punctuation содержит стандартные знаки препинания
                # добавляем тире, кавычки и пробельные символы
                punctuation_marks.append(char)
        
        # Записываем знаки препинания в новый файл
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(''.join(punctuation_marks))
        
        print(f"\nНайдено {len(punctuation_marks)} знаков препинания.")
        print(f"Знаки препинания сохранены в файл '{output_filename}'")
        
        if punctuation_marks:
            print("Первые 50 знаков препинания:", ''.join(punctuation_marks[:50]))
        else:
            print("В исходном файле не найдено знаков препинания.")
            
    except FileNotFoundError:
        print(f"Файл '{input_filename}' не найден!")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")

def task3_words_start_end_with_letter():
    """
    Задача 3: Слова, начинающиеся и заканчивающиеся на заданную букву
    """
    input_filename = input("Введите имя исходного файла: ")
    output_filename = input("Введите имя файла для результатов: ")
    letter = input("Введите букву: ").lower()
    
    if len(letter) != 1 or not letter.isalpha():
        print("Ошибка: нужно ввести одну букву!")
        return
    
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Разбиваем текст на слова, убирая знаки препинания
        words = []
        current_word = ""
        
        for char in text:
            if char.isalpha():
                current_word += char
            else:
                if current_word:
                    words.append(current_word)
                    current_word = ""
        
        # Добавляем последнее слово, если оно есть
        if current_word:
            words.append(current_word)
        
        # Ищем слова, начинающиеся и заканчивающиеся на заданную букву
        matching_words = []
        for word in words:
            if (word.lower().startswith(letter) and 
                word.lower().endswith(letter) and 
                len(word) > 1):  # Исключаем однобуквенные слова
                matching_words.append(word)
        
        # Записываем результаты в файл
        with open(output_filename, 'w', encoding='utf-8') as file:
            for word in matching_words:
                file.write(word + '\n')
        
        print(f"\nНайдено {len(matching_words)} слов, начинающихся и заканчивающихся на букву '{letter}'")
        
        if matching_words:
            print("Найденные слова:", ', '.join(matching_words[:20]))  # Показываем первые 20 слов
            print(f"Все слова сохранены в файл '{output_filename}'")
        else:
            print("Подходящих слов не найдено. Результирующий файл оставлен пустым.")
            
    except FileNotFoundError:
        print(f"Файл '{input_filename}' не найден!")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")

def task4_remove_parasite_words():
    """
    Задача 4: Удаление слов-паразитов из текста
    """
    input_filename = input("Введите имя исходного файла: ")
    parasite_filename = input("Введите имя файла со словами-паразитами: ")
    output_filename = input("Введите имя файла для результатов: ")
    
    try:
        # Читаем исходный текст
        with open(input_filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Читаем слова-паразиты
        with open(parasite_filename, 'r', encoding='utf-8') as file:
            parasite_words = [line.strip().lower() for line in file if line.strip()]
        
        if not parasite_words:
            print("Файл со словами-паразитами пуст!")
            return
        
        print(f"Слова-паразиты для удаления: {', '.join(parasite_words)}")
        
        # Разбиваем текст на слова с сохранением разделителей
        words = []
        current_word = ""
        
        for char in text:
            if char.isalpha():
                current_word += char
            else:
                if current_word:
                    words.append(current_word)
                    current_word = ""
                words.append(char)  # Добавляем разделитель
        
        # Добавляем последнее слово, если оно есть
        if current_word:
            words.append(current_word)
        
        # Удаляем слова-паразиты
        cleaned_words = []
        removed_count = 0
        
        for word in words:
            if word.isalpha() and word.lower() in parasite_words:
                removed_count += 1
            else:
                cleaned_words.append(word)
        
        # Собираем очищенный текст
        cleaned_text = ''.join(cleaned_words)
        
        # Записываем результат в файл
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)
        
        print(f"\nУдалено {removed_count} слов-паразитов.")
        print(f"Очищенный текст сохранен в файл '{output_filename}'")
        
        if removed_count == 0:
            print("Слова-паразиты в тексте не найдены.")
            
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")

def task5_common_words():
    """
    Задача 5: Поиск общих слов в двух файлах
    """
    file1 = input("Введите имя первого файла: ")
    file2 = input("Введите имя второго файла: ")
    output_file = input("Введите имя файла для результатов: ")
    
    def extract_words(filename):
        """Извлекает слова из файла"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                text = f.read().lower()
            
            # Убираем знаки препинания и разбиваем на слова
            words = []
            current_word = ""
            
            for char in text:
                if char.isalpha():
                    current_word += char
                else:
                    if current_word:
                        words.append(current_word)
                        current_word = ""
            
            # Добавляем последнее слово
            if current_word:
                words.append(current_word)
            
            return set(words)  # Используем set для уникальности
            
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден!")
            return None
        except Exception as e:
            print(f"Ошибка при чтении файла '{filename}': {e}")
            return None
    
    # Извлекаем слова из обоих файлов
    words1 = extract_words(file1)
    words2 = extract_words(file2)
    
    if words1 is None or words2 is None:
        return
    
    # Находим общие слова
    common_words = words1.intersection(words2)
    
    # Записываем результат в файл
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for word in sorted(common_words):  # Сортируем для удобства
                f.write(word + '\n')
        
        print(f"\nВ первом файле: {len(words1)} уникальных слов")
        print(f"Во втором файле: {len(words2)} уникальных слов")
        print(f"Найдено {len(common_words)} общих слов")
        
        if common_words:
            print("Общие слова:", ', '.join(sorted(common_words)[:20]))  # Показываем первые 20
            print(f"Все общие слова сохранены в файл '{output_file}'")
        else:
            print("Общих слов не найдено. Результирующий файл оставлен пустым.")
            
    except Exception as e:
        print(f"Ошибка при записи результата: {e}")

def main():
    """
    Главная функция с меню для выбора задач
    """
    print("Программа для обработки текстовых файлов")
    print("=" * 50)
    
    while True:
        print("\nВыберите задачу:")
        print("1. Замена цифр на слова в тексте")
        print("2. Создание файла со знаками препинания")
        print("3. Слова, начинающиеся и заканчивающиеся на букву")
        print("4. Удаление слов-паразитов")
        print("5. Поиск общих слов в двух файлах")
        print("6. Выход")
        
        choice = input("\nВведите номер задачи (1-6): ")
        
        if choice == '1':
            task1_replace_digits()
        elif choice == '2':
            task2_punctuation_marks()
        elif choice == '3':
            task3_words_start_end_with_letter()
        elif choice == '4':
            task4_remove_parasite_words()
        elif choice == '5':
            task5_common_words()
        elif choice == '6':
            print("Выход из программы")
            break
        else:
            print("Неверный выбор! Пожалуйста, введите число от 1 до 6.")

main()
