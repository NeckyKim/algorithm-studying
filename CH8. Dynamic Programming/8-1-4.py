# 8-1-4. 피보나치 수열
# 반복적 풀이법


n = int(input())

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
memo = [0] * (n + 1)

# 첫 번째와 두 번째 피보나치 수는 1
memo[1] = 1
memo[2] = 1


# 피보나지 함수를 반복문으로 구현
for i in range(3, n + 1):
    memo[i] = memo[i - 1] + memo[i - 2]
    
    
print(memo[n])