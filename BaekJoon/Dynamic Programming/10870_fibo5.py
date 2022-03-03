# BaekJoon 03/03 2022
# 10870 피보나치 수 5

n = int(input())

fb = [0, 1]
for i in range(2,n+1):
    fb.append(fb[i-1] + fb[i-2])

if n == 0:
    print(0)
else:
    print(fb[-1])