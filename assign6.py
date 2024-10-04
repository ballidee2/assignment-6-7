num = 1

while num <= 1000:

    if num % 3 == 0:
        print(num)

    num += 1



def inches_to_centimeters(inches):
    return inches * 2.54


while True:

    user_input = input("Enter a value in inches (negative to quit): ")


    try:
        inches = float(user_input)


        if inches < 0:
            print("Exiting the program.")
            break


        centimeters = inches_to_centimeters(inches)
        print(f"{inches} inches is {centimeters:.2f} centimeters.")

    except ValueError:
        print("Please enter a valid number.")



numbers = []

while True:

    user_input = input("Enter a number (or press Enter to quit): ")


    if user_input == "":
        break

    try:

        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")


if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
else:
    print("No numbers were entered.")



import random


secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

while True:

    guess = input("Enter your guess (or type 'quit' to exit): ")


    if guess.lower() == 'quit':
        print("Thanks for playing! Goodbye.")
        break

    try:

        guess = int(guess)


        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Correct! You've guessed the number!")
            break
    except ValueError:
        print("Please enter a valid integer between 1 and 10.")




correct_username = "python"
correct_password = "rules"


attempts = 0
max_attempts = 5

while attempts < max_attempts:

    username = input("Enter your username: ")
    password = input("Enter your password: ")


    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        attempts += 1
        print("Incorrect username or password. Please try again.")


        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempt(s) left.")
        else:
            print("Access denied.")



import random

def approximate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):

        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)


        if x**2 + y**2 < 1:
            inside_circle += 1


    pi_approximation = 4 * inside_circle / num_points
    return pi_approximation

def main():

    try:
        num_points = int(input("Enter the number of random points to generate: "))
        if num_points <= 0:
            print("Please enter a positive integer .")
            return

        pi_value = approximate_pi(num_points)
        print(f"Approximation of π using {num_points} random points: {pi_value}")

    except ValueError:
        print("Please enter a valid integer. ")

if __name__ == "__main__":
    main()


