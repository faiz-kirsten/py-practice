# This programs returns the largest number in a list of integers

list_int = [120, 21, 3, 42, 5, 6, 724, 81, 9, 20]    # List of integers


# The function below takes in a list of integers as an argument
def largest_number(list_input):
    # The base case is when the length is equal to 1
    if len(list_input) == 1:
        return list_input[0]
    else:
        # The max function checks which value is larger  and takes in 2 arguments - the first index position
        # in 'list_input' and the 'largest_number' function is called again, but the arguments contains
        # the list from index position 1.
        return max(list_input[0], largest_number(list_input[1:]))


print(largest_number(list_int))
