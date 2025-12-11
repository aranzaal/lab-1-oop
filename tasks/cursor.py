class Cursor:
    def __init__(self,
                 first: int = 0,
                 second: int = 0,
                 width: int = 1920,
                 height: int = 1200) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Размеры экрана должны быть положительными")

        self.__width = int(width)
        self.__height = int(height)

        if not self._in_range(first, second):
            raise ValueError("Начальные координаты выходят за границы экрана")

        self.__first = int(first)
        self.__second = int(second)

    def _in_range(self, x: int, y: int) -> bool:
        return 0 <= x < self.__width and 0 <= y < self.__height

    def read(self) -> None:
        x = int(input("Введите координату X (по горизонтали): "))
        y = int(input("Введите координату Y (по вертикали): "))

        if not self._in_range(x, y):
            raise ValueError("Координаты выходят за границы экрана")

        self.__first = x
        self.__second = y

    def display(self) -> None:
        print(f"Координаты курсора: ({self.__first}, {self.__second})")
        print(f"Размер экрана: {self.__width} x {self.__height}")

    @property
    def first(self) -> int:
        return self.__first

    @property
    def second(self) -> int:
        return self.__second

    def changex(self, dx: int) -> None:
        new_x = self.__first + int(dx)

        if not self._in_range(new_x, self.__second):
            raise ValueError("Новая координата X выходит за границы экрана")

        self.__first = new_x

    def changey(self, dy: int) -> None:
        new_y = self.__second + int(dy)

        if not self._in_range(self.__first, new_y):
            raise ValueError("Новая координата Y выходит за границы экрана")

        self.__second = new_y
