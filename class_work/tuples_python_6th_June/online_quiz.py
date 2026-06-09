correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

score = 0
wrong_questions = []

# Compare answers
for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1
    else:
        wrong_questions.append(i + 1)

# Count correct and wrong answers
correct_answers = score
wrong_answers = len(correct) - score

# Calculate percentage
percentage = (score / len(correct)) * 100

# Display results
print("Score:", score)
print("Correct Answers:", correct_answers)
print("Wrong Answers:", wrong_answers)

print("Incorrectly Answered Question Numbers:")
for q in wrong_questions:
    print(q)

print("Percentage:", percentage, "%")

# Determine pass/fail
if percentage >= 60:
    print("Result: Pass")
else:
    print("Result: Fail")