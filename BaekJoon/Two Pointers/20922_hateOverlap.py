# BackJoon 12/27 2021
# 20922 겹치는 건 싫어

N, K = map(int, input().split())
arr = list(map(int, input().split()))
maxLength = 0
tmpLength = 0
dic = {}

j = 0
for i in range(N):
    if arr[i] not in dic:
        dic[arr[i]] = 1
        tmpLength += 1
    else:
        dic[arr[i]] += 1
        tmpLength += 1
        if dic[arr[i]] > K:
            tmpLength -= 1
            if maxLength == 0 or maxLength < tmpLength:
                maxLength = tmpLength
            while j < i:
                dic[arr[j]] -= 1
                if dic[arr[i]] <= K:
                    j += 1
                    break
                j += 1
            tmpLength = i - j + 1

if tmpLength > maxLength:
    maxLength = tmpLength

print(maxLength)
