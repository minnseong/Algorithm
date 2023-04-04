# BaekJoon 04/04 2023
# 8980 택배

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

boxes = [list(map(int, input().split())) for _ in range(m)]
boxes.sort(key=lambda x: x[1])

available = [c] * (n+1)
result = 0

for i in range(m):
    tmp = c
    for j in range(boxes[i][0], boxes[i][1]):
        tmp = min(tmp, available[j])
    tmp = min(tmp, boxes[i][2])
    for j in range(boxes[i][0], boxes[i][1]):    
        available[j] -= tmp
    result += tmp

print(result)

"""
delivery.sort(key=lambda x: (x[1]))

print(delivery)

index = 0
tmp = 0
result = 0
arrvied_box = [0] * (N+1)
for town in range(1, N+1):
    tmp -= arrvied_box[town]
    result += arrvied_box[town]

    while index < len(delivery):
        if delivery[index][0] == town and delivery[index][1] > town:
            if tmp == C:
                if delivery[index][0] <= town:
                    index+= 1
                    continue
                else:
                    break
            if tmp + delivery[index][2] <= C:
                tmp += delivery[index][2]
                arrvied_box[delivery[index][1]] += delivery[index][2]
            else:
                arrvied_box[delivery[index][1]] += (C-tmp)
                tmp += (C-tmp)

            index += 1
        else:
            break

print(result)
"""