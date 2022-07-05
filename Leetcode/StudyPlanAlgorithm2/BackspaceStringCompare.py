# LeetCode 07/05 2022
# Study Plan Algorithm2 - Day 4 Two Pointers
# 844. Backspace String Compare

class Solution:
    def backspaceCompare(self, s, t):
        ss, tt = list(), list()

        for v in s:
            if ss and v == "#":
                ss.pop()
            elif v != "#":
                ss.append(v)
        for v in t:
            if tt and v == "#":
                tt.pop()
            elif v != "#":
                tt.append(v)
        
        if "".join(ss) == "".join(tt):
            return True
        else:
            return False
            
sol = Solution()
print(sol.backspaceCompare("y#fo##f", "y#f#o##f"))