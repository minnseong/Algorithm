# LeetCode 2021 . 12 . 25
# Study Plan - Algorithm Day 14 136. Single Number

class Solution:
    def singleNumber(self, nums):
        # arr = set()
        # for n in nums:
        #     if n not in arr:
        #         arr.add(n)
        #     else:
        #         arr.remove(n)
        
        # return list(arr)[0]

        res = 0
        for n in nums:
            res = res ^ n
            print(res)
        return res
        
        
sol = Solution()
print(sol.singleNumber([2,1,3,2,3]))
        