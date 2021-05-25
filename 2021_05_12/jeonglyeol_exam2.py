# 삽입 정렬
# 삽입정렬은 데이터가 거의 정렬되었을때 훨씬 빠름
array = [7,5,9,0,3,4,1,6,2,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):    # 인덱스 i부터 1까지 감소
        if array[j] < array[j - 1]: # j번째 숫자가 j-1 숫자보다 작으면
            array[j], array[j - 1] = array[j - 1], array[j]  # swap
    else:   # 자기보다 작은 데이터를 만나면 그 위치에서 탈출
        break
    # 제일 작은 숫자와 서로 위치 바꿔 줌
print(array)