a = 5
b = 3
'''방법 1
def AddData(arg1,arg2):
    return arg1+arg2

def SubData(arg1,arg2):
    return arg1-arg2

def MulData(arg1,arg2):
    return arg1*arg2

res = AddData(a,b)
print('res :',res)
res = SubData(a,b)
print('res :',res)
res = MulData(a,b)
print('res :',res)
'''
'''방법 2
Funclist = [AddData,SubData,MulData]
for fn in Funclist:
    res = fn(a,b)
    print('res :', res)
'''
''' 방법 3
fn = lambda x,y : x*y   # 함수명 만들필요 없이 lamda로 표현
#print(fn(5,9))
'''
lambdalist = [lambda x,y : x+y, lambda x,y : x-y, lambda x,y : x*y]
for fn in lambdalist:
    print('result :',fn(5,3))