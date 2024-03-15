
class Account():

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("User Personal Details")        
        print("")        
        print("Name :", self.name)
        print("Age :", self.age)
        print("Gender :", self.gender)

class Bank(Account):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Balance has been updated to: Ushs", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance available is : Ushs", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Remaining balance is: Ushs", self.balance)

    def view_balnce(self):
        self.show_details()
        print("Remaining balance is: Ushs", self.balance)

            


user1 = Bank("Jon Doe", "25", "Male")
user1.view_balnce()