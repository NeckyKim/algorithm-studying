# 5-9: BFS(Breadth-First Search, 너비 우선 탐색)


from collections import deque


# 그래프 정보
graph = [
    [],
    [2, 3, 8],  # 1번 노드는 2, 3, 8번 노드와 연결 됨
    [1, 7],     # 2번 노드는 1, 7번 노드와 연결 됨
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 시작 노드
start = 1

# 노드 방문 여부
visited = [False] * len(graph)


# 너비 우선 탐색 알고리즘
def BFS(start):

    # 큐를 사용
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때 까지 반복
    while queue:

        # 큐에서 하나의 원소를 뽑아 출력
        x = queue.popleft()
        print(x)

        # 아직 방문하지 않은 인접한 노드를 큐에 삽입
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


BFS(start)
