# 4-2. 시각


def solution(n):
    count = 0

    for i in range(0, n + 1):
        for j in range(0, 60):
            for k in range(0, 60):

                # 시각에 3이 있는지 확인
                if "3" in str(i) + str(j) + str(k):
                    count = count + 1

    print(count)


solution(int(input()))
