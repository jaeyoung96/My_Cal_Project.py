'''
mytuple = (1,2,3)
print(mytuple, type(mytuple))
print(mytuple[0])
for x in mytuple:
    print(x, end = ' ')
print()
# mytuple[0] = 99 # tuple의 객체는 수정 X

'''

NameData = ("Lee", "Park", "Hong", "Shin")

def LowerModify(Name_arg):
    mylist = []     # mylist라는 새로운 리스트 설정
    for x in Name_arg:  # 들어온 arg만큼 x번 반복
        mylist.append(x.lower())    # 새로운 mylist 리스트에 x번 소문자로 변환한 글자 대입
    return mylist   # mylist값 반환

Namelowerlist = LowerModify(NameData)   # LowerModify 함수에 NameData값 대입
sortedData = sorted(Namelowerlist)  # 오름차순으로 정렬
print(tuple(sortedData))
