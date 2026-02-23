def main():
    print(shorten(input("Input: ")))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    shortened = ""
    for character in word:
        if character not in vowels:
            shortened += character
    return shortened


if __name__ == "__main__":
    main()
