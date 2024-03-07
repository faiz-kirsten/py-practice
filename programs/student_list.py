# This program displays the total number of names the user has entered

end_loop = "Stop"
list_pupils = []

# The user is requested to enter the names of their pupils
# Once the user enters 'Stop' the total number of names entered will be displayed
# Used the append method to add items entered to the defined list
# https://towardsdatascience.com/append-in-python-41c37453400

list_pupils.append(input("Enter the name of the pupil: "))

while end_loop not in list_pupils:
    list_pupils.append(input("Enter the name of the pupil: "))

print(len(list_pupils[0:-1]))
