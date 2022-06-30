# LeetCode 06/30 2022
# Study Plan Algorithm2 - Day 2 Binary Search
# 162. Find Peak Element

class Solution:
    def findPeakElement(self, nums):

        start, end = 0, len(nums)-1
        while start < end:
            mid = (start+end) // 2
            if (nums[mid] > nums[mid+1]):
                end = mid;
            else:
                start = mid + 1
        return start

sol = Solution()
print(sol.findPeakElement([1,2,3,1]))
        