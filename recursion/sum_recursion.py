# This program adds the sum of all the numbers in the list up until and including the given index point.
list_int = [1, 21, 3, 4, 5, 6, 7, 8, 9, 10]


# The function below takes in two arguments - a list and an integer which is the index position.
def adding_up_to(list_input, index_pos):
    # 'list_idx' is created to store the values in the list until the index position specified by the user.
    list_idx = list_input[:index_pos + 1]
    # If the index position is 0 the first item in 'list_idx' is returned.
    if index_pos == 0:
        return list_input[index_pos]
    else:
        # The current index position is added to the function 'adding_up_to' which we call again.
        # The argument containing the index position is subtracted by one and 'list_idx' is in place of 'list_int'
        return list_idx[index_pos] + adding_up_to(list_idx, index_pos - 1)


print(adding_up_to(list_int, 2))
