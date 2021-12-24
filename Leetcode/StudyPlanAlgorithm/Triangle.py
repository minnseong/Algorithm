# LeetCode 2021 . 12 . 24
# Study Plan - Algorithm Day 12 120. Triangle

class Solution:
    def minimumTotal(self, triangle):
        tri = []
        for i in range(len(triangle)):
            if i == 0:
                tri.append(triangle[i])
            else:   
                tmp = []
                for j in range(i+1):
                    if j == 0:
                        tmp.append(tri[i-1][j] + triangle[i][j])
                    elif j == i:
                        tmp.append(tri[i-1][i-1] + triangle[i][j])
                    else:
                        tmp.append(min(tri[i-1][j-1], tri[i-1][j]) + triangle[i][j])
                tri.append(tmp)

        return min(tri[-1])

sol = Solution()
print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
        