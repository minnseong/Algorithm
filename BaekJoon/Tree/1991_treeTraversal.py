# BaekJoon 03/20 2023
# 1991 트리 순회

import sys

N = int(input())
tree = dict()

for _ in range(N):
    a, b, c = sys.stdin.readline().split()
    tree[a] = [b, c]

preorder_list = []
inorder_list = []
postorder_list = []

def preorder(root):
    preorder_list.append(root)
    if tree[root][0] != '.':
        preorder(tree[root][0])
    if tree[root][1] != '.':
        preorder(tree[root][1])

def inorder(root):
    if tree[root][0] != '.':
        inorder(tree[root][0])
    inorder_list.append(root)
    if tree[root][1] != '.':
        inorder(tree[root][1])

def postorder(root):
    if tree[root][0] != '.':
        postorder(tree[root][0])
    if tree[root][1] != '.':
        postorder(tree[root][1])
    postorder_list.append(root)

preorder('A')
inorder('A')
postorder('A')

print(''.join(preorder_list))
print(''.join(inorder_list))
print(''.join(postorder_list))
