# 5-8. DFS(Depth-First Search, 깊이 우선 탐색)


# graph: 그래프 정보
# start: 시작 노드
# visited: 방문한 노드

def DFS(graph, start, visited):

    # 현재 노드를 방문 처리
    visited[start] = True

    print(start, end=" ")

    # 현재 노드와 인접한 노드를 재귀적으로 방문
    for i in graph[start]:

        # 인접한 노드가 방문되지 않으면 방문을 진행
        if not visited[i]:
            
            # 재귀를 사용
            DFS(graph, i, visited)


graph = [
    [],
    [2, 3, 8],  # 1번 노드는 2, 3, 8번 노드와 연결 됨
    [1, 7],     # 2번 노드는 7번 노드와 연결 됨
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


DFS(graph, start, visited)
