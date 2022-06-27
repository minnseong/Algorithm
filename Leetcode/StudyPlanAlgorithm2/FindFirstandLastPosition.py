# LeetCode 06/27 2022
# Study Plan Algorithm2 - Day 1 Binary Search
# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums, target):
        
        start, end = 0, len(nums)-1
        first = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                first = mid
                end -= 1
            elif nums[mid] >= target:
                end = mid-1
            else:
                start =mid+1

        start, end = 0, len(nums)-1
        second = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                second = mid
                start += 1
            elif nums[mid] >= target:
                end = mid-1
            else:
                start = mid+1

        return [first, second]

sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))
        