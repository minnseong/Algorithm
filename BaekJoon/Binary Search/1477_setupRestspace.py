# BaekJoon 03/06 2023
# 골드4 - 휴게소 세우기

N, M, L = map(int, input().split())
positions = list(map(int, input().split()))
positions.append(0)
positions.append(L-1)
positions.sort()
start, end = 0, L-1
result = 0

while start <= end:
    mid = (start+end) // 2

    count = 0
    for i in range(1, len(positions)):
        if positions[i]-positions[i-1] > mid:
            count += ((positions[i]-positions[i-1]-1)//mid)
    
    if count > M:
        start = mid + 1
    else:
        end = mid -1
        result = mid

print(result)