# Say hello


def main():
    name = input("What's your name? ")
    print(f"hello, {name}")
    number = int(input("enter a number: "))
    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


def is_even(n):
    return n % 2 == 0


if __name__ == "__main__":
    main()
