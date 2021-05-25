def myfunctest(*arg):   # 가변인수 사용
    print(arg)
    print(arg[0])
    print(arg[1])
    print(arg[2])

myfunctest(3,[1,2,3],{'a':7, 'b':9})