def display_records():
    file = open("employees.txt", "r")
    print("\nEmployee Records:")
    print("------------------")
    for line in file:
        print(line.strip())
    file.close()


def search_employee(emp_id):
    file = open("employees.txt", "r")

    found = False
    for line in file:
        eid, name, salary = line.strip().split(",")

        if eid == emp_id:
            print("\nEmployee Found:")
            print("ID:", eid)
            print("Name:", name)
            print("Salary:", salary)
            found = True
            break

    if not found:
        print("Employee not found.")

    file.close()


def average_salary():
    file = open("employees.txt", "r")

    total = 0
    count = 0

    for line in file:
        eid, name, salary = line.strip().split(",")
        total += int(salary)
        count += 1

    avg = total / count
    print("Average Salary =", avg)

    file.close()


def highest_lowest_salary():
    file = open("employees.txt", "r")

    employees = []

    for line in file:
        eid, name, salary = line.strip().split(",")
        employees.append((eid, name, int(salary)))

    highest = max(employees, key=lambda x: x[2])
    lowest = min(employees, key=lambda x: x[2])

    print("\nHighest Paid Employee:")
    print(highest)

    print("\nLowest Paid Employee:")
    print(lowest)

    file.close()


def employees_above_50000():
    file = open("employees.txt", "r")

    print("\nEmployees earning above ₹50,000:")
    for line in file:
        eid, name, salary = line.strip().split(",")

        if int(salary) > 50000:
            print(eid, name, salary)

    file.close()


def add_employee():
    file = open("employees.txt", "a")

    eid = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Salary: ")

    file.write(f"\n{eid},{name},{salary}")

    file.close()

    print("Employee record added successfully.")


def salary_categories():
    file = open("employees.txt", "r")

    print("\nSalary Categories:")
    print("------------------")

    for line in file:
        eid, name, salary = line.strip().split(",")
        salary = int(salary)

        if salary >= 60000:
            category = "High"
        elif salary >= 40000:
            category = "Medium"
        else:
            category = "Low"

        print(eid, name, salary, "->", category)

    file.close()


# Main Menu
while True:
    print("\n===== Employee Payroll Management System =====")
    print("1. Display All Employee Records")
    print("2. Search Employee by ID")
    print("3. Calculate Average Salary")
    print("4. Find Highest and Lowest Paid Employee")
    print("5. Display Employees Earning Above ₹50,000")
    print("6. Add New Employee")
    print("7. Generate Salary Categories")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_records()

    elif choice == 2:
        emp_id = input("Enter Employee ID: ")
        search_employee(emp_id)

    elif choice == 3:
        average_salary()

    elif choice == 4:
        highest_lowest_salary()

    elif choice == 5:
        employees_above_50000()

    elif choice == 6:
        add_employee()

    elif choice == 7:
        salary_categories()

    elif choice == 8:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")