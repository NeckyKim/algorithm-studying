# Q27-2. 정렬된 배열에서 특정 수의 개수 구하기(bisect 사용)


# Python의 이진 탐색 라이브러리 사용
from bisect import bisect_left, bisect_right


# 수열에서 값이 target인 원소 개수 계산
def countByRange(array, left_target, right_target):
    # 숫자의 총 개수
    n = len(array)

    # target이 처음으로 등장한 인덱스
    left_index = bisect_left(array, left_target)

    # target이 마지막으로 등장한 인덱스
    right_index = bisect_right(array, right_target)

    # 개수를 반환
    return right_index - left_index


# 원소의 개수와 target 입력 받기
n, target = map(int, input().split())

# 원소 입력 받기
numbers = list(map(int, input().split()))

# target의 원소 개수 계산
count = countByRange(numbers, target, target)

if count:
    print(count)

else:
    print(-1)
