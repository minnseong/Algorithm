# BaekJoon 05/30 2022
# 2812 크게 만들기

N, K = map(int, input().split())
num = list(map(int, str(input())))
stack = []
cnt = 0

i = 0
while i < len(num):
    while stack and stack[-1] < num[i]:
        stack.pop()
        cnt += 1
        if cnt == K:
            break
    if cnt == K:
        stack.extend(num[i:])
        break
    stack.append(num[i])
    i += 1

res = ''.join(map(str,stack[:N-K]))
print(int(res))