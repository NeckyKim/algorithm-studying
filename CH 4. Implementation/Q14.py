# Q14. 외벽 점검


from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)

    # 원형 벽을 일자 형태로 변환
    weak = weak + [(w + n) for w in weak]
        
    # 투입할 친구 수의 최솟값
    answer = len(dist) + 1
    
    
    for start in range(0, length):
        
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            
            # 투입해야 할 친구의 수
            count = 1
            
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            
            # 시작점부터 모든 취약 지점 확인
            for i in range(start, start + length):
                
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[i]:
                    
                    # 새로운 친구를 투입
                    count = count + 1
                    
                    # 더 투입이 불가능하면 종료
                    if count > len(dist):
                        break
                        
                    position = weak[i] + friends[count - 1]
            
            # 최솟값 계산
            answer = min(answer, count)
            
    if answer > len(dist):
        return -1
    
    return answer



print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))