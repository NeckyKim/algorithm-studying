# Q02. 곱하기 혹은 더하기


strings = str(input())


def solution(strings):
    numbers = list(map(int, list(strings)))

    # 첫 번째 숫자를 대입
    answer = numbers[0]

    for i in range(1, len(numbers)):

        # 숫자가 0이거나 1이면 더하기 수행
        if answer <= 0 and answer <= 1:
            answer = answer + numbers[i]

        # 그렇지 않으면 곱하기 수행
        else:
            answer = answer * numbers[i]

    return answer


print(solution(strings))
