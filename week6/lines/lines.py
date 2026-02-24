import os
import sys


def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".py"):
        print("Not a python file")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    else:
        print(count_lines(sys.argv[1]))


def count_lines(filename):
    number_of_lines = 0
    with open(filename) as file:
        for line in file:
            if not line.strip().startswith("#") and line.strip() != "":
                number_of_lines += 1
    return number_of_lines


if __name__ == "__main__":
    main()
