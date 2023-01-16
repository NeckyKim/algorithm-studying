# Q05. 볼링공 고르기


n, m = map(int, input().split())

balls = list(map(int, input().split()))


# 1부터 10까지의 무게를 담을 수 있는 리스트
weights = [0] * 11


# 각 무게에 해당하는 볼링공의 개수 카운트
for ball in balls:
    weights[ball] = weights[ball] + 1
    

result = 0


# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    
    # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    n = n - weights[i]
    
    # B가 선택하는 경우의 수와 곱하기
    result = result + weights[i] * n
    

print(result)