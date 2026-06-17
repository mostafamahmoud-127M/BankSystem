import json
import os

savedFile = "savingFile.json"


class bankAcc:
    def __init__(self, uname, balance=0, trans=None, password=None):
        self.uname = uname
        self.balance = float(balance)
        self.trans = trans if trans is not None else []
        self.password = password

    def deposit(self, amount):
        self.balance += float(amount)
        self.trans.append(f"{amount} is added successfully")
        print(f"{amount} is added successfully")
        self.saveToFile()

    def withdraw(self, wamount):
        wamount = float(wamount)
        if wamount <= self.balance:
            self.balance -= wamount
            self.trans.append(f"{wamount} is taken")
            print(f"You withdrew {wamount} from your account.")
            self.saveToFile()
        else:
            print("mafesh floos (Insufficient funds)")

    def check_balance(self):
        print(f"Your current balance is {self.balance}")
        return self.balance

    def saveToFile(self):
        try:
            data = {
                'uname': self.uname,
                'balance': self.balance,
                'trans': self.trans,
                'pass': self.password
            }
            with open(savedFile, "w") as sav:
                json.dump(data, sav, indent=5)
            print("[File Updated Automatically]")
        except Exception as e:
            print("The account cannot be saved:", e)

    def loadFromFile(self):
        try:
            with open(savedFile, "r") as lod:
                data = json.load(lod)
                self.uname = data["uname"]
                self.balance = float(data["balance"])
                self.trans = data["trans"]
                self.password = data.get("pass", None)
        except Exception as e:
            print("Error loading account:", e)


def main():
    print("--- Welcome to the Bank ---")
    username = input("Enter your username: ")

    # Check if a saved file exists
    file_exists = os.path.exists(savedFile)
    is_existing_user = False

    if file_exists:
        # Peek into the file to check if the username matches
        with open(savedFile, "r") as lod:
            try:
                data = json.load(lod)
                if data.get("uname") == username:
                    is_existing_user = True
                    saved_password = data.get("pass")
            except Exception:
                pass  # If file is corrupted, treat as new

    # Create the account instance
    acc = bankAcc(username)

    if is_existing_user:
        # Existing User Logic
        print(f"Welcome back, {username}!")
        attempts = 3
        while attempts > 0:
            entered_pass = input("Enter your password: ")
            if entered_pass == saved_password:
                acc.loadFromFile()  # Successfully load the data
                print("Login successful.")
                break
            else:
                attempts -= 1
                print(f"Incorrect password. Attempts remaining: {attempts}")
        else:
            print("Too many incorrect attempts. Exiting program.")
            return 0
    else:
        # New User Logic
        print(f"Username '{username}' not found. Let's create a new account.")
        new_password = input("Create a new password: ")
        try:
            starting_bal = float(input("Enter your initial deposit/balance: "))
        except ValueError:
            print("Invalid balance amount. Defaulting to 0.")
            starting_bal = 0.0

        acc.balance = starting_bal
        acc.password = new_password
        acc.saveToFile()
        print("Account created successfully!")

    # Main application loop
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            dep = input("Enter the amount you want to deposit: ")
            acc.deposit(dep)
        elif choice == 2:
            am = input("Enter the amount you want to withdraw: ")
            acc.withdraw(am)
        elif choice == 3:
            acc.check_balance()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


main()