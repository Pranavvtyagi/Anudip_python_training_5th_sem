# Batsman's scores
scores = [45, 78, 12, 100, 67, 8, 90, 55]

# 1. Count half-centuries and centuries
half_centuries = 0
centuries = 0

for score in scores:
    if score >= 50 and score < 100:
        half_centuries += 1
    elif score >= 100:
        centuries += 1

print("Half-Centuries:", half_centuries)
print("Centuries:", centuries)

# 2. Find the highest score
highest = scores[0]

for score in scores:
    if score > highest:
        highest = score

print("\nHighest Score:", highest)

# 3. Display scores below 20
print("\nScores Below 20:")

for score in scores:
    if score < 20:
        print(score)

# 4. Calculate average score
total = 0

for score in scores:
    total += score

average = total / len(scores)

print("\nAverage Score:", average)