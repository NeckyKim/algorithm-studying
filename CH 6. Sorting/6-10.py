# 6-10. 위에서 아래로


n = int(input())

numbers = [int(input()) for _ in range(0, n)]

numbers.sort(reverse=True)

for number in numbers:
    print(number, end=" ")
