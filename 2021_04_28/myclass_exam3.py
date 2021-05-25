# 오버로딩 : 추가, 오버라이딩 : 재정의
class Myclscal():
    def __init__(self,arg1):
        self.Mylist = arg1
    def ShowData(self):
        print(self.Mylist)
    def __add__(self, other):
        print('self :',self.Mylist)
        print('other :',other.Mylist)
        mylist = []
        mylist.append(self.Mylist)
        mylist.extend(other.Mylist)
        return mylist
    def __sub__(self, other):
        setdata = set(self.Mylist) - set(other.Mylist)
        return list(setdata)
    def __mul__(self, other):
        setdata = set(self.Mylist) & set(other.Mylist)
        return list(setdata)
inst1 = Myclscal([5,6,7,8])
inst1.ShowData()

inst2 = Myclscal([7,8,9,10])
inst2.ShowData()

res = inst1 + inst2 # inst1. __add__(inst2)
print(res)
res = inst1 - inst2
print(res)  # [5, 6]
res = inst1 * inst2
print(res)