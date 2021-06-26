import time, random
import numpy as np
N, M = list(map(int, input().split())) # 100, 10000
# money = np.random.randint(1,10000,size=N)
print(N, M)
money = []

for _ in range(N):
    money.append(int(input()))
start_time = time.time()

money = sorted(money)
print(money)

count = 0
while N > 0:
    a = M//money[N-1]
    count += a
    M = M - (a * money[N-1])
    N -= 1

if M != 0:
    print('-1')
else:
    print(count)
end_time = time.time()
print('time = ',end_time-start_time)
