def main():
    testdata = input("Enter a input: ")
    print(convert(testdata))

def convert(string):
    return string.replace(":)", "🙂").replace(":(", "🙁")

main()
