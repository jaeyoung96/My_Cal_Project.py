# 퀵 정렬
#
array = [5,7,9,0,3,4,1,6,2,8]
# start = 0, end = 9
def quick_sort(array, start, end):
    if start >= end:    # 원소가 1개인 경우 종료
        return
    pivot = start   # 피벗에 첫번째 원소 대입
    left = start + 1    # left에 피벗 다음 원소 대입
    right = end     # right에 마지막 원소 대입
    while left <= right:    # left가 right를 넘어설 때 까지
        # 피벗보다 큰 데이터를 찾을 때까지 오른쪽으로 한칸씩 이동
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 왼쪽으로 한칸씩 이동
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈릴 경우 작은데이터와 피벗 swap
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은데이터와 큰 데이터 교체
        else:
            array[left], array[right] = array[right], array[left]
    # right == pivot
    quick_sort(array, start, right - 1) # 처음부터 right 전까지 배열 다시 비교
    quick_sort(array, right + 1, end) # right 다음부터 끝까지 배열 다시 비교

quick_sort(array, 0, len(array) - 1) # 0 ~ 9
print(array)
