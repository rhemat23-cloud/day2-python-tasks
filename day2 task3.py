# Python program demonstrating input() and type casting

def get_integer(prompt):
    """Safely get an integer from user input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

# 1. Take a name from user input and print its data type
name = input("Enter your name: ")
print(f"Name: {name}, Data type: {type(name)}")

# 2. Take age from user input and convert it into integer
age = get_integer("Enter your age: ")
print(f"Age: {age}, Data type: {type(age)}")

# 3. Take two numbers from user input and print their sum
num1 = get_integer("Enter first number: ")
num2 = get_integer("Enter second number: ")
print(f"Sum of {num1} and {num2} is: {num1 + num2}")

# 4. Take two marks from user input and print their average
mark1 = get_integer("Enter first mark: ")
mark2 = get_integer("Enter second mark: ")
average = (mark1 + mark2) / 2
print(f"Average of marks: {average}")

# 5. Take two numbers and print 3*a*2 + b - 2
a = get_integer("Enter value for a: ")
b = get_integer("Enter value for b: ")
expression_result = 3 * a * 2 + b - 2
print(f"Result of 3*a*2 + b - 2: {expression_result}")

# 6. Take a number and print its data type before and after type casting
num_str = input("Enter a number: ")
print(f"Before type casting: Value = {num_str}, Type = {type(num_str)}")
try:
    num_int = int(num_str)
    print(f"After type casting: Value = {num_int}, Type = {type(num_int)}")
except ValueError:
    print("Cannot convert input to integer.")
