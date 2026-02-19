months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        date_input = input("Date: ").strip()
        try:
            month, day, year = date_input.split("/")
            if validate(int(month), int(day)):
                print(f"{year}-{int(month):02d}-{int(day):02d}")
                break
        except ValueError:
            pass
        try:
            month_date, year = date_input.split(",")
            month, day = month_date.split(" ")
            month = months.index(month) + 1
            if validate(month, int(day)):
                print(f"{int(year)}-{month:02d}-{int(day):02d}")
                break
        except ValueError:
            pass
        continue


def validate(month, day):
    return month in range(1, 13) and int(day) in range(1, 32)


if __name__ == '__main__':
    main()
