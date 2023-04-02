# Q38. 정확한 순위
# [백준] https://www.acmicpc.net/problem/11404


import heapq
import sys
input = sys.stdin.readline


INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(0, n + 1)]

for _ in range(0, m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    
    
    
def dijkstra(vertex):
    distance = [INF] * (n + 1)
    distance[vertex] = 0
    
    queue = []
    heapq.heappush(queue, (0, vertex))
    
    while queue:
        min_dist, min_vertex = heapq.heappop(queue)
        
        if min_dist > distance[min_vertex]:
            continue
        
        for v, d in graph[min_vertex]:
            cost = min_dist + d
            
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))
                
    return distance

answer = 0

paths = []

for i in range(1, n + 1):
    paths.append(dijkstra(i)[1:])
    
for i in range(0, n):
    count = 0
    for j in range(0, n):
        if paths[i][j] != INF or paths[j][i] != INF:
            count = count + 1
            
    if count == n:
        answer = answer + 1
        
print(answer)
    