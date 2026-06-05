# Problem Statement: Accept a number from the user and determine whether it is a prime number or not. 
# Additional Requirement: If the number is not prime, display all its factors. 
#---------------------------------------------------------------------------------------------------
#Factor of a number
num = int(input("Enter a number: ")) #taking input from user
count = 0             #initial count is 0
print("Factors are: ")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        count = count + 1
#---------------------------------------------------------------------------------------------------
# Prime number 
if count == 2:     #Prime number has exactly 2 factors
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")
