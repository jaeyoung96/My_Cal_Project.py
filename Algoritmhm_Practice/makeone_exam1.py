# 0 ~ X 까지의 경우의 수 d에 저장
import time
X = int(input())
start_time = time.time()
d = [0] * (X + 1)
for i in range(2,X + 1):
    d[i] = d[i - 1] + 1

    if i % 5 == 0 and d[i//5] + 1 < d[i]:
        d[i] = d[i//5] + 1
    if i % 3 == 0 and d[i//3] + 1 < d[i]:
        d[i] = d[i//3] + 1
    if i % 2 == 0 and d[i//2] + 1 < d[i]:
        d[i] = d[i//2] + 1
#26 25 5 1
#32 16 15 3 1
#47 46 45 9 3 1

print(d[X])
print(d)
end_time = time.time()
print("time = ",end_time - start_time)