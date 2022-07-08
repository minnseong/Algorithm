# LeetCode 07/08 2022
# Study Plan Algorithm2 - Day 6 Breadth-First Search / Depth-First Search
# 200. Number of Islands

class Solution:
    def numIslands(self, grid):
        
        dir = [[1,0], [0,1], [-1,0], [0,-1]]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == "1":
                    stack = [[i, j]]
                    cnt += 1
                    while stack:
                        x, y = stack.pop()
                        visited[x][y] = True

                        for d in dir:
                            dx, dy = x + d[0], y + d[1]
                            if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]):
                                if grid[dx][dy] == "1" and not visited[dx][dy]:
                                    stack.append([dx, dy])
        return cnt

sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
        