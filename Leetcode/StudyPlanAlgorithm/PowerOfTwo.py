# LeetCode 2021 . 12 . 25
# Study Plan - Algorithm Day 13 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n):
        if n != 1 and n & 1:
            return False
        if n == 0:
            return False

        while n != 1:
            n //= 2
            if n != 1 and n & 1:
                return False
        
        return True

sol = Solution()
print(sol.isPowerOfTwo(3))
        