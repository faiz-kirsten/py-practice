# This program calculates the total cost of a holiday based on the users input.

# The function below determines and returns the total cost of the hotel stay based on the number of nights the user
# enters.
def hotel_cost(num_nights):
    total_cost_hotel = num_nights * 99.99
    return total_cost_hotel


# The function below determines and returns the cost of the flight based on what city the user enters.
def plane_cost(city):
    if city == 'jhb':
        flight_cost = 199.99
    elif city == 'dbn':
        flight_cost = 149.99
    elif city == 'cpt':
        flight_cost = 99.99

    return flight_cost


# The function below determines and returns the total cost of the car rental based on the amount of days the user
# would like to rent it.
def car_rental(num_days_hired):
    total_cost_rental = num_days_hired * 15.99
    return total_cost_rental


# The function below calculates and returns the total cost of the users holiday.
# It calls the functions 'hotel_cost(num_nights)', 'plane_cost(city)' and 'car_rental(num_days_hired)'
# in order to calculate the total cost of the holiday.
def holiday_cost(num_nights_hotel, user_city, num_days_rental):
    total_holiday_cost = round(hotel_cost(num_nights_hotel) + plane_cost(user_city) + car_rental(num_days_rental), 2)
    return total_holiday_cost


num_nights_hotel1 = int(input("How many nights will you be staying at the hotel: "))
user_city1 = input("Enter the city you're flying to: (DBN, JHB, CPT) ").lower()
num_days_rental1 = int(input("How many days would you like to rent the car: "))

print(f"The total cost of your holiday is: "
      f"R{holiday_cost(num_nights_hotel1, user_city1, num_days_rental1)}")
