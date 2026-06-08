books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# Display unavailable books
print("Unavailable Books:")
for book, copies in books:
    if copies == 0:
        print(book)

# Find books with more than 2 copies
print("\nBooks with more than 2 copies:")
for book, copies in books:
    if copies > 2:
        print(book)

# Count available books
count = 0
for book, copies in books:
    if copies > 0:
        count += 1

print("\nNumber of available books:", count)

# Stop searching once requested book is found
requested_book = "Java Programming"

print("\nSearching for requested book...")
for book, copies in books:
    if book == requested_book:
        print(requested_book, "found in library.")
        break