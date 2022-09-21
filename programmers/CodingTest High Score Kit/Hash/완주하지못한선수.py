# Programmers 09/21 2022
# Level 1 - 완주하지못한선수

from collections import defaultdict

def solution(participant, completion):
    
    dict = defaultdict(int)
    for p in participant:
        dict[p] += 1
    
    for c in completion:
        if dict[c] == 1:
            del dict[c]
        else:
            dict[c] -= 1
    
    for k in dict.keys():
        return k