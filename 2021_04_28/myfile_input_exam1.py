'''
f = open('mytest.txt','r+')
print(f.read())
print(f.tell())
f.seek(0,0)
f.write('C/C++')
f.flush()   # 버퍼 비우기
f.seek(0,0)
print(f.read())

f.close()
'''
f = open('mytext.txt','r')

mystr = f.read()

mylist = mystr.split(" ")

print(mylist)
mylist_cnv = {}
for s in mylist:
    tmp = s.strip()     # 문자열 공백 제거
    if tmp in mylist_cnv:
        mylist_cnv[tmp] = mylist_cnv[tmp] +1
    else:
        mylist_cnv[tmp] = 1

print(len(mylist_cnv))
print(mylist_cnv)
