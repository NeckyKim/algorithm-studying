# Q03-2. 문자열 뒤집기


numbers = [int(i) for i in list(input())]


# number의 원소들을 0과 1을 분리하여 담을 리스트
splited = []

init = 0


# 0과 1을 분리
for i in range(0, len(numbers)):
    try:
        if numbers[i] != numbers[i - 1] and numbers[init: i] != []:
            splited.append(numbers[init: i])
            init = i

        if i == len(numbers) - 1:
            splited.append(numbers[init:])

    except:
        pass


count0 = 0
count1 = 0


for i in splited:
    if i.count(0):
        count0 = count0 + 1

    if i.count(1):
        count1 = count1 + 1


print(min(count0, count1))
