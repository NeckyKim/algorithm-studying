# 7-5. 부품 찾기(이진 탐색)


def binarySearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None


# 부품의 개수 입력 받기
n = int(input())

# 부품 입력 받기
parts = list(map(int, input().split()))

# 이진 탐색을 위해 부품을 정렬
parts.sort()


# 주문의 개수 입력 받기
m = int(input())

# 주문 입력 받기
orders = list(map(int, input().split()))


# 부품을 하나씩 확인
for order in orders:
    if binarySearch(parts, order, 0, n - 1):
        print("yes", end=" ")

    else:
        print("no", end=" ")
