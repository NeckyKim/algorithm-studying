# 3-1. 거스름돈


price = int(input())


def solution(price):
    count = 0

    # 동전의 종류
    # 큰 동전의 종류가 작은 동전의 배수일 때, 최적의 해를 보장
    coins = [500, 100, 50, 10]

    for i in coins:
        count = count + price // i
        price = price % i

    return count


print(solution(price))
