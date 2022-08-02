# BaekJoon 08/02 2022
# 4358 생태학

import sys
input = sys.stdin.readline

trees = dict()
cnt = 0

while True:
    tree = input().rstrip()
    if not tree:
        break

    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
    cnt += 1

tree_list = sorted(list(trees.keys()))
for t in tree_list:
    print('%s %.4f' %(t, trees[t]/cnt * 100))
