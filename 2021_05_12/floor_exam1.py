# 바닥 공사 문제
import time, random
N = 1000 # int(input())
start_time = time.time()
result = [0] * N
result[0] = 1
result[1] = 3

for i in range(3,N+1):
    result[i-1] = (result[i-2] + (result[i-3] * 2)) % 796796
print(result[N-1])

end_time = time.time()
print("time = ",end_time - start_time)
# N = 1, 1가지
# N = 2, 3가지
# N = 3, 5가지, 3 + (1*2)
# N = 4, 11가지, 5 + (3*2)
# N = 5, 21가지, 11 + (5*2)
# N = 6, 43가지
# N = 10? for i in range(10):
# result