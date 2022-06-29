# LeetCode 06/29 2022
# Study Plan Algorithm2 - Day 1 Binary Search
# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix, target):
        
        start, end = 0, len(matrix)
        idx = -1
        while start <= end:
            mid = (start + end) // 2
            
            if not (0 <= mid <= len(matrix)-1):
                break
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                idx = mid
                break

            if matrix[mid][0] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        if idx == -1:
            return False
        else:
            start, end = 0, len(matrix[idx])
            while start <= end:
                mid = (start + end) // 2

                if matrix[idx][mid] == target:
                    return True
                
                if matrix[idx][mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1

        return False

sol = Solution()

# print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(sol.searchMatrix([[1]], 2))
        