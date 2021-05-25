'''
string_obj = "python programing"
print(string_obj)
print(id(string_obj))
string_obj = string_obj.upper()
print(string_obj)
print(id(string_obj))   # 새로운 주소의 객체를 생성하여 대문자 변환

a = 50
def functest(): # 함수 정의
    global a # a를 전역변수로 호출
    a =50
    a +=1
    print('a :',a)

functest()  # 함수 호출
print('a :', a)

str1 = ['k', 'b', 's']
print('/'.join(str1))
print('='*50)
'''
string_obj = "python programing"
str_list = []   # list()
for x in string_obj:
    if x != ' ':
        str_list.append(chr(ord(x)-32))  # x:한 문자
    else:
        str_list.append(x)
print()
print(str_list)
string_up = ''.join(str_list)
print(string_up)