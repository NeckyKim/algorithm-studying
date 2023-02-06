# 7-6. 부품 찾기(계수 정렬)


# 부품의 개수 입력 받기
n = int(input())

# 부품 입력 받기
parts = [0] * 100001

for i in input().split():
    parts[int(i)] = 1


# 주문의 개수 입력 받기
m = int(input())

# 주문 입력 받기
orders = list(map(int, input().split()))


# 부품을 하나씩 확인
for order in orders:
    if parts[order]:
        print("yes", end=" ")

    else:
        print("no", end=" ")
