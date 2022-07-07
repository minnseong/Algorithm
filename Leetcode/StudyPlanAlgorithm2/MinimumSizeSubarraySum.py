# LeetCode 07/07 2022
# Study Plan Algorithm2 - Day 5 Sliding Window
# 209. Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target, nums):
        minSize = 1e9

        i = 0
        size = 0
        ssum = 0
        for j in range(len(nums)):
            ssum += nums[j]
            size += 1
            if ssum >= target:
                minSize = min(minSize, size)
                while ssum >= target:
                    ssum -= nums[i]
                    i += 1
                    size -= 1
                minSize = min(minSize, size+1)

        if minSize == 1e9:
            return 0
        return minSize

sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))
print(sol.minSubArrayLen(4, [1,4,4]))
print(sol.minSubArrayLen(4, [1,1,1]))
print(sol.minSubArrayLen(11, [1,2,3,4,5]))
