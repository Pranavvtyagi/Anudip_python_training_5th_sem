attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# Count present and absent days
present = attendance.count('P')
absent = attendance.count('A')

print("Present Days:", present)
print("Absent Days:", absent)

# Calculate attendance percentage
total_days = len(attendance)
percentage = (present / total_days) * 100

print("Attendance Percentage:", percentage, "%")

# Determine eligibility
if percentage >= 75:
    print("Student is Eligible")
else:
    print("Student is Not Eligible")

# Display positions where student was absent
print("Absent on days:")

for i in range(total_days):
    if attendance[i] == 'A':
        print(i + 1)