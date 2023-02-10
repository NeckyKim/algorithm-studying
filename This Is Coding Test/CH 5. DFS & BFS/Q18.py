# Q18. 괄호 변환
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/60058


# 균형잡힌 문자열의 인덱스를 반환
def balancedIndex(p):
    count = 0
    
    for i in range(0, len(p)):
        if p[i] == "(":
            count = count + 1
            
        else:
            count = count - 1
            
        if count == 0:
            return i
            

# 올바른 괄호 문자열인지 확인
def isRight(p):
    count = 0
    
    for i in range(0, len(p)):
        if p[i] == "(":
            count = count + 1
            
        else:
            # 올바르지 괄호 문자열이 아닌 경우 False 반환
            if count == 0:
                return False
            
            count = count - 1
     
    # 올바르지 괄호 문자열이 아닌 경우 True 반환        
    return True


def solution(p):
    answer = ""
    
    if p == "":
        return answer
    
    index = balancedIndex(p)
    
    u = p[0 : index + 1]
    v = p[index + 1 :]
    
    # 올바른 괄호 문자열이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if isRight(u):
        answer = u + solution(v)
        
    else:
        # 빈 문자열에 "("를 붙이기
        answer = "("
        
        # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        answer = answer + solution(v)
        answer = answer + ")"

        # u의 첫 번째와 마지막 문자를 제거
        u = list(u[1 : -1])
        
        # 나머지 문자열의 괄호 방향을 뒤집기
        for i in range(0, len(u)):
            if u[i] == "(":
                u[i] = ")"
            
            else:
                u[i] = "("
        
        answer = answer + "".join(u)


    return answer        