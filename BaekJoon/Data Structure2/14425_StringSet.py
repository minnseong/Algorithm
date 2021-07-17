import sys

N, M = map(int, input().split())
strSet = []
cnt = 0

for i in range(N):
    strSet.append(sys.stdin.readline().strip())

for i in range(M):
    tmp = sys.stdin.readline().strip()
    if tmp in strSet:
        cnt += 1

print(cnt)