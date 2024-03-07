# This programs reads from 'numbers1.txt' and 'numbers2.txt'
# and writes to 'all_numbers.txt'.
# Files 'numbers1.txt' and 'numbers2.txt' contain integers which are sorted
# from smallest to largest.

# The first and second with statement extract the first line from 'numbers1.txt'
# and 'numbers2.txt' which form a new string 'all_numbers'.

all_numbers = ""

with open('numbers1.txt', 'r') as f:
    for line in f:
        all_numbers += line
with open('numbers2.txt', 'r') as f:
    for line in f:
        all_numbers += line

# The with statement below creates and writes to 'all_numbers.txt'.
# 'all_numbers_format' replaces and strips '[]' from 'all_numbers'
# and converts 'all_numbers' into a list.
# The for loop converts each list item into an integer and appends them to 'all_numbers_2'.
# 'all_numbers_2' is sorted from smallest to largest and
# converted into a string which is written to 'all_numbers.txt'.

all_numbers_2 = []

with open('all_numbers.txt', 'w') as f:
    all_numbers_format = all_numbers.replace("][", ",").strip("[]").split(',')
    for i in all_numbers_format:
        num = int(i)
        all_numbers_2.append(num)
    sorted_numbers = sorted(all_numbers_2, reverse=False)
    f.write(str(sorted_numbers))
