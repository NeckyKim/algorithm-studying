# 6-11. 성적이 낮은 순서로 학생 출력하기


n = int(input())

grades = [list(input().split()) for _ in range(0, n)]

grades.sort(key=lambda x: x[1])


for grade in grades:
    print(grade[0], end=" ")
