class Test2():
    var1 = 78
    def __init__(self,data):
        self.var = data
        print('__init__self.var:', self.var)
    def method1(self):
        print('method1 Test2.var:', Test2.var1)
        print('method1 self.var:', self.var)
    @classmethod
    def change_data(cls,de):
        cls.var = de

inst = Test2(50)
print('inst var:', inst.var)    # 50

inst3 = Test2(60)
print('inst3 var:', inst3.var)  # 60

inst.method1()      # 78, 50
inst3.method1()     # 78, 60

Test2.change_data(217)
print('Test2.var:', Test2.var)  # 217
Test2.var = 33
print('Test2.var:', Test2.var)  # 33
print(dir(Test2))
print(dir(inst))
print(dir(inst3))

class HouseClass():
    Company = 'python Academy'
    def __init__(self, year, address, price):
        self.year = year
        self.address = address
        self.price = price
    def show_company(self):
        print(self.Company)
    def change_company(self,name):
        self.Company = name
    def show_info(self):
        print('''This house was built by {} in {}, address : {}, price : {}'''.format(self.Company, self.year, self.address, self.price))

houseA = HouseClass(2019,'Guro',34.56)
houseA.show_company()   # python Academy
houseA.change_company('MDS Academy')
houseA.show_company()   # MDS Academy
houseA.show_info() # MDS Academy in 2019, address : Guro, price : 34.56
houseB = HouseClass(2020, 'Pangyo', 999.99)
houseB.show_info() # python Academy in 2020, address : Pangyo, price : 999.99

class Calculator():
    def __init__(self,mylistdata):
        self.mylist = mylistdata
    def mysum(self):
        self.total = 0
        for x in self.mylist:
            self.total += x
        return self.total
    def myavg(self):
        list_len = len(self.mylist)
        self.avg = self.total / list_len
        return self.avg

cal1 = Calculator([1,2,3,4,5])
print(cal1.mysum())
print(cal1.myavg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.mysum())
print(cal2.myavg())