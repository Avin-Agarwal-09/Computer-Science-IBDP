class Accounts:
    def __init__(self, AccNum, First, Last):
        self.BankID = "JBB244"
        self.AccNum = AccNum
        self.First = First
        self.Last = Last
        self.__Balance = 0.00

    def Deposit(self, amount):
        if type(amount) != float:
            print("Amount must be a float.")
        elif amount < 0:
            print("Cannot deposit a negative amount.")
        else:
            self.__Balance += amount
            print("Deposit successful.")

    def WithDraw(self, amount):
        if type(amount) != float:
            print("Amount must be a float.")
        elif amount < 0:
            print("Cannot withdraw a negative amount.")
        elif amount > self.__Balance:
            print("Insufficient funds.")
        else:
            self.__Balance -= amount
            print("Withdrawal successful.")

    def SeeBalance(self):
        print("Current balance:", self.__Balance)


acc1 = Accounts("40001", "Julian", "Good")

amount = float(input("Enter deposit amount: "))
acc1.Deposit(amount)
acc1.SeeBalance()

withdraw_amount = float(input("Enter withdrawal amount: "))
acc1.WithDraw(withdraw_amount)
acc1.SeeBalance()