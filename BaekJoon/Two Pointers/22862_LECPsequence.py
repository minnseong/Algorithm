# BackJoon 12/27 2021
# 22862 가장 긴 짝수 연속한 부분 수열 (large)

N, K = map(int, input().split())
arr = list(map(int, input().split()))

maxLength = 0
tmpLength = 0
oddCnt = 0
evenCnt = 0
j = 0

for i in range(len(arr)):
    if arr[i] & 1:
        oddCnt += 1
        if oddCnt > K:
            tmpLength = i - j - oddCnt + 1
            if maxLength == 0 or maxLength < tmpLength:
                maxLength = tmpLength
            while j < i:
                if arr[j] & 1:
                    oddCnt -= 1
                    j += 1
                    break
                else:
                    j += 1
    else: 
        evenCnt += 1

    if i == len(arr) - 1:
        tmpLength = i - j - oddCnt + 1
        
if K > oddCnt:
    maxLength = evenCnt
elif tmpLength > maxLength:
    maxLength = tmpLength

print(maxLength)