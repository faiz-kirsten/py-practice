# Note for mentor: the get_unread_emails does return the list of unread emails and get_spam_emails does return a list of
# all spam emails. Could you please elaborate on what correction I need to make in regard to that? Thank you

# An SMS Simulation
class Email:
    # Constructor method with instance variables 'email_contents', 'from_address', 'has_been_read' and 'is_spam'.
    def __init__(self, email_contents, from_address, has_been_read=False, is_spam=False):
        self.email_contents = email_contents
        self.from_address = from_address
        self.has_been_read = has_been_read
        self.is_spam = is_spam

    # This method changes the 'has_been_read' parameter to True
    def mark_as_read(self):
        self.has_been_read = True

    # This method changes the 'is_spam' parameter to True
    def mark_as_spam(self):
        self.is_spam = True


def add_email(list_input, email_cont, email_add):
    # 'email_cont' and 'email_add' are placed in the parameter of the 'Email' class to append them as new objects to
    # 'list_input'.
    list_input.append(Email(email_cont, email_add))
    return list_input


# The function below returns the length of 'list_input'.
def get_count(list_input):
    return len(list_input)


# The function below returns the selected email.
def get_email(list_input, user_input):
    # The email the user selects is marked as read and the contents within the 'email_contents' parameter in
    # the 'Email' object is returned.
    list_input[user_input].mark_as_read()
    return list_input[user_input].email_contents


# The function below displays all the emails that are unread or there 'has_been_read' parameter is False.
# The for loop within the function iterates through 'list_input' and uses the enumerate function to give each iteration
# an index value.
# The if statement within the for loop checks whether the 'has_been_read' parameter in each iteration is False
# and prints out those specific iterations.
def get_unread_emails(list_input):
    count = 0
    for index, i in enumerate(list_input, 1):
        if list_input[count].has_been_read == False:
            print(f"Email no. : {index} Email content: {i.email_contents}, Email Address: {i.from_address}")
        count += 1


# The function below displays all the emails that are marked as spam or there 'is_spam' parameter is True.
# The for loop within the function iterates through 'list_input' and uses the enumerate function to give each iteration
# an index value.
# The if statement within the for loop checks whether the 'is_spam' parameter in each object(iteration) is True
# and appends each of these iterations to 'list_spam_emails'
def get_spam_emails(list_input):
    count = 0
    list_spam_emails = []
    for index, i in enumerate(list_input, 1):
        if list_input[count].is_spam == True:
            list_spam_emails.append(f"Email no. : {index} Email content: {i.email_contents},"
                                    f" Email Address: {i.from_address}")
        count += 1

    # The if statement checks whether 'list_spam_emails' is empty
    # If it is not empty then it returns the iterations stored in this list
    if len(list_spam_emails) != 0:
        for i in list_spam_emails:
            print(i)
    else:
        print("Spam folder is empty.")


# The function below allows the user to delete an email by using their index value.
def delete_email(list_input):
    # The for loop iterates through 'list_input' and uses the enumerate function to give each iteration
    # an index value and prints out each iteration.
    for index, i in enumerate(list_input, 1):
        print(f"Email no. : {index} Email content: {i.email_contents}, Email Address: {i.from_address}")
    if len(list_input) != 0:
        # The user is prompted to enter the index of the email the user would like to delete.
        email_to_remove = int(input('Enter the index of the email you want to delete: ')) - 1
        # The while loop below ensures that the user enters a valid index number within the range of 'list_input'.
        while email_to_remove not in range(len(list_input)):
            email_to_remove = int(input('Invalid index number! Enter the index of the email you want to delete: ')) - 1
        # We make use of the pop function to remove the email selected by the user.
        list_input.pop(email_to_remove)
        print("Email has been deleted.")
    else:
        print('Inbox is empty. ')


# 'inbox' stores the various objects as objects from the 'Email' class.
inbox = [Email('i love dogs', 'faizkirsten@gmail.com'), Email('i play with dogs', 'faizkirsten1@gmail.com'),
         Email('i like dogs', 'faizkirsten2@gmail.com'), Email('i feed my dogs', 'faizkirsten3@gmail.com')]

