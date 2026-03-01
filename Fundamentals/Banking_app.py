def show_menu():
    print("\n---- MENU ----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Choose: "))
    return choice


def check_balance(balance):
    print("Balance:", balance)


def deposit(balance, amount):
    if amount <= 0:
        print("Invalid amount")
        return balance
    else:
        return amount + balance

def withdraw(balance, amount):
    if amount <= 0 :
        print("Invalid")
        return balance
    elif amount > balance:
        print("Insufficient")
        return balance
    else:
        return balance - amount
    

balance = 100

pin = input("Set your 4-digit PIN: ")
while not pin.isdigit() and len(pin) == 4:
    print("Entered invalid pin, Please retry")
    pin = input("Set your 4-digit PIN: ")

# 2) Login (3 tries)
attempts = 3
while attempts > 0:
    entered = input("Enter PIN to login: ")
    if entered == pin:
        print("Login successful ")
        break
    else:
        attempts -= 1
        print("Wrong PIN. Attempts left:", attempts)

if attempts == 0:
    print("Account locked ")
else:
    # 3) Menu loop
    while True:
        choice = show_menu()

        if choice == 1:
            check_balance(balance)

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            balance = deposit(balance, amount)
            print("Balance:", balance)

        elif choice == 3:
            amount = int(input("Enter withdraw amount: "))
            balance = withdraw(balance, amount)
            print("Balance:", balance)

        elif choice == 4:
            print("Goodbye ")
            break

        else:
            print("Invalid choice ")