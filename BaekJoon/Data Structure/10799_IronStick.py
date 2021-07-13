import sys

bracket = list(sys.stdin.readline())
stack = []
ans = 0

for i in range(len(bracket)-1):
    if bracket[i] == '(':
        stack.append('(')
    else:
        if bracket[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1

print(ans)