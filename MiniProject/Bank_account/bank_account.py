#  Build a BankAccount Class
# - Attributes: balance, owner
# - Methods: deposit(), withdraw(), check_balance()
# - Add logic to prevent overdrawing


class Logger:
    def log(self, owner, action, amount, balance, filename="data.txt"):
        with open(filename, "a") as file:
            file.write(f"Owner: {owner}\n")
            file.write(f"Action: {action}\n")
            file.write(f"Amount: {amount}\n")
            file.write(f"Balance: {balance}\n\n")

class BankAccount:
    def __init__(self, owner, balance, logger):
        self.owner = owner
        self.balance = balance
        self.logger = logger
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} tk")
            self.logger.log(self.owner, "deposit", amount, self.balance)
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to make the withdrawal!")
        elif amount <= 0:
            print("You cannot withdraw zero or less than zero funds!")
        else:
            self.balance -= amount
            print(f"You have withdrawn {amount} tk.")
            self.logger.log(self.owner, "withdraw", amount, self.balance)
    
    def check_balance(self):
        print(f"Your current balance is {self.balance} tk")

    def __str__(self):
        return f"Account owner: {self.owner}, Current balance: {self.balance} tk"

# --- User Interaction ---
logger = Logger()
owner_name = input("What is your name: ")
initial_balance = float(input("What is your current account balance: "))
account = BankAccount(owner_name, initial_balance, logger)

while True:
    print("\nChoose any option from the list:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        amount = float(input("\nHow much do you want to deposit: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("\nHow much do you want to withdraw: "))
        account.withdraw(amount)
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        print(f"\n{account}")
        print("Thank you for using our service!")
        break
    else:
        print("\nInvalid choice. Choose between (1-4).")


    