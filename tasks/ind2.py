from window_package import ModelWindow

def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"

if __name__ == '__main__':
    print(bold("Создание первого окна"))
    win1 = ModelWindow()
    win1.read()

    print("\n" + bold("Создание второго окна"))
    win2 = ModelWindow()
    win2.read()

    print("\n" + bold("Параметры первого окна"))
    win1.display()

    print("\n" + bold("Параметры второго окна"))
    win2.display()

    print("\n" + bold("Перемещение первого окна на (8, 2)"))
    win1.move(8, 2)
    win1.display()

    print("\n" + bold("Изменение размера первого окна на 200 x 200"))
    win1.resize(200, 200)
    win1.display()

    print("\n" + bold("Скрываем первое окно"))
    win1.set_visible(False)
    win1.display()

    print("\n" + bold("Убираем рамку у первого окна"))
    win1.set_framed(False)
    win1.display()

    print("\n" + bold("Проверка пересечения окон"))
    if win1.intersects(win2):
        print("Окна пересекаются.")
    else:
        print("Окна не пересекаются.")
