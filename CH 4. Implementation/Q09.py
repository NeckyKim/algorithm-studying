# Q09. 문자열 압축
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    # 압축한 문자열을 보관
    results = []

    # 압축 단위 최소: 1
    # 압축 단위 최대: 문자열 길이(len(s))
    for size in range(1, len(s) + 1):
        compressed = ""

        # 개수 체크
        count = 1

        # 이전 문자열
        prev = s[0: size]

        # 압축 단위만큼 이동해서 현재 문자열과 이전 문자열을 비교
        for i in range(size, len(s) + size, size):

            # 현재 문자열과 이전 문자열이 같은 경우
            if s[i: i + size] == prev:
                count = count + 1

            # 현재 문자열과 이전 문자열이 다른 경우
            else:

                # 개수가 1이면 숫자를 붙이지 않음
                if count == 1:
                    compressed = compressed + prev

                # 개수가 1보다 크면 숫자를 붙임
                else:
                    compressed = compressed + str(count) + prev

                prev = s[i: i + size]
                count = 1

        results.append(len(compressed))

    return min(results)
