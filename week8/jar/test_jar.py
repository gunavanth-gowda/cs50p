import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0


@pytest.mark.parametrize("capacity", [-1, 1.5, "12", None, [], {}])
def test_init_invalid_capacity(capacity):
    with pytest.raises(ValueError):
        Jar(capacity)


def test_zero_capacity():
    jar = Jar(0)
    assert jar.capacity == 0
    assert jar.size == 0
    jar.deposit(0)
    jar.withdraw(0)
    with pytest.raises(ValueError):
        jar.deposit(1)
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪" * 12
    jar.withdraw(10)
    assert str(jar) == "🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(0)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5
    assert jar.capacity == 5


def test_deposit_over_capacity():
    jar = Jar(5)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.deposit(3)
    assert jar.size == 3


def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    jar.withdraw(0)
    assert jar.size == 3
    jar.withdraw(3)
    assert jar.size == 0
    assert jar.capacity == 5


def test_withdraw_too_many():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)
    assert jar.size == 0

    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw(4)
    assert jar.size == 3
