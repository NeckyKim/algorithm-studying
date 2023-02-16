# 4-1. 상하좌우


def solution(n, moves):
    x, y = 1, 1

    # L(eft), R(ight), U(p), D(own)
    directions = ["L", "R", "U", "D"]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for move in moves:

        # 이동 방향 확인
        for i in range(0, 4):
            if move == directions[i]:

                # 이동 후, 공간 안에 있는지 확인
                nx = x + dx[i]
                ny = y + dy[i]

                if (1 <= nx <= n) and (1 <= ny <= n):
                    x = nx
                    y = ny

    print(x, y)


solution(int(input()), input().split())
