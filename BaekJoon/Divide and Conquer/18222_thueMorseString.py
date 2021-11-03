# BaekJoon 11/04 2021
# 18222 투에-모스 문자열

k = int(input())
m = 1
res = [0, 1]

cnt = 0
i = 1
while k > 1:
    if k > m:
        m = pow(2, i)
        i += 1
    else:
        m //= 2
        k = k - m
        cnt += 1
        i = 0
        m = 1

if cnt & 1:
    print(res[k])
else:
    print(abs(res[k]-1))
