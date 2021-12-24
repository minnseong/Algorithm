# LeetCode 2021 . 12 . 25
# Study Plan - Algorithm Day 13 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n):
        # binary = bin(n)
        # return binary.count('1')

        cnt = 0
        while n:
            cnt += (n&1)
            n = n>>1
            
        return cnt

sol = Solution()
print(sol.hammingWeight(34242))
        