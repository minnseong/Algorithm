# BaekJoon 06/30 2022
# 20437 문자열 게임 2

import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    w = str(input())
    k = int(input())

    dic = defaultdict(int)
    alphaDic = defaultdict(list)
    ans = []
    for j in range(len(w)):
        dic[w[j]] += 1
        
        if dic[w[j]] >= k:
            i = 0
            if w[j] in alphaDic:
                i = alphaDic[w[j]][-1]
            while i <= j:
                if w[i] == w[j]:
                    alphaDic[w[i]].append(i+1)
                    ans.append(j-i+1)
                    break
                i += 1
    if not ans:
        print(-1)
    else:
        print(min(ans), max(ans))
                
                            