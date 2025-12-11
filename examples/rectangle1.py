class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height

    def get_width(self) -> int:
        return self.__width

    def set_width(self, w) -> None:
        self.__width = w

    def get_height(self) -> int:
        return self.__height

    def set_height(self, h) -> None:
        self.__height = h

    def area(self) -> int:
        return self.__width * self.__height


def main() -> None:
    rect = Rectangle(10, 5)
    print(f"Width: {rect.get_width()}")
    print(f"Height: {rect.get_height()}")
    print(f"Width: {rect._Rectangle__width}")
    print(f"Height: {rect._Rectangle__height}")
    print(f"Area: {rect.area()}")


if __name__ == "__main__":
    main()
