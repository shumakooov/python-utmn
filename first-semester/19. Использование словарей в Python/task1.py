# Реализовать постановку задачи и реализацию функции: создания глоссария, сохранения глоссария в файл, вывод глоссария на экран, функции main() с меню.

import json

# Глобальный словарь для хранения глоссария
glossary = {}

def create_glossary():
    print("\n=== СОЗДАНИЕ ГЛОССАРИЯ ===")
    
    while True:
        term = input("\nВведите термин (или 'стоп' для завершения): ").strip()
        if term.lower() == 'стоп':
            break
            
        if term in glossary:
            print(f"Термин '{term}' уже существует в глоссарии.")
            overwrite = input("Перезаписать? (да/нет): ").strip().lower()
            if overwrite != 'да':
                continue
        
        definition = input("Введите определение термина: ").strip()
        if definition:
            glossary[term] = definition
            print(f"Термин '{term}' успешно добавлен в глоссарий!")
        else:
            print("Определение не может быть пустым!")

def display_glossary():
    print("\n=== ГЛОССАРИЙ ===")
    
    if not glossary:
        print("Глоссарий пуст.")
        return
    
    for (term, definition) in glossary.items():
        print(f"{term}: {definition}")
    
    print(f"\nВсего терминов: {len(glossary)}")

def save_glossary():
    if not glossary:
        print("Глоссарий пуст. Нечего сохранять.")
        return
    
    filename = input("Введите имя файла для сохранения (по умолчанию: glossary.json): ")
    if not filename:
        filename = "glossary.json"
    
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(glossary, file, ensure_ascii=False, indent=2)
        print(f"Глоссарий успешно сохранен в файл '{filename}'!")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

def main():
    while True:
        print("\n" + "="*50)
        print("           ГЛОССАРИЙ - ГЛАВНОЕ МЕНЮ")
        print("="*50)
        print("1. Создать/добавить термины")
        print("2. Показать глоссарий")
        print("3. Сохранить глоссарий в файл")
        print("4. Выход")
        print("="*50)
        
        choice = input("Выберите действие (1-4): ").strip()
        
        if choice == '1':
            create_glossary()
        elif choice == '2':
            display_glossary()
        elif choice == '3':
            save_glossary()
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 4.")

main()
