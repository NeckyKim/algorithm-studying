# Q13. 치킨 배달
# [백준] https://www.acmicpc.net/problem/15686


from itertools import combinations


n, m = map(int, input().split())

# 도시의 정보
city = [list(map(int, input().split())) for _ in range(0, n)]

# 집의 위치
houses = []

# 치킨집의 위치
chickens = []

for i in range(0, n):
    for j in range(0, n):
        if city[i][j] == 1:
            houses.append([i, j])
            
        elif city[i][j] == 2:
            chickens.append([i, j])
            

# 모든 치킨집중 m개의 치킨집을 뽑는 조합
chickens_combinations = list(combinations(chickens, m))


# 치킨 거리의 합을 계산
def getDistance(cc):
    distance = 0
    
    # 모든 집에 대해서
    for hx, hy in houses:
        temp = 1e9
        
        # 가장 가까운 치킨집을 찾기
        for cx, cy in cc:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        
        # 가장 가까운 치킨집의 치킨 거리를 더하기    
        distance = distance + temp
        
    return distance


answer = 1e9

# 치킨 거리의 합의 최소를 찾기
for cc in chickens_combinations:
    answer = min(answer, getDistance(cc))
    

print(answer)   
    