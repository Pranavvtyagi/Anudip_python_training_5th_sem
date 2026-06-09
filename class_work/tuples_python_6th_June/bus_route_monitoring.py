passengers = [12, 18, 25, 30, 28, 15, 8]

# Find the busiest stop
max_passengers = max(passengers)
busiest_stop = passengers.index(max_passengers) + 1

print("Busiest Stop:", busiest_stop)
print("Passengers at busiest stop:", max_passengers)

# Display stops with fewer than 10 passengers
print("\nStops with fewer than 10 passengers:")

for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1)

# Calculate average passengers
average = sum(passengers) / len(passengers)

print("\nAverage Passengers:", average)

# Determine whether any stop exceeded 25 passengers
found = False

for p in passengers:
    if p > 25:
        found = True
        break

if found:
    print("Yes, a stop exceeded 25 passengers.")
else:
    print("No stop exceeded 25 passengers.")