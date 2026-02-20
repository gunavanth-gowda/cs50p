import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        random_integer_1 = generate_integer(level)
        random_integer_2 = generate_integer(level)
        correct_answer = random_integer_1 + random_integer_2

        for attempt in range(3):
            try:
                guess = int(input(f"{random_integer_1} + {random_integer_2} = "))
                if guess == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

            if attempt == 2:
                print(f"{random_integer_1} + {random_integer_2} = {correct_answer}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)
        case _:
            raise ValueError


if __name__ == "__main__":
    main()
