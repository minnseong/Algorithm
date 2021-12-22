# LeetCode 2021 . 12 . 22
# Study Plan - Algorithm Day 9 994. Rotting Oranges
from collections import deque

class Solution:
    def orangesRotting(self, grid) :
        m = len(grid)
        n = len(grid[0])
        queue = deque([])
        dir = [[1,0], [-1,0], [0,1], [0,-1]]
        day = 0
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i,j,0])
        
        while queue:
            x, y, d = queue.popleft()
            for i, j in dir:
                newX = x+i
                newY = y+j
                if 0 <= newX < m and 0 <= newY < n and grid[newX][newY] == 1:
                    grid[newX][newY] = 2
                    fresh -= 1
                    day = d+1
                    queue.append([newX, newY, d+1])

        if fresh:
            return -1
        
        return day

sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))