# def SwapData(arg1, arg2): # 방법 1
#     #global a,b
#     #a = arg2
#     #b = arg1
#     print('a :',a ,'b :',b)

def SwapData(arg1, arg2):   # 방법 2
    return arg2, arg1
a = 5
b = 3
(a,b) = SwapData(a,b) # 튜플이란 객체를 새로 만들어서 a,b 변환 가능
print(a,b)