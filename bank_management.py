# bank_management.py

class BankAccount:
    def __init__(self, account_number, name):
        self.account_number = account_number
        self.name = name
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")


class BankManagementSystem:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1

    def create_account(self, name):
        account_number = self.next_account_number
        new_account = BankAccount(account_number, name)
        self.accounts[account_number] = new_account
        self.next_account_number += 1
        print(f"Account created successfully! Account Number: {account_number}")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def view_account(self, account_number):
        account = self.get_account(account_number)
        if account:
            account.display_account_info()
        else:
            print("Account not found!")

    def deposit_money(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found!")

    def withdraw_money(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found!")

    def menu(self):
        print("\nBank Management System")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter account holder's name: ")
                self.create_account(name)
            elif choice == "2":
                account_number = int(input("Enter account number: "))
                self.view_account(account_number)
            elif choice == "3":
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter amount to deposit: "))
                self.deposit_money(account_number, amount)
            elif choice == "4":
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw_money(account_number, amount)
            elif choice == "5":
                print("Exiting... Thank you for using the Bank Management System.")
                break
            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    bms = BankManagementSystem()
    bms.run()
