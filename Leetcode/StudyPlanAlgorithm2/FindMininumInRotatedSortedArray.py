# LeetCode 06/29 2022
# Study Plan Algorithm2 - Day 2 Binary Search
# 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums):
        
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        start, end = 0, len(nums)-1
        val = -1

        while start <= end:
            mid = (start+end) // 2

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            

            if nums[mid] > nums[0]:
                start = mid + 1
            else:
                end = mid - 1
            
        return val

sol = Solution()
print(sol.findMin([3,4,5,1,2]))
        