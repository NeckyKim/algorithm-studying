# Q28. 고정점 찾기


# 이진 탐색 코드
def binarySearch(array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2


    if array[mid] == mid:
        return mid

    # 중간점의 인덱스보다 중간점의 값이 작으면 왼쪽을 확인
    elif array[mid] > mid:
        return binarySearch(array, start, mid - 1)

    # 중간점의 인덱스보다 중간점의 값이 크면 오을 확인
    else:
        return binarySearch(array, mid + 1, end)
    

# 원소의 개수 입력 받기
n = int(input())

# 원소 입력 받기
numbers = list(map(int, input().split()))

# 이진 탐색 수행
answer = binarySearch(numbers, 0, n - 1)

if answer:
    print(answer)
    
else:
    print(-1)