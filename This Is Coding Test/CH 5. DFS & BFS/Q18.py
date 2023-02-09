# Q18. 괄호 변환
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/60058


def isRight(p):
    p = list(p)
    stack = []
    
    while p:
        x = p.pop(0)
        
        if stack and stack[-1] == "(" and x == ")":
            stack.pop()
            
        else:
            stack.append(x)
            
    return stack == []


def solution(p):
    def myfunc(p):
        for i in range(0, len(p)):
            if isRight(p[0 : i]):
                u = p[0 : i]
                v = p[i + 1 : ]
                
                myfunc(u)
                
        
            
    
solution("(()())()")