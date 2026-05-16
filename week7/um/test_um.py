from um import count


def test_single_um():
    assert count("um") == 1
    assert count("um?") == 1


def test_case_insensitive():
    assert count("Um, thanks for the album.") == 1
    assert count("UM, thanks, um...") == 2


def test_multiple_matches():
    assert count("Um, thanks, um...") == 2
    assert count("um, um, um") == 3


def test_not_substrings():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("circumference, instrument, umbrella") == 0


def test_word_boundaries_without_spaces():
    assert count("hello,um,world") == 1
    assert count("um...um?") == 2
