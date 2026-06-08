units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")

for house, consumption in units.items():
    if consumption > 400:
        print(house)

# 2. Find the highest-consuming house
highest_house = max(units, key=units.get)

print("\nHighest Consumption:", highest_house,
      "(", units[highest_house], "units)", sep=" ")

# 3. Find the lowest-consuming house
lowest_house = min(units, key=units.get)

print("Lowest Consumption:", lowest_house,
      "(", units[lowest_house], "units)", sep=" ")

# 4. Calculate total units consumed
total_units = sum(units.values())

print("Total Units Consumed:", total_units)

# 5. Create lists
low = []
medium = []
high = []

for house, consumption in units.items():

    if consumption < 200:
        low.append(house)

    elif 200 <= consumption <= 400:
        medium.append(house)

    else:
        high.append(house)

print("\nLow Consumption:", low)
print("Medium Consumption:", medium)
print("High Consumption:", high)

# 6. Count houses eligible for energy-saving campaign
count = 0

for consumption in units.values():
    if consumption > 300:
        count += 1

print("\nEligible for Energy-Saving Campaign:", count)