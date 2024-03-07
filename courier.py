# This program calculates what the cost would be for a courier company to deliver a parcel after additional fees are added on - these additional fees are the users delivery preferences.

package_price = float(input("What is the price of the package you would like to purchase: R"))
delivery_distance = float(input("Enter the distance of the delivery (km): "))

# The following if/else statements determine what additional amount should be added on the package price based on what option the user chooses

air_or_freight = input("Air or Freight? ")
if (air_or_freight == "Freight"):
  is_air = delivery_distance * 0.25
else:
  is_air = delivery_distance * 0.36

full_or_limited = input("Full or limited insurance? (Full or Limited) ")
if (full_or_limited == "Limited"):
  full_insurance = + 25
else:
  full_insurance = + 50

gift_or_no_gift = input("Would you like to include a gift? (Yes or No) ")
if (gift_or_no_gift == "No"):
  include_gift = + 0
else:
  include_gift = + 15

priority_or_standard = input("Priority or standard delivery? (Priority or Standard) ")
if (priority_or_standard == "Standard"):
  is_priority = + 20
else:
  is_priority = + 100

total_price = round(package_price + is_air + full_insurance + include_gift + is_priority,2)

print(f"The final cost of your package is R{total_price}")