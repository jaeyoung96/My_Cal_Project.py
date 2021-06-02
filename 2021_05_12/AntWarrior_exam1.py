# 개미는 뚠뚠~오늘도 뚠뚠~열심히 일을 하네~
import time, random

N = 100 #int(input())
K = random.sample(range(0,1000),100) #list(map(int, input().split()))
start_time = time.time()
max_range, first, second = 0, 0, 0
for i in range(N-1):
    max_range += i
result = [0] * max_range
for x in range(max_range):
    if max_range == 1 and K[1] > K[0]+K[2]: result[0] = K[1]; break
    K_result = K[first] + K[2+second]
    result[x] = K_result
    if (2+second) < (N - 1):
        second += 1
    else:
        first += 1
        second = first
# print(K)
# print(result)
print(max(result))
end_time = time.time()
print("time = ",end_time - start_time)

# N=3, [a,b,c], 경우의 수 : [(a+c), b], 2, max(경우의 수)
# N=4, [a,b,c,d], 경우의 수 : [(a+c), (b+d), (a+d)], 2+1, max(경우의 수)
# N=5, [a,b,c,d,e], 경우의 수 : [(a+c), (a+d), (a+e), (b+d), (b+e), (c+e)], 3+2+1, max(경우의 수)
# N=6, [a,b,c,d,e,f], 경우의 수 : [(a+c), (a+d), (a+e), (a+f), (b+d), (b+e), (b+f), (c+e), (c+f), (d+f)], 4+3+2+1, max(경우의 수)

'''답안 예시
# 정수 N을 입력받기
n= int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2,n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])
    
# 계산된 결과 출력
print(d[n - 1])
'''