
'''
listdata = [30,50,60,70,80]
try:
    number = int(input('출력할 리스트 index 정수 입력:'))
    print('{}번째 요소 : {}'.format(number,listdata[number]))
except Exception as e:  # input이 0~4 숫자가 아닐 경우
    print('type e:',type(e))    # Error 타입
    print('e :',e)  # 에러 출력
finally:
    print('프로그램 종료!!')
'''
dictdata = {'kor':30,'math':50,'eng':80}
print(dictdata)
try:
    key = input('사전에서 삭제할 키 입력:')
    del dictdata[key]
except Exception as e:  # input이 0~4 숫자가 아닐 경우
    print('키 입력 오류!!')
    print('type e:',type(e))    # Error 타입
    print('e :',e)  # 에러 출력
    print('키 재입력!')
finally:
    print(dictdata)
    print('프로그램 종료!!')