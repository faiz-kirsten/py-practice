# This program asks the user to input an integer
# It then determines whether these numbers are divisible by 2 or 5

number = int(input("Enter an integer: "))

if (number % 2 == 0) and (number % 5 == 0):
    print(f"{number} is divisible by 2 and 5")
elif (number % 2 == 0) or (number % 5 == 0):
    print(f"{number} is divisible by 2 or 5")
else:
    print(f"{number} is not divisible by 2 or 5")