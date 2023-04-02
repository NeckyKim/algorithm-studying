# 9-4. 전보


import heapq
import sys
input = sys.stdin.readline


# 무한을 의미하는 값
INF = int(1e9)

# 노드의 개수, 간선의 개수, 시작 노드
n, m, c = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보
graph = [[] for _ in range(0, n + 1)]

# 간선 정보 입력
for _ in range(0, m):
    # x번 노드에서 y번 노드로 가는 비용은 z
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(vertex):
    distance[vertex] = 0

    queue = []

    # 시작 노드로 가기 위한 최단 경로를 0으로 설정한 후 큐에 삽입
    heapq.heappush(queue, (0, vertex))

    # 큐가 비어있지 않는 동안 수행
    while queue:
        # 최단 거리가 가장 짧은 노드의 정보 꺼내기
        min_dist, min_vertex = heapq.heappop(queue)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if min_dist > distance[min_vertex]:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for v, d in graph[min_vertex]:
            cost = min_dist + d

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))


# 최단 거리 테이블
distance = [INF] * (n + 1)

# 다익스트라 알고리즘 수행
dijkstra(c)


# 도달할 수 있는 노드의 개수
count = 0

# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0


for d in distance:
    if d != 0 and d < INF:
        count = count + 1
        max_distance = max(max_distance, d)

print(count, max_distance)
