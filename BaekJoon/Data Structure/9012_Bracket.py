T = int(input())
bracket = []
ans = []

for i in range(T):
    bracket.append(list(input()))

for i in range(T):
    b = bracket[i]
    stack = []
    for j in range(len(b)):
        stack.append(b[j])
        if len(stack) >= 2 and stack[-2] == '(' and stack[-1] == ')':
            stack.pop()
            stack.pop()

    if len(stack) == 0:
        ans.append('YES')
    else:
        ans.append('NO')

for i in ans:
    print(i)