# LeetCode 07/08 2022
# Study Plan Algorithm2 - Day 6 Breadth-First Search / Depth-First Search
# 547. Number of Provinces

from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected):
        connect = defaultdict(list)
        visited = [False] * (len(isConnected)+1)
        cnt = 0

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i != j and isConnected[i][j] == 1:
                    connect[i+1].append(j+1)

        for i in range(1, len(isConnected)+1):
            if not visited[i]:
                if i in connect:
                    stack = [i]
                    while stack:
                        x = stack.pop()
                        visited[x] = True

                        for xx in connect[x]:
                            if not visited[xx]:
                                stack.append(xx)
                    cnt += 1
                else:
                    visited[i] = True
                    cnt += 1

        return cnt
        
sol = Solution()
print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
        