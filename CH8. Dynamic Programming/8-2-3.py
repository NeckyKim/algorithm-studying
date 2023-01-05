# 8-2-3. 퇴사


n = int(input())


# 각 상담을 완료하는 데 걸리는 기간
t = []

# 각 상담을 완료했을 때 받을 수 있는 금액
p = []

# 다이내믹 프로그래밍 테이블 초기화
dp = [0] * (n + 1)
max_value = 0


for i in range(0, n):
    x, y = map(int, input().split())

    t.append(x)
    p.append(y)


# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i

    # 상담이 기간 안에 끝나는 경우
    if time <= n:

        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(max_value, p[i] + dp[time])
        max_value = dp[i]

    # 상담이 기간 안에 끝나지 않는 경우
    else:
        dp[i] = max_value


print(max_value)
