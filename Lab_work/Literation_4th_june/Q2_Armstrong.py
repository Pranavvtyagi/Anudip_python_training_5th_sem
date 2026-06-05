#Accept a number from the user and check whether it is an Armstrong Number

# Program to check whether a number is an Armstrong Number
num = int(input("Enter a number: "))
temp = num
sum = 0
# Count number of digits
digits = len(str(num))
# Calculate sum of digits raised to power of digits
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** digits)
    temp = temp // 10
# Check Armstrong condition
if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")
