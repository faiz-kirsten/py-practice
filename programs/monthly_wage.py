# This program calculates the monthly wage for two different types of employees for a department store

type_employee = "Salesperson"

salesperson_or_manager = input("Are you a salesperson or a manager? (Salesperson or Manager) ")
# Used the if/else shorthand
# https://www.w3schools.com/python/gloss_python_if_else_shorthand.asp
type_employee = "Manager" if salesperson_or_manager == "Manager" else type_employee

# Depending on the type of employee - they will be asked a specific question related to their role which will be used to calculate their monthly wage 

if (type_employee == "Salesperson"):
  gross_sales = int(input("What are your gross sales for the month? "))
  monthly_wage = (gross_sales * 0.08) + 2000
else:
  hours_worked = float(input("How much hours did you work this month? "))
  monthly_wage = hours_worked * 40

print(f"Your total wage for the month is R{round(monthly_wage,2)}")