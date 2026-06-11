'''Mobile Contact Directory System Problem Statement Contacts are stored in contacts.txt. 
File Format 
Anuj,9876543210 
Rahul,9876543211 
Priya,9876543212 
Neha,9876543213 
Amit,9876543214 
Sneha,9876543215 
Karan,9876543216 
Pooja,9876543217 
Rohit,9876543218 
Anjali,9876543219 
Requirements Create a menu-driven application to: 
1. Display all contacts.  
2. Search a contact by name.  
3. Add a new contact.  
4. Update an existing contact number.  
5. Delete a contact.  
6. Display contacts whose names start with a vowel.  
7. Save all modifications back to the file. '''

def display_contacts():
    file = open("contacts.txt", "r")

    print("\nContact List")
    print("-" * 30)

    for line in file:
        print(line.strip())

    file.close()


def search_contact(name):
    file = open("contacts.txt", "r")

    found = False

    for line in file:
        cname, number = line.strip().split(",")

        if cname.lower() == name.lower():
            print("\nContact Found")
            print("Name   :", cname)
            print("Number :", number)
            found = True
            break

    if not found:
        print("Contact not found.")

    file.close()


def add_contact():
    name = input("Enter Name: ")
    number = input("Enter Mobile Number: ")

    file = open("contacts.txt", "a")
    file.write(f"\n{name},{number}")
    file.close()

    print("Contact Added Successfully.")


def update_contact():
    name = input("Enter Contact Name: ")

    file = open("contacts.txt", "r")
    contacts = []
    found = False

    for line in file:
        cname, number = line.strip().split(",")

        if cname.lower() == name.lower():
            new_number = input("Enter New Number: ")
            contacts.append(f"{cname},{new_number}\n")
            found = True
        else:
            contacts.append(line)

    file.close()

    file = open("contacts.txt", "w")
    file.writelines(contacts)
    file.close()

    if found:
        print("Contact Updated Successfully.")
    else:
        print("Contact Not Found.")


def delete_contact():
    name = input("Enter Contact Name to Delete: ")

    file = open("contacts.txt", "r")
    contacts = []
    found = False

    for line in file:
        cname, number = line.strip().split(",")

        if cname.lower() == name.lower():
            found = True
        else:
            contacts.append(line)

    file.close()

    file = open("contacts.txt", "w")
    file.writelines(contacts)
    file.close()

    if found:
        print("Contact Deleted Successfully.")
    else:
        print("Contact Not Found.")


def vowel_contacts():
    file = open("contacts.txt", "r")

    print("\nContacts Starting with Vowel")
    print("-" * 30)

    vowels = "AEIOUaeiou"

    for line in file:
        cname, number = line.strip().split(",")

        if cname[0] in vowels:
            print(cname, number)

    file.close()


# Menu Driven Program
while True:
    print("\n===== MOBILE CONTACT DIRECTORY =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add New Contact")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. Display Contacts Starting with Vowel")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_contacts()

    elif choice == 2:
        name = input("Enter Name: ")
        search_contact(name)

    elif choice == 3:
        add_contact()

    elif choice == 4:
        update_contact()

    elif choice == 5:
        delete_contact()

    elif choice == 6:
        vowel_contacts()

    elif choice == 7:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")