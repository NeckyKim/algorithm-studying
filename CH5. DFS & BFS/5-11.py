# 5-11. 미로 찾기


n, m = map(int, input().split())

graph = []

for i in range(0, n):
    graph.append(list(map(int, input())))


def BFS(x, y):
    dx = [0, 0, -1, 1]  # x축 좌우 이동
    dy = [-1, 1, 0, 0]  # y축 상하 이동

    queue = [(x, y)]

    while queue:
        x, y = queue.pop(0)

        # 이동 방향 확인
        for i in range(0, 4):

            # 이동 후, 공간 안에 있는지 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                # 있으면 큐에 삽입
                queue.append((nx, ny))

                # 그리고, 움직임을 1 증가
                graph[nx][ny] = graph[x][y] + 1

    return graph[n - 1][m - 1]


print(BFS(0, 0))
