def listsumfunc(arg1, arg2):
    newlist = []
    for i, x in enumerate(arg1):
        print(i, x)
        x+arg2[i]
        newlist.append(x + arg2[i])
    return newlist

mylist1 = [3,4,5,6]
mylist2 = [7,8,9,10]


res = listsumfunc(mylist1,mylist2)  # 함수 호출
print(res)