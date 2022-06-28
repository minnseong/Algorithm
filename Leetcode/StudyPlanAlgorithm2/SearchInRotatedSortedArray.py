# LeetCode 06/28 2022
# Study Plan Algorithm2 - Day 1 Binary Search
# 33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums, target):
        
        if nums[0] == target:
            return 0

        start, end = 0, len(nums)-1
        k = -1
        flag = True
        if end == 1 and nums[start] > nums[end]:
            flag = False
        
        while start < end:
            mid = (start+end)//2
            
            if nums[mid-1] < nums[mid] < nums[mid+1]:
                flag = True
                if nums[mid] > nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
                
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                flag = False
                if nums[mid] > nums[start]:
                    end = mid - 1
                    start = mid + 1
                else:
                    start = mid + 1
            else:
                k = mid
                break

        if nums[k] == target:
            if k == -1:
                return len(nums)-1
            return k
        elif k == -1 or k == 0:
            start, end = 1, len(nums)-1
        elif nums[0] <= target <= nums[k-1]:
            start, end = 0, k-1
        else:
            start, end = k+1, len(nums)-1
            if end-start == 1 and nums[start] > nums[end]:
                flag = False
        
        res = -1
        if flag:
            while start <= end:
                mid = (start+end) // 2
                if nums[mid] == target:
                    res = mid
                    break
                    
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        else:
            while start <= end:
                mid = (start+end) // 2
                if nums[mid] == target:
                    res = mid
                    break
                    
                if nums[mid] > target:
                    start = mid + 1
                else:
                    end = mid - 1           
            
        return res

sol = Solution()

# print(sol.search([1,3], 3))
print(sol.search([5,1,2,3,4], 3))
# print(sol.search([4,5,6,7,0,1,2], 7))