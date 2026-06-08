# Parking slot status
slots = [1, 0, 1, 1, 0, 0, 1, 0]

# 1. Count occupied and available slots
occupied = 0
available = 0

for slot in slots:
    if slot == 1:
        occupied += 1
    else:
        available += 1

print("Occupied Slots:", occupied)
print("Available Slots:", available)

# 2. Find the first available slot
for i in range(len(slots)):
    if slots[i] == 0:
        print("\nFirst Available Slot:", i)
        break

# 3. Display all available slot numbers
available_slots = []

for i in range(len(slots)):
    if slots[i] == 0:
        available_slots.append(i)

print("\nAvailable Slot Numbers:", available_slots)

# 4. Check if occupancy exceeds 75%
occupancy_percentage = (occupied / len(slots)) * 100

print("\nOccupancy Percentage:", occupancy_percentage, "%")

if occupancy_percentage > 75:
    print("Parking occupancy exceeds 75%")
else:
    print("Parking occupancy does not exceed 75%")