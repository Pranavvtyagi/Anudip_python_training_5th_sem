# Program to check whether a number is a Strong Number

num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    # Find factorial of digit
    factorial = 1
    for i in range(1, digit + 1):
        factorial = factorial * i
    sum = sum + factorial
    temp = temp // 10
# Check Strong Number condition
if sum == num:
    print(num, "is a Strong Number")
else:
    print(num, "is Not a Strong Number")
