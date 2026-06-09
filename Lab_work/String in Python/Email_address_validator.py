email = "rahul.sharma2026@gmail.com"

# 1. Extract username
username = email.split("@")[0]

# 2. Extract domain name
domain = email.split("@")[1].split(".")[0]

# 3. Extract extension
extension = email.split(".")[-1]

# 4. Count digits in username
digit_count = 0

for ch in username:
    if ch.isdigit():
        digit_count += 1

# 5. Count special characters
special_count = 0
special_chars = []

for ch in email:
    if not ch.isalnum():
        special_count += 1
        special_chars.append(ch)

# 6. Validate email
condition1 = email.count("@") == 1

# Check if '.' exists after '@'
after_at = email.split("@")[1]

condition2 = "." in after_at

if condition1 and condition2:
    status = "Valid"
else:
    status = "Invalid"

# Display Output
print("Email:", email)
print()

print("Username:", username)
print("Domain:", domain)
print("Extension:", extension)
print()

print("Digits Found:", digit_count)
print("Special Characters Found:", special_count)
print()

print("Special Characters List:", special_chars)
print()

print("Email Status:", status)