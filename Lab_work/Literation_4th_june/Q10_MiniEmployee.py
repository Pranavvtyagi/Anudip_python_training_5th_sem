# Mini Employee Payroll System

# Input Employee Details
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: ₹"))

# Calculate Salary Components
hra = basic_salary * 0.20
da = basic_salary * 0.10
pf = basic_salary * 0.12

# Calculate Gross and Net Salary
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

# Determine Employee Grade
if net_salary > 50000:
    grade = "Senior Grade"

elif net_salary > 30000:
    grade = "Mid Grade"

else:
    grade = "Junior Grade"

# Display Payroll Details
print("\n----- Employee Payroll Details -----")

print("Employee Name =", name)
print("Basic Salary = ₹", basic_salary)
print("HRA = ₹", hra)
print("DA = ₹", da)
print("PF Deduction = ₹", pf)

print("Gross Salary = ₹", gross_salary)
print("Net Salary = ₹", net_salary)

print("Employee Grade =", grade)
