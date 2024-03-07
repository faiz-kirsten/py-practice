# Amount of characters excluding spaces in 'input.txt'
with open('input.txt', 'r') as f:
    amount_char = len(f.read().replace(" ", ""))
    print(amount_char)

# Amount of characters including spaces in 'input.txt'
with open('input.txt', 'r') as f:
    amount_char = len(f.read())
    print(amount_char)

# Amount of lines in 'input.txt'
with open('input.txt', 'r') as f:
    amount_lines = len(f.read().split("\n"))
    print(amount_lines)

# Amount of words in 'input.txt'
with open('input.txt', 'r') as f:
    amount_words = len(f.read().replace("\n", " ").split(" "))
    print(amount_words)


vowels = ['e', 'E', 'a', 'A', 'i', 'I', 'o', 'O', 'u', 'U']
# The total number of vowels (a, e, i, o and u) in the 'input.txt'.
