message = "Python is awesome and Python is easy to learn"

# 1. Count total characters
total_characters = len(message)

# 2. Count total words
words = message.split()
total_words = len(words)

# 3. Find longest word
longest_word = max(words, key=len)

# 4. Find shortest word
shortest_word = min(words, key=len)

# 5. Count occurrences of "Python"
python_count = words.count("Python")

# 6. Words having more than 4 characters
long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

# 7. Words starting with a vowel
vowel_words = []

for word in words:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

# 8. Count vowels and consonants
vowels = 0
consonants = 0

for ch in message.lower():

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Display Output
print("Message:", message)
print()

print("Total Characters:", total_characters)
print("Total Words:", total_words)
print()

print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print()

print("Occurrences of Python:", python_count)
print()

print("Words Longer Than 4 Characters:", long_words)
print("Words Starting With Vowels:", vowel_words)
print()

print("Vowels:", vowels)
print("Consonants:", consonants)