# BaekJoon 02/16 2022
# 14719 빗물

H, W = map(int, input().split())

block = list(map(int, input().split()))
res = 0

for i in range(1, len(block)-1):
    leftH = max(block[:i+1])
    rightH = max(block[i:])

    if min(leftH, rightH) > block[i]:
        res += (min(leftH, rightH) - block[i])

print(res)