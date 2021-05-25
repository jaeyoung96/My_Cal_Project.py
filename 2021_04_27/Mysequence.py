def functest():
    a = 5
    b = 2
    return a+b

res = functest()
print('res :',res)

mylist = ['s', 'b', 's']*2   # 5개 배열의 list 초기화
mylist[0] = 'k' # 0번째 배열에 k대입
print(mylist)
print("".join(mylist))  # list를 문자열로 변환
print(list(mylist))     # 문자열을 list로 변환