# LeetCode 07/07 2022
# Study Plan Algorithm2 - Day 5 Sliding Window
# 438. Find All Anagrams in a String

from collections import defaultdict

class Solution:
    def findAnagrams(self, s, p):
        answer = []

        if len(p) > len(s):
            return []
            
        sDict = defaultdict(int)
        pDict = defaultdict(int)

        for i in range(len(p)-1):
            sDict[s[i]] += 1
            pDict[p[i]] += 1

        pDict[p[len(p)-1]] += 1

        for i in range(len(p)-1, len(s)):
            sDict[s[i]] += 1
            if sDict == pDict:
                answer.append(i-len(p)+1)
            sDict[s[i-len(p)+1]] -= 1
            if sDict[s[i-len(p)+1]] == 0:
                del sDict[s[i-len(p)+1]]

        return answer

sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))