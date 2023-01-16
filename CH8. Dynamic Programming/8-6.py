# 8-6. 개미 전사
# 서로 인접한 식량 창고는 악탈할 수 없음


n = int(input())
food = list(map(int, input().split()))

dp = [0] * (n + 1)

dp[0] = 0
dp[1] = max(food[0], food[1])

# Bottom-Up 풀이법
for i in range(2, n):
    # dp[i - 1]: (i - 1)번째 식량 창고를 털고, 현재 식량 창고는 털지 않는 경우
    # dp[i - 2] + food[i]: (i - 2)번째 식량 창고를 털고, 현재 식량 창고를 터는 경우
    dp[i] = max(dp[i - 1], dp[i - 2] + food[i])


print(dp[n - 1])
