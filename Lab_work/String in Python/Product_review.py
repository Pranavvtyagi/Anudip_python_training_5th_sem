review = "This product is excellent excellent excellent and very useful"

# Convert review into list of words
words = review.split()

# 1. Count total words
total_words = len(words)

# 2. Create dictionary of word frequencies
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# 3. Find most frequently used word
most_frequent = max(frequency, key=frequency.get)

# 4. Find words appearing only once
single_words = []

for word in frequency:
    if frequency[word] == 1:
        single_words.append(word)

# 5. Count words having more than 5 characters
count_long_words = 0

for word in words:
    if len(word) > 5:
        count_long_words += 1

# 6. Display words in reverse order
reverse_words = words[::-1]

# 7. Create list of unique words
unique_words = list(frequency.keys())

# Display Output
print("Total Words:", total_words)
print()

print("Word Frequencies:")
for word, count in frequency.items():
    print(word, "->", count)

print()

print("Most Frequent Word:", most_frequent)
print()

print("Words Appearing Once:", single_words)
print()

print("Words Having More Than 5 Characters:", count_long_words)
print()

print("Words in Reverse Order:", reverse_words)
print()

print("Unique Words:", unique_words)