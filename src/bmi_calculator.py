# This program calculates a persons BMI by getting their weight and height

weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(m): "))
body_mass_index = round(weight / (height * height))
weight_category = "underweight"

# After the persons BMI is calculated
# It then determines what weight category they fall into based on their BMI

if (body_mass_index >= 30):
    weight_category = "obese"
elif (body_mass_index >= 25):
    weight_category = "overweight"
elif (body_mass_index >= 18.5):
    weight_category = "normal"
else:
    weight_category

print(
    f"Your Body Mass Index(BMI) is {body_mass_index}. This is considered {weight_category}.")
