# 8-2-2. 정수삼각형


n = int(input())


# 다이내믹 프로그래밍 테이블 초기화
triangle = []

for i in range(0, n):
    triangle.append(list(map(int, input().split())))


# 다이내믹 프로그래밍 진행
for i in range(1, n):
    for j in range(0, len(triangle[i])):

        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = triangle[i - 1][j - 1]

        # 바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = triangle[i - 1][j]

        triangle[i][j] = triangle[i][j] + max(up_left, up)


print(max(triangle[n - 1]))
