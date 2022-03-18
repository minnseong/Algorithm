# BaekJoon 03/18 2022
# 1092 배
# python3 시간초과, pypy 성공

import sys
input = sys.stdin.readline

n = int(input())
crain = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
box = sorted(list(map(int, input().split())), reverse=True)

if max(box) > max(crain):
    print(-1)
else:
    time = 0
    while box:
        for c in crain:
            for b in box:
                if c >= b:
                    box.remove(b)
                    break
        time += 1
    print(time)