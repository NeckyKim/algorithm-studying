# 7-3. 이진 탐색(반복적 풀이)


def binarySearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 중간값이 target과 동일하면 인덱스 반환
        if array[mid] == target:
            return mid

        # 중간값이 target보다 큰 경우
        elif array[mid] > target:
            end = mid - 1

        # 중간값이 target보다 작은 경우
        else:
            start = mid + 1
            
    return None


# 원소의 개수와 target 입력 받기
n, target = map(int, input().split())

# 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행
print(binarySearch(array, target, 0, n - 1))
