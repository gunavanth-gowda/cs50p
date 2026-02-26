import csv
import os
import sys


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print(f"{sys.argv[1]} is not a csv file")
        sys.exit(1)
    elif not sys.argv[2].endswith(".csv"):
        print(f"{sys.argv[2]} is not a csv file")
    elif not os.path.isfile(sys.argv[1]):
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)
    else:
        transform(sys.argv[1], sys.argv[2])


def transform(before_csv, after_csv):
    with open(before_csv) as csvfile_before, open(after_csv, "w") as csvfile_after:
        reader = csv.reader(csvfile_before)
        writer = csv.DictWriter(csvfile_after, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for name, house in list(reader):
            names = name.split(",")
            if len(names) == 2:
                writer.writerow(
                    {"first": names[1].strip(), "last": names[0], "house": house}
                )


if __name__ == "__main__":
    main()
