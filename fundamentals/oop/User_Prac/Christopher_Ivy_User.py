

class User:

    def __init__(self,First_Name,Last_Name,Email,Age,gold_card_points):

        #attributes
        self.First_Name=First_Name
        self.Last_Name=Last_Name
        self.Email=Email
        self.Age=Age
        self.is_rewards_member = False
        self.gold_card_points = 0

        #methods
    def display_info(self):
        print(f'First Name: {self.First_Name}')
        print(f'Last Name: {self.Last_Name}')
        print(f'Email: {self.Email}')
        print(f'Age: {self.Age}')
        print(f'Gold Card Points: {self.gold_card_points}')

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points += 200
            print(f'You are now a gold member {self.First_Name}! You have {self.gold_card_points} Points!')
        else:
            print('You are already a rewards member.')
            return False

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f'Thank you for your purchase! You now have {self.gold_card_points} Points!')
        else:
            print(f'You do not have enough points for that! You have {self.gold_card_points} Points.')

user1 = User("Chris","Ivy","email@gmail.com",19,0)
user2 = User('Mark','pryor','email@gmail.com',34,0)
user3 = User('Keith','Mason','email@gmail.com',56,0)

user1.display_info()
user2.display_info()
user3.display_info()

user1.enroll()
user1.spend_points(50)

user2.enroll()
user2.spend_points(80)

user1.display_info()
user2.display_info()
user3.display_info()

user1.enroll()

user3.enroll()
user3.spend_points(240)