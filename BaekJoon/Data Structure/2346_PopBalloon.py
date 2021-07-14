N = int(input())
move = list(map(int, input().split()))
balloon = [i+1 for i in range(N)]
index = 0
res = []

m = move.pop(index)
res.append(balloon.pop(index))

while len(res) != N:
    if m < 0:
        index = (index + m) % len(move)
    else:
        index = (index + (m-1)) % len(move)
    m = move.pop(index)
    res.append(balloon.pop(index))

print(*res)