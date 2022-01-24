# Programmers 01/24 2022
# KaKao 양궁대회

from itertools import *
from collections import *

def solution(n, info):
    answer = [0] * 11
    maxdiff = 0
    maxComb = []

    for comb in combinations_with_replacement(range(11), n):
        apeach, lion = 0, 0
        counter = Counter(comb)
        for i in range(len(info)):
            if info[i] == 0 and counter[10-i] == 0:
                continue
            
            if info[i] >= counter[10-i]:
                apeach += (10-i)
            else:
                lion += (10-i)

        if lion - apeach > maxdiff:
            maxdiff = lion - apeach
            maxComb = comb
    
    if maxdiff == 0:
        answer = [-1]
    else:
        for c in maxComb:
            answer[10-c] += 1

    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
#print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
