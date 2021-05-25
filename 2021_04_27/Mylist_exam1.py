'''
import copy
mylist1 = [3,4,5,[77,88]]   # 리스트 안의 리스트는 복사를 하더라도 같은 주소를 사용함
# mylist2 = copy.copy(mylist1)
mylist2 = copy.deepcopy(mylist1)    # deepcopy를 사용하여 리스트 안의 리스트 까지 새로운 객체 생성
print(mylist1, id(mylist1))
print(mylist2, id(mylist2))
mylist1.append(45)
print(mylist1)
print(mylist2)
mylist1[2] = 17
print(mylist1)
print(mylist2)
mylist1[3].append(99)
print(mylist1, id(mylist1[3]))
print(mylist2, id(mylist2[3]))

'''
mylist3 = [9,4,8,1,3]
mylist3.sort()  # list class method
print('mylist3 sort :',mylist3)

res = sorted(mylist3)   # 정렬 함수, 원본 데이터 유지
print('res sorted :',res)

mylist3 = [9,4,8,1,3]
mylist3.reverse()   # reverse 정렬
print('mylist3 reverse:',mylist3)

mylist3 = [9,4,8,1,3]
mylist3.sort(reverse=True)  # 내림차순 정렬
print('mylist3 내림차순 sort:',mylist3)

listdata = []
for i, x in enumerate(mylist3):
    print(i, x)
    listdata.append(i,x)
print(listdata)