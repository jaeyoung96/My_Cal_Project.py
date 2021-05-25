
mylist1 = [3,4,5,6]
mylist2 = [5,6,7,8]
res = set(mylist1) & set(mylist2)
print(list(res))

mysrc1 = 'Python Programing'
mysrc2 = 'good prog'
res = set(mysrc1) & set(mysrc2)
print(res)
res.remove('g')
print(res)
res.discard('x')
print(res)
