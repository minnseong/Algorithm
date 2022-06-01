# BaekJoon 06/02 2022
# 1991 트리 순회

import sys
input = sys.stdin.readline

n = int(input())
tree = dict()

for _ in range(n):
    node, left, right = map(str, input().split())
    tree[node] = [left, right]

prTravel = []
def preOrder(node):
    prTravel.append(node)
    if tree[node][0] != '.':
        preOrder(tree[node][0])
    if tree[node][1] != '.':
        preOrder(tree[node][1])
iTravel = []
def inOrder(node):
    if tree[node][0] != '.':
        inOrder(tree[node][0])
    iTravel.append(node)
    if tree[node][1] != '.':
        inOrder(tree[node][1])
poTravel = []
def postOrder(node):
    if tree[node][0] != '.':
        postOrder(tree[node][0])
    if tree[node][1] != '.':
        postOrder(tree[node][1])
    poTravel.append(node)

preOrder('A')
inOrder('A')
postOrder('A')

print(''.join(prTravel))
print(''.join(iTravel))
print(''.join(poTravel))