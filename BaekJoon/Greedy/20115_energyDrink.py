# BaekJoon 10/13 2021
# 20115 에너지 드링크

N = int(input())
drink = list(map(int, input().split()))
drink.sort(reverse=True)
res = drink[0]

for i in range(1, N):
    res += (drink[i]/2)

print(res)
