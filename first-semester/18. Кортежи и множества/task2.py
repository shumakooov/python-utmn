# 2) Книги
# Имеются данные о книгах: название книги, автор, год издания. Вывести на экран книги, изданные после 2010 года и написанные автором "Толстой".

# Словарь кортежей с книгами
books = {
    1: ("Название_1", "Толстой", 2015),
    2: ("Название_2", "Достоевский", 2020),
    3: ("Название_3", "Булгаков", 2010),
    4: ("Название_4", "Толстой", 2000),
    5: ("Название_5", "Оруэлл", 2005),
    6: ("Название_6", "Достоевский", 1995),
    7: ("Название_7", "Ремарк", 2015),
    8: ("Название_8", "Толстой", 2020),
    9: ("Название_9", "Булгаков", 1990),
    10: ("Название_10", "Оруэлл", 2010),
}

# Функция для получения следующего доступного ID
def get_next_id():
    if books:
        return max(books.keys()) + 1
    return 1

# Функция для добавления новой книги
def add_book():
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите год издания: "))
    
    book_id = get_next_id()
    books[book_id] = (title, author, year)
    print(f"Книга успешно добавлена с ID: {book_id}")

# Функция для удаления книги
def delete_book():
    display_books()
    try:
        book_id = int(input("Введите ID книги для удаления: "))
        if book_id in books:
            deleted_book = books.pop(book_id)
            print(f"Книга '{deleted_book[0]}' удалена")
        else:
            print("Книга с таким ID не найдена")
    except ValueError:
        print("Ошибка: ID должен быть числом!")

# Функция для отображения всех книг
def display_books():
    if not books:
        print("Список книг пуст")
        return
    
    print("\n" + "="*50)
    print("СПИСОК КНИГ:")
    print("="*50)
    print(f"{'ID':<3} {'Название':<15} {'Автор':<15} {'Год':<6}")
    print("-"*50)
    
    for book_id, (title, author, year) in books.items():
        print(f"{book_id:<3} {title:<15} {author:<15} {year:<6}")
    print("="*50)

# Функция для редактирования книги
def edit_book():
    display_books()
    try:
        book_id = int(input("Введите ID книги для редактирования: "))
        if book_id in books:
            print(f"Текущие данные книги: {books[book_id]}")
            
            title = input("Введите новое название (оставьте пустым для сохранения текущего): ")
            author = input("Введите нового автора (оставьте пустым для сохранения текущего): ")
            year_input = input("Введите новый год (оставьте пустым для сохранения текущего): ")
            
            current_title, current_author, current_year = books[book_id]
            
            # Обновляем только измененные поля
            new_title = title if title else current_title
            new_author = author if author else current_author
            new_year = int(year_input) if year_input else current_year
            
            books[book_id] = (new_title, new_author, new_year)
            print("Книга успешно обновлена")
        else:
            print("Книга с таким ID не найдена")
    except ValueError:
        print("Ошибка: ID и год должны быть числами!")

# Функция для поиска книг по условию
def find_books_by_condition():
    found_books = []
    
    for book_id, (title, author, year) in books.items():
        if author == "Толстой" and year > 2010:
            found_books.append((book_id, title, author, year))
    
    # Вывод результатов поиска
    if found_books:
        print("\n" + "="*60)
        print("НАЙДЕННЫЕ КНИГИ (Толстой, после 2010 года):")
        print("="*60)
        print(f"{'ID':<3} {'Название':<15} {'Автор':<15} {'Год':<6}")
        print("-"*60)
        
        for book_id, title, author, year in found_books:
            print(f"{book_id:<3} {title:<15} {author:<15} {year:<6}")
        print("="*60)
        print(f"Найдено книг: {len(found_books)}")
    else:
        print("Книги, соответствующие условиям поиска, не найдены")

# Функция для отображения меню
def display_menu():
    print("\n" + "="*40)
    print("МЕНЮ УПРАВЛЕНИЯ БИБЛИОТЕКОЙ")
    print("="*40)
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Показать все книги")
    print("4. Редактировать книгу")
    print("5. Найти книги Толстого после 2010 года")
    print("6. Выход")
    print("="*40)

# Главная функция программы
def main():
    print("Добро пожаловать в систему управления библиотекой!")
    
    # Бесконечный цикл для работы меню
    while True:
        display_menu()
        
        try:
            choice = input("Выберите действие (1-6): ")
            
            if choice == "1":
                add_book()
            elif choice == "2":
                delete_book()
            elif choice == "3":
                display_books()
            elif choice == "4":
                edit_book()
            elif choice == "5":
                find_books_by_condition()
            elif choice == "6":
                print("Выход из программы. До свидания!")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите от 1 до 6.")
        
        except KeyboardInterrupt:
            print("\nВыход из программы")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")

main()
