class Coord:
    def __init__(self, first, second):
        if type(first) != int or type(second) != int:
            print("Ошибка: координаты должны быть целыми числами")
            raise SystemExit(1)
        if first <= 0 or second <= 0:
            print("Ошибка: координаты должны быть положительными")
            raise SystemExit(1)

        self.first = first
        self.second = second

    def read(self):
        x = int(input("Введите целую положительную координату по горизонтали (x): "))
        y = int(input("Введите целую положительную координату по вертикали (y): "))
        self.__init__(x, y)

    def display(self):
        print("Координаты курсора: first (x) =", self.first, ", second (y) =", self.second)

    def changex(self, dx):
        new_x = self.first + dx
        # ширина 1920 по x
        if new_x <= 0 or new_x > 1920:
            print("changex: новая координата x выходит за границы экрана (1..1920)")
        else:
            self.first = new_x

    def changey(self, dy):
        new_y = self.second + dy
        # высота 1200 по y
        if new_y <= 0 or new_y > 1200:
            print("changey: новая координата y выходит за границы экрана (1..1200)")
        else:
            self.second = new_y

# Внешняя функция make_тип() → make_Coord()
def make_Coord(first, second):
    """
    Функция получает значения для полей first и second
    и возвращает объект Coord. Если параметры неправильные,
    выводит сообщение и завершает работу.
    """
    try:
        obj = Coord(first, second)
        return obj
    except SystemExit:
        print("Объект Coord не создан из-за некорректных параметров")
        raise


if __name__ == "__main__":
    # Демонстрация возможностей класса Coord

    # 1. Создаём объект с начальными координатами
    cursor = make_Coord(100, 200)
    cursor.display()

    # 2. Вводим координаты с клавиатуры
    print("\nВведите новые координаты:")
    cursor.read()
    cursor.display()

    # 3. Меняем координаты с помощью changex и changey
    print("\nСдвигаем курсор:")
    cursor.changex(50)     # сдвиг по x
    cursor.changey(-30)    # сдвиг по y
    cursor.display()

    # 4. Пример выхода за границы экрана
    print("\nПробуем выйти за границы экрана:")
    cursor.changex(100000)  # заведомо неправильный сдвиг по x
    cursor.changey(-100000) # заведомо неправильный сдвиг по y
    cursor.display()
