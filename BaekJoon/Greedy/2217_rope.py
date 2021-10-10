# BaekJoon 10/10 2021
# 2217 로프

N = int(input())
rope = []
weight = []

for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)

for i in range(N):
    weight.append(rope[i] * (i+1))

print(max(weight))
