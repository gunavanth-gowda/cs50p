def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    num_flag = False
    if  len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s[2:].isalnum():
        return False
    for c in s:
        if c.isdigit():
            if c == '0' and not num_flag:
                return False
            num_flag = True
        elif num_flag:
            return False
    return True


main()
