def withdraw(balance,amount):
    if amount > balance:
        print("Insufficient Balance")
        return balance
    else:
        return balance - amount
        
balance = 100

while True:
    amount = int(input("Enter amount (0 to stop): "))
    
    if amount == 0:
        print("Goodbye!")
        break
    
    balance = withdraw(balance, amount)
    print("Remaining balance:", balance)

