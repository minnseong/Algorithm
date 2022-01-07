# BaekJoon 01/07 2022
# 1654 랜선 자르기

K, N = map(int, input().split())
LAN = []
for k in range(K):
    LAN.append(int(input()))

start, end = 1, max(LAN)

while start <= end:
    mid = (start + end) // 2   
    cnt = 0
    for l in LAN:
        cnt += l // mid
    
    if cnt >= N:
        start = mid+1
    else:
        end = mid-1

print(end)
