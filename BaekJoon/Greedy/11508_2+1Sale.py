# BaekJoon 10/11 2021
# 11508 2+1 세일

N = int(input())
product = [int(input()) for _ in range(N)]
product.sort(reverse=True)
money = 0

for i in range(N):
    if i % 3 == 2:
        continue
    else:
        money += product[i]

print(money)
