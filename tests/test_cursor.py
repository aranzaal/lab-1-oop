import pytest
from tasks.cursor import Cursor

def test_initialization_default():
    cursor = Cursor()
    assert cursor.first == 0
    assert cursor.second == 0

def test_initialization_custom():
    cursor = Cursor(100, 200, width=500, height=500)
    assert cursor.first == 100
    assert cursor.second == 200

def test_initialization_out_of_bounds():
    with pytest.raises(ValueError):
        Cursor(1000, 2000, width=500, height=500)

def test_changex_within_bounds():
    cursor = Cursor(10, 10, width=20, height=20)
    cursor.changex(5)
    assert cursor.first == 15

def test_changex_out_of_bounds():
    cursor = Cursor(10, 10, width=20, height=20)
    with pytest.raises(ValueError):
        cursor.changex(15)

def test_changey_within_bounds():
    cursor = Cursor(10, 10, width=20, height=20)
    cursor.changey(5)
    assert cursor.second == 15

def test_changey_out_of_bounds():
    cursor = Cursor(10, 10, width=20, height=20)
    with pytest.raises(ValueError):
        cursor.changey(15)

# Тест свойства read() через мок ввода
def test_read(monkeypatch):
    cursor = Cursor(0, 0, width=100, height=100)
    inputs = iter(["50", "60"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    cursor.read()
    assert cursor.first == 50
    assert cursor.second == 60

def test_read_out_of_bounds(monkeypatch):
    cursor = Cursor(0, 0, width=100, height=100)
    inputs = iter(["150", "60"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(ValueError):
        cursor.read()
