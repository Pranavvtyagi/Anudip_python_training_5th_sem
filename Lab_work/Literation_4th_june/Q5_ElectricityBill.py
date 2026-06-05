# Electricity Bill Calculator

units = int(input("Enter electricity units consumed: "))

# Calculate bill according to slab rates
if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Determine consumption category
if units <= 100:
    category = "Low Consumption"

elif units <= 200:
    category = "Medium Consumption"

else:
    category = "High Consumption"

# Display results
print("\nUnits Consumed =", units)
print("Total Bill = ₹", bill)
print("Category =", category)
