name = "Rahul Sharma"

# 1. Remove spaces
username = name.replace(" ", "")

# 2. Convert to lowercase
username = username.lower()

# 3. Append current year
username = username + "2026"

# Store original generated username
full_username = username

# 4. If length exceeds 12, keep first 12 characters
if len(username) > 12:
    username = username[:12]

# 5 & 6. Count vowels and consonants
vowels = 0
consonants = 0

for ch in full_username:

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# 7. Display username statistics
print("Original Name:", name)
print()

print("Generated Username:", full_username)
print("Final Username:", username)
print()

print("Username Length:", len(full_username))
print("Vowels:", vowels)
print("Consonants:", consonants)
print()

print("Status: Username Generated Successfully")