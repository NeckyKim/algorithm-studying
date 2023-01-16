# 3-3. 숫자 카드 게임


n, m = map(int, input().split())

cards = []

for i in range(0, n):
    cards.append(list(map(int, input().split())))


def solution(cards):
    answer = cards[0]

    for cur in cards:
        if min(cur) > min(answer):
            answer = cur

    return min(answer)


print(solution(cards))
