# 선택 정렬
# 선택 정렬은 swap 논리 사용

array = [7,5,9,0,3,4,1,6,2,8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):    # i 다음 인덱스부터 비교
        if array[min_index] > array[j]:
            min_index = j   # 제일 작은숫자의 인덱스가 min_index에 들어감
    array[i], array[min_index] = array[min_index], array[i]
    # 제일 작은 숫자와 서로 위치 바꿔 줌
print(array)