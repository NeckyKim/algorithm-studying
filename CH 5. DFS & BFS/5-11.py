# 5-11. 미로 탈출


def solution(n, m, graph):
    # 문자열을 2차원 배열로 변환
    graph = [list(map(int, i)) for i in graph.split("\n")]


    def BFS(x, y):
        dx = [0, 0, -1, 1]  # x축 좌우 이동
        dy = [-1, 1, 0, 0]  # y축 상하 이동

        queue = [[x, y]]

        while queue:
            x, y = queue.pop(0)

            # 이동 방향 확인
            for i in range(0, 4):

                # 이동 후, 공간 안에 있는지 확인
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                    # 있으면 큐에 삽입
                    queue.append([nx, ny])

                    # 그리고, 움직임을 1 증가
                    graph[nx][ny] = graph[x][y] + 1

        return graph[n - 1][m - 1]

    print(BFS(0, 0))


n, m = 5, 6

graph = "101010\n" + \
        "111111\n" + \
        "000001\n" + \
        "111111\n" + \
        "111111"
        
solution(n, m, graph)
