# This program determines whether a string is a palindrome

string = input("Enter a word: ")

# This if statement checks whether 'string' is the same when it is reversed

if string == string[::-1]:
    print("Your word is a palindrome")
else:
    print("Your word is not a palindrome")
