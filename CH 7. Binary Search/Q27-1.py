# Q27-1. 정렬된 배열에서 특정 수의 개수 구하기


# 수열에서 값이 target인 원소 개수 계산
def countByValue(array, target):
    # 숫자의 총 개수
    n = len(array)

    # target이 처음으로 등장한 인덱스
    first = searchFirst(array, target, 0, n - 1)

    # target이 존재하지 않는 경우
    if first == None:
        return 0

    # target이 마지막으로 등장한 인덱스
    last = searchLast(array, target, 0, n - 1)

    # 개수를 반환
    return last - first + 1


# target의 처음 위치를 찾기 위해 이진 탐색 수행
def searchFirst(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    # target이 가장 왼쪽에 있는 경우 인덱스 반환
    if array[mid] == target and (mid == 0 or target > array[mid - 1]):
        return mid

    # target보다 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return searchFirst(array, target, start, mid - 1)

    # target보다 큰 경우 오른쪽 확인
    else:
        return searchFirst(array, target, mid + 1, end)


# target의 마지막 위치를 찾기 위해 이진 탐색 수행
def searchLast(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    # target이 가장 오른쪽에 있는 경우 인덱스 반환
    if array[mid] == target and (mid == n - 1 or target < array[mid + 1]):
        return mid

    # target보다 작거나 같은 경우 왼쪽 확인
    elif array[mid] > target:
        return searchLast(array, target, start, mid - 1)

    # target보다 큰 경우 오른쪽 확인
    else:
        return searchLast(array, target, mid + 1, end)


# 원소의 개수와 target 입력 받기
n, target = map(int, input().split())

# 원소 입력 받기
numbers = list(map(int, input().split()))

# target의 원소 개수 계산
count = countByValue(numbers, target)

if count:
    print(count)

else:
    print(-1)
