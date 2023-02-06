# 6-10. 위에서 아래로


n = int(input())

# n개의 정수를 입력받음
numbers = [int(input()) for _ in range(0, n)]


# 정렬 수행
numbers.sort(reverse=True)


# 정렬된 정수 출력
for number in numbers:
    print(number, end=" ")
