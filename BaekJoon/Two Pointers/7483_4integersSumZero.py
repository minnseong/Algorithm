# BaekJoon 01/04 2022
# 7483 합이 0인 네 정수

import sys

n = int(input())
A, B, C, D = [], [], [], []
cnt = 0

for _ in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    A.append(s[0]); B.append(s[1]); C.append(s[2]); D.append(s[3])

AB, CD = [], {}

for i in range(len(A)):
    for j in range(len(A)):
        AB.append(A[i]+B[j])
        
        if C[i]+D[j] in CD:
            CD[C[i]+D[j]] += 1
        else:
            CD[C[i]+D[j]] = 1

for ab in AB:
    if ab*(-1) in CD:
        cnt += CD[ab*(-1)]

print(cnt)
