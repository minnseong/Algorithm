# BaekJoon 01/01 2022
# 22945 팀 빌딩

def getAblity(a1, a2, n):
    return n * min(a1, a2)

N = int(input())
arr = list(map(int, input().split()))
maxAblity = 0

i, j = 0, N-1

while i != j:
    ablity = getAblity(arr[i], arr[j], j-i-1)
    if ablity > maxAblity:
        maxAblity = ablity
    
    if arr[i] > arr[j]:
        j -= 1
    else:
        i += 1

print(maxAblity)