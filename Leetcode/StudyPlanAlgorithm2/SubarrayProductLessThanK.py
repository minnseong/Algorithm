# LeetCode 07/06 2022
# Study Plan Algorithm2 - Day 5 Sliding Window
# 713. Subarray Product Less Than K

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        answer = 0

        i, j = 0, 0
        value = 1

        while j < len(nums) and i < len(nums):
            value *= nums[j]
            while i < len(nums) and value >= k:
                value //= nums[i]
                i += 1
            if value < k:
                answer += (j-i+1)
            j += 1

        return answer

sol = Solution()
print(sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100))

# 10 5 2 6
# 10 -> 1
# 10 5 -> 2
# 10(x) 5 2 -> 2
# 5 2 6 -> 3

