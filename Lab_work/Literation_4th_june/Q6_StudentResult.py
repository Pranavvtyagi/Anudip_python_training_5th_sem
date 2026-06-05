# Student Result Management System

total = 0
failed_subjects = 0

# Input marks of 5 subjects
for i in range(1, 6):
    marks = int(input(f"Enter marks of Subject {i}: "))

    total = total + marks

    if marks < 40:
        failed_subjects = failed_subjects + 1

# Calculate percentage
percentage = total / 5

# Determine grade
if failed_subjects > 0:
    grade = "Fail"

elif percentage >= 90:
    grade = "A+"

elif percentage >= 75:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "Fail"

# Display result
print("\n----- Result -----")
print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)
print("Number of Subjects Failed =", failed_subjects)
