import csv
import os
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a csv file")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    else:
        transform(sys.argv[1])


def transform(filename):
    with open(filename) as file:
        table = list(csv.reader(file))
        print(tabulate(table, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
