# Programmers 09/09 2022 다시 풀어보기 (코테 준비)
# KaKao 양궁대회

from itertools import combinations_with_replacement
from collections import defaultdict

def solution(n, info):
    
    max_score = 0
    result = 0
    
    for combi in reversed(list(combinations_with_replacement(range(11), n))):
        dict = defaultdict(int)
        for c in combi:
            dict[c] += 1
        
        lion_info = []
        for i in range(10, -1, -1):
            lion_info.append(dict.get(i, 0))
        
        apeach_score = 0
        lion_score = 0
        for i in range(11):
            if info[i] < lion_info[i]:
                lion_score += (10-i)
            elif info[i] != 0:
                apeach_score += (10-i)
        diff = lion_score-apeach_score
        if max(max_score, diff, 0) == diff:
            max_score = diff
            result = lion_info
            
    if max_score > 0:
        return result
    else:
        return [-1]

# Programmers 01/24 2022
# KaKao 양궁대회

from itertools import *
from collections import *

def solution(n, info):
    answer = [0] * 11
    maxdiff = 0
    maxComb = []

    for comb in combinations_with_replacement(range(11), n):
        print(comb)
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
