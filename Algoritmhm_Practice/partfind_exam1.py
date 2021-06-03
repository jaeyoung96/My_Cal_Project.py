'''
import time
def bin_find(store_part, target, start, end):
    if start > end:
        return None
    # if target not in store_part:
    #     return 2
    mid = (start + end) // 2
    if store_part[mid] == target:
        return 1
    elif store_part[mid] < target:
        return bin_find(store_part, target, mid + 1, end)
    else:
        return bin_find(store_part, target, start, mid - 1)

N = int(input())
store_part = list(map(int, input().split()))
M = int(input())
customer_part = list(map(int, input().split()))

start_time = time.time()
store_part.sort()
for i in range(M):
    target = customer_part[i]
    result = bin_find(store_part, target, 0, N - 1)
    if result == None:
        print("원소가 존재하지 않습니다.")
    elif result == 1:
        print("yes")
    elif result == 2:
        print("no")

end_time = time.time()
print("time = ", end_time-start_time)
'''

import time

N = int(input())
store_part = list(map(int, input().split()))
M = int(input())
customer_part = list(map(int, input().split()))

start_time = time.time()
count = [0] * (max(store_part)+1)
for i in range(len(store_part)):
    count[store_part[i]] += 1

for i in customer_part:
    if count[i] > 0:
        print("yes", end=' ')
    else:
        print("no", end=' ')

# count_customer = [0] * (max(customer_part)+1)
# for i in range(len(store_part)):
#     count[store_part[i]] += 1

end_time = time.time()
print("time = ", end_time-start_time)

