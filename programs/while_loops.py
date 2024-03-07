# This program calculates and displays the average of the number entered by the user

end_loop = -1
num_list = []

# The user is requested to enter a number
# Once the user enters '-1' the average of the numbers entered before '-1' are calculated and displayed
# Used the append method to add items entered to the defined list
# https://towardsdatascience.com/append-in-python-41c37453400

num_list.append(int(input("Enter a number: ")))

while end_loop not in num_list:
    num_list.append(int(input("Enter a number: ")))

average = sum(num_list[0:-1]) / len(num_list[0:-1])

print(round(average))
