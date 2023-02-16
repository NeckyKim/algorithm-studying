# Q25. 실패율
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    cleared = [0] * (N + 1)

    # 각 스테이지 마다 도달한 플레이어 수 계산
    for i in range(0, len(stages)):
        cleared[stages[i] - 1] = cleared[stages[i] - 1] + 1

    ratio = []

    # 각 스테이지의 실패율 계산
    for i in range(0, len(cleared) - 1):
        try:
            ratio.append([i + 1, cleared[i] / sum(cleared[i:])])

        except:
            ratio.append([i + 1, 0])

    # 각 스테이지의 실패율을 기준으로 정렬
    ratio.sort(key=lambda x: (1 - x[1], x[0]))

    # 스테이지의 번호 출력
    return [r[0] for r in ratio]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
