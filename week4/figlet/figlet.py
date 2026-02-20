import random
import pyfiglet
import sys


def main():
    if (
        len(sys.argv) == 3
        and sys.argv[1] in ["-f", "--font"]
        and sys.argv[2] in pyfiglet.FigletFont.getFonts()
    ):
        print(f"Output: {figlet(font=sys.argv[2])}")
    elif len(sys.argv) == 1:
        print(f"Output: {figlet()}")
    else:
        print("Invalid usage")
        sys.exit(1)


def figlet(font=random.choice(pyfiglet.FigletFont.getFonts())):
    input_text = input("Input: ")
    return pyfiglet.figlet_format(input_text, font=font)


main()
