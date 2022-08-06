# 08/06 2022 
# 2022 토스 NEXT 개발자 챌린지 - Q3

from itertools import permutations

def solution(k, dungeons):
    answer = -1

    permu = list(permutations(dungeons, len(dungeons)))
    tmpK = k

    for p in permu:
        cnt = 0
        for pp in p:
            if tmpK >= pp[0]:
                cnt += 1
                tmpK -= pp[1]
    
        if cnt > answer:
            answer = cnt
        tmpK = k

    return answer