# 3-3. 숫자 카드 게임


def solution(cards):
    answer = cards[0]

    for cur in cards:
        if min(cur) > min(answer):
            answer = cur

    return min(answer)


n, m = map(int, input().split())

cards = [list(map(int, input().split())) for _ in range(0, n)]


print(solution(cards))
