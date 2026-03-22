def get_number(prompt):
    """Safely get an integer from user input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

# 1. Check if a number is even or odd
num1 = get_number("Enter a number to check Even/Odd: ")
if num1 % 2 == 0:
    print(f"{num1} is Even.")
else:
    print(f"{num1} is Odd.")

# 2. Check if marks are pass or fail (pass ≥ 35)
marks = get_number("Enter your marks: ")
if marks >= 35:
    print("Pass ✅")
else:
    print("Fail ❌")

# 3. Check if a number is positive or negative
num2 = get_number("Enter a number to check Positive/Negative: ")
if num2 > 0:
    print(f"{num2} is Positive.")
elif num2 < 0:
    print(f"{num2} is Negative.")
else:
    print("The number is Zero.")

# 4. Check if a number is greater than 10 or not
num3 = get_number("Enter a number to check if greater than 10: ")
if num3 > 10:
    print(f"{num3} is greater than 10.")
else:
    print(f"{num3} is not greater than 10.")
