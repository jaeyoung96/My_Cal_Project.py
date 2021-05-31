import time
start_time = time.time()
# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건(1 혹은 2일때 1을 반환)
    if x == 1 or x ==2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))
end_time = time.time()
print('time = ',end_time - start_time)

# d[99] = fibo(98) + fibo(97)
# d[98] = fibo(97) + fibo(96), d[97] = fibo(96) + fibo(95)
# d[97] = d[97], d[96] = fibo(95) + fibo(94), d[96] = d[96], d[95] = fibo(94) + fibo(93)
# d[95] = d[95], d[94] = fibo(93) + fibo(92), d[94] = d[94], d[93] = fibo(92) + fibo(91)
# ...
# 재귀함수 2번씩만 타고 들어가면 된다.