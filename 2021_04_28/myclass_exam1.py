'''
class Myclstest():  # 클래스 정의
    clsdata = 90    # 클래스 속성 변수, 클래스 안에서는 공유
    def __init__(self,arg1): # 생성자 역할
        print('__init__func oper...')
        m_val = arg1    # 함수 내에서만 사용되는 지역변수
        self.data = arg1
    def ShowData(self): # 사용자 정의 method
        print('data :', self.data)  # 객체 속성 변수
        #print('m_val :',m_val)
    def SettingData(self, arg1):
        self.data = 80


inst1 = Myclstest(50) # 객체 생성
print(inst1.data)   # Myclstest(50)
inst1.ShowData()
inst1.SettingData(80)
inst1.ShowData()
'''
class MylistCal():
    def __init__(self,arg1):
        self.data = arg1
    def SumData(self):
        sum = 0
        print()
        for x in self.data:
            sum += x
        print('sum :',sum)
    def SumList(self,arg1):
        list = []
        for i, x in enumerate(self.data):
            print(x,'/', arg1[i])
            list.append(x+ arg1[i])
        print(list)

inst1 = MylistCal([3,4,5,7])
inst1.SumData() # 19
inst1.SumList([1,2,3,4]) # [4,6,8,11]