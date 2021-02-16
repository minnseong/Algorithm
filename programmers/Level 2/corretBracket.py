# Programmers 02/16 2021
# 올바른 괄호
# 효율성 테스트 1 실패

def solution(s):
    s = list(s)
    cnt = 0
    stk = []

    if s[0] == ")":
        return False
    if s.count('(') != s.count(')'):
        return False

    while True:
        if not s:
            break
        stk.append(s.pop(0))
        cnt += 1

        if stk.count("(") == cnt:
            continue

        for i in range(cnt-2, len(stk)-1):
            if stk[i] == "(" and stk[i+1] == ")":
                stk.pop()
                stk.pop()
                cnt -= 2

    if stk:
        return False
    else:
        return True


print(solution("((()))"))