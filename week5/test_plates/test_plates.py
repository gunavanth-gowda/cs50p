from plates import is_valid


def test_is_valid_only_alphabet():
    assert is_valid("CS") == True


def test_is_valid_numbers():
    assert is_valid("123") == False


def test_is_valid_alphanumeric():
    assert is_valid("CS50") == True


def test_is_valid_starting_with_zero():
    assert is_valid("CS05") == False


def test_is_valid_too_long():
    assert is_valid("CS12345") == False


def test_is_valid_too_short():
    assert is_valid("C") == False


def test_is_valid_non_alphanumeric():
    assert is_valid("CS-50") == False


def test_is_valid_digits_before_letters():
    assert is_valid("CS5P0") == False
