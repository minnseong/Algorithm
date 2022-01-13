# BaekJoon 01/13 2022
# 2110 공유기 설치

N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()

start = 1
end = home[-1] - home[0]
res = 0

while start <= end:
    mid = (start + end) // 2
    tmp = home[0]
    cnt = 1

    for i in range(1, len(home)):
        if home[i] >= tmp+mid:
            cnt += 1
            tmp = home[i]
    
    if cnt >= C:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)