class ModelWindow:
    """
    Класс для моделирования экранного окна.
    """

    def __init__(self, title="", x=0, y=0, width=100, height=100,
                 color="white", visible=True, framed=True):
        self.title = title
        self.x = x                  # координата левого верхнего угла (по горизонтали)
        self.y = y                  # координата левого верхнего угла (по вертикали)
        self.width = width
        self.height = height
        self.color = color
        self.visible = visible
        self.framed = framed

    # -------- ВВОД ДАННЫХ С КЛАВИАТУРЫ --------
    def read(self):
        print("Введите параметры окна:")
        self.title = input("Заголовок окна: ")
        self.x = int(input("Координата X: "))
        self.y = int(input("Координата Y: "))
        self.width = int(input("Ширина: "))
        self.height = int(input("Высота: "))
        self.color = input("Цвет: ")
        self.visible = input("Видимое? (y/n): ").lower() == "y"
        self.framed = input("С рамкой? (y/n): ").lower() == "y"

    # -------- ВЫВОД НА ЭКРАН --------
    def display(self):
        print("\n----- Параметры окна -----")
        print(f"Заголовок: {self.title}")
        print(f"Позиция: ({self.x}, {self.y})")
        print(f"Размер: {self.width} x {self.height}")
        print(f"Цвет: {self.color}")
        print(f"Видимость: {'видимо' if self.visible else 'невидимо'}")
        print(f"Рамка: {'с рамкой' if self.framed else 'без рамки'}")
        print("---------------------------\n")

    # ----------- ОПЕРАЦИИ МОДЕЛИРОВАНИЯ ОКНА ------------

    def move(self, dx=0, dy=0):
        """Перемещение окна на dx/dy"""
        self.x += dx
        self.y += dy

    def resize(self, dwidth=0, dheight=0):
        """Изменение размеров окна"""
        self.width = max(1, self.width + dwidth)
        self.height = max(1, self.height + dheight)

    def change_color(self, new_color):
        """Изменение цвета окна"""
        self.color = new_color

    def toggle_visible(self):
        """Переключить состояние видимости"""
        self.visible = not self.visible

    def toggle_frame(self):
        """Переключить рамку"""
        self.framed = not self.framed

    def intersects_boundary(self, screen_width, screen_height):
        """
        Проверка выхода окна за границы экрана.
        Возвращает True, если окно пересекает границы.
        """
        if self.x < 0 or self.y < 0:
            return True
        if self.x + self.width > screen_width:
            return True
        if self.y + self.height > screen_height:
            return True
        return False


# ------------------ ДЕМОНСТРАЦИЯ ---------------------

if __name__ == "__main__":
    # Создаём окно (можно по умолчанию или через read)
    window = ModelWindow()
    window.read()

    print("\nИзначальное состояние:")
    window.display()

    # Пробуем перемещение
    print("Перемещаем окно на (50, 30)...")
    window.move(50, 30)
    window.display()

    # Пробуем изменение размера
    print("Увеличиваем размеры окна на (100, 50)...")
    window.resize(100, 50)
    window.display()

    # Пробуем смену цвета
    print("Меняем цвет окна на 'blue'...")
    window.change_color("blue")
    window.display()

    # Переключаем видимость
    print("Переключаем видимость...")
    window.toggle_visible()
    window.display()

    # Проверяем пересечение границ
    SCREEN_W, SCREEN_H = 800, 600
    if window.intersects_boundary(SCREEN_W, SCREEN_H):
        print("⚠ Окно выходит за границы экрана!")
    else:
        print("Окно полностью внутри экрана.")
