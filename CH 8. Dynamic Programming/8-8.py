# 8-8. 효율적인 화폐 구성


n, m = map(int, input().split())

# 화폐의 종류
coins = []

for i in range(0, n):
    coins.append(int(input()))


# 10001은 해당 금액은 경우의 수가 존재하지 않음을 의미함
dp = [10001] * (m + 1)


dp[0] = 0

# Bottom-Up 풀이법

# 작은 화폐 순서대로 진행
for i in range(0, n):
    for j in range(coins[i], m + 1):

        # (i - k)원을 만드는 방법이 존재하는 경우
        if dp[j - coins[i]] != 10001:
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)


# 결과 출력
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
