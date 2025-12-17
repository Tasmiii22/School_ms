import os.path

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.data_file = f"{account_number}.txt"
        if not os.path.exists(self.data_file):
            with open(self.data_file, "w") as f:
                f.write("0")

    def deposit(self, amount):
        with open(self.data_file, "r") as f:
            balance = float(f.read())
        balance += amount
        with open(self.data_file, "w") as f:
            f.write(str(balance))
        print(f"Deposited {amount}. New balance: {balance}")

    def withdraw(self, amount):
        with open(self.data_file, "r") as f:
            balance = float(f.read())
        if balance >= amount:
            balance -= amount
            with open(self.data_file, "w") as f:
                f.write(str(balance))
            print(f"Withdrew {amount}. New balance: {balance}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        with open(self.data_file, "r") as f:
            balance = float(f.read())
        print(f"Current balance: {balance}")

def main():
    account_number = input("Enter account number: ")
    account = BankAccount(account_number)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#######################################

import os.path

def bank_operations():
    account_number = input("Enter account number: ")
    data_file = f"{account_number}.txt"

    if not os.path.exists(data_file):
        with open(data_file, "w") as f:
            f.write("0")

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            with open(data_file, "r+") as f:
                balance = float(f.read())
                balance += amount
                f.seek(0)
                f.write(str(balance))
                f.truncate()
            print(f"Deposited {amount}. New balance: {balance}")

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            with open(data_file, "r+") as f:
                balance = float(f.read())
                if balance >= amount:
                    balance -= amount
                    f.seek(0)
                    f.write(str(balance))
                    f.truncate()
                    print(f"Withdrew {amount}. New balance: {balance}")
                else:
                    print("Insufficient balance.")

        elif choice == "3":
            with open(data_file, "r") as f:
                balance = float(f.read())
            print(f"Current balance: {balance}")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    bank_operations()