import random


def main():
    random_number = random.randint(1, get_level())
    verify_guesses(random_number)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass


def verify_guesses(random_number):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
        except ValueError:
            continue
        if guess == random_number:
            print("Just right!")
            return
        elif guess < random_number:
            print("Too small!")
        else:
            print("Too large!")


if __name__ == "__main__":
    main()
