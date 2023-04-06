# 10-3. 서로소 집합 알고리즘


import sys
sys.stdin = open("CH 10. Graphs/testcase/10-3.in")


# 원소가 속한 집합을 찾기
def find(x):
    if parent[x] == x:
        return x

    # 루트 노드가 아니면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    return find(parent[x])


# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b


# 노드의 개수와 간선의 개수
v, e = map(int, input().split())

# 부모 테이블을 자기 자신으로 초기화
parent = [i for i in range(0, v + 1)]


# union 연산을 각각 수행
for _ in range(0, e):
    a, b = map(int, input().split())
    union(a, b)


# 각 원소가 속한 집합 출력
for i in range(1, v + 1):
    print(find(i), end=" ")
print()


# 부모 테이블 내용 출력
for i in range(1, v + 1):
    print(parent[i], end=" ")
