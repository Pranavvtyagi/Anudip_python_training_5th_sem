# Program to remove duplicate entries of a given number

# Creating blank list to store numbers
numbers = []

print("Enter any 20 numbers:")
for x in range(20):
    num = int(input())
    numbers.append(num)

print("----------------------------------------------")

element = int(input("Enter any number to remove its duplicates: "))

# Finding the frequency of the given number
frequency = numbers.count(element)

if frequency == 0:
    print("Element not found")
elif frequency == 1:
    print("No Duplicate Element")
else:
    # Reverse the list
    numbers.reverse()

    # Remove duplicate occurrences
    for i in range(frequency - 1):
        numbers.remove(element)

    # Reverse again to maintain original order
    numbers.reverse()

    print("After removing duplicates:")
    print(numbers)
