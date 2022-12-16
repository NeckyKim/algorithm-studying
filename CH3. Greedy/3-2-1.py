# 3-2-1. 모험가 길드


number = int(input())
fear = list(map(int, input().split()))


def solution(fear):
    fear.sort()

    count = 0

    # 남은 모험가의 수가 가장 높은 공포도를 가진 모험가의 공포도보다 커야 함
    while len(fear) >= max(fear):
        members = fear[0]

        for i in range(0, members):
            fear.pop(0)

        count = count + 1

    return count


print(solution(fear))
