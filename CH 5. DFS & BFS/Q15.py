# Q15. 특정 거리의 도시 찾기
# [백준] https://www.acmicpc.net/problem/18352


from collections import deque
import sys
input = sys.stdin.readline


# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(0, n + 1)]


# 도로 정보 입력받기
for _ in range(0, m):
    a, b = map(int, input().split())

    graph[a].append(b)


# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)

distance[x] = 0


# 너비 우선 탐색 알고리즘
def BFS(start):
    queue = deque([start])

    while queue:
        now = queue.popleft()

        # 현재 도시에서 이동할 수 있는 모든 도시를 확인
        for i in graph[now]:

            # 아직 방문하지 않은 도시라면
            if distance[i] == -1:

                # 최단 거리 갱신
                queue.append(i)
                distance[i] = distance[now] + 1


BFS(x)


answer = []

for i in range(1, n + 1):
    # 해당 도시의 최단 거리와 k가 일치하는지 확인
    if distance[i] == k:
        answer.append(i)

# 최단 거리가 k인 도시가 없으면 -1을 출력
if answer == []:
    print(-1)

else:
    for i in answer:
        print(i)
