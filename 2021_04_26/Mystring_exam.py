mystr1 = 'Python'
mystr2 = 'is Good'
mystr3 = str('test')
# 내부적으로 문자열 클래스에서 동작
myres = mystr1+ ' ' + mystr2
print(myres)
print(mystr1*3)     # mystr1 3번 반복 출력
print(mystr1[0])    # 0번째 배열 출력
# print(mystr1[len(mystr1)-1])
print(mystr1[-1])   # 마지막 문자 출력
print(mystr1[:3])  # slicing [0, 1, 2] 출력
print(mystr1[2:])  # slicing [2~끝] 출력
print(mystr1[::2])  # slicing 한개 띄우고 출력
print(mystr1[::-1])  # slicing 거꾸로 출력

mystr2 = 'Hello Python Programing'
count = 0
for x in mystr2:
    if x == 'o':
        count+=1
print('count :',count)
print('count : %d %d' %(count,50))
print('count : {},{}'.format(count,3.5))
print('data : %.5f' %3.45)