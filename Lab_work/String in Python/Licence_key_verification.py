license_key = "ABCD-EFGH-IJKL-MNOP"

# 1. Create list of groups
groups = license_key.split("-")

# Verify number of groups
group_count = len(groups)

# 2. Verify each group has exactly 4 characters
valid_groups = True

for group in groups:
    if len(group) != 4:
        valid_groups = False

# 3. Count total letters
total_letters = 0

for ch in license_key:
    if ch.isalpha():
        total_letters += 1

# 4. Count vowels
vowel_count = 0

for ch in license_key.lower():
    if ch in "aeiou":
        vowel_count += 1

# 5. Remove hyphens
merged_key = license_key.replace("-", "")

# 6. Groups list already created above

# 7. Check overall validity
if group_count == 4 and valid_groups:
    status = "Valid"
else:
    status = "Invalid"

# Display Output
print("License Key:", license_key)
print()

print("Groups:", groups)
print("Number of Groups:", group_count)
print()

print("Total Letters:", total_letters)
print("Total Vowels:", vowel_count)
print()

print("Merged Key:", merged_key)
print()

print("License Key Status:", status)