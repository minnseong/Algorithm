# Programmers 06/02 2022
# 2 x n 타일링

def solution(n):

    tile = [0] * n
    tile[0] = 1
    tile[1] = 2

    for i in range(2, n):
        tile[i] = (tile[i-1] + tile[i-2]) % 1000000007
        
    return tile[n-1]

print(solution(5))
