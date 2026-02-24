def main():
    while True:
        fraction = input("Fraction: ")
        try:
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
    except (ValueError, AttributeError):
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    if x < 0 or y < 0 or x > y:
        raise ValueError

    return int(round((x / y), 2) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
