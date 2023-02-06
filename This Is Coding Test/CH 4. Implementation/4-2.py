# 4-2. 시각
# 00시 00분 00초 ~ N시 59분 59초까지의 모든 시각 중에 3이 하나라도 포함되는 모든 경우의 수 구하기


n = int(input())


def solution(n):
    hours = 0
    minutes = 0
    seconds = 0

    count = 0

    for i in range(0, n + 1):
        for j in range(0, 60):
            for k in range(0, 60):

                # 시각에 3이 있는지 확인
                if "3" in str(i).zfill(2) + str(j).zfill(2) + str(k).zfill(2):
                    count = count + 1

    print(count)


solution(n)
