# BaekJoon 08/01 2022
# 1918 후위 표기식

import sys
input = sys.stdin.readline

notation = list(input().strip())

res = ""
stack = []
for n in notation:
    if 65 <= ord(n) <= 90:
        res += n
    else:
        if n == "(":
            stack.append(n)
        elif n == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()
        elif n in ("+", "-"):
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(n)
        elif n in ("*", "/"):
            while stack and stack[-1] not in ("(", ")", "+", "-"):
                res += stack.pop()
            stack.append(n)

while stack:
    res += stack.pop()

print(res)