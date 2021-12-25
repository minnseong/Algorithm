# BaekJoon 12/26 2021
# 21921 블로그

N, X  = map(int, input().split())
visit = list(map(int, input().split()))

maxVisit = 0
cnt = 0

j = 0
tmp = 0
for i in range(0, N-X+1):
    if i == 0:
        tmp = sum(visit[i:i+X])
        maxVisit = tmp
        cnt = 1
    else:
        tmp = tmp - visit[j] + visit[i+X-1]
        j+= 1
        if tmp > maxVisit:
            maxVisit = tmp
            cnt = 1
        elif tmp == maxVisit:
            cnt += 1

if maxVisit == 0:
    print('SAD')
else:
    print(maxVisit)
    print(cnt)