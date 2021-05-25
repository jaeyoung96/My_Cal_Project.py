'''
inputdata1 = input('Data Input : ')
inputdata1 = int(inputdata1)
print(inputdata1)
print(type(inputdata1))

inputdata2 = input('Data Input : ')
inputdata2 = int(inputdata2)
print(inputdata2)
print(type(inputdata2))

res = inputdata1 + inputdata2
print('res : ',res)


saved_pw = 'python'

while True:
    input_str = input("password 입력(종료:quit)==>")
    if input_str == saved_pw:
        print('pw success!!')
    elif input_str == 'quit':
        break
    else:
        print('pw fail!!')
'''
import time
now = time.localtime()
print(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
