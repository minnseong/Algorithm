N, K = map(int, input().split())

circle = [i+1 for i in range(N)]
ans = []
n = 0

while len(circle) > 0:
    n = (n + (K-1)) % len(circle)
    ans.append(circle.pop(n))

print("<", end="")
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end=">")
    else:
        print(ans[i], end=", ")