import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    match = re.search(
        r'<iframe\b[^>]*\bsrc="https?://(?:www\.)?youtube\.com/embed/([^"]+)"',
        s,
    )
    if match:
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()
