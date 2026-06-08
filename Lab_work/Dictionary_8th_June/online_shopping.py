sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Display products sold more than 20 times
print("Products Sold More Than 20 Times:")

for product, quantity in sales.items():
    if quantity > 20:
        print(product)

# 2. Find the best-selling product
best_product = max(sales, key=sales.get)

print("\nBest Selling Product:", best_product, "(", sales[best_product], ")", sep="")

# 3. Find the least-selling product
least_product = min(sales, key=sales.get)

print("Least Selling Product:", least_product, "(", sales[least_product], ")", sep="")

# 4. Calculate total products sold
total_sales = sum(sales.values())

print("Total Units Sold:", total_sales)

# 5. Create a list of products requiring promotion
promotion_products = []

for product, quantity in sales.items():
    if quantity < 15:
        promotion_products.append(product)

print("Products Requiring Promotion:", promotion_products)

# 6. Count products having sales between 10 and 30
count = 0

for quantity in sales.values():
    if 10 <= quantity <= 30:
        count += 1

print("Products Having Sales Between 10 and 30:", count)