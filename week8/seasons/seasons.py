from datetime import date
import re
import sys

import inflect


def main():
    try:
        birthdate = parse_date(input("Date of Birth: "))
        minutes = age_in_minutes(birthdate, date.today())
    except (ValueError, EOFError):
        sys.exit("Invalid date")
    print(minutes_in_words(minutes))


def parse_date(value):
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        raise ValueError("Expected YYYY-MM-DD")
    return date.fromisoformat(value)


def age_in_minutes(birthdate, today):
    if birthdate > today:
        raise ValueError("Birthdate cannot be in the future")
    return (today - birthdate).days * 24 * 60


def minutes_in_words(minutes):
    words = str(inflect.engine().number_to_words(minutes, andword=""))
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
