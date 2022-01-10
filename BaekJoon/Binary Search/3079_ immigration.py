# BaekJoon 01/11 2022
# 3079 입국심사

# N : 심사대 수, M : 사람 수
N, M = map(int, input().split())
jt = []
res = 0

for _ in range(N):
    jt.append(int(input()))

start = 0
end = max(jt) * M

while start <= end:
    mid = (start + end) // 2
    total = 0

    for j in jt:
        total += mid // j
    
    if total >= M:
        end = mid-1
    else:
        start = mid+1
    
print(start)