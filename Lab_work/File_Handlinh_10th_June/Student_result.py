''' Student Result Processing System 
Problem Statement Student marks are stored in results.txt. 
File Format 
S101,Anuj,85 
S102,Rahul,72 
S103,Priya,96 
S104,Neha,68 
S105,Amit,39 
S106,Sneha,54 
S107,Karan,91 
S108,Pooja,78 
S109,Rohit,47 
S110,Anjali,88 
Requirements Write a program to: 
1. Display all student records.  
2. Search a student using Student ID.  
3. Find topper and lowest scorer.  
4. Calculate class average.  
5. Count pass and fail students.  
6. Generate grades:  
o A (90+)  
o B (75–89)  
o C (40–74)  
o F (<40)  
7. Write grade reports into a new file named grades.txt.  '''

def display_records():
    file = open("results.txt", "r")

    print("\nStudent Records")
    print("-" * 30)

    for line in file:
        print(line.strip())

    file.close()


def search_student(student_id):
    file = open("results.txt", "r")

    found = False

    for line in file:
        sid, name, marks = line.strip().split(",")

        if sid == student_id:
            print("\nStudent Found")
            print("ID    :", sid)
            print("Name  :", name)
            print("Marks :", marks)
            found = True
            break

    if not found:
        print("Student not found.")

    file.close()


def topper_lowest():
    file = open("results.txt", "r")

    students = []

    for line in file:
        sid, name, marks = line.strip().split(",")
        students.append((sid, name, int(marks)))

    topper = max(students, key=lambda x: x[2])
    lowest = min(students, key=lambda x: x[2])

    print("\nTopper:")
    print(topper)

    print("\nLowest Scorer:")
    print(lowest)

    file.close()


def class_average():
    file = open("results.txt", "r")

    total = 0
    count = 0

    for line in file:
        sid, name, marks = line.strip().split(",")
        total += int(marks)
        count += 1

    print("Class Average =", total / count)

    file.close()


def pass_fail():
    file = open("results.txt", "r")

    passed = 0
    failed = 0

    for line in file:
        sid, name, marks = line.strip().split(",")
        marks = int(marks)

        if marks >= 40:
            passed += 1
        else:
            failed += 1

    print("Passed Students =", passed)
    print("Failed Students =", failed)

    file.close()


def generate_grades():
    file = open("results.txt", "r")
    grade_file = open("grades.txt", "w")

    print("\nGrade Report")
    print("-" * 30)

    for line in file:
        sid, name, marks = line.strip().split(",")
        marks = int(marks)

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 40:
            grade = "C"
        else:
            grade = "F"

        report = f"{sid},{name},{marks},{grade}\n"

        print(report.strip())
        grade_file.write(report)

    file.close()
    grade_file.close()

    print("\nGrades written successfully to grades.txt")


# Menu Driven Program
while True:
    print("\n===== STUDENT RESULT PROCESSING SYSTEM =====")
    print("1. Display All Student Records")
    print("2. Search Student by ID")
    print("3. Find Topper and Lowest Scorer")
    print("4. Calculate Class Average")
    print("5. Count Pass and Fail Students")
    print("6. Generate Grades and Save to File")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_records()

    elif choice == 2:
        sid = input("Enter Student ID: ")
        search_student(sid)

    elif choice == 3:
        topper_lowest()

    elif choice == 4:
        class_average()

    elif choice == 5:
        pass_fail()

    elif choice == 6:
        generate_grades()

    elif choice == 7:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")