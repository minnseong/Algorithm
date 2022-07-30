# BaekJoon 07/29 2022
# 2493 탑

import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))
stack = [[0, tops[0]]]
res = [0]

for i in range(1, n):
    if stack and stack[-1][1] > tops[i]:
        res.append(stack[-1][0]+1)
    else:
        while stack:
            stack.pop()
            if stack and stack[-1][1] > tops[i]:
                res.append(stack[-1][0]+1)
                break
        if not stack:
            res.append(0)
    stack.append([i, tops[i]])

print(*res)