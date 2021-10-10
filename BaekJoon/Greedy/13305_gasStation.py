# BaekJoon 10/11 2021
# 13305 주유소

N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
cost = 0

minPrice = price[0]

for i in range(N-1):
    if price[i] < minPrice:
        minPrice = price[i]
    cost += (minPrice * distance[i])

print(cost)
