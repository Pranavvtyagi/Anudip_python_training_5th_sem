# List of product orders
orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# 1. Display products costing more than 1000
print("Products Costing More Than ₹1000:")

for product in orders:
    if product[1] > 1000:
        print(product[0], "-", product[1])

# 2. Find the most expensive product
most_expensive = orders[0]

for product in orders:
    if product[1] > most_expensive[1]:
        most_expensive = product

print("\nMost Expensive Product:")
print(most_expensive[0], "-", most_expensive[1])

# 3. Calculate total order value
total = 0

for product in orders:
    total += product[1]

print("\nTotal Order Value:", total)

# 4. Count products costing below 1000
count = 0

for product in orders:
    if product[1] < 1000:
        count += 1

print("\nProducts Costing Below ₹1000:", count)