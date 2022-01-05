# BaekJoon 01/05 2022
# 10815 숫자 카드

def binarySearch(arr, n):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < n:
            start = mid + 1
        elif arr[mid] > n:
            end = mid - 1
        elif arr[mid] == n:
            return 1
    
    return 0

N = int(input())
nList = list(map(int, input().split()))
M = int(input())
mList = list(map(int, input().split()))
nList.sort()
ans = []

for m in mList:
    ans.append(binarySearch(nList, m))

print(*ans)