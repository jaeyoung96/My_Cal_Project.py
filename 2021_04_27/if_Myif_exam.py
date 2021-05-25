import numpy as np

data = list(range(1,10))    # range(1~9) 출력
print(data)

arr = np.arange(1,10)   # numpy에 있는 arrange 메소드 사용
print(arr)
'''
strarg = 'PYTHON PROGRAM'
strlist = [chr(ord(x)+32) if x != '' else x for x in strarg]
for x in strarg:
     if x != ' ':
         strlist.append(chr(ord(x)+32))
     else:
         strlist.append(x)
print(''.join(strlist))

my_dict = {'a':1, 'b':2, 'c':3, 'd':4}
print(my_dict)
rev_dict={}
for x in my_dict:
    rev_dict[my_dict[x]] = x
print(rev_dict)

mystrdata = '#3V42AR34!@43dvd'
mylistdata = []

for x in mystrdata:
    if (x >= 'A') and (x <= 'Z'):
        mylistdata.append(x)
    elif (x >= 'a') and (x <= 'z'):
        mylistdata.append(x)
print(mylistdata)
mystr_cov = ''.join(mylistdata)
print(mystr_cov)
'''

words = ['apple', 'bat', 'air', 'bar', 'atom', 'book']
by_letter = {}
for x in words:
    letter = x[0]
    if letter not in by_letter:
        by_letter[letter] = [x]
    else:
        by_letter[letter].append(x)

print(by_letter)
