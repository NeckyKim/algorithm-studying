# Q12. 기둥과 보 설치
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/60061


def isPossible(answer):
    for x, y, stuff in answer:

        # 기둥이 설치되었을 때
        if stuff == 0:
            if (
                y == 0 or                       # 바닥 위에 있을 때
                [x - 1, y, 1] in answer or      # 보의 한쪽 끝 부분 위에 있을 때
                [x, y, 1] in answer or          # 보의 한쪽 끝 부분 위에 있을 때
                [x, y - 1, 0] in answer         # 다른 기둥 위에 있을 때
            ):
                continue
            return False

        # 보가 설치되었을 때
        elif stuff == 1:
            if (
                [x, y - 1, 0] in answer or      # 한쪽 끝 부분이 기둥 위 일 때
                [x + 1, y - 1, 0] in answer or  # 한쪽 끝 부분이 기둥 위 일 때
                ([x - 1, y, 1] in answer and [x + 1, y, 1]
                 in answer)  # 양쪽 끝 부분이 다른 보와 동시에 연결되어있을 때
            ):
                continue
            return False

        return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, command = frame

        # 삭제하는 경우
        if command == 0:

            # 일단 삭제해 봄
            answer.remove([x, y, stuff])

            # 삭제한 뒤 가능한 구조물이 아니면 다시 복구
            if not isPossible(answer):
                answer.append([x, y, stuff])

        # 설치하는 경우
        if command == 1:

            # 일단 설치해 봄
            answer.append([x, y, stuff])

            # 설치한 뒤 가능한 구조물이 아니면 다시 복구
            if not isPossible(answer):
                answer.remove([x, y, stuff])

    return sorted(answer)
