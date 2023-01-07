# Q35-2. 못생긴 수


n = int(input())


# 다이내믹 프로그래밍 테이블 초기화
dp = [1, 2, 3, 5]


for i in range(0, 1000):
    try:
        array = []
        
        # 2배, 3배, 5배 곱한 수를 추가
        array.append(dp[i] * 2)
        array.append(dp[i] * 3)
        array.append(dp[i] * 5)

        dp = dp + array
        
        # 집합으로 변경하여 중복을 제거
        dp = list(set(dp))
        
        dp.sort()
    
    except:
        pass
    
print(dp[n - 1])    