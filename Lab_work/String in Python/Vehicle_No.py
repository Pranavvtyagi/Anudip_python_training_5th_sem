vehicle_number = "MH12AB4589"

# 1. Extract state code
state_code = vehicle_number[0:2]

# 2. Extract district code
district_code = vehicle_number[2:4]

# 3. Extract vehicle series
series = vehicle_number[4:6]

# 4. Extract vehicle number
number = vehicle_number[6:]

# 5. Count letters and digits
letters = 0
digits = 0

for ch in vehicle_number:

    if ch.isalpha():
        letters += 1

    elif ch.isdigit():
        digits += 1

# 6. Verify number plate format
condition1 = vehicle_number[0:2].isalpha()
condition2 = vehicle_number[2:4].isdigit()
condition3 = vehicle_number[4:6].isalpha()
condition4 = vehicle_number[6:].isdigit()

if condition1 and condition2 and condition3 and condition4:
    status = "Valid"
else:
    status = "Invalid"

# Display Output
print("Vehicle Number:", vehicle_number)
print()

print("State Code:", state_code)
print("District Code:", district_code)
print("Series:", series)
print("Vehicle Number:", number)
print()

print("Total Letters:", letters)
print("Total Digits:", digits)
print()

print("Vehicle Number Status:", status)