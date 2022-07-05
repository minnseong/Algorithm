# LeetCode 07/05 2022
# Study Plan Algorithm2 - Day 4 Two Pointers
# 11. Container With Most Water

class Solution:
    def getArea(i, j, height):
        return (j-i) * min(height[i], height[j])
        
    def maxArea(self, height):
        i, j = 0, len(height)-1
        maxSize = 0
        while i < j:
            area = Solution.getArea(i, j, height)
            maxSize = max(maxSize, area)

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxSize
    
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,1]))

            

        