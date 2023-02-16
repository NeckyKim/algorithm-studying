# Q17. 경쟁적 전염
# [백준] https://www.acmicpc.net/problem/18405


from collections import deque
import sys
input = sys.stdin.readline


n, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(0, n)]

target_s, target_x, target_y = map(int, input().split())



viruses = []

for i in range(0, n):
    for j in range(0, n):
        if graph[i][j] != 0:
            viruses.append([graph[i][j], 0, i, j])

viruses.sort()


def BFS():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    queue = deque(viruses)
    
    while queue:
        virus, s, x, y = queue.popleft()
        
        if s == target_s:
            break
    
        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append([virus, s + 1, nx, ny])

    
BFS()


print(graph[target_x - 1][target_y - 1])