names = []

try:
    while True:
        names.append(input("Name: "))
except EOFError:
    pass

print("")
print("Adieu, adieu, to ", end="")

number_of_names = len(names)

if number_of_names == 1:
    print(f"{names[0]}")
elif number_of_names == 2:
    print(f"{names[0]} and {names[1]}")
else:
    # for i in range(number_of_names):     # This is the same as the code below, but it is more complex and less efficient
    #     print(f"{names[i]}", end="")
    #     if i < number_of_names - 1 and number_of_names > 2:
    #         print(", ", end="")
    #     if i == number_of_names - 2 and number_of_names > 1:
    #         print("and ", end="")
    print(f"{', '.join(names[:-1])}, and {names[-1]}")