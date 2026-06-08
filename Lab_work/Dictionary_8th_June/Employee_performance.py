performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Display employees scoring above 80
print("Employees Scoring Above 80:")

for emp, score in performance.items():
    if score > 80:
        print(emp)

# 2. Count employees needing improvement
improvement_count = 0

for score in performance.values():
    if score < 60:
        improvement_count += 1

# 3. Find the top performer
top_employee = max(performance, key=performance.get)

# 4. Calculate average performance score
average_score = sum(performance.values()) / len(performance)

# 5. Create separate lists
excellent = []
good = []
average = []
poor = []

for emp, score in performance.items():

    if score >= 90:
        excellent.append(emp)

    elif 75 <= score <= 89:
        good.append(emp)

    elif 60 <= score <= 74:
        average.append(emp)

    else:
        poor.append(emp)

# Display results
print("\nTop Performer:", top_employee, "(", performance[top_employee], ")", sep="")

print("Employees Needing Improvement:", improvement_count)

print("Average Score:", average_score)

print("\nExcellent:", excellent)
print("Good:", good)
print("Average:", average)
print("Poor:", poor)