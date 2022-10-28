# Programmers 10/28 2022
# 2022 CJ 올리브네트웍스 Q3

from itertools import combinations
from collections import Counter

def solution(s, n):
    answer = 300000

    for combi in combinations(range(1, len(s)-1), n):
        cnt = 0
        for idx, c in enumerate(combi):
            if idx == 0:
                counter = Counter(s[:c])
                for ss in list(set(s[:c])):
                    cnt = max(cnt, counter[ss])   
            else:
                counter = Counter(s[combi[idx-1]:c])
                for ss in list(set(s[combi[idx-1]:c])):
                    cnt = max(cnt, counter[ss])

        counter = Counter(s[combi[-1]:])
        for ss in list(set(s[combi[-1]:])):
            cnt = max(cnt, counter[ss])

        answer= min(cnt, answer)

    return answer