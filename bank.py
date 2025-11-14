import os

def deposit():
    acc = int(input("Enter account no: "))
    password = input("Enter password: ")
    name = input("Enter Name of Account Holder: ")
    amt = input("Enter how much money you want to deposit: ")

    with open("Bank.txt", "a") as f:
        f.write(f"{acc},{name},{amt},{password}\n")
    print("\nAmount Deposited Successfully!\n")


def withdrawal():
    acc_no = int(input("Enter account no: "))
    pass_word = input("Enter password: ")
    money =int(input("Enter amount to withdraw: "))

    if not os.path.exists("Bank.txt"):
        print("\nNo data found.")
        return

    with open("Bank.txt", "r") as f:
        lines = f.readlines()

    found = False
    with open("Bank.txt", "w") as f:
        for line in lines:
            acc,name,amt,pasword=line.strip().split(",")
            if acc==acc_no and pasword==pass_word:
                found=True
                
                if money > amt:
                    print("\nInsufficient balance!")
                else:
                    amt -= money
                    print(f"\n₹{money} withdrawn successfully.")
                    print(f"Your current balance is ₹{amt}.")
                f.write(f"{acc},{name},{amt},{pasword}\n")
            else:
                f.write(line)

    if not found:
        print("\nAccount not found or wrong password.\n")


def check_balance():
    acc_no = input("Enter account no: ")
    pass_word = input("Enter password: ")

    if not os.path.exists("Bank.txt"):
        print("\nNo data found.")
        return

    with open("Bank.txt", "r") as f:
        lines = f.readlines()

    found = False
    for line in lines:
        acc,name,amt,pasword=line.strip().split(",")
        if acc==acc_no and pasword==pass_word:
            found = True
            print(f"\nAccount Holder: {name}")
            print(f"Available Balance: ₹{amt}\n")
            break

    if not found:
        print("\nAccount not found or wrong password.\n")


def main():
    while True:
        print("----------- ACCOUNT MENU ------------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        ch = input("Enter your choice: ")

        if ch == "1":
            deposit()
        elif ch == "2":
            withdrawal()
        elif ch == "3":
            check_balance()
        elif ch == "4":
            print("-x-x-x-x-x- THANK YOU -x-x-x-x-x-")
            break
        else:
            print("Invalid Input\n")


if __name__ == "__main__":
    main()
