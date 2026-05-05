class BankAccount:
    BankName = None
    AccCount = 0
    def __init__(self, AccNumber, FirstName, LastName, 
                 AccType):
        self.AccNumber = AccNumber
        self.FirstName = FirstName
        self.LastName = LastName
        self.AccType = AccType
        self._Balance = 0
        self.TransactionLog = []
        BankAccount.AccCount += 1
    
    @property
    def get_balance(self):
            return self._Balance
    
    def deposit(self, amount):
        if amount < 0:
            print("Invalid amount")
            return
        self.__Balance += amount
        self.TransactionLog += [f"Deposited: {amount}"]
    
    def withdraw(self, amount):
        if amount < 0 or amount > self._Balance:
            print("Invalid amount")
            return
        self._Balance -= amount
        self.TransactionLog += [f"Withdrew: {amount}"]
    
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

if __name__ == "__main__":
    acc1 = BankAccount("A123", "Julian", "Dizon", "Savings")
    acc2 = BankAccount("B123", "Avin", "Agarwal", "Checking")
    acc3 = BankAccount("C123", "Ryan", "Eng", "Investment")
    
    acc1.deposit(500)
    acc2.deposit(10)
    acc3.deposit(190)

    acc1.withdraw(200)
    acc2.withdraw(5)
    acc3.withdraw(150)

    acc1.SeeBalance()
    acc1.PrintLog()
    
    acc2.SeeBalance()
    acc2.PrintLog()

    acc3.SeeBalance()
    acc3.PrintLog()

