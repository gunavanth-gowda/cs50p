from bank import value


def test_value_hello():
    assert value("hello") == 0
    assert value("Hello, how are you?") == 0
    assert value("HELLO") == 0


def test_value_h():
    assert value("hi") == 20
    assert value("Hey there!") == 20
    assert value("h") == 20


def test_value_other():
    assert value("good morning") == 100
    assert value("welcome") == 100
    assert value("greeting") == 100


def test_value_whitespace():
    assert value("   hello   ") == 0
    assert value("   hi   ") == 20
    assert value("   good morning   ") == 100


def test_value_negative():
    assert value("") == 100
    assert value(" ") == 100
    assert value("123") == 100
