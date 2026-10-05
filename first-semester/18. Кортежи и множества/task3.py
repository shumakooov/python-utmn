# 5. Дана строка символов. Найти и вывести все гласные буквы (без повторений), которые встретились в словах и количество слов.

def find_unique_vowels(text):
    """
    Функция для поиска уникальных гласных букв в тексте и подсчета количества слов.
    """
    # Множество гласных букв русского языка (в нижнем регистре)
    vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
    
    # Приводим текст к нижнему регистру для единообразия
    text_lower = text.lower()
    
    # Разбиваем текст на слова
    words = text_lower.split()
    
    # Множество для хранения найденных гласных
    found_vowels = set()
    
    # Перебираем все слова и ищем гласные
    for word in words:
        # Очищаем слово от знаков препинания
        clean_word = ''.join(char for char in word if char.isalpha())
        
        # Если слово не пустое после очистки
        if clean_word:
            # Находим гласные в текущем слове
            word_vowels = {char for char in clean_word if char in vowels}
            # Добавляем найденные гласные в общее множество
            found_vowels.update(word_vowels)
    
    return found_vowels, len(words)

def print_results(vowels_set, word_count):
    """
    Функция для вывода результатов.
    """
    print("=" * 50)
    print("РЕЗУЛЬТАТЫ АНАЛИЗА ТЕКСТА")
    print("=" * 50)
    
    # Выводим информацию о количестве слов
    print(f"Количество слов в тексте: {word_count}")
    
    # Выводим информацию о найденных гласных
    if vowels_set:
        print(f"Найдено уникальных гласных букв: {len(vowels_set)}")
        print("Список найденных гласных:")
        for vowel in vowels_set:
            print(f"  - '{vowel}'")
    else:
        print("Гласные буквы в тексте не найдены.")
    
    print("=" * 50)

def main():
    """
    Основная функция программы.
    """
    # Пример текста для анализа
    example_text = "Дана строка символов. Найти и вывести все гласные буквы без повторений."
    
    print("Программа для поиска уникальных гласных букв в тексте")
    print("Используемый текст для анализа:")
    print(f"\"{example_text}\"")
    print()
    
    # Вызываем функцию анализа
    vowels_found, total_words = find_unique_vowels(example_text)
    
    # Выводим результаты
    print_results(vowels_found, total_words)
    
main()
