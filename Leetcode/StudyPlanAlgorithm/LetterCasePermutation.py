# LeetCode 2021 . 12 . 23
# Study Plan - Algorithm Day 11 784. Letter Case Permutation
from itertools import combinations

class Solution:
    def letterCasePermutation(self, s):
        letterIdx = [i for i in range (len(s)) if s[i].isalpha()]
        permu = []
        s = s.lower()
        res = [s]

        for i in range(1, len(s)+1):
            permu.extend(combinations(letterIdx, i))

        for i in permu:
            ss = list(s)
            for j in i:
                ss[j] = ss[j].upper()
            res.append("".join(ss))

        return res

sol = Solution()
print(sol.letterCasePermutation("Jw"))
        