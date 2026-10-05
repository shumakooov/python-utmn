# 1. Дана строка символов. Символами могут быть только заглавные латинские буквы. Найти и вывести все гласные буквы (без повторений), которые встретились в двух самых длинных словах.
# 2. Дана строка символов. Символами могут быть только заглавные латинские буквы. Найти и вывести все глухие согласные буквы (без повторений), которые встретились в двух самых коротких словах.
# 3. Дана строка символов. Элементами слов могут быть любые графические символы. Удалить из массива все слова, содержащие не меньше трех четных цифр.
# 4. Дана строка символов. Символами могут быть только заглавные латинские буквы. Найти и вывести все слова, у которых число гласных букв превышает число согласных
# 5. Дана строка символов. Слова могут содержать латинские буквы и цифры. Найти слова, содержащие соответственно наибольшее и наименьшее количество заглавных латинских букв, и поменять их местами.

def task1(text):
    """
    Найти и вывести все гласные буквы (без повторений), которые встретились в двух самых длинных словах.
    """
    # Гласные буквы
    VOWELS = 'AEIOUY'
    
    # Разбиваем строку на слова и сортируем по длине в убывающем порядке
    words = text.split()
    words.sort(key=len, reverse=True)
    
    # Берем два самых длинных слова (если есть хотя бы два слова)
    if len(words) < 2:
        print("В строке меньше двух слов")
        return
    
    longest_words = words[:2]
    print(f"Два самых длинных слова: {longest_words}")
    
    # Собираем все гласные из двух самых длинных слов
    vowels_found = []
    for word in longest_words:
        for char in word:
            if char in VOWELS and char not in vowels_found:
                vowels_found.append(char)
    
    # Выводим результат
    if vowels_found:
        print(f"Гласные буквы в двух самых длинных словах: {sorted(vowels_found)}")
    else:
        print("В двух самых длинных словах нет гласных букв")


def task2(text):
    """
    Найти и вывести все глухие согласные буквы (без повторений), которые встретились в двух самых коротких словах.
    """
    # Глухие согласные буквы
    VOICELESS_CONSONANTS = 'KPSTFH'
    
    # Разбиваем строку на слова и сортируем по длине в возрастающем порядке
    words = text.split()
    words.sort(key=len)
    
    # Берем два самых коротких слова (если есть хотя бы два слова)
    if len(words) < 2:
        print("В строке меньше двух слов")
        return
    
    shortest_words = words[:2]
    print(f"Два самых коротких слова: {shortest_words}")
    
    # Собираем все глухие согласные из двух самых коротких слов
    consonants_found = []
    for word in shortest_words:
        for char in word:
            if char in VOICELESS_CONSONANTS:
                consonants_found.append(char)
    
    # Выводим результат
    if consonants_found:
        print(f"Глухие согласные в двух самых коротких словах: {sorted(consonants_found)}")
    else:
        print("В двух самых коротких словах нет глухих согласных букв")


def task3(text):
    """
    Удалить из массива все слова, содержащие не меньше трех четных цифр.
    """
    # Четные цифры
    EVEN_DIGITS = '02468'
    
    words = text.split()
    filtered_words = []
    
    for word in words:
        # Считаем количество четных цифр в слове
        even_count = 0
        for char in word:
            if char in EVEN_DIGITS:
                even_count += 1
        
        # Сохраняем слово только если в нем меньше 3 четных цифр
        if even_count < 3:
            filtered_words.append(word)
    
    # Выводим результат
    print(f"Исходная строка: {text}")
    print(f"Результат после удаления: {' '.join(filtered_words)}")
    
    removed_count = len(words) - len(filtered_words)
    print(f"Удалено слов: {removed_count}")


def task4(text):
    """
    Найти и вывести все слова, у которых число гласных букв превышает число согласных.
    """
    VOWELS = 'AEIOUY'
    CONSONANTS = 'BCDFGHJKLMNPQRSTVWXZ'
    
    words = text.split()
    result_words = []
    
    for word in words:
        vowel_count = 0
        consonant_count = 0
        
        # Считаем гласные и согласные в слове
        for char in word:
            if char in VOWELS:
                vowel_count += 1
            elif char in CONSONANTS:
                consonant_count += 1
        
        # Проверяем условие: гласных больше чем согласных
        if vowel_count > consonant_count:
            result_words.append(word)
    
    # Выводим результат
    if result_words:
        print(f"Исходная строка: {text}")
        print(f"Слова, где гласных больше чем согласных: {result_words}")
    else:
        print("Нет слов, где гласных больше чем согласных")


def task5(text):
    """
    Найти слова с максимальным и минимальным количеством заглавных латинских букв и поменять их местами.
    """
    # Заглавные латинские буквы
    UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    words = text.split()
    
    if len(words) < 2:
        print("В строке меньше двух слов")
        return
    
    # Находим слова с максимальным и минимальным количеством заглавных букв
    max_upper_count = -1
    min_upper_count = float('inf')
    max_upper_word = ""
    min_upper_word = ""
    max_index = -1
    min_index = -1
    
    for i, word in enumerate(words):
        upper_count = 0
        for char in word:
            if char in UPPERCASE_LETTERS:
                upper_count += 1
        
        # Обновляем максимум
        if upper_count > max_upper_count:
            max_upper_count = upper_count
            max_upper_word = word
            max_index = i
        
        # Обновляем минимум (только если есть хотя бы одна заглавная буква)
        if 0 < upper_count < min_upper_count:
            min_upper_count = upper_count
            min_upper_word = word
            min_index = i
    
    # Проверяем, найдены ли подходящие слова
    if max_index == -1 or min_index == -1:
        print("Не найдено слов с заглавными латинскими буквами")
        return
    
    # Меняем слова местами
    words[max_index], words[min_index] = words[min_index], words[max_index]
    
    # Выводим результат
    print(f"Исходная строка: {text}")
    print(f"Слово с максимальным количеством заглавных букв: '{max_upper_word}' ({max_upper_count} заглавных)")
    print(f"Слово с минимальным количеством заглавных букв: '{min_upper_word}' ({min_upper_count} заглавных)")
    print(f"Результат после замены: {' '.join(words)}")


# Демонстрация работы всех функций
def main():
    print("ЗАДАНИЕ 1")
    text1 = "PROGRAMMING IS FUN AND CHALLENGING"
    task1(text1)
    
    print("\nЗАДАНИЕ 2")
    text2 = "HELLO WORLD PYTHON CODE"
    task2(text2)
    
    print("\nЗАДАНИЕ 3")
    text3 = "abc 1234 def56 789ghi 2468jkl 1357mno"
    task3(text3)
    
    print("\nЗАДАНИЕ 4")
    text4 = "HELLO APPLE UNIVERSITY EDUCATION"
    task4(text4)
    
    print("\nЗАДАНИЕ 5")
    text5 = "Hello WORLD Python CODE Example"
    task5(text5)

main()
