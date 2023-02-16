# Q11. 뱀
# [백준] https://www.acmicpc.net/problem/3190


# 뱀이 이동할 지도
field_size = int(input())
fields = [[0] * field_size for _ in range(0, field_size)]

# 사과 위치
apples = [list(map(int, input().split())) for _ in range(0, int(input()))]
apples = [[apple[0] - 1, apple[1] - 1] for apple in apples]

# 회전 정보
moves = [list(input().split()) for _ in range(0, int(input()))]
moves = [[int(move[0]), move[1]] for move in moves]

# 뱀의 길이
snakes = [[0, 0]]


# 지도에 사과를 표시
for apple in apples:
    fields[apple[0]][apple[1]] = 1

# 좌표 초기화
y = 0
x = 0


# 회전 방향
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

d = 0

# 시간 계산
count = 0

i = 0


while True:
    count = count + 1

    # 뱀이 앞으로 이동할 칸 계산
    ny = y + dy[d]
    nx = x + dx[d]

    # 회전하는 시간인지 확인
    if i < len(moves):
        if count == moves[i][0]:
            if moves[i][1] == "D":
                d = (d + 1) % 4

            else:
                d = (d - 1) % 4

            i = i + 1

    # 뱀이 지도 안에 있는지 확인
    if 0 <= nx < field_size and 0 <= ny < field_size:

        # 뱀의 머리가 꼬리에 부딪치면
        if [ny, nx] in snakes:
            break

        else:
            snakes.append([ny, nx])

            # 뱀 앞에 사과가 있는 경우
            if fields[ny][nx] == 1:
                fields[ny][nx] = 0

            # 뱀 앞에 사과가 없는 경우
            elif fields[ny][nx] == 0:
                snakes.pop(0)

            y = ny
            x = nx

    else:
        break


print(count)
