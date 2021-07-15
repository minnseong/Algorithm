s = list(input())
stack = []
res = 0
cnt = 0

for i in s:
    if i == '(' or i == '[':
        stack.append(i)
    else:
        if i == ')' and stack[-1] == '(':
            stack.pop()
        if i == ']' and stack[-1] == '[':
            stack.pop()

if stack:
    print(0)
else:
    print(res)


# (()[[]])([])