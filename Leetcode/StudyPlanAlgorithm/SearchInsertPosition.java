// LeetCode 2021 . 12 . 13
// Study Plan - Algorithm Day 1 35. Search Insert Position
package Leetcode.StudyPlanAlgorithm;

class Solution {
    public int searchInsert(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        int res = 0;
        
        while(low <= high) {
            int mid = low + (high-low)/2;
            if (nums[mid] == target) {
                return mid;
            }
            else if(nums[mid] > target) {
                res = low;
                high = mid-1;
            }
            else {
                res = low+1;
                low = mid+1;
            }
        }
        
        return res;
    }
}