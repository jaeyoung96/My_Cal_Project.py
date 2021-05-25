mydict = {(1,2):30}
print(mydict,type(mydict))
mydict['A'] = 90
print(mydict)
mydict['B'] = 70
print(mydict)
mydict['C'] = 50
print(mydict)

mydict['B'] = 22
print(mydict)
mydict['k'] = 30
print(mydict)

for item in mydict:
    print(item,end=' ') # key 값 출력
    print(mydict[item]) # key의 value값

print(mydict)
popdata = mydict.pop('B')
print('popdata :',popdata)
print(mydict)

mydicsrc = {'A':30, 'B':50, 'C':70}
mydicupdate = {'B':33, 'K':90, 'M':111}
mydicsrc.update(mydicupdate)
print(mydicsrc)