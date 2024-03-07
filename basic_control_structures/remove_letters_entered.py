# This programs strips a set of characters from a string
# The user is requested to input a sentence
# The user is asked how many characters they would like to remove

string = input("Enter a sentence: ")
char_list = []
char_remove = int(input("How many characters would you like to remove: "))

# The user is asked which characters they would like to remove from 'string'
# These characters are added to 'char_list'
# The translate function is used to replace each instance of the entered characters in 'string'
# Reference: https://www.journaldev.com/23674/python-remove-character-from-string

for i in range(0, char_remove):
    char_list.append(input("Enter the character you would like to remove: "))
str_replace = string.translate({ord(i): '' for i in char_list})

print(f"After stripping {','.join(char_list)}:\n{str_replace}")
