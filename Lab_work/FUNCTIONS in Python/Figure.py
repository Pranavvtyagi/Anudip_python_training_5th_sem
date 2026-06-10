import math

# --------- Circle Functions ---------
def circle_area(radius):
    return math.pi * radius * radius

def circle_perimeter(radius):
    return 2 * math.pi * radius


# --------- Rectangle Functions ---------
def rectangle_area(length, breadth):
    return length * breadth

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)


# --------- Square Functions ---------
def square_area(side):
    return side * side

def square_perimeter(side):
    return 4 * side


# --------- Circle Menu ---------
def circle_menu():

    radius = float(input("Enter radius of circle: "))

    while True:

        print("\n--- CIRCLE OPERATIONS ---")
        print("1. Area")
        print("2. Perimeter")
        print("3. Exit from Circle")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Area of Circle =", circle_area(radius))

        elif choice == 2:
            print("Perimeter of Circle =", circle_perimeter(radius))

        elif choice == 3:
            print("Exiting Circle Menu...")
            break

        else:
            print("Invalid Choice!")


# --------- Rectangle Menu ---------
def rectangle_menu():

    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    while True:

        print("\n--- RECTANGLE OPERATIONS ---")
        print("1. Area")
        print("2. Perimeter")
        print("3. Exit from Rectangle")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Area of Rectangle =", rectangle_area(length, breadth))

        elif choice == 2:
            print("Perimeter of Rectangle =", rectangle_perimeter(length, breadth))

        elif choice == 3:
            print("Exiting Rectangle Menu...")
            break

        else:
            print("Invalid Choice!")


# --------- Square Menu ---------
def square_menu():

    side = float(input("Enter side of square: "))

    while True:

        print("\n--- SQUARE OPERATIONS ---")
        print("1. Area")
        print("2. Perimeter")
        print("3. Exit from Square")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Area of Square =", square_area(side))

        elif choice == 2:
            print("Perimeter of Square =", square_perimeter(side))

        elif choice == 3:
            print("Exiting Square Menu...")
            break

        else:
            print("Invalid Choice!")


# --------- Main Program ---------
while True:

    print("\n====== 2D FIGURE MENU ======")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        circle_menu()

    elif choice == 2:
        rectangle_menu()

    elif choice == 3:
        square_menu()

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")