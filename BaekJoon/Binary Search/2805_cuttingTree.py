# BaekJoon 01/07 2022
# 2805 나무 자르기
import sys

def cutTree(arr, height):
    res = 0
    for a in arr:
        if a > height:
            res += (a-height)
    
    return res

N, M = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)
mid = 0

while start <= end:
    mid = (start + end) // 2
    if cutTree(tree, mid) >= M:
        start = mid + 1
    elif cutTree(tree, mid) < M:
        end = mid - 1
        
print(end)
