# BaekJoon 10/13 2021
# 11399 ATM

N = int(input())
time = list(map(int, input().split()))
time.sort(reverse=True)
res = 0

for i in range(N):
    res += (time[i] * (i+1))

print(res)
