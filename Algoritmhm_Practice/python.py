import time
import numpy as np
N = int(input('N = '))
start_time = time.time()
cnt = 1
a = np.zeros((N,N))
# result = [0] * (N*N)

for i in range(N):
    if i % 2 == 1:
        for j in range(N-1,-1,-1):
            a[i][j] = cnt
            cnt += 1
    else:
        for j in range(N):
            a[i][j] = cnt
            cnt += 1

print(a)
end_time = time.time()
print('time = ',end_time - start_time)
