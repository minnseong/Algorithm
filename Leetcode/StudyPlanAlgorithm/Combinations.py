# LeetCode 2021 . 12 . 23
# Study Plan - Algorithm Day 11 77. Combinations
from itertools import combinations

class Solution:
    def combine(self, n: int, k: int):
        arr = [i+1 for i in range(n)]
        res = combinations(arr, k)
        return res

sol = Solution()
print(sol.combine(4, 2))