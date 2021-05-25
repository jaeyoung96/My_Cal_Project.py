myscorelist = [['kor'], ['math'], ['eng']]
# 국어, 수학, 영어 점수를 입력 처리
# 예) 입력 된 결과(input)
# [['kor',89],['math',75],['eng',88]]
# 총점, 평균을 계산해서 출력(format()활용)

inputData1 = int(input('{} 점수를 입력하시오 : '.format('국어')))
myscorelist[0].append(inputData1)
inputData2 = int(input('{} 점수를 입력하시오 : '.format('수학')))
myscorelist[1].append(inputData2)
inputData3 = int(input('{} 점수를 입력하시오 : '.format('영어')))
myscorelist[2].append(inputData3)
print(myscorelist)

total = 0
for item in myscorelist:
    total += item[1]
avg = total/3
myexam = '총점 :{}, 평균 :{}'.format(total, avg)
print(myexam)