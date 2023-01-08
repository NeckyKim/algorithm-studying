# Q04-1. 만들 수 없는 금액


n = int(input())

coins = list(map(int, input().split()))
coins.sort()


target = 1

for coin in coins:
    
    # 만들 수 없는 금액을 찾으면 반복문 종료
    if target < coin:
        break
    target = target + coin
    
    
# 만들 수 없는 금액 출력
print(target)