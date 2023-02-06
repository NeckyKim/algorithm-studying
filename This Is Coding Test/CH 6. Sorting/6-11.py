# 6-11. 성적이 낮은 순서로 학생 출력하기


n = int(input())

# n명의 학생 정보를 입력 받음
grades = [list(input().split()) for _ in range(0, n)]


# [이름, 성적]으로 저장된 학생 정보를 성적 기준으로 정렬
grades.sort(key=lambda x: x[1])


# 정렬된 정수 출력
for grade in grades:
    print(grade[0], end=" ")
