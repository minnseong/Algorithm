# BaekJoon 05/28 2022
# 22856 트리 순회

n = int(input())

tree = dict()
for i in range(1, n+1):
    tree[i] = [0, 0, 0]

for _ in range(n):
    a, b, c = map(int, input().split())
    tree[a][0] = b
    tree[a][2] = c
    if b != -1:
        tree[b][1] = a
    if c != -1:
        tree[c][1] = a

check = [True] * (n+1)
cnt = 0
stack = [1]

end = 1
while tree[end][2] != -1:
    end = tree[end][2]

while True:
    if tree[stack[-1]][0] != -1:
        stack.append(tree[stack[-1]][0])
    elif tree[stack[-1]][2] != -1:
        stack.append(tree[stack[-1]][2])
    elif stack[-1] == end:
        break
    else:
        if stack[-1] == tree[tree[stack[-1]][1]][0]:
            tree[tree[stack[-1]][1]][0] = -1
        else:
            tree[tree[stack[-1]][1]][2] = -1
        stack.append(tree[stack[-1]][1])

print(len(stack)-1)