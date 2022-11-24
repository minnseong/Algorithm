# Programmers 11/24 2022
# 햄버거 만들기

def solution(ingredient):
    
    answer = 0

    if len(ingredient) <= 3:
        return answer
    
    stack = []
    
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        
        if len(stack) >= 4 and ingredient[i] == 1:
            if stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1
    
    return answer