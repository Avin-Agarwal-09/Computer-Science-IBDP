class Transaction:
    next_id = 1

    def __init__(self, amount, transaction_type, description=""):
        self.transaction_id = Transaction.next_id
        Transaction.next_id += 1
        self.amount = amount
        self.type = transaction_type
        self.description = description

    def __str__(self):
        details = f" - {self.description}" if self.description else ""
        return f"{self.transaction_id} | {self.type} | {self.amount}{details}"


class BankAccount:
    BankName = None
    AccCount = 0

    def __init__(self, AccNumber, FirstName, LastName, AccType):
        self.AccNumber = AccNumber
        self.FirstName = FirstName
        self.LastName = LastName
        self.AccType = AccType
        self._Balance = 0
        self.TransactionLog = []
        self._transactions = []
        BankAccount.AccCount += 1

    @property
    def get_balance(self):
        return self._Balance

    def deposit(self, amount):
        if amount < 0:
            print("Invalid amount")
            return
        self._Balance += amount
        self._transactions.append(Transaction(amount, "DEPOSIT"))
        self.TransactionLog.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount < 0 or amount > self._Balance:
            print("Invalid amount")
            return
        self._Balance -= amount
        self._transactions.append(Transaction(amount, "WITHDRAWAL"))
        self.TransactionLog.append(f"Withdrew: {amount}")

    def get_transactions(self):
        return self._transactions.copy()

    def print_transaction_history(self):
        for transaction in self._transactions:
            print(transaction)

    def SeeBalance(self):
        print(self._Balance)

    def PrintLog(self):
        for log in self.TransactionLog:
            print(log)

    @staticmethod
    def UpdateBank(name):
        BankAccount.BankName = name

    @staticmethod
    def get_bank():
        return BankAccount.BankName

    @staticmethod
    def get_acc_count():
        return BankAccount.AccCount


class SalaryAccount(BankAccount):
    def __init__(self, AccNumber, FirstName, LastName, salary=0):
        super().__init__(AccNumber, FirstName, LastName, "Salary")
        self.salary = salary

    def deposit_salary(self, amount):
        self.deposit(amount)
        self.TransactionLog[-1] = f"Salary deposited: {amount}"


class FixedDepositAccount(BankAccount):
    def __init__(self, AccNumber, FirstName, LastName, principal, interest_rate, years):
        super().__init__(AccNumber, FirstName, LastName, "FixedDeposit")
        self.principal = principal
        self.interest_rate = interest_rate
        self.years = years
        self.is_matured = False
        self._Balance = principal

    def calculate_maturity_amount(self):
        return self.principal * (1 + self.interest_rate / 100) ** self.years

    def withdraw(self, amount):
        if not self.is_matured:
            print("Cannot withdraw before maturity")
            return
        super().withdraw(amount)


class AccountFactory:
    def create(account_type, account_number, first_name, last_name, amount=0, interest_rate=0, years=0):

        if account_type == "salary":
            return SalaryAccount(account_number, first_name, last_name, amount)
        elif account_type == "fixed":
            return FixedDepositAccount(
                account_number,
                first_name,
                last_name,
                amount,
                interest_rate,
                years,
            )
        elif account_type in ["savings", "checking", "investment"]:
            return BankAccount(account_number, first_name, last_name, account_type)
        else:
            return None


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.AccNumber == account_number:
                return account
        return None

    def total_funds(self):
        return sum(account.get_balance for account in self.accounts)

    def print_all_accounts(self):
        for account in self.accounts:
            print(account.AccNumber, account.FirstName, account.LastName, account.get_balance)


if __name__ == "__main__":
    acc1 = AccountFactory.create("savings", "A123", "Julian", "Dizon")
    acc2 = AccountFactory.create("checking", "B123", "Avin", "Agarwal")
    acc3 = AccountFactory.create("investment", "C123", "Ryan", "Eng")
    acc4 = AccountFactory.create("fixed", "D123", "Rayed", "Sidiqui", 500, 5, 2)
    acc5 = AccountFactory.create("salary", "E123", "Kenzo", "Geier", 3000)

    accounts: list[BankAccount] = [acc1, acc2, acc3, acc4, acc5]

    bank = Bank()
    for account in accounts:
        bank.add_account(account)

    acc1.deposit(500)
    acc2.deposit(10)
    acc3.deposit(190)
    acc4.deposit(500)
    acc5.deposit_salary(1000)

    acc1.withdraw(200)
    acc2.withdraw(5)
    acc3.withdraw(150)
    acc4.withdraw(20)

    print("Polymorphic withdrawals:")
    for account in accounts:
        print(account.AccType, end=": ")
        account.withdraw(20)

    acc1.SeeBalance()
    acc1.PrintLog()

    acc2.SeeBalance()
    acc2.PrintLog()

    acc3.SeeBalance()
    acc3.PrintLog()

    acc4.SeeBalance()
    acc4.PrintLog()

    print("Bank name:", BankAccount.get_bank())
    BankAccount.UpdateBank("Chase")
    print("Bank name after update:", BankAccount.get_bank())
    print("Total accounts:", BankAccount.get_acc_count())
    print("Bank total funds:", bank.total_funds())
    print("Found account:", bank.find_account("A123").FirstName)
    print("Transaction history for acc1:")
    acc1.print_transaction_history()
