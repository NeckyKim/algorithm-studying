# 7-7. 부품 찾기(집합 자료형)


# 부품의 개수 입력 받기
n = int(input())

# 부품 입력 받기
parts = set(map(int, input().split()))


# 주문의 개수 입력 받기
m = int(input())

# 주문 입력 받기
orders = list(map(int, input().split()))


# 부품을 하나씩 확인
for order in orders:
    if order in parts:
        print("yes", end=" ")

    else:
        print("no", end=" ")
