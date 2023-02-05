# X02. 토마토
# [백준] https://www.acmicpc.net/problem/7576


import sys
from collections import deque

input = sys.stdin.readline


m, n = map(int, input().split())
            
graphs = [list(map(int, input().split())) for _ in range(0, n)]


queue = deque()

for i in range(0, n):
    for j in range(0, m):
        if graphs[i][j] == 1:
            queue.append([i, j])


def BFS():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graphs[nx][ny] == 0:
                queue.append((nx, ny))
                graphs[nx][ny] = graphs[x][y] + 1


BFS()

answer = -1

for graph in graphs:
    for g in graph:
        if g == 0:
            print(-1)
            exit(0)
            
        answer = max(answer, g)
    
print(answer - 1)