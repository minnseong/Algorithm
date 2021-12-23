# LeetCode 2021 . 12 . 24
# Study Plan - Algorithm Day 12 198. House Robber

class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            dp = [nums[0], max(nums[0], nums[1])]
            
            for i in range(2, len(nums)):
                if dp[i-1] > dp[i-2] + nums[i]:
                    dp.append(dp[i-1])
                else:
                    dp.append(dp[i-2] + nums[i])
            return dp[-1]

sol = Solution()
print(sol.rob([1,3,1,1,5,1,1,10]))