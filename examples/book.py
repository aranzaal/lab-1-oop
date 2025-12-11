# Класс Book
class Book:
    # Атрибуты класса
    material = "paper"
    cover = "paperback"
    all_books = []


def main():
    # Экземпляр класса Book
    my_book = Book()
    print(" Экземпляр класса Book: \n")
    print(
        f" Material: {my_book.material}\n Cover: \
            {my_book.cover}\n Books: {my_book.all_books}"
    )


if __name__ == "__main__":
    main()