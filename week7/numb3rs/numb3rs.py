import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    regex = r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
    pattern = rf"^(?:{regex}\.){{3}}{regex}$"
    if not re.match(pattern, ip):
        return "False"
    else:
        return "True"


if __name__ == "__main__":
    main()
