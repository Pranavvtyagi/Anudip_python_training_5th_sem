'''Library Book Issue System 
Problem Statement A library stores book information in books.txt. 
File Format B101,Python Basics,5 
B102,Java Programming,2 
B103,Data Science,0 
B104,DBMS,3 
B105,Machine Learning,1 
B106,Operating Systems,4 
B107,Networking,2 
B108,Cyber Security,6 
B109,Cloud Computing,0 
B110,Web Development,3 
Requirements Develop a program to: 
1. Display all books.  
2. Search a book using Book ID.  
3. Issue a book (decrease quantity by 1).  
4. Return a book (increase quantity by 1).  
5. Display unavailable books.  
6. Display books requiring restocking (copies < 2).  
7. Update the file after every issue/return operation.  '''

def display_books():
    file = open("books.txt", "r")

    print("\nBook Records")
    print("-" * 30)

    for line in file:
        print(line.strip())

    file.close()


def search_book(book_id):
    file = open("books.txt", "r")

    found = False

    for line in file:
        bid, title, qty = line.strip().split(",")

        if bid == book_id:
            print("\nBook Found")
            print("Book ID :", bid)
            print("Title   :", title)
            print("Quantity:", qty)
            found = True
            break

    if not found:
        print("Book not found.")

    file.close()


def issue_book(book_id):
    file = open("books.txt", "r")
    books = []

    for line in file:
        bid, title, qty = line.strip().split(",")

        if bid == book_id:
            qty = int(qty)

            if qty > 0:
                qty -= 1
                print("Book Issued Successfully.")
            else:
                print("Book Not Available.")

        books.append(f"{bid},{title},{qty}\n")

    file.close()

    file = open("books.txt", "w")
    file.writelines(books)
    file.close()


def return_book(book_id):
    file = open("books.txt", "r")
    books = []

    for line in file:
        bid, title, qty = line.strip().split(",")

        if bid == book_id:
            qty = int(qty) + 1
            print("Book Returned Successfully.")

        books.append(f"{bid},{title},{qty}\n")

    file.close()

    file = open("books.txt", "w")
    file.writelines(books)
    file.close()


def unavailable_books():
    file = open("books.txt", "r")

    print("\nUnavailable Books")
    print("-" * 30)

    for line in file:
        bid, title, qty = line.strip().split(",")

        if int(qty) == 0:
            print(bid, title)

    file.close()


def restocking_books():
    file = open("books.txt", "r")

    print("\nBooks Requiring Restocking")
    print("-" * 30)

    for line in file:
        bid, title, qty = line.strip().split(",")

        if int(qty) < 2:
            print(bid, title, qty)

    file.close()


# Main Menu
while True:
    print("\n===== LIBRARY BOOK ISSUE SYSTEM =====")
    print("1. Display All Books")
    print("2. Search Book by ID")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_books()

    elif choice == 2:
        book_id = input("Enter Book ID: ")
        search_book(book_id)

    elif choice == 3:
        book_id = input("Enter Book ID to Issue: ")
        issue_book(book_id)

    elif choice == 4:
        book_id = input("Enter Book ID to Return: ")
        return_book(book_id)

    elif choice == 5:
        unavailable_books()

    elif choice == 6:
        restocking_books()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")