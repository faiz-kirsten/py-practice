# This program calculates the area that the foundation of a building covers

import math

# The user has to input what shape they would like their foundation to be

type_foundation = input(
    "Enter the shape of the buildings foundation?(Square or Rectangular or Round) ")

# The following if/elif/else statements prompt the user to input the appropriate dimensions
# Depending on what shape is selected it then calculates the area of the foundation of the building

if (type_foundation == "Square"):
    square_length = float(
        input("What is the length of each side of the square? "))
    area = math.pow(square_length, 2)

elif (type_foundation == "Rectangular"):
    rectangle_width = float(input("What is the width of the rectangle? "))
    rectangle_length = float(input("What is the length of the rectangle? "))
    area = rectangle_width * rectangle_length

else:
    circle_radius = float(input("What is the radius of the circle? "))
    area = math.pi * math.pow(circle_radius, 2)

print(f"The area of the foundation {round(area, 2)}")
