class BankAccount:
    def __init__(self,name):
        self.name = name 
        self.balance = 0.0 

    def deposit (self, amount) :
        if amount > 0:
            self.balance = self.balance + amount

    def withdraw (self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            self.balance = 0

    def transfer (self,amount,recipient):
        if self.balance >= amount:
            self.withdraw (amount)
            recipient.deposit(amount)
        else:
            initial = self.balance
            self.withdraw(self.balance)
            recipient.deposit(initial)

    def get_balance(self):
        return self.balance

    def __str__ (self) :
        return f"Account {self.name} has balance ${self. balance}"
    

amy = BankAccount ("Amy") 
brian = BankAccount ("Brian") 
clare = BankAccount ("Clare")

amy.deposit (100) 
brian.deposit(100) 
clare.deposit(150)
amy.withdraw(75) 
brian.deposit(75) 
brian.transfer(250,clare)

print (amy)
print (brian)
print (clare)

print(amy.get_balance())
print(brian.get_balance())
print(clare.get_balance())