# 5-9: BFS(Breadth-First Search, 너비 우선 탐색)
# graph: 그래프 정보
# start: 시작 노드
# visited: 방문한 노드


def BFS(graph, start, visited):

    # 큐를 사용
    queue = [start]

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때 까지 반복
    while queue:

        # 큐에서 하나의 원소를 뽑아 출력
        x = queue.pop(0)
        print(x, end=" ")

        # 아직 방문하지 않은 인접한 노드를 큐에 삽입
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],  # 1번 노드는 2, 3, 8번 노드와 연결
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 1번 노드에서 시작
start = 1

# 방문 노드 초기화
visited = [False] * 9


BFS(graph, start, visited)
