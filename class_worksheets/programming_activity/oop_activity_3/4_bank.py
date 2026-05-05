class Account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def __str__(self):
        return f"{self.name} | {self.account_number} | Balance: ${self.balance}"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                self.accounts.remove(acc)

    def deposit(self, account_number, amount):
        for acc in self.accounts:
            if acc.account_number == account_number:
                acc.deposit(amount)

    def withdraw(self, account_number, amount):
        for acc in self.accounts:
            if acc.account_number == account_number:
                acc.withdraw(amount)



bank = Bank()

a1 = Account("Alice", 101, 500)
a2 = Account("Bob", 102, 300)

bank.add_account(a1)
bank.add_account(a2)

bank.deposit(101, 200)
bank.withdraw(102, 100)

for acc in bank.accounts:
    print(acc)
