# Q23. 국영수
# [백준] https://www.acmicpc.net/problem/10825


n = int(input())

grades = []


# 학생들의 정보를 입력 받음
for _ in range(0, n):
    temp = input().split()
    grades.append([temp[0], int(temp[1]), int(temp[2]), int(temp[3])])


# 두 번째 원소를 기준으로 내림차순 정렬: -x[1]
# 세 번째 원소를 기준으로 오림차순 정렬: x[2]
# 네 번째 원소를 기준으로 내림차순 정렬: -x[3]
# 첫 번째 원소를 기준으로 오림차순 정렬: x[0]
grades.sort(key=lambda x: (100 - x[1], x[2], 100 - x[3], x[0]))


for grade in grades:
    print(grade[0])
