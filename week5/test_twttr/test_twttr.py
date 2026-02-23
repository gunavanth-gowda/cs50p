from twttr import shorten


def test_shorten1():
    assert shorten("hello") == "hll"


def test_shorten2():
    assert shorten("hello world") == "hll wrld"


def test_shorten3():
    assert shorten("h0ll0 w0rld") == "h0ll0 w0rld"


def test_shorten4():
    assert shorten("AEIOU") == ""


def test_shorten5():
    assert shorten("aeiou") == ""


def test_shorten6():
    assert shorten("AEIO,Uaeiou") == ","
