# BackJoon 12/29 2021
# 15961 회전 초밥
import sys

N, d, k, c = map(int, input().split())
sushi = [int(sys.stdin.readline()) for _ in range(N)]
sushi.extend(sushi)

dic = {c : 1}
for i in range(k):
    if sushi[i] not in dic:
        dic[sushi[i]] = 1
    else:
        dic[sushi[i]] += 1

maxSushi = len(dic)

j = k
for i in range(N):
    if sushi[j] not in dic:
        dic[sushi[j]] = 1
    else:
        dic[sushi[j]] += 1
    j += 1

    if dic[sushi[i]] == 1:
        del dic[sushi[i]]
    else:
        dic[sushi[i]] -= 1

    if maxSushi < len(dic):
        maxSushi = len(dic)

print(maxSushi)