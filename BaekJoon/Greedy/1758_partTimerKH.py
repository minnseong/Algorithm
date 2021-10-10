# BaekJoon 10/11 2021
# 1758 알바생 강호

N = int(input())
tip = [int(input()) for _ in range(N)]
tip.sort(reverse=True)
money = 0

for i in range(N):
    m = tip[i] - i
    if m > 0:
        money += m

print(money)
