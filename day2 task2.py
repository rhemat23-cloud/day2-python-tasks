# Task 1: Create a string "python" and print it 3 times
text = "python"
print("Task 1 Output:", text * 3)  # Multiplication repeats the string

# Task 2: Combine "super" and "man" using + operator
str1 = "super"
str2 = "man"
combined = str1 + str2
print("Task 2 Output:", combined)

# Task 3: Create "hello", " ", "world" and print "hello world"
part1 = "hello"
space = " "
part2 = "world"
sentence = part1 + space + part2
print("Task 3 Output:", sentence)

# Task 4: Take a name from user input and print it 5 times
name = input("Enter your name: ").strip()
if name:  # Ensure input is not empty
    print("Task 4 Output:", name * 5)
else:
    print("Task 4 Output: No name entered.")

# Task 5: Take two strings from user input and concatenate them
first_str = input("Enter first string: ").strip()
second_str = input("Enter second string: ").strip()
if first_str and second_str:
    concatenated = first_str + second_str
    print("Task 5 Output:", concatenated)
else:
    print("Task 5 Output: One or both strings were empty.")
