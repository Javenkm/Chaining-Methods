class User:
    def __init__(self, name, email):
        self.name = name 
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def display_user_balance(self):
        print(f"Name: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, amount, other_user):
        self.account_balance = self.account_balance - amount
        other_user.account_balance = other_user.account_balance + amount
        print(f"{self.name} just transferred {amount} dollars to {other_user.name}")
        return self

Javen = User("Javen", "Javenkm@gmail.com")
Israel = User("Alpha", "alphaDog@gmail.com")
Ella = User("Beta", "betasucks@gmail.com")

Javen.make_deposit(5000).make_deposit(1500).make_deposit(250).make_deposit(-120).display_user_balance()
Israel.make_deposit(800).make_deposit(100).make_deposit(100).make_deposit(-50).make_deposit(-50).display_user_balance()
Ella.make_deposit(1225).make_deposit(-100).make_deposit(-50).make_deposit(-100).display_user_balance()

Javen.display_user_balance()
Israel.display_user_balance()
Javen.transfer_money(250, Ella)
Javen.display_user_balance()
Ella.display_user_balance()