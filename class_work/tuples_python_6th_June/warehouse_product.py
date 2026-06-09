products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

passed = 0
failed = 0
failure_count = 0

print("Failed Product IDs:")

for product_id, status in products:
    
    if status == "Fail":
        print(product_id)
        failed += 1
        failure_count += 1
    else:
        passed += 1

    # Stop checking if 3 failures are found
    if failure_count == 3:
        print("3 failures found. Stopping inspection.")
        break

# Calculate pass percentage
total_products = passed + failed
pass_percentage = (passed / total_products) * 100

print("\nPassed Products:", passed)
print("Failed Products:", failed)
print("Pass Percentage:", pass_percentage, "%")