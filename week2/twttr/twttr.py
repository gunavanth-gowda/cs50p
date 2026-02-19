vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

word = input("Input: ")

for character in word:
    if character in vowels:
        print("", end="")
    else:
        print(character, end="")
