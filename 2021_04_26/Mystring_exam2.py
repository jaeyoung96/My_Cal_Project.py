'''
mystr = '   Python_good_   study  '
mysplit = mystr.split('_')
print(mysplit)
# strip() : 앞,뒤 공백/ 개행/ \r 모두 제거
mystrip = [ x.strip() for x in mysplit]    # list comporation(반복문 돌면서 list 안에 Data 바로 대입)
print(mystrip)
myjoin = ' '.join(mystrip)  # 문자열 합치고 사이사이에 null값 하나씩 추가
print(myjoin)

myweb1 = 'py%thon'
res = myweb1.replace('%', ' ')
print(res)
'''

mywebData = ['35.2%', '23.7%', '78.9%']
mywebData1 = [ x.replace('%',' ') for x in mywebData]
print(mywebData1)
mywebData2 = [ float(x.strip()) for x in mywebData1]
print(mywebData2)

#myjoin2 = ''.join(mywebData)
#print(myjoin2)
#mysplit2 = mywebData.replace('%', ' ')
#print(mysplit2)