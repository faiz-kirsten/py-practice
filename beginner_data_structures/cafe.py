# This program calculates the total stock worth in the cafe
# 'menu' contains the items in the cafe
# 'stock' contains the amount of each item in 'menu'
# 'price' contains the prices of each item in 'menu'

menu = ['chicken', 'eggs', 'coffee', 'banana']
stock = {menu[0]: 23, menu[1]: 12, menu[2]: 40, menu[3]: 55}
price = {menu[0]: 40.13, menu[1]: 20.30, menu[2]: 12.23, menu[3]: 4.50}
stock_worth = []

# The for loop below iterates through the dictionaries 'stock' and 'price' to
# attain the values of each key in 'stock' and 'price' by using the value function
# The values of each key in 'stock' and 'price' are multiplied using the
# zip function and appended to 'stock_worth'
# The sum of 'stock_worth' is calculated and printed out

for stock, price in zip(stock.values(), price.values()):
    stock_worth.append(stock * price)

print(round(sum(stock_worth), 2))
