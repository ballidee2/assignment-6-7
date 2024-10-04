import random


def roll_dice():
    """Return a random dice roll between 1 and 6."""
    return random.randint(2, 6)


def main():
    """Main program to roll the dice until a 6 is rolled."""
    result = 0

    while result != 6:
        result = roll_dice()
        print(f"You rolled: {result}")

    print("You rolled a 6! Game over over.")


if __name__ == "__main__":
    main()

import random


def roll_dice(sides):
    """Return a random dice roll between 1 and the specified number of sides."""
    return random.randint(1, sides)


def main():
    """Main program to roll the dice until the maximum number is rolled."""
    try:

        sides = int(input("Enter the number of sides on the dice: "))

        if sides <= 0:
            print("Please enter a positive integer for the number of sides.")
            return

        result = 0

        print(f"Rolling a {sides}-sided dice until we roll a {sides}...")

        while result != sides:
            result = roll_dice(sides)
            print(f"You rolled: {result}")

        print(f"You rolled a {sides}! Game over.")

    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()


def gallons_to_liters(gallons):
    """Convert gallons to liters."""
    return gallons * 3.78541  # 1 gallon is approximately 3.78541 liters


def main():
    """Main program to convert gallons to liters."""
    while True:
        try:

            gallons = float(input("Enter the volume in gallons (negative to quit): "))


            if gallons < 0:
                print("Exiting the program.")
                break


            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is approximately {liters:.2f} liters.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()



def sum_of_list(numbers):
    """Return the sum of all integers in the list."""
    return sum(numbers)


def main():
    """Main program to test the sum_of_list function."""

    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]


    total_sum = sum_of_list(test_list)


    print(f"The sum of the list {test_list} is: {total_sum}")


if __name__ == "__main__":
    main()


def remove_odd_numbers(numbers):
    """Return a new list with all odd numbers removed."""
    return [num for num in numbers if num % 2 == 0]


def main():
    """Main program to test the remove_odd_numbers function."""

    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    filtered_list = remove_odd_numbers(original_list)


    print(f"Original list: {original_list}")
    print(f"Filtered list (without odd numbers): {filtered_list}")


if __name__ == "__main__":
    main()


import math

def calculate_unit_price(diameter, price):
    """Calculate the unit price of pizza per square meter."""
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    area_square_meters = area / 10000
    unit_price = price / area_square_meters
    return unit_price

def main():
    """Main program to compare the unit prices of two pizzas."""

    diameter1 = float(input("Enter the diameter of the first pizza in cm: "))
    price1 = float(input("Enter the price of the first pizza in euros: "))


    diameter2 = float(input("Enter the diameter of the second pizza in cm: "))
    price2 = float(input("Enter the price of the second pizza in euros: "))


    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)


    print(f"Unit price of the first pizza: {unit_price1:.2f} euros per square meter")
    print(f"Unit price of the second pizza: {unit_price2:.2f} euros per square meter")


    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money .")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")

if __name__ == "__main__":
    main()
