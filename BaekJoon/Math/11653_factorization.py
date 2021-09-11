# BackJoon 09/10 2021
# 11653 소인수분해

N = int(input())

f = 2
flag = True

while N != 1:
    if N % f == 0:
        print(f)
        N /= f
        flag = True
    else:
        flag = False

    if not flag:
        f += 1
