# 8-2. 피보나치 수열
# 재귀적 풀이법


n = int(input())

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
memo = [0] * (n + 1)

# 첫 번째와 두 번째 피보나치 수는 1
memo[1] = 1
memo[2] = 1


def fib(n):
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if memo[n] != 0:
        return memo[n]

    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


print(fib(n))
