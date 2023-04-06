# 10-4. 서로소 집합 알고리즘을 활용한 사이클 판별하기


import sys
sys.stdin = open("CH 10. Graphs/testcase/10-4.in")


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


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
parent = [i for i in range(0, v + 1)]


# 사이클 존재 여부
isCycle = False

# union 연산을 각각 수행
for _ in range(0, e):
    a, b = map(int, input().split())
    
    # 사이클이 발생한 경우 반복문 종료
    if find(a) == find(b):
        isCycle = True
        break
    
    # 사이클이 발생하지 않으면, union 연산 수행
    else:
        union(a, b)


if isCycle:
    print("사이클이 발생했습니다.")
    
else:
    print("사이클이 발생하지 않았습니다.")