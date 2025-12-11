from __future__ import annotations

class ModelWindow:

    def __init__(
        self,
        title: str = "Окно",
        x: int = 0,
        y: int = 0,
        width: int = 1920,
        height: int = 1200,
        color: str = "серый",
        visible: bool = True,
        framed: bool = True,
    ) -> None:
        self.__title = str(title)
        self.__x = int(x)
        self.__y = int(y)
        self.__width = int(width)
        self.__height = int(height)
        self.__color = str(color)
        self.__visible = bool(visible)
        self.__framed = bool(framed)

    @property
    def title(self) -> str:
        return self.__title

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def color(self) -> str:
        return self.__color

    @property
    def visible(self) -> str:
        return "Да" if self.__visible else "Нет"

    @property
    def framed(self) -> str:
        return "Да" if self.__framed else "Нет"

    def read(self) -> None:
        self.__title = input("Заголовок окна: ")
        self.__x = int(input("Координата X левого верхнего угла: "))
        self.__y = int(input("Координата Y левого верхнего угла: "))
        self.__width = int(input("Ширина окна: "))
        self.__height = int(input("Высота окна: "))
        self.__color = input("Цвет окна: ")

        visible_str = input("Окно видимо? (Да/Нет): ").strip().lower()
        self.__visible = visible_str == "да"

        framed_str = input("Окно с рамкой? (Да/Нет): ").strip().lower()
        self.__framed = framed_str == "да"

    def display(self) -> None:
        print("Модель окна:")
        print(f"  Заголовок: {self.__title}")
        print(f"  Позиция:   ({self.__x}, {self.__y})")
        print(f"  Размер:    {self.__width} x {self.__height}")
        print(f"  Цвет:      {self.__color}")
        print(f"  Видимо:    {self.visible}")
        print(f"  С рамкой:  {self.framed}")

    def move(self, dx: int, dy: int) -> None:
        self.__x += dx
        self.__y += dy

    def resize(self, new_width: int, new_height: int) -> None:
        if new_width > 0:
            self.__width = new_width
        if new_height > 0:
            self.__height = new_height

    def set_visible(self, state: bool) -> None:
        self.__visible = bool(state)

    def set_framed(self, state: bool) -> None:
        self.__framed = bool(state)

    def intersects(self, other: ModelWindow) -> bool:
        return not (
            self.__x + self.__width < other.__x or
            other.__x + other.__width < self.__x or
            self.__y + self.__height < other.__y or
            other.__y + other.__height < self.__y
        )
