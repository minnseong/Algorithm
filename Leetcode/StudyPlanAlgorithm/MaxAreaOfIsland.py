# LeetCode 2021 . 12 . 20
# Study Plan - Algorithm Day 7 695. Max Area of Island
from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        queue = deque([])

        maxArea = 0
        for y in range(m):
            for x in range(n):
                if not visited[y][x] and grid[y][x]:
                    queue.append([y,x])
                    areaSize = 0
                    while(len(queue) != 0):
                        q = queue.popleft()
                        if not visited[q[0]][q[1]] and grid[q[0]][q[1]]:
                            visited[q[0]][q[1]] = True
                            areaSize += 1
                            if q[0] >= 1: queue.append([q[0]-1, q[1]])
                            if q[0] < m-1: queue.append([q[0]+1, q[1]])
                            if q[1] >= 1: queue.append([q[0], q[1]-1])
                            if q[1] < n-1: queue.append([q[0], q[1]+1])
                    if(maxArea < areaSize):
                        maxArea = areaSize

        return maxArea

sol = Solution()
print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))