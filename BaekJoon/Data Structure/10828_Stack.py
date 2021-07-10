def isEmpty():
    if len(stack) == 0:
        return 1
    else:
        return 0


N = int(input())
stack = []
cmd = []
for i in range(N):
    cmd.append(input().split())

for i in range(N):
    c = cmd[i]

    if c[0] == 'push':
        stack.append(c[1])
    elif c[0] == 'pop':
        if isEmpty():
            print(-1)
        else:
            print(stack.pop())
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        print(isEmpty())
    elif c[0] == 'top':
        if isEmpty():
            print(-1)
        else:
            print(stack[-1])