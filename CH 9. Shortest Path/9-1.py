# 9-1. 다익스트라 알고리즘


import sys
input = sys.stdin.readline


INF = int(1e9)  # 무한을 의미하는 값


# 노드의 개수와 간선의 개수
n, m = map(int, input().split())

# 시작 노드 번호
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보
graph = [[] for _ in range(0, n + 1)]

# 노드 방문 여부
visited = [False] * (n + 1)

# 최단 거리 테이블
distance = [INF] * (n + 1)


# 간선 정보 입력
for _ in range(0, m):
    # a번 노드에서 b번 노드로 가는 비용은 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서, 최단 거리가 가장 짧은 노드의 번호를 반환
def getSmallestNode():
    min_value = INF

    # 최단 거리가 가장 짧은 노드의 인덱스
    index = 0

    for i in range(0, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def dijkstra(start):
    # 시작 노드에 대해서 노드 방문 여부와 최단 거리 테이블 초기화
    visited[start] = True
    distance[start] = 0


    for i in graph[start]:
        distance[i[0]] = i[1]

    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for _ in range(0, n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = getSmallestNode()
        visited[now] = True

        #  현재 노드와 연결된 다른 노드를 확인
        for i in graph[now]:
            cost = distance[now] + i[1]

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)


for i in range(1, n + 1):
    # 도달할 수 없는 경우
    if distance[i] == INF:
        print("INF")

    # 도달할 수 있는 경우
    else:
        print(distance[i])
