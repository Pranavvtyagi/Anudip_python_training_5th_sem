employee_id = "EMP2026ANUJ458"

# 1. Count uppercase letters
uppercase_count = 0
for ch in employee_id:
    if ch.isupper():
        uppercase_count += 1

# 2. Count digits
digit_count = 0
for ch in employee_id:
    if ch.isdigit():
        digit_count += 1

# 3. Extract joining year
year = employee_id[3:7]

# 4. Extract employee name
name = employee_id[7:-3]

# 5. Validate ID
starts_correct = employee_id.startswith("EMP")
year_valid = employee_id[3:7].isdigit()
end_valid = employee_id[-3:].isdigit()

if starts_correct and year_valid and end_valid:
    status = "Valid"
else:
    status = "Invalid"

# 6. Create list of all digits
digit_list = []

for ch in employee_id:
    if ch.isdigit():
        digit_list.append(int(ch))

# 7. Sum of digits
digit_sum = sum(digit_list)

# 8. Display results
print("Employee ID:", employee_id)
print("Uppercase Letters:", uppercase_count)
print("Digits:", digit_count)
print("Joining Year:", year)
print("Employee Name:", name)
print("Digit List:", digit_list)
print("Sum of Digits:", digit_sum)
print("ID Status:", status)