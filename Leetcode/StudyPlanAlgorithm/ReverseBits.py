# LeetCode 2021 . 12 . 25
# Study Plan - Algorithm Day 14 190. Reverse Bits

class Solution:
    def reverseBits(self, n): 
        reverseBit = bin(n)[2:][::-1]
        reverseBit += '0' * (32 - len(reverseBit))

        return int(reverseBit ,2)
        
sol = Solution()
print(sol.reverseBits(43261596))
        