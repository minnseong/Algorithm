# LeetCode 2021 . 12 . 20
# Study Plan - Algorithm Day 7 733. Flood Fill
from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        m = len(image)
        n = len(image[0])
        color = image[sr][sc]
        queue = deque([[sr, sc]])
        visited = [[False] * n for _ in range(m)]
        
        while(len(queue) != 0):
            def direction(loc):
                if(loc[0] >= 1): queue.append([loc[0]-1, loc[1]])
                if(loc[0]+1 < m): queue.append([loc[0]+1, loc[1]])
                if(loc[1] >= 1): queue.append([loc[0], loc[1]-1])
                if(loc[1]+1 < n): queue.append([loc[0], loc[1]+1])

            tmp = queue.popleft()
            if (not visited[tmp[0]][tmp[1]] and image[tmp[0]][tmp[1]] == color):
                image[tmp[0]][tmp[1]] = newColor
                visited[tmp[0]][tmp[1]] = True
                direction(tmp)
 
        return image

sol = Solution()
print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))