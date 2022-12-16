# 5-1-10. 음료수 얼려 먹기


n, m = map(int, input().split())

graph = []

for i in range(0, n):
    graph.append(list(map(int, input())))


def DFS(x, y):
    global n, m
    global graph

    # 주어진 범위를 벗어나면 즉시 종료
    if not (0 <= x < n and 0 <= y < m):
        return False

    # 현재 노드를 아직 방문하지 않으면
    if graph[x][y] == 0:

        # 해당 노드를 방문 처리
        graph[x][y] = 1

        # 상, 하, 좌, 우 위치의 노드들을 모두 재귀적으로 호출
        DFS(x, y - 1)
        DFS(x, y + 1)
        DFS(x - 1, y)
        DFS(x + 1, y)

        return True

    return False


result = 0

# 모든 노드들을 방문해서 확인
for i in range(0, n):
    for j in range(0, m):

        # 반환 값이 True이면 값 증가
        if DFS(i, j):
            result = result + 1


print(result)
