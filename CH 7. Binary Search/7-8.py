# 7-8. 떡볶이 떡


# 떡의 개수와 요청한 떡의 길이 입력 받기
n, m = map(int, input().split())

# 떡의 개별 높이 입력 받기
ddeoks = list(map(int, input().split()))

# 이진 탐색을 위해 시작과 끝 지정
start = 0
end = max(ddeoks)


answer = 0

# 이진 탐색 수행
while start <= end:
    mid = (start + end) // 2

    total = 0

    # 잘랐을 때 떡의 양 계산
    for ddeok in ddeoks:
        if ddeok > mid:
            total = total + ddeok - mid

    # 떡의 양이 부족하면, 더 많이 자르기(end를 왼쪽으로 이동)
    if total < m:
        end = mid - 1

    # 떡의 양이 충분하면, 더 적게 자르기(start를 오른쪽으로 이동)
    else:

        # 정답을 기록
        answer = mid
        start = mid + 1


# 정답 출력
print(answer)
