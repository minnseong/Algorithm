# BaekJoon 02/14 2022
# 1181 단어 정렬

import sys

N = int(input())
words = [sys.stdin.readline().strip() for _ in range(N)]

words = list(set(words))
words.sort(key= lambda x : (len(x), x))

for w in words:
    print(w)