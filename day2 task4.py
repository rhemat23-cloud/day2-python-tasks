
# 1️Take number as string and print last digit
num_str = input("Enter a number (string input): ").strip()
if not num_str.isdigit():
    print("Invalid input. Please enter digits only.")
else:
    print("Last digit (string method):", num_str[-1])

# 2️Take number as integer and print unit digit using % operator
try:
    num_int = int(input("Enter a number (integer input): "))
    print("Unit digit (% method):", num_int % 10)
except ValueError:
    print("Invalid integer input.")

# 3️Remove last digit using // operator
try:
    print("Number without last digit (// method):", num_int // 10)
except NameError:
    pass  # num_int not defined if invalid input earlier

# 4️Print second last digit
if abs(num_int) >= 10:  # Ensure at least 2 digits
    second_last = abs(num_int) // 10 % 10
    print("Second last digit:", second_last)
else:
    print("Number has no second last digit.")

# 5️Take a 5-digit number and write last digit to Excel
try:
    five_digit = int(input("Enter a 5-digit number: "))
    if 10000 <= abs(five_digit) <= 99999:
        last_digit = abs(five_digit) % 10

        # Create a new Excel workbook
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = "LastDigitData"
        sheet["A1"] = "Last Digit"
        sheet["A2"] = last_digit

        # Save the Excel file
        wb.save("last_digit.xlsx")
        print(f"Last digit {last_digit} saved to 'last_digit.xlsx'")
    else:
        print("Please enter a valid 5-digit number.")
except ValueError:
    print("Invalid input for 5-digit number.")
