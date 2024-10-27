class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ${amount}. New balance: ${self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

def main():
    account_number = input("Enter your account number: ")
    account = BankAccount(account_number)

    while True:
        print("\nOptions:")
        print("a) Deposit money")
        print("b) Withdraw money")
        print("c) Check balance")
        print("d) Exit")
        choice = input("Choose an option: ").strip().lower()

        if choice == 'a':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 'b':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 'c':
            account.check_balance()
        elif choice == 'd':
            print("Thank you for using the bank system. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

# Run the main program
if __name__ == "__main__":
    main()
