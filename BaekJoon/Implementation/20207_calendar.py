# BaekJoon 02/06 2022
# 20207 달력

N = int(input())
calendar = [0]*365
res = 0

cl = [list(map(int, input().split())) for _ in range(N)]

for c in cl:
    s, e = c 
    for i in range(s-1, e):
        calendar[i] += 1

w, h = 0, 0
i = 0
while i < 365: 
    c = calendar[i]

    if c == 0:
        res += (w*h)
        w, h = 0 ,0
    else:
        w += 1
        h = max(h, c)
    
    i += 1

res += (w*h)
print(res)