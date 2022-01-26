# BaekJoon 01/26 2022
# 12933 오리

'''
    풀지 못한 문제 - 시도한 코드는 아래에 주석처리.
    1) flag를 통해서 한 for문에서 "quack"가 만들어지면 그 이후에 만들어지는 "quack"는 생각하지않아도 된다.
    2) 또한 visited 배열을 통해 전에 본 문자에 대해서는 처리하지 않아도 된다.
    3) all 함수 - 중간에 비어있는 값이나 0, False 값이 하나라도 있으면 False를 반환한다. -> 모든 값이 True면 True 반환
'''

import sys

record = input()
quack = ['q', 'u', 'a', 'c', 'k']
visited = [False] * len(record)

res = 0
idx = 0

if len(record) % 5 != 0:
    print(-1)
    sys.exit(0)

else:
    for i in range(len(record)):
        if record[i] == 'q' and not visited[i]:
            flag = True
            for j in range(len(record)):
                if record[j] == quack[idx] and not visited[j]:
                    visited[j] = True
                    if record[j] == 'k':
                        if flag:
                            res += 1
                            flag = False
                        idx = 0
                        continue
                    idx += 1

if res == 0 or not all(visited):
    print(-1)
else:
    print(res)

'''
record = input()
res = 0

q, u, a, c, k = list(), list(), list(), list(), list()

for idx, r in enumerate(record):
    if r == "q":
        q.append(idx)
    elif r == "u":
        u.append(idx)
    elif r == "a":
        a.append(idx)
    elif r == "c":
        c.append(idx)
    else: # "k"
        k.append(idx)

minLen = min(len(q), len(u), len(a), len(c), len(k))

arr = []
for i in range(minLen):
    tmp = []
    tmp.append(q[i]); tmp.append(u[i]); tmp.append(a[i]); tmp.append(c[i]); tmp.append(k[i])

    if i == 0 and tmp == sorted(tmp):
        res += 1
    elif i != 0:
        outer = 0
        for aa in arr:
            if aa[0] < tmp[0] < aa[-1]:
                pass
            else:
                outer+= 1
            
        if outer < 1:
            res+= 1
            
        
    arr.append(tmp)

if res == 0:
    res = -1

print(res)
'''