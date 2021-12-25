# BackJoon 12/25 2021
# 11728 배열 합치기

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = []
i, j = 0, 0

while len(res) != N+M:
    if i == N:
        res.append(B[j])
        j += 1
    elif j == M:
        res.append(A[i])
        i += 1
    else:
        if A[i] < B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1

print(*res)