# 3-1-2. 큰 수의 법칙
# 배열의 크기: n, 총 더하는 횟수: m, 한 수를 연속으로 더할 수 있는 횟수: k


n, m, k = map(int, input().split())

numbers = list(map(int, input().split()))


def solution(numbers, m, k):
    numbers.sort()

    # 가장 큰 수와 두 번째로 큰 수 2개를 사용
    number1 = numbers[-1]
    number2 = numbers[-2]

    # 가장 큰 수를 k번 더 하고, 두 번째로 큰 수를 1번 더 하면 되므로, (k + 1)번을 계속 반복해주면 된다.

    # (k + 1)번을 반복할 수 있을 만큼 반복한다.
    count = (m // (k + 1)) * k

    # (k + 1)번을 전부 더 하지 못할 때는, 더할 수 있을만큼만 더한다.
    count = count + (m % (k + 1))

    answer = count * number1 + (m - count) * number2

    return answer


print(solution(numbers, m, k))
