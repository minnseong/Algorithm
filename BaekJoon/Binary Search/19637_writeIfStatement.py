# BaekJoon 01/09 2022
# 19637 IF문 좀 대신 써줘
import sys

def binarySearch(arr, score):
    start = 0
    end = len(arr)

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] >= score:
            end = mid-1
        else:
            start = mid+1
    
    return start

N, M = map(int, input().split())
titleDic = {}
titleArr = []

for i in range(N):
    t, s = sys.stdin.readline().split()
    titleArr.append(int(s))
    titleDic[i] = t

for _ in range(M):
    i = int(sys.stdin.readline())
    print(titleDic[binarySearch(titleArr, i)])