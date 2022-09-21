# Programmers 09/21 2022
# Level 1 - 폰켓몬

from collections import defaultdict

def solution(nums):
    
    dict = defaultdict(int)
    
    for n in nums:
        dict[n] += 1
    
    nums_n = len(nums) // 2
    
    if len(dict) > nums_n:
        return nums_n
    else:
        return len(dict)
    