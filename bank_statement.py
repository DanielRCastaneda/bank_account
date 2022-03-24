class BankAccount:
    accounts =[]
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        if(self.balance- amount) >= 0:
            self.balance += amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -=5
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"balance of ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.int_rate *= self.balance
            self.balance += self.int_rate
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

checkings = BankAccount(.004, 2207)
savings = BankAccount(.002, 25000)
checkings.deposit(960).deposit(856).deposit(600).withdraw(230).yield_interest().display_account_info()
savings.deposit(2500).deposit(3351).withdraw(1343).withdraw(4500).withdraw(978).yield_interest().display_account_info()


BankAccount.print_all_accounts()