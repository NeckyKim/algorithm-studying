# Q05-2. 볼링공 고르기


n, m = map(int, input().split())

balls = list(map(int, input().split()))
balls.sort()

count = 0

# 첫 번째 공을 선택
for i in range(0, len(balls)):
    
    # 두 번째 공을 선택
    for j in range(i, len(balls)):
        
        # 첫 번째와 두 번째 공이 같지 않으면 경우의 수 포함
        if balls[i] != balls[j]:
            count = count + 1
            
            
print(count)
