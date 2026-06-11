'''Smart Parking Management System 
Problem Statement The parking status of vehicles in a mall is maintained as follows. 
Sample Data 
parking_slots = [     "Occupied", "Vacant", "Occupied", "Vacant",     "Occupied", "Occupied", "Vacant", "Occupied",     "Vacant", "Occupied" ] 
Tasks 
1.Display vacant parking slot numbers.  
2. Count occupied and vacant slots.  
3. Allocate the first vacant slot to a new vehicle.  
4. Calculate parking occupancy percentage.  
5. Store updated parking information in parking.txt.  '''
#Data
parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]
#---------------------------------------------------------------------------------------------------------------
#Display vacant parking slot numbers
print("Vacant Parking Slots:")
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        print(i + 1, end=" ")
print()
#----------------------------------------------------------------------------------------------------------------
#Count occupied and Vacant slots
occupied = 0
vacant = 0
for slot in parking_slots:
    if slot == "Occupied":
        occupied += 1
    else:
        vacant += 1
print("\nOccupied Slots:", occupied)
print("Vacant Slots:", vacant)
#---------------------------------------------------------------------------------------------------------------------
#Allocate the first Vacant slot
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        parking_slots[i] = "Occupied"
        print(f"\nVehicle Allocated to Slot {i + 1}")
        break
#---------------------------------------------------------------------------------------------------------------------
#Calculate occupancy percentage
occupied_count = 0
for slot in parking_slots:
    if slot == "Occupied":
        occupied_count += 1
occupancy_percentage = (occupied_count / len(parking_slots)) * 100
print(f"Occupancy Percentage: {occupancy_percentage}%")
#----------------------------------------------------------------------------------------------------------------------
#Store updated parking information in parking.txt
file = open("parking.txt", "w")
for i in range(len(parking_slots)):
    file.write(f"Slot {i + 1}: {parking_slots[i]}\n")
file.close()
print("Parking Details Saved Successfully.")
