class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(self.balance)

        else:
            print("Insufficient Funds")

data = input().split()
start_money = int(data[0])
take_money = int(data[1])

my_account = Account(start_money)
my_account.withdraw(take_money)