 #Python Bitwise Operator Tasks (1–8)

# 1. Bitwise AND
a = 10  # binary: 1010
b = 6   # binary: 0110
print("1. a & b =", a & b)  # 1010 & 0110 = 0010 (2)

#2. Define variables
x = 12  # Binary: 1100
y = 5   # Binary: 0101

# Perform bitwise OR operation
result = x | y  # Binary result: 1101 (Decimal: 13)

# Print the result
print(f"x | y = {result}")

# 3.Create variable num
num = 8
# Bitwise NOT (~) flips all bits
result_not = ~num
print(f"~{num} = {result_not}")  # Expected: -9 (because ~x = -x - 1)

#4. Create variables a and b
a = 15
b = 9
# Bitwise XOR (^)
result_xor = a ^ b
print(f"{a} ^ {b} = {result_xor}") 

#5.Perform left shift
try:
    # First operation: Left shift
    num = 7
    left_shift_result = num << 2  # Shift bits 2 places to the left
    print(f"{num} << 2 = {left_shift_result}")
#6.perform right shift
    # Second operation: Right shift
    num = 20
    right_shift_result = num >> 1  # Shift bits 1 place to the right
    print(f"{num} >> 1 = {right_shift_result}")

except Exception as e:
    print(f"An error occurred: {e}")

#7. Bitwise AND of two numbers in Python

def get_integer(prompt):
    """Safely get an integer from user input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    # Take two integers from the user
    num1 = get_integer("Enter the first integer: ")
    num2 = get_integer("Enter the second integer: ")

    # Perform bitwise AND
    and_result = num1 & num2

    # Display results
    print(f"\nBitwise AND of {num1} and {num2} is: {and_result}")
    print(f"Binary form: {bin(num1)} & {bin(num2)} = {bin(and_result)}")

if __name__ == "__main__":
    main()
#8. Bitwise XOR of two numbers in Python

def get_integer(prompt):
    """Safely get an integer from user input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    # Get two integers from the user
    num1 = get_integer("Enter the first integer: ")
    num2 = get_integer("Enter the second integer: ")

    # Perform bitwise XOR
    xor_result = num1 ^ num2

    # Display the result
    print(f"Bitwise XOR of {num1} and {num2} is: {xor_result}")

if __name__ == "__main__":
    main()

