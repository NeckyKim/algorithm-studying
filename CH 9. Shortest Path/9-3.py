# 9-3. 플로이드 워셜 알고리즘


INF = int(1e9)  # 무한을 의미하는 값

n = int(input())
m = int(input())

graph = [[INF] * n for _ in range(0, n)]


for a in range(0, n):
    for b in range(0, n):
        if a == b:
            graph[a][b] = 0
            
            
for _ in range(0, m):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = min(c, graph[a - 1][b - 1])
    
for k in range(0, n):
    for i in range(0, n):
        for j in range(0, n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            

for a in range(0, n):
    for b in range(0, n):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    
    print("")