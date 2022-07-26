# BaekJoon 07/26 2022
# 2504 괄호의 값

import sys
input = sys.stdin.readline

bracket = list(input().strip())
stack = []
flag = True

tmp = 0
for b in bracket:
    if (b == ")" or b == "]") and not stack:
        flag = False
        break
    elif b == ")":
        if stack and stack[-1] == "(":
            stack.pop()
            stack.append(2)
        elif stack and stack[-1] == "[":
            flag = False
            break
        else:
            tmp = stack.pop()
            while (stack and type(stack[-1]) == int):
                tmp += stack.pop()
            if not stack or stack[-1] != "(":
                flag = False
                break
            stack.pop()
            stack.append(2*tmp)
    elif b == "]":
        if stack and stack[-1] == "[":
            stack.pop()
            stack.append(3)
        elif stack and stack[-1] == "(":
            flag = False
            break
        else:
            tmp = stack.pop()
            while (stack and type(stack[-1]) == int):
                tmp += stack.pop()
            if not stack or stack[-1] != "[":
                flag = False
                break
            stack.pop()
            stack.append(3*tmp)
    else:
        stack.append(b)

if flag:
    res = 0
    for s in stack:
        if (type(s) != int):
            print(0)
            sys.exit(0)
        res += s
    print(res)
else:
    print(0)