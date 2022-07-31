# BaekJoon 07/31 2022
# 22942 데이터 체커

import sys
input = sys.stdin.readline

n = int(input())
circles = []
stack = []

for i in range(n):
    circle = list(map(int, input().split()))
    circles.append([int(circle[0])-int(circle[1]),i, 0])
    circles.append([int(circle[0])+int(circle[1]),i, 1])

circles.sort()

for i in range(n):
    if circles[i][2] == 0:
        stack.append(circles[i])
    else:
        if stack[-1][2] == 0:
            if stack[-1][1] == circles[i][1]:
                stack.pop()
            else:
                print("NO")
                sys.exit()

print("YES")

'''
def isMeet(x1, r1, x2, r2):
    d = abs(x1 - x2)
    
    if abs(r1-r2) < d < r1+r2:
        return True
    elif r1 + r2 == d:
        return True
    elif abs(r1-r2) == d:
        return True
    return False

n = int(input())
circles = []

for _ in range(n):
    circles.append(list(map(int, input().split())))

circles.sort()
for i in range(n-1):
    if isMeet(circles[i][0], circles[i][1], circles[i+1][0], circles[i+1][1]):
        print("No")
        sys.exit()

print("Yes")
'''