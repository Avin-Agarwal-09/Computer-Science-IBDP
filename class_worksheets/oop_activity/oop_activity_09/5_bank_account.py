class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew {amount}. Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 500:
            print("Withdrawal denied. Limit is $500.")
        else:
            super().withdraw(amount)


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        super().withdraw(amount + 2)
        print("$2 transaction fee applied.")

savings = SavingsAccount(1000)
savings.withdraw(400)  
savings.withdraw(600)   

checking = CheckingAccount(1000)
checking.withdraw(100)