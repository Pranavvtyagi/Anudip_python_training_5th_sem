# ATM Simulation System

balance = 10000

while True:

    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Check Balance
    if choice == 1:
        print("Current Balance = ₹", balance)

    # Deposit Money
    elif choice == 2:
        amount = int(input("Enter amount to deposit: ₹"))

        balance = balance + amount

        print("Amount Deposited Successfully")
        print("Updated Balance = ₹", balance)

    # Withdraw Money
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: ₹"))

        if amount <= balance:
            balance = balance - amount

            print("Withdrawal Successful")
            print("Remaining Balance = ₹", balance)

        else:
            print("Insufficient Balance")

    # Exit
    elif choice == 4:
        print("Thank You for Using ATM")
        break

    # Invalid Choice
    else:
        print("Invalid Choice! Please try again.")
