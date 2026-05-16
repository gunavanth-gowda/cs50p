import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)
    if not match:
        raise ValueError

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = (
        match.groups()
    )
    start = _convert_time(start_hour, start_minute, start_period)
    end = _convert_time(end_hour, end_minute, end_period)
    return f"{start} to {end}"


def _convert_time(hour, minute, period):
    hour = int(hour)
    minute = int(minute or 0)

    if hour < 1 or hour > 12 or minute > 59:
        raise ValueError

    if period == "AM":
        hour %= 12
    else:
        hour = hour % 12 + 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
