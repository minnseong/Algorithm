# Programmers 03/23 2021
# KaKao 괄호 변환


def isBalance(b):
    cnt = 0
    for i in range(len(b)):
        if b[i] == "(":
            cnt += 1
        else:
            cnt -= 1

    if cnt == 0:
        return True
    else:
        return False


def isCorrect(b):
    stk = []

    for i in range(len(b)):
        if b[i] == "(":
            stk.append(b[i])
        else:
            if not stk:
                return False
            stk.pop()

    if not stk:
        return True
    else:
        return False


def solution(p):

    # step 1
    if not p or isCorrect(p):
        return p

    # step 2
    for i in range(len(p)):
        if isBalance(p[:i+1]):
            u, v = p[:i+1], p[i+1:]
            break

    # step 3
    if isCorrect(u):
        return u + solution(v)
    # step 4
    else:
        pBlank = "(" + solution(v) + ")"
        u = u[1:-1]
        for ui in u:
            if ui == "(":
                pBlank += ")"
            else:
                pBlank += "("

    return pBlank

#print(solution("(()())()"))
print(solution(")("))