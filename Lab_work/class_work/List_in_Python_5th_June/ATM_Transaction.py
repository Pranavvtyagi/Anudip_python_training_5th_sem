# List of transactions
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# 1. Calculate current balance

balance = 0

for i in transactions:
    balance += i

print("Current Balance:", balance)

# 2. Count total deposits and withdrawals

deposit_count = 0
withdrawal_count = 0

for i in transactions:
    if i > 0:
        deposit_count += 1
    else:
        withdrawal_count += 1

print("Total Deposits:", deposit_count)
print("Total Withdrawals:", withdrawal_count)

# 3. Find largest deposit and largest withdrawal

largest_deposit = transactions[0]
largest_withdrawal = transactions[0]

for i in transactions:

    # Largest Deposit
    if i > 0 and i > largest_deposit:
        largest_deposit = i

    # Largest Withdrawal
    if i < 0 and i < largest_withdrawal:
        largest_withdrawal = i

print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)

# 4. Create separate lists for deposits and withdrawals

deposits = []
withdrawals = []

for i in transactions:
    if i > 0:
        deposits.append(i)
    else:
        withdrawals.append(i)

print("Deposits List:", deposits)
print("Withdrawals List:", withdrawals)