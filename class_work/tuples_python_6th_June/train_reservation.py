passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

confirmed_count = 0
waiting_count = 0

confirmed_list = []
waiting_list = []

# Display waiting-list passengers
print("Waiting List Passengers:")

for name, status in passengers:
    
    if status == "Waiting":
        print(name)
        waiting_count += 1
        waiting_list.append(name)
        
    else:
        confirmed_count += 1
        confirmed_list.append(name)

# Count passengers
print("\nConfirmed Passengers:", confirmed_count)
print("Waiting Passengers:", waiting_count)

# Check whether a passenger has confirmed ticket
search_name = "Priya"
found = False

for name, status in passengers:
    if name == search_name and status == "Confirmed":
        found = True
        break

if found:
    print("\n", search_name, "has a confirmed ticket.")
else:
    print("\n", search_name, "does not have a confirmed ticket.")

# Separate lists
print("\nConfirmed Passenger List:", confirmed_list)
print("Waiting Passenger List:", waiting_list)