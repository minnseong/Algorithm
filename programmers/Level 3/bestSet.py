# Programmers 07/13 2022
# 최고의 집합

def solution(n, s):
    if n > s:
        return [-1]
    
    div, mod = divmod(s, n)
    answer = [div] * n
    for i in range(mod):
        answer[i] += 1
    return sorted(answer)

print(solution(2, 9))

'''
from itertools import combinations_with_replacement

def multiple(arr):
    res = 1
    for a in arr:
        res *= a
    return res

def solution(n, s):
    answer = []

    rg = [i for i in range(1, s+1)]
    combi = combinations_with_replacement(rg, n)
    print(list(combi))
    maxMulti = 0
    for c in list(combi):
        if sum(c) == s:
            if maxMulti < multiple(c):
                maxMulti = multiple(c)
                answer = list(c)

    return answer
'''