def Mytestfunc():
    global data
    data = 20
    print('data :',data)    # 지역공간 -> 전역공간 순서로 변수 찾음
    print('Function Inner :',locals())     # 현재 함수에 등록된 지역변수 출력

data = 80
Mytestfunc()
print('data :',data)
print('Function Outter :',locals())