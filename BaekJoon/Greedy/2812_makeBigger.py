# BaekJoon 11/07 2021
# 2812 크게 만들기

N, K = map(int, input().split())
num = list(map(int, str(input())))
stack = []
cnt = 0
res = ""

i = 0
while i != N:
    if cnt == K:
        stack += num[i:]
        break
    if stack:
        while True:
            if stack and num[i] > stack[-1]:
                stack.pop()
                cnt += 1
                if cnt == K:
                    break
            else:
                break
        stack.append(num[i])
    else:
        stack.append(num[i])
    i += 1

for s in stack:
    res += str(s)

if len(res) > N-K:
    res = res[:N-K]

print(int(res))
