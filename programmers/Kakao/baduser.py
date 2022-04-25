# Programmers 04/25 2022
# 불량 사용자

from itertools import permutations

def match(user, ban):
    for u, b in zip(user, ban):
        if len(u) != len(b):
            return False
        
        for i in range(len(u)):
            if u[i] == b[i] or b[i] == '*':
                continue
            else:
                return False
    return True


def solution(user_id, banned_id):
    answer = 0
    banned_set = []
    
    for p in permutations(user_id, len(banned_id)):
        if match(p, banned_id):
            if set(p) not in banned_set:
                banned_set.append(set(p))

    return len(banned_set)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
