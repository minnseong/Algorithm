# LeetCode 2021 . 12 . 23
# Study Plan - Algorithm Day 11 46. Permutations
from itertools import permutations

class Solution:
    def permute(self, nums):
        res = permutations(nums, len(nums))
        return res

sol = Solution()
print(sol.permute([1,2,3]))