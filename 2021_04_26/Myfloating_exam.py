from decimal import Decimal # decimal 모듈의 Decimal 클래스만 사용
x = Decimal('0.1')+Decimal('0.2')
print("x :",x)
print(type(x))
x = float(x)
print("x :",x,type(x))

a = [1,2,3]
print(a, type(a))
print(a[0])

b=(45, 1, 3)  # (n,) 형태로 만들어야 tuple로 출력
print(b, type(b))
print(b[0])

c = 'python'
print(c,type(c))
print(c[0])

d = {'a':30, 'b':50, 'c':90}    #
print((d, type(d)))
for bae in d:
    print(bae)

f = {1, 2, 2, 5, 5}
print("f:",f)

mylistdata = [3,3,5,6,8,22,5,7,3,8,5,3]
mysetdata = set(mylistdata)
print(mysetdata)