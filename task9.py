class BankAccount:
    def __init__(self):
        self.name = ""
        self.balance = 0
        self.address = ""
        self.account_number = 0

    def create_account(self):
        self.name = input("Enter Account Holder's Name: ")
        self.balance = int(input("Enter Initial Deposit Amount: "))
        self.address = input("Enter Address: ")
        self.account_number = int(input("Enter Account Number: "))

    def display_account_details(self):
        print("\n------Account Details------")
        print(f"Account Holder's Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")

    def deposit_amount(self):
        deposit = int(input("Enter the amount to deposit: "))
        if deposit > 0:
            self.balance += deposit
            print(f"Deposited {deposit}. Updated Balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw_amount(self):
        withdrawal = int(input("Enter the amount to withdraw: "))
        if 0 < withdrawal <= self.balance:
            self.balance -= withdrawal
            print(f"Withdrew {withdrawal}. Updated Balance: {self.balance}")
        elif withdrawal > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Available Balance: {self.balance}")


def main():
    account = BankAccount()
    print("Initialize Your Account:")
    account.create_account()

    while True:
        print("\n------Menu------")
        print("1. View Account Details")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        user_choice = int(input("Choose an option: "))

        if user_choice == 1:
            account.display_account_details()
        elif user_choice == 2:
            account.deposit_amount()
        elif user_choice == 3:
            account.withdraw_amount()
        elif user_choice == 4:
            account.check_balance()
        elif user_choice == 5:
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
