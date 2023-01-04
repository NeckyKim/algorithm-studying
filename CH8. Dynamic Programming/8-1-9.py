# 8-1-9. 금광


for tc in range(0, int(input())):
    n, m = map(int, input().split())

    golds = list(map(int, input().split()))


    # 2차원 다이내믹 프로그래밍 테이블 초기화
    dp = []

    for i in range(0, m):
        temp = []

        for j in range(0, n):
            temp.append(golds[j * m + i])

        dp.append(temp)


    # 다이내믹 프로그래밍 진행
    for i in range(1, m):
        for j in range(0, n):

            # 왼쪽 위에서 오는 경우
            if j == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            # 왼쪽 아래에서 오는 경우
            if j == n - 1:
                left_down = 0
            else:
                left_down = dp[i - 1][j + 1]

            # 왼쪽에서 오는 경우
            left = dp[i - 1][j]

            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    print(max(dp[m - 1]))
