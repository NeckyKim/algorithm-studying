# 4-3. 왕실의 나이트
# 행: 1 ~ 8, 열: a ~ c


location = input()


def solution(location):
    # 알파벳으로 이루어진 열을 좌표로 변환
    x = ["a", "b", "c", "d", "e", "f", "g", "h"].index(location[0]) + 1
    y = int(location[1])

    count = 0

    # 나이트가 이동할 수 있는 모든 경우의 수
    dx = [2, 2, 1, 1, -2, -2, -1, -1]
    dy = [-1, 1, -2, 2, -1, 1, -2, 2]

    # 이동 방향 확인
    for i in range(0, 8):

        # 이동 후, 공간 안에 있는지 확인
        if (x + dx[i] >= 1 and x + dx[i] <= 8) and (y + dy[i] >= 1 and y + dy[i] <= 8):
            count = count + 1

    print(count)


solution(location)
