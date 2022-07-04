# LeetCode 07/04 2022
# Study Plan Algorithm2 - Day 3 Two Pointers
# 15. 3Sum

class Solution:
    def threeSum(self, nums):
        answer = []
        if len(nums) < 3:
            return answer
        
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start, end = i+1, len(nums)-1

            while start < end:
                thrsum = nums[i] + nums[start] + nums[end]

                if thrsum == 0:
                    answer.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    end -= 1
                    start += 1
                elif thrsum > 0:
                    end -= 1
                else:
                    start += 1

        return answer

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))