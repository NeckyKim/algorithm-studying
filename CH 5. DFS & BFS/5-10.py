# 5-10. 음료수 얼려 먹기


def solution(n, m, graph):
    # 문자열을 2차원 배열로 변환
    graph = [list(map(int, i)) for i in graph.split("\n")]


    def DFS(x, y):
        # 주어진 범위를 벗어나면 즉시 종료
        if not (0 <= x < n and 0 <= y < m):
            return False

        # 현재 노드를 아직 방문하지 않으면
        if graph[x][y] == 0:

            # 해당 노드를 방문 처리
            graph[x][y] = 1

            # 상, 하, 좌, 우 위치의 노드들을 모두 재귀적으로 호출
            DFS(x, y - 1)
            DFS(x, y + 1)
            DFS(x - 1, y)
            DFS(x + 1, y)

            return True

        return False


    result = 0

    # 모든 노드들을 방문해서 확인
    for i in range(0, n):
        for j in range(0, m):

            # 반환 값이 True이면 값 증가
            if DFS(i, j):
                result = result + 1

    print(result)


n, m = 4, 5

graph = "00110\n" + \
        "00011\n" + \
        "11111\n" + \
        "00000"

solution(n, m, graph)


n, m = 15, 14

graph = "00000111100000\n" + \
        "11111101111110\n" + \
        "11011101101110\n" + \
        "11011101100000\n" + \
        "11011111111111\n" + \
        "11011111111100\n" + \
        "11000000011111\n" + \
        "01111111111111\n" + \
        "00000000011111\n" + \
        "01111111111000\n" + \
        "00011111111000\n" + \
        "00000001111000\n" + \
        "11111111110011\n" + \
        "11100011111111\n" + \
        "11100011111111\n"

solution(n, m, graph)
