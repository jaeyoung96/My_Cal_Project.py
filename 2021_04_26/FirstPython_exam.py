'''
a = '3'
print('a :',a)  # a값 출력
print(a)
print(type(a))  # a 타입 출력
print(id(a))    # a의 주소값

b = 'Python'
print('b :',b)  # a값 출력
print(b)
print(type(b))  # a 타입 출력
print(id(b))    # a의 주소값

c = 5+3
print(c, type(c), id(c))
print('S')
print('B',end=' ')
print('S')
'''

for x in range(5):
    print(x, end=' ')
else:
   print() # '\n' 개행 출력

mylist = [1.2, 51.5, 7.9]
list1 = [str(x) for x in mylist]
mystrjoin = '/'.join(list1)
print(mystrjoin)