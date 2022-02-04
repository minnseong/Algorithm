# BaekJoon 02/04 2022
# 15787 기차가 어둠을 헤치고 은하수를

import sys

input = sys.stdin.readline
N, M = map(int, input().split())


train = [['x']*20 for _ in range(N)]

for _ in range(M):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        train[cmd[1]-1][cmd[2]-1] = 'o'
    elif cmd[0] == 2:
        train[cmd[1]-1][cmd[2]-1] = 'x'
    elif cmd[0] == 3:
        train[cmd[1]-1][1:] = train[cmd[1]-1][:-1]
        train[cmd[1]-1][0] = 'x'
    else:  
        train[cmd[1]-1][:-1] = train[cmd[1]-1][1:]
        train[cmd[1]-1][-1] = 'x'

passTrain = set()
for i in range(N):
    passTrain.add(''.join(train[i]))
    
print(len(passTrain))