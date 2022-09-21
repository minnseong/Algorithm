# Programmers 09/21 2022
# Level 2 - 위장

from collections import defaultdict

def solution(clothes):
    
    dict = defaultdict(list)
    
    for c in clothes:
        dict[c[1]].append(c[0])
    
    result = 1
    
    for v in dict.values():
        result *= (len(v)+1)
        
    return result - 1