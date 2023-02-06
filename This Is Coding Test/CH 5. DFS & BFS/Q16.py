# Q16. 연구소
# [백준] https://www.acmicpc.net/problem/14502


from collections import deque
from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(0, n)]

no_walls = []

for i in range(0, n):
    for j in range(0, m):
        if graph[i][j] == 0:
            no_walls.append([i, j])

no_walls_iter = list(combinations(no_walls, 3))


answer = 0


def solution(add_walls):
    global answer
    
    new_graph = deepcopy(graph)
    
    
    for i in range(0, 3):
        new_graph[add_walls[i][0]][add_walls[i][1]] = 1
        
    
    viruses = []

    for i in range(0, n):
        for j in range(0, m):
            if new_graph[i][j] == 2:
                viruses.append([i, j])
                

    def BFS(x, y):
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        queue = deque()
        queue.append([x, y])

        while queue:
            x, y = queue.popleft()

            for i in range(0, 4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and new_graph[nx][ny] == 0:
                    new_graph[nx][ny] = 2
                    queue.append([nx, ny])

    for virus in viruses:
        BFS(virus[0], virus[1])
    


    count = 0
    
    for i in new_graph:
        for j in i:
            if j == 0:
                count = count + 1
                
    answer = max(answer, count)
    



for add_walls in no_walls_iter:
    solution(add_walls)

print(answer)