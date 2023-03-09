# BaekJoon 03/09 2023
# 골드3 - 줄 세우기

import sys
from collections import defaultdict

N, M = map(int, input().split())

students = defaultdict(list)

front_count = [0] * (N+1)
front_count[0] = -1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    students[b].append(a)
    front_count[a] += 1

line = list()
line_cnt = 0

while line_cnt < N:
    student = front_count.index(0)
    line.append(student)
    line_cnt+= 1
    front_count[student] = -1
    
    for s in students[student]:
        front_count[s] -= 1

for s in reversed(line):
    print(s, end= " ")