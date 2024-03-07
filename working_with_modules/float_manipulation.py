# The statistics module is imported
import statistics

list_numbers = []

# The for loop below asks the user to input 10 numbers, an integer or float
# It appends(adds) these numbers to 'list_numbers'
for i in range(1, 11):
    num = float(input("Enter a number (float or integer): "))
    list_numbers.append(num)

# The sum function is used to determine the sum of 'list_numbers'
list_numbers_sum = sum(list_numbers)

# The min function is used to find the maximum number in 'list_numbers'
# The max function is used to find the minimum number in 'list_numbers'

list_numbers_max = max(list_numbers)
list_numbers_min = min(list_numbers)

# The index function is used to find the index positions of the max and min numbers in 'list_numbers'
index_max = list_numbers.index(list_numbers_max)
index_min = list_numbers.index(list_numbers_min)

# The mean function in the statistics module is used to find the average of 'list_numbers'
# The median function in the statistics module is used to find the median of 'list_numbers'
list_numbers_average = statistics.mean(list_numbers)
list_numbers_median = statistics.median(list_numbers)

print(f'''List: {list_numbers}
Sum of list : {list_numbers_sum}
Index of maximum value: {index_max}
Index of minimum value: {index_min}
Average of list: {round(list_numbers_average, 2)}
Median of list: {list_numbers_median}''')

# References
# https://www.geeksforgeeks.org/find-median-of-list-in-python/
# https://www.geeksforgeeks.org/find-average-list-python/
