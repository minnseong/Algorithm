# Programmers 01/19 2022
# 피로도
from itertools import permutations

def solution(k, dungeons):

    answer = 0
    pm = list(permutations(dungeons, len(dungeons)))
    tmpK = k

    for p in pm:
        ans = 0
        for pp in p:
            if tmpK >= pp[0]:
                ans += 1
                tmpK -= pp[1]
        
        if ans > answer:
            answer = ans
        tmpK = k

    return answer 

print(solution(80, [[80,20],[50,40],[30,10]]))