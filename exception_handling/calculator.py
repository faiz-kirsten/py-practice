menu_options = 0

# The while loop below ensures that the loop will continue executing until the user selects option 3.
while menu_options != 3:
    # We use exception handling('ValueError') to ensure that the users input is an integer and not a string
    try:
        menu_options = int(input("Select one of the options below:\n1. Calculator\n"
                                 "2. Read all equations from text file\n3. Exit\n"))
        # The while loop below ensures that the user selects a valid option.
        # Once the user enters the correct option we break out of the loop.
        while menu_options not in range(1, 4):
            menu_options = int(input("Invalid Option!\nSelect one of the options below:\n1. Calculator\n"
                                     "2. Read all equations from text file\n3. Exit\n"))
            break
    except ValueError:
        print("Invalid Input!")
        continue

    operation = 0

    # The if statements will execute based on what option the user selected.
    if menu_options == 1:
        # The while loop below ensures that the loop will execute if the user selects an invalid option.
        while operation not in range(1, 5):
            # We use exception handling('ValueError') to ensure that the users input is an integer and not a string.
            try:
                operation = int(input("Select one of the options below:\n1. Subtract\n2. Add\n"
                                      "3. Multiply\n4. Divide\n"))
                # The while loop below ensures that the user selects a valid option.
                # Once the user enters the correct option we break out of the loop.
                while operation not in range(1, 5):
                    menu_options = int(input("Invalid Option!\nSelect one of the options below:\n1. Subtract\n2. Add\n"
                                             "3. Multiply\n4. Divide\n"))
                    break
            except ValueError:
                print("Invalid Input!")
                continue

        # The while loop below will continue to execute until the user enters the inputs within the loop
        while True:
            # We use exception handling('ValueError') to ensure that the users input is an integer and not a string.
            try:
                num1 = float(input("Enter number 1: "))
                num2 = float(input("Enter number 2: "))

                # The while loop is used to ensure that the user is not allowed to divide by zero.
                while num2 == 0 and operation == 4:
                    print("Division by zero!")
                    num1 = float(input("Enter number 1: "))
                    num2 = float(input("Enter number 2: "))
                break
            except ValueError:
                print("Invalid Input. Input must be an integer or float. ")

        # The with statement below  creates and appends to 'equations.txt'
        with open('equations.txt', 'a') as f:
            # Based on the operation selected by the user, the entire equation is appended to 'equations.txt'
            if operation == 1:
                f.write(f" {num1} - {num2} = {round(num1 - num2, 2)}, ")
                print(round(num1 - num2, 2))
            elif operation == 2:
                f.write(f" {num1} + {num2} = {round(num1 + num2, 2)}, ")
                print(round(num1 + num2, 2))
            elif operation == 3:
                f.write(f" {num1} * {num2} = {round(num1 * num2, 2)}, ")
                print(round(num1 * num2, 2))
            else:
                f.write(f" {num1} / {num2} = {round(num1 / num2, 2)}, ")
                print(round(num1 / num2, 2))
    elif menu_options == 2:
        file = None
        while True:
            # The exception block below ensures that the user inputs a valid file name.
            try:
                file_name = input("Enter the files name - eg. 'input.txt': ")
                file = open(file_name, 'r')
            except FileNotFoundError as error:
                print("The file that you are trying to open does not exist.")
                print(error)
            # The finally block is used to close the file and to read from 'file' and display its contents.
            finally:
                if file is not None:
                    # The for loop below iterates through the line in 'file' and splits it at ', ' which creates a
                    # list - 'list_equations'
                    for line in file:
                        list_equations = line.split(', ')
                    # The for loop below iterates through 'list_equations' and prints each iteration
                    for i in list_equations:
                        print(i)
                    file.close()
                    break

print("Exiting Application...")
exit()
