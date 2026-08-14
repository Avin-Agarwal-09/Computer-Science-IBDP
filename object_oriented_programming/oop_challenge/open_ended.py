class BankAccount:
    BankName = None
    AccCount = 0
    def __init__(self, AccNumber, FirstName, LastName, 
                 AccType, PIN):
        self.AccNumber = AccNumber
        self.FirstName = FirstName
        self.LastName = LastName
        self.AccType = AccType
        self._Balance = 0
        self.TransactionLog = []
        self.Frozen = False
        BankAccount.AccCount += 1
        self.Withdrawal_Limit = 100
        self.Withdrawn_Today =  0
        self.PIN = " "
    
    @property
    def get_balance(self):
            return self._Balance
    
    def new_day(self):
        self.Withdrawn_Today = 0
    
    def PIN(self, PIN):
        self.PIN = PIN
    
    def set_withdrawal_limit(self, limit):
        self.Withdrawal_Limit = limit

    def Freeze_Account(self):
        self.Frozen = True
    
    def deposit(self, amount):
        if self.Frozen:
            print("Account Frozen")
            return
        if amount < 0:
            print("Invalid amount")
            return
        self._Balance += amount
        self.TransactionLog += [f"Deposited: {amount}"]
    
    def withdraw(self, amount):
        if self.Frozen:
            print("Account Frozen")
            return
        check = input("Enter your PIN: ")
        if check != self.PIN:
            print("Incorrect pin. ")
            return
        if amount < 0 or amount > self._Balance:
            print("Invalid amount")
            return
        if  self.Withdrawn_Today > self.Withdrawal_Limit:
            print("Amount exceeds daily withdrawal limit")
            return
        self._Balance -= amount
        self.Withdrawn_Today += amount
        self.TransactionLog += [f"Withdrew: {amount}"]
    
    def interest(self, years):
        self._Balance += (self._Balance * 0.02) * years
        
    
    def SeeBalance(self):
        print(self._Balance)

    def PrintLog(self):
        for log in self.TransactionLog:
            print(log)

    def UpdateBank(name): 
        BankName = name

    def get_bank():
        return BankAccount.BankName
    
    def get_acc_count():
        return BankAccount.AccCount
    
    def __str__(self):
        return f'''Account Number: {self.AccNumber}
        Name: {self.FirstName} {self.LastName}
        AccType: {self.AccType}
        Balance: {self._balance}
                 '''

if __name__ == "__main__":
    acc1 = BankAccount("A123", "Julian", "Dizon", "Savings", "6767")
    acc2 = BankAccount("B123", "Avin", "Agarwal", "Checking", "8888")
    acc3 = BankAccount("C123", "Ryan", "Eng", "Investment", "0987")
    
    acc1.deposit(500)
    acc2.deposit(10)
    acc3.deposit(190)

    acc2.Freeze_Account()

    acc1.withdraw(200)
    acc2.withdraw(5)
    acc3.withdraw(150)

    acc1.SeeBalance()
    acc2.SeeBalance()
    acc3.SeeBalance()
    
    acc1.interest(2)
    acc2.interest(4)
    acc3.interest(3)

    acc1.SeeBalance()
    acc2.SeeBalance()
    acc3.SeeBalance()

    acc1.PrintLog()
    acc2.PrintLog()
    acc3.PrintLog()
    
    
    

