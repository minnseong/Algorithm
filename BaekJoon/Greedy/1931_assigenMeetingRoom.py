# BaekJoon 10/08 2021
# 1931 회의실 배정

N = int(input())
time = []
cnt = 1

for _ in range(N):
    s, e = map(int, input().split())
    tmp = [s, e]
    time.append(tmp)

time.sort(key=lambda x: (x[0], x[1]))
time.sort(key=lambda x: (x[1], x[0]))

e = time[0][1]
for i in range(1, len(time)):
    if e <= time[i][0]:
        e = time[i][1]
        cnt += 1

print(cnt)
