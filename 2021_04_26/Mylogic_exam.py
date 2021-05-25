a = 10 and 0    # 논리 and 연산, 좌항이 True 이면 우항 값 출력
print('a :',a)

b = 0 or 20     # 논리 or 연산, 좌항이 True 이면 좌항 값, 좌항이 False 이면 우항 값 출력
print('b:',b)

def functest():
    c =257
    print('C ID:',id(c))
# -5 ~ 256 ID를 불러와서 사용

functest()
d =257
print('D ID:',id(d))

print("""i`m 
jaeyoung""")
# \n : 0x0A, \r : 0x0D