
def day_of_week(num):
    """Return day name for numbers 1-7."""
    match num:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number! Please enter 1-7."

def color_name(num):
    """Return color name for numbers 1-3."""
    match num:
        case 1:
            return "Red"
        case 2:
            return "Blue"
        case 3:
            return "Green"
        case _:
            return "Invalid color number! Please enter 1-3."

def fruit_name(num):
    """Return fruit name for numbers 1-4."""
    match num:
        case 1:
            return "Apple"
        case 2:
            return "Mango"
        case 3:
            return "Orange"
        case 4:
            return "Banana"
        case _:
            return "Invalid fruit number! Please enter 1-4."

# Main program with input validation
try:
    # Days
    day_num = int(input("Enter a number (1-7) for day: "))
    print("Day:", day_of_week(day_num))

    # Colors
    color_num = int(input("Enter a number (1-3) for color: "))
    print("Color:", color_name(color_num))

    # Fruits
    fruit_num = int(input("Enter a number (1-4) for fruit: "))
    print("Fruit:", fruit_name(fruit_num))

except ValueError:
    print("Invalid input! Please enter integers only.")
