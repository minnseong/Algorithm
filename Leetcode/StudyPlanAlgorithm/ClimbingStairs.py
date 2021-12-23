# LeetCode 2021 . 12 . 24
# Study Plan - Algorithm Day 12 70. Climbing Stairs

class Solution:
    def climbStairs(self, n):
        res = [0, 1, 2]
        
        if n == 1:
            return res[1]
        elif n == 2:
            return res[2]
        else:
            for i in range(3, n+1):
                res.append(res[i-1] + res[i-2]) 
            return res[-1]
            
sol = Solution()
print(sol.climbStairs(5))
        