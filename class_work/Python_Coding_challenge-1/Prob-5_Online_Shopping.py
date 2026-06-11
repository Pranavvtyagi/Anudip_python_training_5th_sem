'''Online Shopping Cart Analyzer 
Problem Statement :
The prices of products added to a shopping cart are stored below. 
Sample Data cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 
Tasks 
1. Calculate the total cart value.  
2. Find the most expensive and cheapest products.  
3. Count products eligible for premium shipping (price > ₹1000). 
4. Generate a discount list (products above ₹1500).  
5. Calculate the average product price.'''
#------------------------------------------------------------------------------------------------------------------
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]
# Calculate Total Cart Value
total_value = sum(cart)
#-------------------------------------------------------------------------------------------------------------------
# Find Most Expensive and Cheapest Products
most_expensive = max(cart)
cheapest = min(cart)
#-------------------------------------------------------------------------------------------------------------------
# Count Premium Shipping Eligible Products (price > 1000)
premium_count = 0
for price in cart:
    if price > 1000:
        premium_count += 1
#---------------------------------------------------------------------------------------------------------------------
# Generate Discount Eligible Products (price > 1500)
discount_products = []
for price in cart:
    if price > 1500:
        discount_products.append(price)
#--------------------------------------------------------------------------------------------------------------------  
# Calculate Average Product Price
average_price = total_value / len(cart)
#------------------------------------------------------------------------------------------------------------------
# Display Results
print("Total Cart Value: ₹", total_value)
print("Most Expensive Product: ₹", most_expensive)
print("Cheapest Product: ₹", cheapest)
print("Premium Shipping Eligible Products:", premium_count)
print("Discount Eligible Products:", discount_products)
print("Average Product Price: ₹", average_price)