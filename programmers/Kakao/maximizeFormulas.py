# Programmers 01/17 2022
# KaKao 수식 최대화
from itertools import permutations

def solution(expression):
    answer = []
    expr = []
    op = set()

    i = -1
    for idx in range(len(expression)):
        if not expression[idx].isdigit():
            expr.append(expression[i+1:idx])
            expr.append(expression[idx])
            i = idx
            op.add(expression[idx])
    expr.append(expression[i+1:])

    op = list(op)
    pmOP = list(permutations(op, len(op)))

    for p in pmOP:
        tmp = expr.copy()
        for pp in p:
            t = 0
            while t < len(tmp):
                if tmp[t] == pp:
                    tmp[t] = str(eval(tmp[t-1]+tmp[t]+tmp[t+1]))
                    del tmp[t-1]
                    del tmp[t]
                    t -= 1
                t += 1

        answer.append(abs(int(tmp[0])))    

    return max(answer)

print(solution("50*6-3*2"))