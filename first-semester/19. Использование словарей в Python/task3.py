# Указания к заданию:
# • задание должно быть реализовано с помощью функций;
# • в программе обязательно должны быть комментарии к тексту программы, поясняющие ее работу;
# • программу реализовать с использованием словарей;
# • необходимо предусмотреть обработку ошибок ввода;
# • в программе должны быть реализованы функции содержащие базовые операции со словарями, такие как добавление, удаление, доступ по ключу и итерация.
# Задание 1: Подсчет частоты слов
# Напишите программу, которая получает строку текста от пользователя и подсчитывает количество вхождений каждого слова в этой строке. Сохраните результаты в словаре, где ключ — слово, а значение — количество его вхождений.

def get_text_from_user():
    while True:
        try:
            text = input("Введите текст для анализа: ").strip()
            if not text:
                print("Ошибка: Текст не может быть пустым. Попробуйте снова.")
                continue
            return text
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            exit()
        except Exception as e:
            print(f"Произошла ошибка ввода: {e}. Попробуйте снова.")

def clean_word(word):
    # Удаляем знаки препинания с начала и конца слова
    punctuation = '.,!?;:"()[]{}«»—'
    cleaned_word = word.strip(punctuation).lower()
    return cleaned_word

def count_word_frequency(text):
    # Разбиваем текст на слова
    words = text.split()
    
    # Создаем пустой словарь для хранения частот
    word_frequency = {}
    
    # Итерация по всем словам в тексте
    for word in words:
        # Очищаем слово от знаков препинания
        cleaned_word = clean_word(word)
        
        # Пропускаем пустые строки (могли остаться после очистки)
        if not cleaned_word:
            continue
            
        # Доступ по ключу и добавление в словарь
        if cleaned_word in word_frequency:
            # Если слово уже есть в словаре - увеличиваем счетчик
            word_frequency[cleaned_word] += 1
        else:
            # Если слова нет - добавляем со значением 1
            word_frequency[cleaned_word] = 1
    
    return word_frequency

def add_word_to_dictionary(dictionary, word):
    cleaned_word = clean_word(word)
    if cleaned_word:
        if cleaned_word in dictionary:
            dictionary[cleaned_word] += 1
        else:
            dictionary[cleaned_word] = 1
    return dictionary

def remove_word_from_dictionary(dictionary, word):
    cleaned_word = clean_word(word)
    if cleaned_word in dictionary:
        # Удаление элемента по ключу
        del dictionary[cleaned_word]
        print(f"Слово '{cleaned_word}' удалено из словаря.")
    else:
        print(f"Слово '{cleaned_word}' не найдено в словаре.")
    return dictionary

def display_frequency_statistics(dictionary):
    if not dictionary:
        print("Словарь частот пуст.")
        return
    
    print("\n" + "="*50)
    print("СТАТИСТИКА ЧАСТОТЫ СЛОВ")
    print("="*50)
    
    # Итерация по словарю и вывод всех пар ключ-значение
    for word, frequency in dictionary.items():
        print(f"'{word}': {frequency} раз(а)")
    
    # Дополнительная статистика
    print("\n" + "-"*50)
    print(f"Всего уникальных слов: {len(dictionary)}")
    print(f"Самое частое слово: '{max(dictionary, key=dictionary.get)}'")
    print(f"Максимальная частота: {max(dictionary.values())}")

def sort_dictionary_by_frequency(dictionary, reverse=True):
    # Создаем отсортированный словарь
    sorted_dict = dict(sorted(dictionary.items(), 
                            key=lambda item: item[1], 
                            reverse=reverse))
    return sorted_dict

def save_results_to_file(dictionary, filename="word_frequency.txt"):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("РЕЗУЛЬТАТЫ ПОДСЧЕТА ЧАСТОТЫ СЛОВ\n")
            file.write("=" * 40 + "\n")
            
            # Итерация по словарю и запись в файл
            for word, frequency in dictionary.items():
                file.write(f"{word}: {frequency}\n")
                
        print(f"Результаты сохранены в файл: {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении в файл: {e}")

def interactive_mode():
    print("\nИНТЕРАКТИВНЫЙ РЕЖИМ РАБОТЫ СО СЛОВАРЕМ")
    print("Изначальный словарь создан из введенного текста.")
    
    # Получаем начальный текст от пользователя
    text = get_text_from_user()
    frequency_dict = count_word_frequency(text)
    
    while True:
        print("\n" + "="*40)
        print("ВОЗМОЖНЫЕ ДЕЙСТВИЯ:")
        print("1. Показать статистику частот")
        print("2. Добавить слово в словарь")
        print("3. Удалить слово из словаря")
        print("4. Отсортировать словарь по частоте")
        print("5. Сохранить результаты в файл")
        print("6. Выйти в главное меню")
        print("="*40)
        
        try:
            choice = input("Выберите действие (1-6): ").strip()
            
            if choice == '1':
                display_frequency_statistics(frequency_dict)
                
            elif choice == '2':
                word = input("Введите слово для добавления: ").strip()
                frequency_dict = add_word_to_dictionary(frequency_dict, word)
                print(f"Слово '{clean_word(word)}' добавлено в словарь")
                
            elif choice == '3':
                word = input("Введите слово для удаления: ").strip()
                frequency_dict = remove_word_from_dictionary(frequency_dict, word)
                
            elif choice == '4':
                frequency_dict = sort_dictionary_by_frequency(frequency_dict)
                print("Словарь отсортирован по убыванию частоты")
                display_frequency_statistics(frequency_dict)
                
            elif choice == '5':
                filename = input("Введите имя файла (по умолчанию word_frequency.txt): ").strip()
                if not filename:
                    filename = "word_frequency.txt"
                save_results_to_file(frequency_dict, filename)
                
            elif choice == '6':
                break
            else:
                print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")
                
        except KeyboardInterrupt:
            print("\n\nВозврат в главное меню.")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")

def simple_count_mode():
    print("\nПРОСТОЙ ПОДСЧЕТ ЧАСТОТЫ СЛОВ")
    text = get_text_from_user()
    frequency_dict = count_word_frequency(text)
    display_frequency_statistics(frequency_dict)
    
    # Предлагаем сохранить результаты
    save_choice = input("\nСохранить результаты в файл? (да/нет): ").strip().lower()
    if save_choice in ['да', 'д', 'yes', 'y']:
        save_results_to_file(frequency_dict)

def main():
    print("ПРОГРАММА ПОДСЧЕТА ЧАСТОТЫ СЛОВ")
    print("=" * 40)
    
    while True:
        print("\nГЛАВНОЕ МЕНЮ:")
        print("1. Простой подсчет частоты слов")
        print("2. Интерактивный режим работы со словарем")
        print("3. Выход")
        
        try:
            choice = input("Выберите режим работы (1-3): ").strip()
            
            if choice == '1':
                simple_count_mode()
            elif choice == '2':
                interactive_mode()
            elif choice == '3':
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.")
                
        except KeyboardInterrupt:
            print("\n\nПрограмма завершена.")
            break
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

main()
