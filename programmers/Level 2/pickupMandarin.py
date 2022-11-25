# Programmers 11/25 2022
# 귤 고르기

from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    
    fruits = defaultdict(int)
    for t in tangerine:
        fruits[t] += 1
        
    arr = sorted([value for value in fruits.values()], reverse=True)
    
    for a in arr:
        k -= a
        answer += 1
        if k <= 0:
            break
    
    return answer