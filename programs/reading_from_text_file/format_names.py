# This program reads the data from 'DOB.txt'
# and prints it out in two sections - 'Name' and 'Birtdate'.

print("Name:")

# The with statement below reads from the text document 'DOB.txt'.
# The for loop loops over each line of the file
# and splits each line into a list of strings in 'list_convert'.
# It prints out the first letter of each line
# and prints out the string with the index value of 1.

with open('DOB.txt', 'r') as f:
    for line in f:
        list_convert = line.split(" ")
        print(f"{line[0]} {list_convert[1]}")

print("\nBirthdate:")

# The with statement below reads from the text document 'DOB.txt'.
# The for loop loops over each line of the file
# and splits each line into a list of string in 'list_convert'.
# It only prints out the strings with the index value between 2 and 5

with open('DOB.txt', 'r') as f:
    for line in f:
        list_convert = ' '.join(line.split(" ")[2:5])
        print(list_convert.strip("\n"))

# There is a duplicate at the just in case the FileNotFound Error appears - the file path is different

# print("Name:")

# with open('DOB.txt', 'r') as f:
#     for line in f:
#         list_convert = line.split(" ")
#         print(f"{line[0]} {list_convert[1]}")

# print("\nBirthdate:")

# with open('DOB.txt', 'r') as f:
#     for line in f:
#         list_convert = ' '.join(line.split(" ")[2:5])
#         print(list_convert.strip("\n"))
