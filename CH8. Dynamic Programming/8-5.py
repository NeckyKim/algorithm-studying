# 8-5. 1로 만들기
# x가 5/3/2로 나누어 떨어지면, 5/3/2로 나눈다. 그렇지 않으면 x에서 1을 뺀다.


n = int(input())

dp = [0] * (n + 1)


# Bottom-Up 풀이법
for i in range(2, n + 1):
    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1

    # 현재의 수가 2로 나누어 지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 현재의 수가 2로 나누어 지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    # 현재의 수가 2로 나누어 지는 경우
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[n])
