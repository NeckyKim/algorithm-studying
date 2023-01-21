# Q24. 안테나
# [백준] https://www.acmicpc.net/problem/18310


n = int(input())

# 집의 위치를 입력 받음
houses = list(map(int, input().split()))


# 집의 위치를 정렬
houses.sort()
         
# 중간값을 출력                
print(houses[(n - 1) // 2])
        