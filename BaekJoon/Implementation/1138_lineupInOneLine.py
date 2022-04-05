# BaekJoon 04/05 2022
# 1138 한 줄로 서기

n = int(input())
info = list(map(int, input().split()))

line = [0] * n
line[info[0]] = 1

for i in range(1, n):
    idx = info[i]
    while True:
        if line[idx] == 0 and line[:idx].count(0) == info[i]:
            line[idx] = i+1
            break
        idx += 1

print(*line)