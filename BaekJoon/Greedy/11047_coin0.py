# BaekJoon 10/14 2021
# 11047 동전0

N, K = map(int, input().split())
money = [int(input()) for _ in range(N)]
money.sort(reverse=True)
res = 0

for m in money:
    if K == 0:
        break

    elif K >= m:
        res += (K//m)
        K -= ((K//m) * m)

print(res)
