# Q04-2. 만들 수 없는 금액


n = int(input())

coins = list(map(int, input().split()))
coins.sort()
coins = coins[::-1]


def makeAmount(amount):
    for coin in coins:
        if amount >= coin:
            amount = amount - coin

    return amount == 0


amount = 1

while True:
    if not(makeAmount(amount)):
        print(amount)
        break

    else:
        amount = amount + 1
