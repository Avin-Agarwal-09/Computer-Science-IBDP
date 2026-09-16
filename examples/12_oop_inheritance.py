"""Topic 12 - OOP: inheritance and polymorphism.

inheritance   a subclass IS-A superclass and reuses its code
super()       call the parent's version of a method (usually __init__)
overriding    redefine a parent method to change the behaviour
polymorphism  the SAME call does different things depending on the object

    BankAccount
        |
    +---+-----------------+
    |                     |
SalaryAccount     FixedDepositAccount

The loop at the bottom calls account.withdraw(50) on every account without
knowing or caring which subclass it is - that is polymorphism.
"""


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
        return f"#{self.transaction_id} | {self.type} | {self.amount}{details}"


class BankAccount:
    bank_name = "Unnamed Bank"
    account_count = 0

    def __init__(self, account_number, first_name, last_name, account_type):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.account_type = account_type
        self._balance = 0
        self._transactions = []
        BankAccount.account_count += 1

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return False
        self._balance += amount
        self._transactions.append(Transaction(amount, "DEPOSIT"))
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self._balance:
            print(f"  {self.account_number}: withdrawal of {amount} refused")
            return False
        self._balance -= amount
        self._transactions.append(Transaction(amount, "WITHDRAWAL"))
        return True

    def print_transactions(self):
        for transaction in self._transactions:
            print("  ", transaction)

    def __str__(self):
        return (f"{self.account_number} {self.first_name} {self.last_name} "
                f"[{self.account_type}] balance {self._balance}")

    @staticmethod
    def set_bank_name(name):
        BankAccount.bank_name = name


class SalaryAccount(BankAccount):
    """Adds behaviour the parent does not have."""

    def __init__(self, account_number, first_name, last_name, salary=0):
        super().__init__(account_number, first_name, last_name, "Salary")
        self.salary = salary

    def deposit_salary(self, amount):
        if self.deposit(amount):
            self._transactions[-1].description = "monthly salary"
            return True
        return False


class FixedDepositAccount(BankAccount):
    """OVERRIDES withdraw to add a rule the parent does not enforce."""

    def __init__(self, account_number, first_name, last_name,
                 principal, interest_rate, years):
        super().__init__(account_number, first_name, last_name, "FixedDeposit")
        self.principal = principal
        self.interest_rate = interest_rate
        self.years = years
        self.is_matured = False
        self._balance = principal

    def calculate_maturity_amount(self):
        return self.principal * (1 + self.interest_rate / 100) ** self.years

    def mature(self):
        self.is_matured = True
        self._balance = self.calculate_maturity_amount()

    def withdraw(self, amount):
        if not self.is_matured:
            print(f"  {self.account_number}: locked until maturity")
            return False
        return super().withdraw(amount)      # reuse the parent's logic


class Bank:
    """Aggregation: the Bank holds accounts but does not own their behaviour."""

    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def total_funds(self):
        return sum(account.balance for account in self.accounts)


if __name__ == "__main__":
    BankAccount.set_bank_name("Chase")

    savings = BankAccount("A123", "Julian", "Dizon", "Savings")
    checking = BankAccount("B123", "Avin", "Agarwal", "Checking")
    salary = SalaryAccount("C123", "Kenzo", "Geier", 3000)
    deposit = FixedDepositAccount("D123", "Ryan", "Eng", 500, 5, 2)

    bank = Bank(BankAccount.bank_name)
    accounts = [savings, checking, salary, deposit]
    for account in accounts:
        bank.add_account(account)

    savings.deposit(500)
    checking.deposit(200)
    salary.deposit_salary(3000)

    print("Polymorphism - same call, different behaviour:")
    for account in accounts:
        succeeded = account.withdraw(50)
        outcome = "withdrew 50" if succeeded else "refused"
        print(f"  {account.account_type:12} -> {outcome}")

    print("\nAll accounts:")
    for account in accounts:
        print("  ", account)

    print("\nFixed deposit matures:")
    print("  maturity amount:", round(deposit.calculate_maturity_amount(), 2))
    deposit.mature()
    deposit.withdraw(50)
    print("  after maturity: ", deposit)

    print("\nisinstance checks:")
    print("  salary is a SalaryAccount:", isinstance(salary, SalaryAccount))
    print("  salary is a BankAccount:  ", isinstance(salary, BankAccount))
    print("  savings is a SalaryAccount:", isinstance(savings, SalaryAccount))

    print(f"\nBank: {bank.name}")
    print("  total funds:   ", bank.total_funds())
    print("  accounts made: ", BankAccount.account_count)
    print("  find 'A123':   ", bank.find_account("A123").first_name)

    print("\nTransactions for the salary account:")
    salary.print_transactions()
