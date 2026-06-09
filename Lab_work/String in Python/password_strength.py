password = "Python@2026!"

# Counters
uppercase = 0
lowercase = 0
digits = 0
special = 0

# Lists
digit_list = []
special_list = []

# Checking each character
for ch in password:

    if ch.isupper():
        uppercase += 1

    elif ch.islower():
        lowercase += 1

    elif ch.isdigit():
        digits += 1
        digit_list.append(ch)

    else:
        special += 1
        special_list.append(ch)

# Password Strength Check
if (len(password) >= 8 and
    uppercase >= 1 and
    lowercase >= 1 and
    digits >= 1 and
    special >= 1):

    strength = "Strong"

elif len(password) >= 6:
    strength = "Medium"

else:
    strength = "Weak"

# Display Output
print("Password:", password)
print()

print("Uppercase Letters:", uppercase)
print("Lowercase Letters:", lowercase)
print("Digits:", digits)
print("Special Characters:", special)
print()

print("Digits Found:", digit_list)
print("Special Characters Found:", special_list)
print()

print("Password Strength:", strength)