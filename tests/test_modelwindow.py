import pytest
from tasks.window_package import ModelWindow

def test_initialization_defaults():
    win = ModelWindow()
    assert win.title == "Окно"
    assert win.x == 0
    assert win.y == 0
    assert win.width == 1920
    assert win.height == 1200
    assert win.color == "серый"
    assert win.visible == "Да"
    assert win.framed == "Да"

def test_move_and_resize():
    win = ModelWindow(x=10, y=20, width=100, height=200)
    win.move(5, -10)
    assert win.x == 15
    assert win.y == 10

    win.resize(300, 400)
    assert win.width == 300
    assert win.height == 400

    # resize с нулём не меняет размер
    win.resize(0, 0)
    assert win.width == 300
    assert win.height == 400

def test_set_visible_and_framed():
    win = ModelWindow()
    win.set_visible(False)
    win.set_framed(False)
    assert win.visible == "Нет"
    assert win.framed == "Нет"

    win.set_visible(True)
    win.set_framed(True)
    assert win.visible == "Да"
    assert win.framed == "Да"

def test_intersects():
    win1 = ModelWindow(x=0, y=0, width=100, height=100)
    win2 = ModelWindow(x=50, y=50, width=100, height=100)
    win3 = ModelWindow(x=200, y=200, width=50, height=50)

    assert win1.intersects(win2) is True
    assert win1.intersects(win3) is False
    assert win2.intersects(win3) is False

# Тест метода read() через мок ввода
def test_read(monkeypatch):
    win = ModelWindow()
    inputs = iter([
        "Новое окно", "10", "20", "300", "400", "красный", "Да", "Нет"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    win.read()
    assert win.title == "Новое окно"
    assert win.x == 10
    assert win.y == 20
    assert win.width == 300
    assert win.height == 400
    assert win.color == "красный"
    assert win.visible == "Да"
    assert win.framed == "Нет"
