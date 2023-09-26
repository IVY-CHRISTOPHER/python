class Checking_Account:

    def __init__(self,bal,int_rate):

        self.int_rate = int_rate * 0.1
        self.bal = bal

    def deposit(self,amount):
        self.bal += amount
        print(f'Your new balance is ${self.bal}')

    def withdrawl(self,amount):
        if amount <= self.bal:
            self.bal -= amount
            print(f'Withdrew {amount}, Your new balance is ${self.bal}')
        elif amount > self.bal:
            print(f'Insufficient Funds: Charging a $5 Fee.')
            self.bal - 5
        return self

    def yield_interest(self):
        if self.bal >=0:
            self.bal += self.int_rate * self.bal
        else:
            print('Insufficient Funds')
        return self

    def display_account_info(self):
        print(f'Interest Rate: {self.int_rate}')
        print(f'Balance: ${self.bal}')
        return self
# _______________________________________________________

# ______________________Users____________________________
class User:

    def __init__(self,First_Name,Last_Name,Email,Age):

        self.first_Name=First_Name
        self.last_Name=Last_Name
        self.email=Email
        self.age=Age
        self.checking = Checking_Account(0, 0.01)

    def deposit(self,amount):
        self.checking.deposit(amount)
        return self

    def withdrawl(self,amount):
        self.checking.withdrawl(amount)
        return self

    def display_account_info(self):
        self.checking.display_account_info()
        return self

    def display_info(self):
        print(f'First Name: {self.first_Name}')
        print(f'Last Name: {self.last_Name}')
        print(f'Email: {self.email}')
        print(f'Age: {self.age}')
        return self
#___________________Bonus_____________________________
    def Transfer(self,amount,User):
        if amount <= self.checking.bal:
            self.checking.bal -= amount
            User.deposit(amount)
            print(f'{amount} has succesfully been transfered to {User}')
            print(f'Your new balance is {self.checking.bal}')
        elif amount > self.checking.bal:
            print(f'Insufficiant Funds, your current balance is ${self.checking.bal}')
        return self
#____________________Bonus____________________________

user1 = User('James','Evans','FakeEmail@email.com','22')
user2 = User('Mike','Evans','FakeEmail2@gmail.com','56')

user1.display_info().deposit(500).withdrawl(150).display_account_info

user1.Transfer(50, user2)

user2.display_account_info()