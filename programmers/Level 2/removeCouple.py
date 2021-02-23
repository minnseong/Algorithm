# Programmers 02/23 2021
# 짝지어 제거하기

def solution(s):
    answer = 0
    stk = []
    s = list(s)

    for n in s:
        if stk:
            if stk[-1] == n:
                stk.pop()
            else:
                stk.append(n)
        else:
            stk.append(n)

    if stk:
        answer = 0
    else:
        answer = 1

    return answer

print(solution("baabaa"))