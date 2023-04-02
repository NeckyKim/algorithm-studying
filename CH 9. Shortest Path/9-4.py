# 9-3. 미래 도시


# 무한을 의미하는 값
INF = int(1e9)


# 노드의 개수와 간선의 개수
n, m = map(int, input().split())

# 2차원 리스트로 그래프를 만들고 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(0, n + 1)]

# 시작과 도착이 같으면 0으로 초기화
for a in range(1, n):
    for b in range(1, n):
        if a == b:
            graph[a][b] = 0

# 간선 정보 입력
for _ in range(0, m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드와 최종 목적지
x, k = map(int, input().split())


# 플로이드 워셜 알고리즘 수행
for z in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][z] + graph[z][j])


distance = graph[1][k] + graph[k][x]


# 도달할 수 없는 경우
if distance > INF:
    print(-1)

# 도달할 수 있는 경우
else:
    print(distance)
