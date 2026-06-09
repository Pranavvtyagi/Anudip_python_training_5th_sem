attendance = "PPAPPPAAPPPPAPP"

# 1. Count Present and Absent days
present_days = attendance.count("P")
absent_days = attendance.count("A")

# Total days
total_days = len(attendance)

# 2. Calculate attendance percentage
attendance_percentage = (present_days / total_days) * 100

# 3. Longest consecutive streak of Presence
max_present_streak = 0
current_present_streak = 0

for ch in attendance:

    if ch == "P":
        current_present_streak += 1

        if current_present_streak > max_present_streak:
            max_present_streak = current_present_streak

    else:
        current_present_streak = 0

# 4. Longest consecutive streak of Absence
max_absent_streak = 0
current_absent_streak = 0

for ch in attendance:

    if ch == "A":
        current_absent_streak += 1

        if current_absent_streak > max_absent_streak:
            max_absent_streak = current_absent_streak

    else:
        current_absent_streak = 0

# 5. Attendance status
if attendance_percentage < 75:
    status = "Below 75%"
else:
    status = "Good Attendance"

# Display Output
print("Attendance Record:", attendance)
print()

print("Present Days:", present_days)
print("Absent Days:", absent_days)
print()

print("Attendance Percentage:", round(attendance_percentage, 2), "%")
print()

print("Longest Present Streak:", max_present_streak)
print("Longest Absent Streak:", max_absent_streak)
print()

print("Attendance Status:", status)