# This program allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.

import math

financial_calculator_type = input('''Choose either 'investment' or 'bond' from the menu below to proceed:

investment\t - to calculate the amount of interest you'll earn on interest
bond\t\t - to calculate the amount you'll have to pay on a home loan\n''').lower()

# The following if/elif/else statement determine what questions to ask the user based on their selection
# The answer to these questions will be used in a formula to calculate their investment value or bond repayment
# The program ends and displays an error message if the users input is invalid

if (financial_calculator_type == 'investment'):
    P = float(input("Enter the amount you would like to deposit: "))
    r = float(input("Enter the interest rate(Exclude '%' symbol): "))
    t = int(input("Enter the amount of years: "))
    interest = input("'Simple' or 'compound' interest? ").lower()
    if (interest == 'simple'):
        A = P * (1 + r/100 * t)
    elif (interest == 'compound'):
        A = P * math.pow((1 + r/100), t)
    else:
        print("Invalid input. Please select 'compound' or 'simple'.")
    print(f"R{round(A, 2)}")

elif (financial_calculator_type == 'bond'):
    P = float(input("What is the present value of the house: "))
    i = float(input("What is the annual interest rate(Exclude '%' symbol): "))
    n = int(input("Enter the amount of months: "))
    repayment = ((i/12 * P)/(1 - math.pow((1 + i/12), -n)))/12
    print(f"R{round(repayment, 2)}")

else:
    print("Invalid input. Please select 'bond' or 'investment.'")
