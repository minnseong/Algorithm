# BaekJoon 10/27 2021
# 13164 행복 유치원

N, K = map(int, input().split())
member = list(map(int, input().split()))
dif = []
res = 0

if N == K:
    print(res)
else:
    for i in range(1, N):
        dif.append(member[i] - member[i-1])
    dif.sort()

    for i in range(N-K):
        res += dif[i]
    print(res)