# The while loop below ensures that the program does not end after an option is selected.
while True:
    # The try and except block below ensures that if the user input is invalid - not an integer, then the user
    # will be prompted to select the correct input or brought back to the main options.
    try:
        # 'menu_options' contains the different options the user can select.
        menu_options = int(input("Select one of the options below:\n1. Read\n2. Mark Spam\n3. Send\n"
                                 "4. Get Email Count\n5. Get Email By Index\n6. Get Spam Emails\n7. Delete Email\n"
                                 "8. Quit\n"))
        # The if/elif/else statement below ensures that the user inputs a valid option.
        if menu_options == 1:
            # The 'get_unread_emails' function is executed with inbox in place of the parameter.
            get_unread_emails(inbox)
            # The user is prompted to enter the index of the email the user would like to read.
            user_idx = int(input("Enter the index of email you would like to read: "))
            # The while loop below ensures that the user enters a valid index number within the range of 'inbox'.
            while user_idx not in range(len(inbox) + 1):
                user_idx = int(input("Invalid index number! Enter the index of email you "
                                     "would like to read: "))

            # The value in the 'has_been_read' parameter in the object(iteration) stored in 'inbox' is changed to True.
            inbox[user_idx - 1].mark_as_read()
            print("Email marked as read.")
        elif menu_options == 2:
            # The for loop iterates through 'inbox' and uses the enumerate function to
            # give each iteration an index value.
            # The if statement within the for loop checks whether the 'is_spam' parameter in each iteration is False
            # and prints out those specific iterations.
            count = 0
            for index, i in enumerate(inbox, 1):
                if inbox[count].is_spam == False:
                    print(f"Email no. : {index} Email content: {i.email_contents}"
                          f" Email Address: {i.from_address}")
                count += 1
            # The user is prompted to enter the index of the email the user would like to mark as spam.
            user_idx = int(input("Enter the index of email you would like to mark as spam: "))
            # The while loop below ensures that the user enters a valid index number within the range of 'inbox'.
            while user_idx not in range(len(inbox) + 1):
                user_idx = int(input("Index out of range !Enter the index of email you "
                                     "would like to mark as spam: "))
            # The value in the 'is_spam' parameter in the object(iteration) stored in 'inbox' is changed to True.
            inbox[user_idx - 1].mark_as_spam()
            print("Email marked as spam.")
        elif menu_options == 3:
            # The user is prompted to enter the contents of the email and the email address of the email.
            email_content = input("Enter the contents of the email: ")
            email_address = input("Enter the email address: ")
            # The 'add_email' function is executed with 'inbox', 'email_content' and 'email_address'
            # in place of the parameter.
            add_email(inbox, email_content, email_address)
            print("Email has been sent.")
        elif menu_options == 4:
            # The 'get_count' function is executed with inbox in place of the parameter.
            print(get_count(inbox))
        elif menu_options == 5:
            # The 'get_unread_emails' function is executed with inbox in place of the parameter.
            get_unread_emails(inbox)
            # The user is prompted to enter the index of the email the user would like to read.
            user_idx = int(input('Enter the index value of the email you want to read: ')) - 1
            # The while loop below ensures that the user enters a valid index number within the range of 'inbox'.
            while user_idx not in range(len(inbox)):
                user_idx = int(input('Index out of range! Enter the index value of the email you '
                                     'want to read: ')) - 1
            # The 'get_email' function is executed with 'inbox' and 'user_idx' in place of the parameters.
            print(get_email(inbox, user_idx))
        elif menu_options == 6:
            # The 'get_spam_emails' function is executed with inbox in place of the parameter.
            get_spam_emails(inbox)
        elif menu_options == 7:
            # The 'delete_email' function is executed with inbox in place of the parameter.
            delete_email(inbox)
        elif menu_options == 8:
            print("Exiting application")
            exit()
        else:
            print("Invalid Option!")

    except ValueError:
        print('Invalid Input!')