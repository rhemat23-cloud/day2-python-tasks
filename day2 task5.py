
def get_number(prompt):
    """Safely get a number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# 1. Check if 10 ≥ 5
if 10 >= 5:
    print(" 10 is greater than or equal to 5.")

# 2. Take a number from user and check if it is greater than 50
num1 = get_number("Enter a number to check if it is greater than 50: ")
if num1 > 50:
    print(f"{num1} is greater than 50.")
else:
    print(f" {num1} is not greater than 50.")

# 3. Take age from user and check if age ≥ 18
age = get_number("Enter your age: ")
if age >= 18:
    print(" You are an adult (18 or older).")
else:
    print(" You are under 18.")

# 4. Take a number and check if it is greater than 100
num2 = get_number("Enter a number to check if it is greater than 100: ")
if num2 > 100:
    print(f" {num2} is greater than 100.")
else:
    print(f" {num2} is not greater than 100.")

# 5. Take a number and check if number ≥ 0
num3 = get_number("Enter a number to check if it is non-negative: ")
if num3 >= 0:
    print(f" {num3} is non-negative.")
else:
    print(f" {num3} is negative.")
