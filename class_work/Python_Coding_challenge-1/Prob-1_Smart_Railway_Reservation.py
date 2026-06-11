'''Problem Statement 
A railway reservation system stores the booking status of seats in a train coach. 
Sample Data seats = {     1: "Booked",     2: "Available",     3: "Booked",     4: "Available",     5: "Booked",     6: "Booked",     7: "Available",     8: "Booked",     9: "Available",     10: "Booked" } 
Tasks 1. Display all available seat numbers.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Cancel booking for a given seat number.  
5. Store the updated reservation status in reservations.txt. 
6. Display occupancy percentage. '''
#----------------------------------------------------------------------------------------------------------------
#Data Given
seats = {
    1: "Booked",
    2: "Available",
    3: "Booked",
    4: "Available",
    5: "Booked",
    6: "Booked",
    7: "Available",
    8: "Booked",
    9: "Available",
    10: "Booked"
}
#Display all available seat numbers
print("Available Seats:")
for seat_no, status in seats.items():
    if status == "Available":
        print(seat_no, end=" ")
print()
#----------------------------------------------------------------------------------------------------------------------
#Count booked and available seats
booked = 0
available = 0

for status in seats.values():
    if status == "Booked":
        booked += 1
    else:
        available += 1

print("\nBooked Seats:", booked)
print("Available Seats:", available)
#--------------------------------------------------------------------------------------------------------------------.
#Reserve the first available seat
for seat_no, status in seats.items():
    if status == "Available":
        seats[seat_no] = "Booked"
        print(f"\nSeat {seat_no} Reserved Successfully.")
        break
#---------------------------------------------------------------------------------------------------------------------
#Cancel booking for a given seat number
seat_cancel = int(input("\nEnter seat number to cancel booking: "))

if seat_cancel in seats:
    if seats[seat_cancel] == "Booked":
        seats[seat_cancel] = "Available"
        print("Booking Cancelled Successfully.")
    else:
        print("Seat is already available.")
else:
    print("Invalid Seat Number.")
#---------------------------------------------------------------------------------------------------------------------
#Store updated reservation status in reservations.txt
file = open("reservations.txt", "w")

for seat_no, status in seats.items():
    file.write(f"Seat {seat_no}: {status}\n")
file.close()
print("Reservation Details Saved Successfully.")
#---------------------------------------------------------------------------------------------------------------------
#Display occupancy percentage
booked_count = 0
for status in seats.values():
    if status == "Booked":
        booked_count += 1
occupancy = (booked_count / len(seats)) * 100
print(f"Occupancy Percentage: {occupancy}%")
