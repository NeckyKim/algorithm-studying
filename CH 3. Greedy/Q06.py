# Q06. 무지의 먹방 라이브
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/42891


import heapq


def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같으면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐(최소 힙)를 이용
    queue = []

    # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
    for i in range(0, len(food_times)):
        heapq.heappush(queue, (food_times[i], i + 1))


    sum_value = 0   # 먹기 위해 사용한 시간
    previous = 0    # 이전에 다 먹은 음식 시간
    length = len(food_times)    # 남은 음식의 개수


    # ((현재의 음식 시간(queue[0][0]) - 이전에 다 먹은 음식 시간(previous)) * (남은 음식의 개수))와 k를 비교
    while sum_value + (queue[0][0] - previous) * length <= k:
        now = heapq.heappop(queue)[0]

        sum_value = sum_value + (now - previous) * length

        # 다 먹은 음식은 제외
        length = length - 1

        # 이전에 다 먹은 음식 시간 재설정
        previous = now


    result = sorted(queue, key=lambda x: x[1])

    return result[(k - sum_value) % length][1]



