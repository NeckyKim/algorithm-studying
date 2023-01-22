# Q26. 카드 정렬하기
# [백준] https://www.acmicpc.net/problem/1715


import heapq

n = int(input())


# 힙(heap)에 초기 카드 묶음을 모두 삽입
cards = []

for _ in range(0, n):
    heapq.heappush(cards, int(input()))


result = 0


# 힙에 원소가 1개 남을 때 까지 반복
while len(cards) != 1:

    # 가장 작은 두 개의 카드 꺼내기
    one = heapq.heappop(cards)
    two = heapq.heappop(cards)

    # 두 카드를 합쳐서 다시 삽입
    sum_value = one + two

    result = result + sum_value
    heapq.heappush(cards, sum_value)

print(result)
