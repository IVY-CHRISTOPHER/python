

class BankAccount:

    accounts = []

    def __init__(self,bal,int_rate):

    #Attributes
        self.int_rate = int_rate * 0.1
        self.bal = bal
        BankAccount.accounts.append(self)

    #methods
    def deposit(self,amount):
        if amount > 0:
            self.bal += amount
            print(f'Your new balance is ${self.bal}')
        else:
            print('insufficient Funds')
        return self

    def withdrawl(self,amount):
        if amount <= self.bal:
            self.bal -= amount
            print(f'Your new balance is ${self.bal}')
        elif amount > self.bal:
            print(f'insufficient Funds: Charging a $5 Fee.')
            self.bal -= 5
        return self

    def display_account_info(self):
        print(f'interest Rate: {self.int_rate}')
        print(f'Balance: ${self.bal}')
        return self

    def yield_interest(self):
        if self.bal >= 0:
            self.bal += self.int_rate * self.bal
        else:
            print('Insufficient Funds')
        return self

    @classmethod
    def all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


account1 = BankAccount(1000, 5)
account2 = BankAccount(15000, 3)

account1.deposit(500).deposit(150).deposit(100).withdrawl(200).yield_interest().display_account_info()

account2.deposit(1000).deposit(500).withdrawl(10000).withdrawl(15).yield_interest().display_account_info()

print('_________')
BankAccount.all_accounts()