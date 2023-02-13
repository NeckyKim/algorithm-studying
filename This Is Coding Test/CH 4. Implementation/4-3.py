# 4-3. 왕실의 나이트


def solution(location):
    # 알파벳으로 이루어진 열을 좌표로 변환
    x = ["a", "b", "c", "d", "e", "f", "g", "h"].index(location[0])
    y = int(location[1]) - 1

    count = 0

    # 나이트가 이동할 수 있는 모든 경우의 수
    dx = [2, 2, 1, 1, -2, -2, -1, -1]
    dy = [-1, 1, -2, 2, -1, 1, -2, 2]

    # 이동 방향 확인
    for i in range(0, 8):
        nx = x + dx[i]
        ny = y + dy[i]

        # 이동 후, 공간 안에 있는지 확인
        if 0 <= nx < 8 and 0 <= ny < 8:
            count = count + 1

    print(count)


solution("a1")
solution("c2")
