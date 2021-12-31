# BackJoon 12/31 2021
# 3151 합이 0

def getCombination(arr1, arr2):
    dic = {}
    cnt = 0

    for i in arr2:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    for i in range(len(arr1)-1):
        for j in range(i+1, len(arr1)):
            if (arr1[i]+arr1[j]) * -1 in dic:
                cnt += dic[(arr1[i]+arr1[j]) * -1]
    
    return cnt

N = int(input())
num = list(map(int, input().split()))
res = 0
zeroCnt = 0

Pnum, Nnum = [], []

for n in num:
    if n >= 0:
        Pnum.append(n)
    else:
        Nnum.append(n)
    
    if n == 0:
        zeroCnt += 1

res += getCombination(Pnum, Nnum)
res += getCombination(Nnum, Pnum)
res += (zeroCnt*(zeroCnt-1)*(zeroCnt-2))//6

print(res)