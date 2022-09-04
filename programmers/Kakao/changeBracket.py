# Programmers 09/05 2022 다시 풀어보기 (코테 준비)
# KaKao 괄호 변환

def isBalance(p):
    openCnt = 0
    closeCnt = 0
    
    for i in range(len(p)):
        if p[i] == "(":
            openCnt += 1
        elif p[i] == ")":
            closeCnt += 1
    
    return openCnt == closeCnt

def isCorrect(p):
    stack = []
    
    for i in range(len(p)):
        if not stack:
            if p[i] == ")":
                return False
            elif p[i] == "(":
                stack.append("(")
        else:
            if p[i] == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(p[i])
    
    if not stack:
        return True
    else:
        return False
    
def logic(p):
    if p == "":
        return ""
    
    for i in range(1, len(p)+1):
        if (isBalance(p[:i])):
            u = p[:i]
            v = p[i:]
            break
    
    if isCorrect(u):
        return u + logic(v)
    else:
        tmp = ""
        for i in range(1, len(u)-1):
            if u[i] == "(":
                tmp += ")"
            else:
                tmp += "("
            
        return "(" + logic(v) + ")" + tmp
    
def solution(p):
    return logic(p)

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