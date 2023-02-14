# 3-4. 1이 될 때까지


def solution(n, k):
    count = 0

    while n > 1:
        # n이 k로 나누어 떨어지는지 확인

        # 나누어 떨어지면, 나누기
        if n % k == 0:
            n = n // k

        # 나누어 떨어지지 않으면, k를 빼기
        else:
            n = n - 1

        count = count + 1

    return count


n, k = map(int, input().split())


print(solution(n, k))
