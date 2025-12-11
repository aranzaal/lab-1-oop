from cursor import Cursor

if __name__ == "__main__":
    try:
        cursor = Cursor(2, 2)
        cursor.display()

        cursor.read()
        cursor.display()

        print("Попробуем изменить координаты курсора:")
        dx = int(input("Смещение по X: "))
        dy = int(input("Смещение по Y: "))

        cursor.changex(dx)
        cursor.changey(dy)
        cursor.display()
    except ValueError as e:
        print("Ошибка:", e)
