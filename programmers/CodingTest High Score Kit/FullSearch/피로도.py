from itertools import permutations

def solution(k, dungeons):
    
    result = 0
    for permu in list(permutations(dungeons, len(dungeons))):
        tmp_k = k
        tmp_cnt = 0
        for p in permu:
            if p[0] <= tmp_k:
                tmp_cnt += 1
                tmp_k -= p[1]
            else:
                break
        result = max(result, tmp_cnt)
        
    return result

