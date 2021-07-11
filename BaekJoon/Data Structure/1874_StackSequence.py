N = int(input())
num = []
stack = []
ans = []
flag = False

for i in range(N):
    num.append(int(input()))

num.reverse()
i = 1

while len(num) != 0:
    if flag:
        break
    tmp = num.pop()

    while True:
        if len(stack) > 0 and stack[-1] == tmp:
            ans.append('-')
            stack.pop()
            break
        else:
            ans.append('+')
            stack.append(i)
            i += 1
            if i > N+1:
                flag = True
                break

if flag:
    print("NO")
else:
    for i in ans:
        print(i)