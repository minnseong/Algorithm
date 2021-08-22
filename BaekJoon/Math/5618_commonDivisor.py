import sys

input = sys.stdin.readline()
N = int(input())
num = input().split()

ans = []
num = list(map(int, num))

for i in range(1, min(num)):
    cnt = 0
    for n in num:
        if n % i == 0:
            cnt += 1
    if cnt == len(num):
        ans.append(i)

for i in ans:
    print(i)
