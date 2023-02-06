# Q34. 병사 배치하기


n = int(input())

soldiers = list(map(int, input().split()))
soldiers.reverse()

print(soldiers)

dp = [1] * (n + 1)


for i in range(1, n):
    for j in range(0, i):
        if soldiers[i] > soldiers[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        
        print(dp)