# List of numbers
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# Find consecutive pairs

for i in range(len(numbers) - 1):

    # Check if difference is 1
    if numbers[i] + 1 == numbers[i + 1]:

        print(numbers[i], "and", numbers[i + 1], "are consecutive")