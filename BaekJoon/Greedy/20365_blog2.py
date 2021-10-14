# BaekJoon 10/14 2021
# 20365 블로그2

N = int(input())
color = list(input())
Bcnt = color.count('B')
Rcnt = color.count('R')
res = 1

if Bcnt >= Rcnt:
    for i in range(len(color)):
        if color[i] == 'R':
            if color[i-1] != 'R':
                res += 1
else:
    for i in range(len(color)):
        if color[i] == 'B':
            if color[i-1] != 'B':
                res += 1

print(res)
