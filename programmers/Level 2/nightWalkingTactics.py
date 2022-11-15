# Programmers 11/15 2022
# 야간 보행 전술

def solution(distance, scope, times):
    
    answer = distance
    for i in range(len(scope)):
        if scope[i][0] > scope[i][1]:
            scope[i].sort()
        for j in range(scope[i][0], scope[i][1]+1, 1):
            if 0 < j % (times[i][0] + times[i][1]) <= times[i][0]:
                if answer > j:
                    answer = j
    return answer