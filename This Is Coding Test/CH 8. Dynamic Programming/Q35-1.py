# Q35-1. 못생긴 수


n = int(input())


# 다이내믹 프로그래밍 테이블 초기화
dp = [0] * n
dp[0] = 1


# 2배, 3배, 5배를 위한 인덱스
i2 = 0
i3 = 0
i5 = 0


# 처음에 곱셈값을 초기화
next2 = 2
next3 = 3
next5 = 5


for i in range(1, n):

    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    dp[i] = min(next2, next3, next5)

    # 인덱스에 따라서 곱셈 결과를 증가
    if dp[i] == next2:
        i2 = i2 + 1
        next2 = dp[i2] * 2

    if dp[i] == next3:
        i3 = i3 + 1
        next3 = dp[i3] * 3

    if dp[i] == next5:
        i5 = i5 + 1
        next5 = dp[i5] * 5
        
print(dp[n - 1])