# Q16. 연구소
# [백준] https://www.acmicpc.net/problem/14502


from collections import deque
from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline


# 초기 지도
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(0, n)]


# 벽이 없는 곳의 위치
no_walls = []

for i in range(0, n):
    for j in range(0, m):
        if graph[i][j] == 0:
            no_walls.append([i, j])


# 바이러스의 위치
viruses = []

for i in range(0, n):
    for j in range(0, m):
        if graph[i][j] == 2:
            viruses.append([i, j])


# 3개의 울타리를 세우는 조합
added_walls = list(combinations(no_walls, 3))


answer = 0


# 특정 위치에 3개의 울타리를 세웠을 때 실행할 함수
def solution(walls):
    global answer


    # 초기 지도의 정보를 복사
    new_graph = deepcopy(graph)


    # 빈 공간에 3개의 울타리를 설치
    for i in range(0, 3):
        new_graph[walls[i][0]][walls[i][1]] = 1


    # 깊이 탐색
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

                # 상, 하, 좌, 우 바이러스가 퍼질 수 있는지 확인
                if 0 <= nx < n and 0 <= ny < m and new_graph[nx][ny] == 0:
                    new_graph[nx][ny] = 2
                    queue.append([nx, ny])


    # 각 바이러스의 위치에서 전파 진행
    for virus in viruses:
        BFS(virus[0], virus[1])


    # 바이러스가 전파를 완료했으면, 안전 영역의 크기를 갱신
    score = 0

    for i in range(0, n):
        for j in range(0, m):
            if new_graph[i][j] == 0:
                score = score + 1

    answer = max(answer, score)


# 3개의 벽을 세우는 조합의 경우의 수 마다 바이러스 전파를 시작
for walls in added_walls:
    solution(walls)


# 정답 출력
print(answer)
