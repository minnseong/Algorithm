// LeetCode 2021 . 12 . 12
// Study Plan - Algorithm Day 1 704. Binary Search
package Leetcode.StudyPlanAlgorithm;

class Solution {
    public int search(int[] nums, int target) {
        int low = 0;
        int mid;
        int high = nums.length - 1;

        while (low <= high) {
            mid = (low + high) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            else if (nums[mid] > target) {
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        return -1;
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        int [] arr = {-1,0,3,5,9,12};
        System.out.println(solution.search(arr, 9));
    }
}