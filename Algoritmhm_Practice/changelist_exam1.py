import time

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

start_time = time.time()

A.sort()
B.sort()
min_a = 0

for i in range(K):
    if A[min_a] > B[N-1]:
        break
    A[min_a] = B[N-1]
    min_a += 1
    N -= 1

print(sum(A))

end_time = time.time()
print("time = ",end_time-start_time)
