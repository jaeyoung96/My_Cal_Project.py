import time
import random
n = 100000
n_list =[]
for _ in range(n):
    n_list.append(random.randint(0, 100))# sorted(map(int, input().split()))
m = 100000
m_list = []
for _ in range(m):
    m_list.append(random.randint(0, 100))# list(map(int,input().split()))
# print(n_list)
# print(m_list)

start_time = time.time()
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid]  == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

for target in m_list:
    result = binary_search(n_list, target, 0, n - 1)
    if result == None:
        print(0)
    else:
        print(1)

end_time = time.time()
print('time = ', end_time - start_time)