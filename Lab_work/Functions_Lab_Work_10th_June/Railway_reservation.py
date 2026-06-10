'''Railway Reservation Seat Analyzer Problem Statement 
A railway coach has seats represented as follows: 
seats = [     "Booked", "Available", "Booked", "Booked",     "Available", "Available", "Booked", "Available",     "Booked", "Booked", "Available", "Booked" ] 
Requirements Create the following functions:
1. count_seats(seats) Returns the number of booked and available seats. 
2. first_available(seats) Returns the seat number of the first available seat. 
3. occupancy_percentage(seats) Returns the percentage of occupied seats. 
4. display_available_seats(seats) Displays all available seat numbers. 
   Sample Output Booked Seats: 7 Available Seats: 
5  First Available Seat: 2  Occupancy Percentage: 58.33%  Available Seat Numbers: 2 5 6 8 11 '''
#------------------------------------------------------------------------------------------------------------
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"]

#Function to Count Booked and Available Seats

def count_seats(seats):
    booked = seats.count("Booked")
    availabe = seats.count("Available")
    return booked,availabe

#Function to find Available Seat
def available_seat(seats):
    for i in range (len(seats)):
        if seats[i]=="Available":
            return i+1
        return None
    
#Function to calculate Occupancy Percentage
def occupancy_percentage(seats):
    booked = seats.count("Booked")
    total = len(seats)
    return (booked / total) * 100

#Function to display availabe seat numbers
def display_available_seats(seats):
    print("Available Seat Numbers:", end=" ")
    
    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1, end=" ")
    print()

#---------------------------------------------------------------------
booked = count_seats(seats)
available = count_seats(seats)
print("Booked Seats:", booked)
print("Available Seats:", available)
print("\nFirst Available Seat:", available_seat(seats))
print("\nOccupancy Percentage: {:.2f}%".format(
    occupancy_percentage(seats)
))
display_available_seats(seats)