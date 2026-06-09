# List of student marks
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# 1. Display passed students
print("Passed Students Marks:")
for i in marks:
    if i >= 40:
        print(i)

# 2. Count failed students
failed_count = 0

for i in marks:
    if i < 40:
        failed_count += 1

print("Number of Failed Students:", failed_count)

# 3. Find highest and lowest marks without max() or min()

highest = marks[0]
lowest = marks[0]

for i in marks:
    if i > highest:
        highest = i

    if i < lowest:
        lowest = i

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# 4. Create new list containing marks above 75

above_75 = []

for i in marks:
    if i > 75:
        above_75.append(i)

print("Marks Above 75:", above_75)