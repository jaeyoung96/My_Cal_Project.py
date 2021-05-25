mylist = []
print(mylist, type(mylist))
mylist.append('ABC')
mylist.append(90)
mylist.append(5.6)
mylist.append([2,3,4])
print(mylist)   # list는 객체의 ID를 저장하기 때문에 제한이 없다

mylist1 = [1,2,3]
mylist1.append([90,100])
print(mylist1)
mylist1.extend([90,100])
print(mylist1)
mylist1.insert(2,55)    # 리스트[2]에 90 대입
print(mylist1)
mylist1.insert(len(mylist1), 50)    # 리스트의 제일 마지막에 50 대입
print(mylist1)
mylist1.remove(90)
print(mylist1)

def functest():
    a = 5
    b = 3
    return a, b

res = functest()
print('res:',res, type(res))

res1 = 3,4,5    # 여러개의 정수를 하나의 tuple로 묶음
print('res1:',res1)

res1, res2, res3 = 9,234,554    # 변수 여러개 정의 시 tuple 풀리고 int형 변수 하나만 반환
print('res1:',res1,type(res1))