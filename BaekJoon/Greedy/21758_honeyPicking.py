# BaekJoon 10/24 2021
# 21758 꿀 따기

N = int(input())
place = list(map(int, input().split()))
honey = sum(place) * 2
res = [0, 0, 0]
# 벌통 맨뒤
for i in range(1, len(place)):
    tmp = honey - place[0] - place[i] - sum(place[0:i+1])
    if res[0] < tmp:
        res[0] = tmp

# 벌통이 가운데
for i in range(1, len(place)-1):
    tmp = sum(place[1:i+1]) + sum(place[i:-1])
    if res[1] < tmp:
        res[1] = tmp

# 벌통 맨앞
place.reverse()
for i in range(1, len(place)):
    tmp = honey - place[0] - place[i] - sum(place[0:i+1])
    if res[2] < tmp:
        res[2] = tmp

print(max(res))
