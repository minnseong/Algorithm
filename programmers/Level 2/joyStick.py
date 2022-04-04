# Programmers 04/04 2022
# 조이 스틱

import copy

def terminationCondition(visited):
    flag = True
    for v in visited:
        if not v:
            flag = False
            break
    return flag

def maxIndexExcess(idx, length):
    if idx == length:
        return 0
    else:
        return idx

def solution(name):
    move = []
    operationCnt = [min(ord(n)-ord('A'), ord('Z')-ord(n)+1) for n in name]

    # visited, 커서, 방향, moveCnt
    # 종료 조건이 0인 지점외에 다 거쳐서 지나갓다면??
    def tracking(visited, cur, dir, moveCnt):
        visited_ = copy.deepcopy(visited)

        if terminationCondition(visited_):
            move.append(moveCnt)
            return;
        if moveCnt > len(name):
            return;
        
        while True:
            visited_[cur] = True

            if terminationCondition(visited_):
                move.append(moveCnt)
                break

            if operationCnt[cur] != 0 and (operationCnt[cur-1] == 0 or operationCnt[maxIndexExcess(cur+1, len(name))] == 0):
                moveCnt += 1
                tracking(visited_, cur+1, 1, moveCnt)
                tracking(visited_, cur-1, -1, moveCnt)
                return;
            else:
                moveCnt += 1
                if dir == 1:
                    cur += 1
                else:
                    cur -= 1

    visited = [False if c != 0 else True for c in operationCnt]
    if 'A' not in name:
        return sum(operationCnt) + len(name) - 1
    
    tracking(visited, 0, 1, 0)
    tracking(visited, 0, -1, 0)
    # print(move)
    return sum(operationCnt) + min(move)
    
print(solution("JEROEN"))