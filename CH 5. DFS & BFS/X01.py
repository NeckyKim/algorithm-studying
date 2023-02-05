# X01. 연결 요소의 개수
# [백준] https://www.acmicpc.net/problem/11724


import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


n, m = map(int, input().split())
            
inputs = [list(map(int, input().split())) for _ in range(0, m)]

graph = [[] for _ in range(0, n + 1)]
visited = [False] * (n + 1)

for i in inputs:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])


def DFS(start):
    visited[start] = True
        
    for i in graph[start]:
        if not visited[i]:
            DFS(i)
 

count = 0

for i in range(1, n + 1):
    if not visited[i]:
        DFS(i)
        count = count + 1
        
print(count)