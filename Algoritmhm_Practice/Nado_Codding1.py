""" 자료형
print("vvip")   # 문자열 자료형
print(5*4)  # 숫자 자료형
print(not(5>10))    # boolean 자료형
print(5<10) # True
print(not True) # False
"""
''' 변수
animal = "고양이"
name = "고영희"
age = 2
hobby = "잠자기"
is_adult = age >=4

print("우리집" + animal + "의 이름은 " + name + "에요")
hobby = "공놀이"
print(name, "는", age, "살이며, ", hobby, "이(가) 취미에요")
print(name + "는 어른일까요? " + str(is_adult))
'''
''' 퀴즈 #1
 QUIZ) 변수를 이용하여 다음 문장을 출력하시오.

 변수명 : station
 변수값 : "사당", "신도림", "의정부" 순서대로 입력
 출력 문장 : XX 행 열차가 들어오고 있습니다.

station = "사당"
print(station, "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station, "행 열차가 들어오고 있습니다.")
station = "의정부"
print(station, "행 열차가 들어오고 있습니다.")
'''
''' 연산자
print(1+1)  # 2
print(8-5)  # 3
print(2*7)  # 14
print(8/2)  # 4
print(2**3)  # 2^3 = 8
print(5%3)  # 5/3 나머지 = 2
print(5//3)  # 5/3 몫 = 1
print(10 >= 7) # True
print(3 == 3)   # 3은 3과 같은지? True
print(3 * 5 == 10)  # 3 * 5 = 10? False
print(3 != 7)  # 3은 7과 같지 않다? True
print(not(3 != 7))  # 3은 7과 같지 않다의 반대 = False
print((3 > 1) & (3 > 5))    # True & False = False
print((3 > 1) | (3 > 5))    # True | False = True
print(7 > 6 > 5)    # True
print(7 > 4 > 6)    # False
'''
''' 간단한 수식
print(2 + 3 * 5)    # 17
print((2 + 3) * 5)    # 25
number = 2 + 3 * 4  # 14
print(number)
number = number + 4 # 18
print(number)
number += 4 # 22
print(number)
number *= 2 # 44
print(number)
number -= 4 # 40
print(number)
number /= 2 # 20
print(number)
number %= 3 # 2
print(number)
'''
''' 숫자처리 함수
print(abs(-5))  # 5
print(pow(4,2))  # 4^2 = 16
print(max(5 , 8))  # 8
print(min(5 , 8))  # 5
print(round(3.14))  # 반올림 값 = 3
print(round(4.58))  # 반올림 값 = 5

from math import *  # math 라이브러리 활용
print(floor(4.99))  # 내림 = 4
print(ceil(4.01))  # 올림 = 5
print(sqrt(16)) # 제곱근 = 4
'''
''' 랜덤함수
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 정수값 생성
print(int(random() * 45) +1) # 1 ~ 45 사이의 임의의 정수값 생성, ex)로또 번호
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45))  # 1, 45 포함한 범위의 임의의 값 생성
'''
''' 퀴즈 #2
QUIZ) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

<출력문 예제>
오프라인 스터디 모임 날짜는 매월 X 일로 선정되었습니다.

from random import *
date =  randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 ",date ,"일로 선정되었습니다.")
'''
''' 문자열
sentence = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence)
'''
'''슬라이싱
jumin = "960822-1194736"

print("성별 : " + jumin[7]) # jumin의 7번째 자리
print("년도 : " + jumin[0:2])   # jumin 0 부터 2 직전까지 값[0,1]
print("월 : " + jumin[2:4])   # jumin 2 부터 4 직전까지 값[2,3]
print("일 : " + jumin[4:6])   # jumin 4 부터 6 직전까지 값[4,5]
print("생년월일 : " + jumin[:6])   # jumin 처음부터 6 직전까지 값[0,1,2,3,4,5]
print("뒷자리 : " + jumin[7:])   # jumin 7부터 끝까지 값[7,8,9,10,11,12,13]
print("뒷자리(뒤에서부터) : " + jumin[-7:])   # jumin 맨 뒤에서 7번째부터 끝까지 값[7,8,9,10,11,12,13]
'''
''' 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())   # 모든 문자 소문자로 출력
print(python.upper())   # 모든 문자 대문자로 출력
print(python[0].isupper())   # 0번째 문자가 대문자인지 판단 : True
print(len(python))   # 문자열의 길이 출력
print(python.replace("Python", "Java"))   # 문자열 안의 문자 다른 문자로 대체

index = python.index("n")   # 변수 내에서 첫번째로 나오는 "n" 단어의 위치
print(index)
index = python.index("n", index + 1)    # 첫번째 "n" 다음 나오는 "n"의 위치
print(index)

print(python.find("Java"))  # index와 비슷하나 원하는 값이 없을 경우 -1 출력
print(python.count("n"))    # "n" 단어가 몇번 나오는지 표시
'''
''' 문자열 포맷
print("나는 %d살입니다." % 26)  # %d는 정수형 변수 출력 가능
print("Apple 은 %c로 시작해요." %"A")   # %c는 한글자 출력 가능
print("나는 %s을 좋아해요." % "파이썬")   # %s는 문자형 변수 출력 가능
# 방법 1
print("나는 %s과 %s색을 좋아해요." % ("흰색", "검정색"))
# 방법 2
print("나는 {}살 입니다." .format(20))  # {} 사용시 .format()에 값 입력
print("나는 {}과 {}색을 좋아해요." .format("흰색", "검정색"))
print("나는 {0}과 {1}색을 좋아해요." .format("흰색", "검정색"))
print("나는 {1}과 {0}색을 좋아해요." .format("흰색", "검정색")) # {}안에 숫자로 순번을 정해줌
# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 26, color = "보라"))
# 방법 4
age = 26
color = "보라"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
'''
''' 탈출 문자
print("백문이 불여일견\n백견이 불여일타")   # 문장 내 줄바꿈 \n
print("저는 \"배재영\" 입니다.")    # \"\" 또는 \'\'는 문장 내의 따움표 사용 가능
print("C:\\Users\\john8\\OneDrive\\바탕 화면\\Python_Code") # \\ : 문장 내에서 \
print("Red Apple\rPine")    # \r : 커서를 맨 앞으로 이동
print("Pinee\bApple")    # \b : 백스페이스 (한 글자 삭제)
print("Pine\tApple")    # \t : 탭
'''
''' 퀴즈 #3
QUIZ) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙 1 : http:// 부분은 제외 => naver.com
규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => navaer
규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
                (nav)                 (5)           (1)             (!)
예) 생성된 비밀번호 : nav51!

site = "http://youtube.com"
slice_site = site.replace("http://", "")
#index = site.index(".")   # 변수 내에서 첫번째로 나오는 "." 단어의 위치
slice_site = slice_site[:slice_site.index(".")] # 0 ~ "." 직전까지 슬라이싱
#print(slice_site)
print("생성된 비밀번호 :" + slice_site[:3] + str(len(slice_site)) + str(slice_site.count("e")) + "!")
'''
'''
# 리스트[]
subway = ['유재석', '조세호', '하하']
print(subway)
# 하하의 위치
print(subway.index('하하'))
# 박명수 다음 칸에 타게 함
subway.append('박명수')
print(subway)
# 정형돈 유재석 / 조세호 사이에 타게 함
subway.insert(1,'정형돈')
print(subway)
# 지하철에 있는 사람 뒤에서부터 꺼냄
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
# 같은 이름의 사람 몇 명 있는지 확인
subway.append('유재석')
print(subway)
print('유재석 count:',subway.count('유재석'))
# 정렬도 가능
num_list = [4,2,3,5,1]
num_list.sort()
print(num_list)
# 순서 뒤집기
num_list.reverse()
print(num_list)
# 모두 지우기
num_list.clear()
print(num_list)
# 다양한 자료형 사용 가능
mix_list = ['조세호',20,True]
print(mix_list)
# 리스트 확장
num_list = [4,2,3,5,1]
num_list.extend(mix_list)
print(num_list)
'''
'''
# 사전 생성
cabinet = {3:'유재석',100:'김태호'}
print(cabinet[3])
print(cabinet[100])
# 사전 안의 값 접근
print(cabinet.get(3))
# print(cabinet[5])     # 없는 key값 가져오려 하면 error 발생
print(cabinet.get(5))   # .get() 사용하면 None 출력 후 다음 문장 정상 실행
print(cabinet.get(5,'사용 가능'))
print('error')
# 사전 안에 자료형 있는지 확인
print(3 in cabinet)
print(5 in cabinet)
# 여러 자료형 key값 설정
cabinet = {'A-3':'유재석','B-100':'김태호'}
print(cabinet['A-3'])
# 새로운 손님
print(cabinet)
cabinet['A-3'] = '김종국'
cabinet['C-20'] = '조세호'
print(cabinet)
# 떠난 손님
del cabinet['A-3']
print(cabinet)
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
# 목욕탕 폐점
cabinet.clear()
print(cabinet)
'''
'''
# 튜플
menu = ('돈까스', '치즈까스')
print(menu[0])
print(menu[1])
# menu.add('생선까스') # 튜플은 리스트 추가 불가능
name = '김종국'
age = 20
hobby = '코딩'
print(name,age,hobby)
# 튜플의 활용
(name, age, hobby) = ('김종국', 20, '코딩')
print(name,age,hobby)
'''
'''
# set(집합), 중복 불가능
my_set = {1,2,3,3,3}
print(my_set)
# set의 활용
java = {'유재석','정형돈','김태호'}
python = {'유재석', '박명수'}
# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
# 합집합 (java 또는 python 둘중에 하나라도 할 수 있는 개발자)
print(java|python)
# 차집합(java는 할 수 있지만 python은 못하는 개발자)
print((java - python))
# python 할 줄 아는 사람이 늘어남
python.add('김태호')
print(python)
# java를 까먹음
java.remove('김태호')
print(java)
'''
'''
# 자료구조의 변경
menu = {'커피','쥬스','우유'}
print(menu, type(menu))
# list로 변경
menu = list(menu)
print(menu, type(menu))
# tuple로 변경
menu = tuple(menu)
print(menu, type(menu))
# 다시 set로 변경
menu = set(menu)
print(menu, type(menu))
'''
'''
# 퀴즈 #4
조건 1: 댓글은 20명이 작성하고 아이디는 1~20 이라고 가정
조건 2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건 3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 17
커피 당첨자 : [12, 1, 3]
-- 축하합니다 --

from random import *
mylist = range(1,21)
mylist = list(mylist)
shuffle(mylist)
chicken = sample(mylist,4)
print(mylist)
print('-- 당첨자 발표 --')
print('치킨 당첨자 : {0}'.format(chicken[0]))
print('커피 당첨자 : {0}'.format(chicken[1:]))
print('-- 축하합니다 --')
'''
'''
# if
weather = input('오늘의 날씨는? ')
if weather == '비' or weather == '눈':
    print('우산을 챙기세요')
elif weather == '미세먼지':
    print('마스크를 챙기세요')
else:
    print('준비물이 필요 없어요')

temp = int(input('기온은 어때요? '))
if temp >= 30:
    print('너무 더워요!')
elif 0 <= temp <= 15:
    print('외투를 챙기세요~')
elif 15< temp <30:
    print('적당한 날씨에요~')
else:
    print('너무 추워요. 나가지 마세요!')
'''
'''
# for
for num in range(1,6):  #  num : 1,2,3,4,5
    print('대기번호 : {}'.format(num))
# for문 활용
starbucks = ['아이언맨', '토르', '스파이더맨']
for customer in starbucks:  
    print('{}님 커피가 준비되었습니다.'.format(customer))
'''
'''
# while
customer = '토르'
index = 5
while index >= 1:
    print('{}님 커피가 준비 되었습니다. {}번 남았어요~'.format(customer, index))
    index -= 1
    if index == 0:
        print('커피는 폐기처분 되었습니다.')
# while 무한 반복
customer '아이언맨'
index = 1
while True:
    print('{}님 커피가 준비 되었습니다. {}번째 호출~'.format(customer, index))
    index += 1
# while 계속 비교
customer = '토르'
person = 'Unknown'

while person != customer:
    print('{}님 커피가 준비 되었습니다.'.format(customer))
    person = input('이름을 입력하세요 : ')
'''
'''
# contine & break
absent = [2,5]
no_book = [7]
for x in range(1,11):    # 1 ~ 10번 까지 반복
    if x in absent:
        continue    # continue는 현재 넘어가고 다음 반복문으로 진행
    elif x in no_book:
        print('오늘 수업은 여기까지...{}번 학생은 교무실로 따라와'.format(x))
        break   # break는 바로 반복문 탈출
    print('{}번 학생 책을 읽어보세요.'.format(x))

'''
'''
# 한줄 for
출석번호 1,2,3,4 앞에 100 붙이기로 함 -> 101, 102, 103...
stuendts = [1,2,3,4,5]
print(stuendts)
stuendts = [i+100 for i in stuendts]
print(stuendts)

# 학생 이름을 길이로 변환
students = ['iron man', 'thor', 'spider man']
students = [len(x) for x in students]
print(students)

# 학생 이름을 대문자로 변환
students = ['iron man', 'thor', 'spider man']
students = [x.upper() for x in students ]
print(students)
'''
# 퀴즈 # 5
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램 작성
#
# 조건1 : 승객별 운행 소요시간은 5 ~ 50분 사이의 난수로 설정
# 조건2 : 목적지까지 소요시간 5 ~ 15분 사이의 승객만 매칭
#
# (출력문 예제)
'''
from random import *

total = 0   # 총 탑승 승객 수

for x in range(1,51):
    time = randint(5, 50)
    # print(time, type(time))
    check = ''
    if 5 <= time <= 15:
        check = 'O'
        total += 1
    else:
        check = ' '
    print('[{}],{}번째 손님 (소요시간 : {}분)'.format(check, x, time))

print('총 탑승 승객 : {}명'.format(total))
'''
'''
# 함수
def open_account():
    print('새로운 계좌 생성')

def deposit(balance, money):
    print('입금이 완료되었습니다. 잔액은 {}원 입니다.'.format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print('출금이 완료되었습니다. 잔액은 {}원 입니다.'.format(balance - money))
        return balance - money
    else:
        print('출금이 불가능합니다. 잔액은 {}원 입니다.'.format(balance))
        return balance

def withdraw_night(balance,money):
    commission = 100    # 수수료 100원
    print('수수료는 {}원이며, 잔액은 {}원 입니다.'.format(commission, balance - money - commission))
    return commission, balance - money - commission


open_account()
balance = 0
balance = deposit(balance,2000)
# balance = withdraw(balance,2000)
balance = withdraw(balance,500)
commission, balance = withdraw_night(balance, 500)
'''
'''
# 함수의 기본값
# def profile(name, age, main_lang):
#     print('이름 : {}\t 나이 : {}\t주 사용 언어 : {}'.format(name,age,main_lang))
#
# profile('배재영',26,'C++')
# profile('유재석',20,'Python')

# 같은 학교, 같은 학년, 같은 반, 같은 수업
def profile(name, age = 17, main_lang = 'Python'):
    print('이름 : {}\t 나이 : {}\t주 사용 언어 : {}'.format(name,age,main_lang))

profile('배재영')
profile('유재석')
'''
'''
# 키워드 값
def profile(name, age, main_lang):
    print(name,age,main_lang)

profile(name='유재석',main_lang='Python',age=20)
profile(main_lang='C++',age=25,name='김태호')
'''
'''
# 가변 인자
def profile(name, age, *language):
    print('이름 : {}\t나이 : {}\t'.format(name,age),end=' ')
    for lang in language:
        print(lang, end=' ')
    print()
profile('유재석',20,'python','java','c++','c#', 'c', 'script')
profile('김태호',25,'kotlin','swift')
'''
'''
gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))

'''
'''
# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
    # 함수명 : std_weight
    # 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# 출력 예제
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == '남자' or gender == 'man':
        return height * height * 22
    elif gender == '여자' or gender == 'woman':
        return height * height * 21
    print("키 {} 남자의 표준 체중은 {} 입니다.".format(height,weight))

gender = input("성별 : ")
height = input("키(cm) : ")
weight = round(std_weight(int(height)/100,gender),2) # 두번째 자리까지 반올림

print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height,gender,weight))
'''
print('a')