text = "AAABBBCCCDDDAAA"

# 1 & 2. Count occurrences and create frequency dictionary
frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# 3. Display unique characters
unique_characters = list(frequency.keys())

# 4. Find most frequent character
most_frequent = max(frequency, key=frequency.get)

# 5. Create compressed output
compressed = ""

count = 1

for i in range(len(text) - 1):

    if text[i] == text[i + 1]:
        count += 1

    else:
        compressed += text[i] + str(count)
        count = 1

# Add last character group
compressed += text[-1] + str(count)

# 6. Calculate compression ratio
original_length = len(text)
compressed_length = len(compressed)

compression_ratio = compressed_length / original_length

# Display Output
print("Original Text:", text)
print()

print("Character Frequencies:")
for key, value in frequency.items():
    print(key, "->", value)

print()

print("Unique Characters:", unique_characters)
print()

print("Most Frequent Character:", most_frequent)
print()

print("Compressed Output:", compressed)
print()

print("Original Length:", original_length)
print("Compressed Length:", compressed_length)

print("Compression Ratio:", round(compression_ratio, 2))