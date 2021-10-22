# BaekJoon 10/22 2021
# 16953 A->B

A, B = map(int, input().split())
res = 1
flag = True

while B != A:
    if not flag or B < A:
        res = -1
        break
    flag = False

    if B & 1 and B % 10 == 1:
        B //= 10
        res += 1
        flag = True
    elif not B & 1:
        B //= 2
        res += 1
        flag = True

print(res)
