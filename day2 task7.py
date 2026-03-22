# Using Nested If Statements

def job_eligibility(age, height, weight):
    """Check job eligibility based on given conditions."""
    if age >= 18:
        if height >= 160:
            if weight >= 60:
                return "Selected for Job"
            else:
                return "Rejected: Weight below requirement"
        else:
            return "Rejected: Height below requirement"
    else:
        return "Rejected: Age below requirement"


def college_admission(marks, age):
    """Check college admission eligibility."""
    if marks >= 60:
        if age >= 17:
            return "Eligible for College Admission"
        else:
            return "Not Eligible: Age below requirement"
    else:
        return "Not Eligible: Marks below requirement"


def sports_selection(age, height, weight):
    """Check sports selection eligibility."""
    if age >= 16:
        if height >= 150:
            if weight >= 50:
                return "Selected for Sports"
            else:
                return "Rejected: Weight below requirement"
        else:
            return "Rejected: Height below requirement"
    else:
        return "Rejected: Age below requirement"
# ------------------ MAIN PROGRAM ------------------
try:
    # Job Eligibility
    print("\n--- Job Eligibility Check ---")
    age = int(input("Enter Age: "))
    height = float(input("Enter Height (cm): "))
    weight = float(input("Enter Weight (kg): "))
    print(job_eligibility(age, height, weight))

    # College Admission
    print("\n--- College Admission Check ---")
    marks = float(input("Enter Marks: "))
    age = int(input("Enter Age: "))
    print(college_admission(marks, age))

    # Sports Selection
    print("\n--- Sports Selection Check ---")
    age = int(input("Enter Age: "))
    height = float(input("Enter Height (cm): "))
    weight = float(input("Enter Weight (kg): "))
    print(sports_selection(age, height, weight))

except ValueError:
    print("Invalid input! Please enter numeric values only.")


