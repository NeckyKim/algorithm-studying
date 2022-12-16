# 4-2-2. 문자열 재정렬
# 모든 알파벳을 오름차순으로 정렬하여 출력하고, 뒤에 모든 숫자를 더한 값을 이어서 출력


strings = input()


def solution(strings):
    strings = list(strings)

    letters = []
    numbers = 0

    # 각 자리가 숫자인지 문자열인지 분류
    for i in strings:
        if i.isalpha():
            letters.append(i)
        else:
            numbers = numbers + int(i)

    # 문자열 정렬
    letters.sort()

    # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
    if numbers != 0:
        print("".join(letters) + str(numbers))

    else:
        print("".join(letters) + "0")


solution(strings)
