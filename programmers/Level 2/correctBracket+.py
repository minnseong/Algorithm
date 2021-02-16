# Programmers 02/16 2021
# 올바른 괄호
# 효율성 테스트 1 실패

def solution(s):
    s = list(s)
    stk = []
    for i in s:
        if i == "(":
            stk.append(i)
        elif i == ")":
            if len(stk) == 0:
                return False
            stk.pop()

    if len(stk) == 0:
        return True
    else:
        return False

print(solution("((())"))