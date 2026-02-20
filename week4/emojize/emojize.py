import emoji

input_text = input("Input: ")

print(f'Output: {emoji.emojize(input_text, language="alias")}')
