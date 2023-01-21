# 6-12. 두 배열의 원소 교체


m, n = map(int, input().split())

# 배열 A, B를 입력 받음
a = list(map(int, input().split()))
b = list(map(int, input().split()))


# A는 오름차순 정렬 수행
a.sort()

# B는 내림차순 정렬 수행
b.sort(reverse=True)


# 두 배열의 원소를 최대 n번 비교
for i in range(0, n):

    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:

        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]

    # A의 원소가 B의 원소보다 크거나 같으면, 반복문을 탈출
    else:
        break


# 배열 A 모든 원소의 합을 출력
print(sum(a))
