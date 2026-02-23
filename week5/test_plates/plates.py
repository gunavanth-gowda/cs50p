def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6 and s.isalnum()):
        return False

    if not s[:2].isalpha():
        return False

    if s.isalpha():
        return True

    first_digit_index = -1
    for i in range(len(s)):
        if s[i].isdigit():
            first_digit_index = i
            break

    if first_digit_index == -1:
        return False

    if s[first_digit_index] == "0":
        return False

    num_count = 0
    for i in range(first_digit_index, len(s)):
        if not s[i].isdigit():
            return False
        num_count += 1

    if num_count < 2:
        return False

    return True


if __name__ == "__main__":
    main()
