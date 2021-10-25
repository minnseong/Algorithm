# BaekJoon 10/24 2021
# 21758 꿀 따기

N = int(input())
place = list(map(int, input().split()))
reservePlace = list(reversed(place))
res = [0, 0, 0]

rightPlus = []
leftPlus = []

for i in range(len(place)):
    if i == 0:
        rightPlus.append(place[i])
    else:
        rightPlus.append(rightPlus[i-1]+place[i])

for i in range(len(reservePlace)):
    if i == 0:
        leftPlus.append(reservePlace[i])
    else:
        leftPlus.append(leftPlus[i-1]+reservePlace[i])

# 벌통 맨뒤
for i in range(1, len(place)):
    tmp = (2 * rightPlus[-1]) - place[0] - rightPlus[i] - place[i]
    if res[0] < tmp:
        res[0] = tmp

tmp = 0
# 벌통이 가운데
for i in range(1, len(place)-1):
    tmp = rightPlus[i] + leftPlus[len(place)-i-1] - place[0] - reservePlace[0]
    if res[1] < tmp:
        res[1] = tmp

tmp = 0
# 벌통 맨앞
for i in range(1, len(reservePlace)):
    tmp = (2 * leftPlus[-1]) - reservePlace[0] - leftPlus[i] - reservePlace[i]
    if res[2] < tmp:
        res[2] = tmp

print(max(res))
