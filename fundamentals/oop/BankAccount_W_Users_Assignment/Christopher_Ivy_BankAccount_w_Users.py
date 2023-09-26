#-----------------------CHECKING ACCOUNT--------------------------
class Checking_Account:

    def __init__(self,bal,Int_rate):

    #Attributes
        self.Int_rate = Int_rate * 0.1
        self.bal = bal

    #methods
    def deposit(self, amount):
        self.bal += amount
        print(f'Your new balance is ${self.bal}')

    def withdrawl(self, amount):
        if amount <= self.bal:
            self.bal -= amount
            print(f'Your new balance is {self.bal}')
        elif amount > self.bal:
            print(f'insufficient Funds: Charging a $5 Fee.')
            self.bal -= 5
        return self

    def yield_interest(self):
        if self.bal >= 0:
            self.bal += self.Int_rate * self.bal
        else:
            print('insufficient Funds')
        return self

    def display_account_info(self):
        print(f'Intrest Rate: {self.Int_rate}')
        print(f'Balance: ${self.bal}')
        return self
#-------------------------------------------------------------

#---------------------USERS------------------------
class User:

    def __init__(self,First_Name,Last_Name,Email,Age):

        #attributes
        self.first_Name=First_Name
        self.last_Name=Last_Name
        self.email=Email
        self.age=Age
        self.checking = Checking_Account(Int_rate = 0.01, bal = 0)

        #methods

    def deposit(self, amount):
        self.checking.deposit(amount)
        return self

    def withdrawl(self, amount):
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
#-------------------------------------------------------------

user1 = User("Chris","Ivy","Email@gmail.com","19")

user1.display_info().deposit(100).withdrawl(100).display_account_info()
