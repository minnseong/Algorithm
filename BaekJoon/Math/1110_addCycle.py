# BackJoon 09/08 2021
# 1110 더하기 사이클

N = int(input())

num = N
cnt = 0

while True:
    rightNum = num % 10
    tmp = (num % 10) + int(num // 10)
    num = rightNum * 10 + int(tmp % 10)
    cnt += 1
    if num == N:
        break

print(cnt)
