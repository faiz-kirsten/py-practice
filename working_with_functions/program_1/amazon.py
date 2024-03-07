# This program computes the answer to some operation on a list of numbers
# Import mean method from the statistics module
# Import ceil method from the math module

from statistics import mean
from math import ceil


# Function to get the maximum number in the list
def get_max_number(list_input):
    return max(list_input)


# Function to get the minimum number in the list
def get_min_number(list_input):
    return min(list_input)


# Function to get the average of the list using the 'mean' method from the statistics module
def get_avg_list(list_input):
    return round(mean(list_input), 2)


# Function to get the 'x' percentile of the list
# The percentile is determined by multiplying the length of the list by 'x' percent
def get_x_percentile(list_input, x):
    percentile = len(list_input) * x / 100
    return percentile


# Function to get the sum of the list
def get_sum_list(list_input):
    return sum(list_input)


# The function below stores the logic that obtains the list of integers from each line in 'input.txt'.
# It obtains the item at index value 1 in each iteration in 'list_operations'.
# '\n' is removed from each iteration and is split by ',' which is converts it into a list of strings
# The strings are converted to integers using list comprehension
def get_list_nums():
    list_num = [int(i) for i in list_operations[count][1].strip('\n').split(',')]
    return list_num


list_operations = []

# The with statement below reads from 'input.txt'.
# It iterates through each line in the file and splits it where there is a colon - ':'
# and appends it to 'list_operations'.
# 'encoding=utf-8-sig' removes the space at the beginning of the file.
with open('input.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        list_operations.append(line.split(":"))

# The with statement below creates and writes to 'equations.txt'
# 'count' is defined as 0 but is incremented by 1 for each iteration in 'list_operations'
# The if/elif statements checks what operation is at the index value 0 for each iteration
# and then calls the correlating function
with open('output.txt', 'w') as f:
    count = 0
    for i in list_operations:
        if list_operations[count][0] == 'max':
            f.write(f"The max of {get_list_nums()} is {get_max_number(get_list_nums())}\n")
        elif list_operations[count][0] == 'min':
            f.write(f"The min of {get_list_nums()} is {get_min_number(get_list_nums())}\n")
        elif list_operations[count][0] == 'avg':
            f.write(f"The avg of {get_list_nums()} is {get_avg_list(get_list_nums())}\n")
        elif list_operations[count][0] == 'sum':
            f.write(f"The sum of {get_list_nums()} is {get_sum_list(get_list_nums())}\n")
        elif 'p' in list_operations[count][0][:1] and list_operations[count][0][1:].isdigit():
            # The split function below splits the operation at the index value 0 at 'p' which
            # creates a list stored in int_percent.
            # 'int_percent' stores the index value 1 from the list created and converts it to an integer
            int_percent = int(list_operations[count][0].split('p', 1)[1])
            percentile_num = get_x_percentile(get_list_nums(), int_percent)
            f.write(f"The {int_percent}th percentile of {get_list_nums()} is {ceil(percentile_num)}\n")
        count += 1

# References
# https://www.freecodecamp.org/news/how-to-round-numbers-up-or-down-in-python/
# https://www.geeksforgeeks.org/python-get-the-string-after-occurrence-of-given-substring/
# https://stackoverflow.com/questions/17912307/u-ufeff-in-python-string
