# BaekJoon 03/12 2022
# 1316 그룹 단어 체커

import sys

n = int(input())
cnt = n

for _ in range(n):
    word = sys.stdin.readline().strip()
    for i in range(1, len(word)):
        if word[i-1] != word[i]:
            if word[i-1] in word[i:]:
                cnt -= 1
                break

print(cnt)