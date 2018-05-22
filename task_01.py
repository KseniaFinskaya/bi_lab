# simple program no.12
# code correction w/o changing logic


class BankAccount(object):

    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def overdrawn(self):
        return self.balance < 0


my_account = BankAccount(15)
my_account.withdraw(20)
my_account.deposit(3)  # added deposit input

print(my_account.balance)  # show balance
print(my_account.overdrawn())  # added show overdrawn
