#  Build a BankAccount Class
# - Attributes: balance, owner
# - Methods: deposit(), withdraw(), check_balance()
# - Add logic to prevent overdrawing

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited amount {amount} tk")
            self.transaction_log("deposit", amount)
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficent funds to initiate the transaction.")
        elif amount <= 0:
            print("withdraw amount must be more than 1tk")
        else:
            self.balance -= amount
            print(f"Your withdraw of {amount}tk has been initiated.")
            self.transaction_log("withdraw", amount)
    
    def check_balance(self):
        print(f"\nCurrent balance is {self.balance}tk")

    def __str__(self):
        return f"{self.owner} has a balance of {self.balance}tk"

    def transaction_log(self, action, amount, filename="data.txt"):
        with open(filename, "a") as file:
            file.write(f"Owner: {self.owner}\n")
            file.write(f"Action: {action}\n")
            file.write(f"Amount: {amount}\n")
            file.write(f"Balance: {self.balance}\n")
            file.write("\n")  # Add newline for better redability

# user interaction

owner_name = input("What is your name: ")
initial_balance = float(input("What is your current account balance: "))
account = BankAccount(owner_name, initial_balance)

while True:
    print("\nchooose any option from the list: ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option from (1-4): ")  # user choose what to do with the program

    if choice == "1":
        amount = float(input("\nHow much you wants to deposit: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("\nHow much do you wants to withdraw: "))
        account.withdraw(amount)
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        print("\nThank you for using our service!")
        break
    else:
        print("\nInvalid choice. Choose (1-4)")

    