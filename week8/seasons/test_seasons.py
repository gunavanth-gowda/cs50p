from datetime import date

import pytest

from seasons import age_in_minutes, minutes_in_words, parse_date


@pytest.mark.parametrize("value, expected", [
    ("1999-01-01", date(1999, 1, 1)),
    ("2000-02-29", date(2000, 2, 29)),
    ("2024-12-31", date(2024, 12, 31)),
    ("0001-01-01", date(1, 1, 1)),
])
def test_parse_date(value, expected):
    assert parse_date(value) == expected


@pytest.mark.parametrize("value", [
    "", "January 1, 2000", "01-01-2000", "2000/01/01",
    "2000-1-01", "2000-01-1", "20000101", "2000-W01-1",
    " 2000-01-01", "2000-01-01 ", "2000-01-01\n",
    "2000-01-01T00:00:00", "２０００-０１-０１",
    "0000-01-01", "2000-00-01", "2000-13-01",
    "2000-01-00", "2000-04-31", "1900-02-29", "2023-02-29",
])
def test_parse_date_invalid(value):
    with pytest.raises(ValueError):
        parse_date(value)


@pytest.mark.parametrize("birthdate, today, expected", [
    (date(2023, 1, 1), date(2024, 1, 1), 525600),
    (date(2024, 1, 1), date(2025, 1, 1), 527040),
    (date(2021, 1, 1), date(2023, 1, 1), 1051200),
    (date(2023, 1, 1), date(2025, 1, 1), 1052640),
    (date(2000, 2, 28), date(2000, 3, 1), 2880),
    (date(1900, 2, 28), date(1900, 3, 1), 1440),
    (date(2024, 2, 29), date(2025, 2, 28), 525600),
    (date(2024, 12, 31), date(2025, 1, 1), 1440),
    (date(2025, 1, 1), date(2025, 1, 1), 0),
])
def test_age_in_minutes(birthdate, today, expected):
    assert age_in_minutes(birthdate, today) == expected


def test_age_in_minutes_future_birthdate():
    with pytest.raises(ValueError):
        age_in_minutes(date(2025, 1, 2), date(2025, 1, 1))


@pytest.mark.parametrize("minutes, expected", [
    (0, "Zero minutes"),
    (1440, "One thousand, four hundred forty minutes"),
    (525600, "Five hundred twenty-five thousand, six hundred minutes"),
    (527040, "Five hundred twenty-seven thousand forty minutes"),
    (1051200, "One million, fifty-one thousand, two hundred minutes"),
    (1052640, "One million, fifty-two thousand, six hundred forty minutes"),
])
def test_minutes_in_words(minutes, expected):
    assert minutes_in_words(minutes) == expected
