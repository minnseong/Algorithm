# BaekJoon 01/03 2022
# 1789 수들의 합

S = int(input())
num = [0]

n = 1
while True:
    if S-n == 0:
        num.append(n)
        break

    if S-n >= n+1:
        num.append(n)
        S -= n
        n += 1
    else:
        n += 1

print(len(num)-1)

