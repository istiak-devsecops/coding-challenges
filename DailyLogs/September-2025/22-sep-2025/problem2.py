#  Build a BankAccount Class
# - Attributes: balance, owner
# - Methods: deposit(), withdraw(), check_balance()
# - Add logic to prevent overdrawing

class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited amount {amount} tk")
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
    
    def check_balance(self):
        print(f"Current balance is {self.balance}tk")

    def __str__(self):
        return f"{self.owner} has a balance of {self.balance}tk"


account1 = BankAccount(1000, "istiak")
print(account1)