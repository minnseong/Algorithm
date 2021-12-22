# LeetCode 2021 . 12 . 22
# Study Plan - Algorithm Day 9 542. 01 Matrix
from collections import deque

class Solution:
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        queue = deque([])
        dir = [[0,1], [0,-1],[1,0],[-1,0]]
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    mat[i][j] = 10001
                else:
                    queue.append([i,j])

        while queue:
            x, y = queue.popleft()
            for i, j in dir:
                newX = x+i
                newY = y+j
                if 0 <= newX < m and 0 <= newY < n and mat[x][y] < mat[newX][newY]:
                    mat[newX][newY] = mat[x][y] + 1
                    queue.append([newX, newY])

        return mat

sol = Solution()
print(sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))