# BaekJoon 01/10 2022
# 11663 선분 위의 점
import sys

def getPoint(point, line):
    sp, ep = line[0], line[1]
    s, e = 0 , 0

    start, end = 0, len(point)-1
    while start <= end:
        s = (start + end) // 2

        if point[s] >= sp:
            end = s-1
        else:
            start = s+1
    s = end

    start, end = 0, len(point)-1
    while start <= end:
        e = (start + end) // 2

        if point[e] <= ep:
            start = e+1
        else:
            end = e-1
    e = start

    return e-s-1
            
N, M = map(int, input().split())
point = list(map(int, sys.stdin.readline().split()))
point.sort()
line = []
res = []

for _ in range(M):
    line.append(list(map(int, sys.stdin.readline().split())))

for l in line: 
    res.append(getPoint(point, l))

for r in res:
    print(r)