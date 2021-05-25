# 퀵 정렬 간단한 코드
#
array = [5,7,9,0,3,4,1,6,2,8]
# start = 0, end = 9
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있으면 종료
    if len(array) <= 1:    # 원소가 1개인 경우 종료
        return array

    pivot = array[0]   # 피벗에 첫번째 원소 대입
    tail = array[1:]    # left에 피벗 다음 원소 대입

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 왼쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))