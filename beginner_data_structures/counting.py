# This program counts the number of times a character occurs in a string.

string = 'google.com'
lower_string = string.lower()
count = 0
dict_letters = {}

# The for loop below iterates through each character in 'lower_string'
# and counts the amount of characters each character occurs in 'lower_string'.
# 'count' is defined as 0 and incremented by one in order to iterate through
# 'lower_string'.
# Then it adds each character as a key to 'dict_letters'
# and the amount it occurs as a value to each of those keys.
# Duplicate letters aren't created as keys because python does not allow duplicate keys

for i in lower_string:
    dict_letters[i] = lower_string.count(lower_string[count])
    count += 1

print(dict_letters)
