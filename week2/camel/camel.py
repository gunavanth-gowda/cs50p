def main():
    camel_case = input("camelCase: ").strip()
    print("snake_case: ", end="")
    print_snake_case(camel_case)


def print_snake_case(s):
    for letter in s:
        if letter.isupper():
            print("_", end="")
            print(letter.lower(), end="")
        else:
            print(letter, end="")


main()
