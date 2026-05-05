class Account:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self,value):
        if value >= 0:
            self.balance += value
        else:
            return "try withdrawing instead"
    
    def withdraw(self,value):
        if 0<=value<=self.balance:
            self.balance -= value
        else:
            print("not enough balance")
        

class SavingsAccount(Account):
    def __init__(self,account_number,balance,interest_rate):
        super().__init__(account_number,balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        self.balance *=  (1+self.interest_rate)

class PremiumSavingsAccount(SavingsAccount):
    def __init__(self,account_number,balance,interest_rate,bonus_rate):
        super().__init__(account_number,balance,interest_rate)
        self.bonus_rate = bonus_rate
    
    def apply_interest(self):
        self.balance *= (1+self.interest_rate+self.bonus_rate)

a1 = SavingsAccount("S1", 1000, 0.05)
a1.apply_interest()
print(round(a1.balance,2))   # 1050.00

a2 = PremiumSavingsAccount("P1", 1000, 0.05, 0.02)
a2.apply_interest()
print(round(a2.balance,2))   # 1070.00

a2.withdraw(-200)
print(round(a2.balance,2))   # 870.00