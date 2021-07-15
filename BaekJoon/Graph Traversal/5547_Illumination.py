from collections import deque


W, H = map(int, input().split())
grid = []
for i in range(H):
    grid.append(input().split(" "))

dx = [0, 0, 1, 1, 1, -1]
dy = [-1, 1, -1, 0, 1, 0]

queue = deque()
visit = []

for i in range(H):
    visit.append([False] * W)

while queue:
