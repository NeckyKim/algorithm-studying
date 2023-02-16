# Q16. 연구소
# [백준] https://www.acmicpc.net/problem/14502


# 초기 지도
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(0, n)]

# 벽을 설치한 뒤 지도
new_graph = [[0] * m for _ in range(0, n)]

answer = 0


# 깊이 우선 탐색을 이용해 각 바이러스가 사방에 퍼지도록 하기
def virus(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(0, 4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 상, 하, 좌, 우 바이러스가 퍼질 수 있는지 확인
        if 0 <= nx < n and 0 <= ny < m and new_graph[nx][ny] == 0:
            new_graph[nx][ny] = 2

            # 해당 위치에 바이러스를 배치하고, 다시 재귀적으로 수행
            virus(nx, ny)


# 안전 영역의 크기 계산
def getScore():
    score = 0

    for i in range(0, n):
        for j in range(0, m):
            if new_graph[i][j] == 0:
                score = score + 1

    return score


# 깊이 우선 탐색을 이용해 울타리를 설치하면서, 매번 안전 여역의 크기를 갱신
def DFS(count):
    global answer

    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(0, n):
            for j in range(0, m):
                new_graph[i][j] = graph[i][j]

        # 각 바이러스의 위치에서 전파 진행
        for i in range(0, n):
            for j in range(0, m):
                if new_graph[i][j] == 2:
                    virus(i, j)

        answer = max(answer, getScore())

        return

    # 빈 공간에 울타리를 설치
    for i in range(0, n):
        for j in range(0, m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count = count + 1

                DFS(count)

                graph[i][j] = 0
                count = count - 1


DFS(0)

print(answer)
