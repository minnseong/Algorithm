# BaekJoon 02/03 2022
# 16926 배열 돌리기 1

# python3 시간초과 / PyPy3 으로 통과
import sys

N, M, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

for _ in range(R):
    for p in range(min(N,M)//2):
        x, y = p, p
        tmp = arr[x][y]

        for i in range(p+1, N-p): # 하
            x = i
            prv = arr[x][y]
            arr[x][y] = tmp
            tmp = prv
        
        for i in range(p+1, M-p): # 좌
            y = i
            prv = arr[x][y]
            arr[x][y] = tmp
            tmp = prv
        
        for i in range(p+1, N-p): # 상
            x = N - i - 1
            prv = arr[x][y]
            arr[x][y] = tmp
            tmp = prv
        
        for i in range(p+1, M-p): # 우
            y = M - i - 1
            prv = arr[x][y]
            arr[x][y] = tmp
            tmp = prv

for a in arr:
    print(*a)