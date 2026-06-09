# List of stock quantities
stock = [25, 5, 0, 12, 3, 18, 0, 30]

# 1. Display products that are out of stock

print("Out of Stock Products:")

for i in stock:
    if i == 0:
        print(i)

# 2. Display products that need restocking (quantity less than 10)

print("Products Needing Restock:")

for i in stock:
    if i < 10:
        print(i)

# 3. Count available products

available_products = 0

for i in stock:
    if i > 0:
        available_products += 1

print("Available Products Count:", available_products)

# 4. Create new list containing stock >= 15

high_stock = []

for i in stock:
    if i >= 15:
        high_stock.append(i)

print("Products with Stock >= 15:", high_stock)