# This programs prints out a list of all the incorrect names entered by the user

# The user is requested to enter their name
# The names the user enters are added to 'list_names'
list_names = []
list_names.append(input("Enter your name: "))

# The user is requested to enter their name until 'John' is entered
# When 'John' is entered the program stops
# All the names entered previously are displayed in a list excluding 'John'
while "John" not in list_names:
    list_names.append(input("Enter your name: "))
else:
    print(f"Incorrect names: {list_names[:-1]}")
