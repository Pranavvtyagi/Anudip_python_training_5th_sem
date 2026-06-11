'''School Report Card Generator 
Problem Statement Student marks are stored in marks.txt. 
Sample Input/Data (marks.txt) 
S101,Anuj,92 
S102,Rahul,76 
S103,Priya,88 
S104,Neha,45 
S105,Amit,58 
S106,Sneha,95 
S107,Karan,81 
S108,Pooja,73 
S109,Rohit,39 
S110,Anjali,90 
Tasks 
1. Calculate grades for all students.  Passed Students: 9 Failed Students: 1 
2. Generate a report card file report_card.txt.  
3. Display topper details.  
4. Count pass and fail students.  
5. Display students eligible for merit certificates (marks ≥ 90). '''
#-------------------------------------------------------------------------------------------------------------------
# Read student records
file = open("marks.txt", "r")
records = file.readlines()
file.close()
#-------------------------------------------------------------------------------------------------------------------
# Report card file
report_file = open("report_card.txt", "w")
#-------------------------------------------------------------------------------------------------------------------
# Variables
pass_count = 0
fail_count = 0
#------------------------------------------------------------------------------------------------------------------
topper_name = ""
topper_marks = 0
print("Merit Certificate Holders:")
#------------------------------------------------------------------------------------------------------------------
# Process each student
for record in records:
    sid, name, marks = record.strip().split(",")
    marks = int(marks)
    # Grade Calculation
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"
#---------------------------------------------------------------------------------------------------------------------
# Pass / Fail Count
    if marks >= 40:
        pass_count += 1
    else:
        fail_count += 1
    # Topper
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name
    # Merit Certificate
    if marks >= 90:
        print(name)
    # Write Report Card
    report_file.write(
        f"{sid}, {name}, Marks: {marks}, Grade: {grade}\n"
    )
report_file.close()
#--------------------------------------------------------------------------------------------------------------------
# Display Results
print(f"\nTopper: {topper_name} ({topper_marks})")
print("\nPassed Students:", pass_count)
print("Failed Students:", fail_count)
print("\nReport Cards Generated Successfully.")