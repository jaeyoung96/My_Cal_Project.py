class Account():
    def __init__(self,money):
        self.balance = money
    def deposit(self,money):
        self.balance += money
    def withdraw(self,money):
        self.balance -= money
    def show_Account(self):
        print('balance : {} 원'.format(self.balance))

class stock_account(Account):
    def __init__(self,name,money):
        Account.__init__(self,money)
        self.name = name
    def deposit(self,money):
        self.balance +=money *1.37
    def withdraw(self,money):
        self.balance -= money +50
    def show_Account(self):
        print('Account owner : {}'.format(self.name))
        print('balance : {} 원'.format(self.balance))

myact = stock_account('MDS',500)
myact.deposit(200)
myact.show_Account()

a = 6
b = 7
oper = 'a+b'
res = eval(oper)
print(res)

a = 5
b = 4
res = eval(oper)
print(res)
