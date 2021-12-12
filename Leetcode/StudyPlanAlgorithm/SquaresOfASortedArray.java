// LeetCode 2021 . 12 . 13
// Study Plan - Algorithm Day 2 977. Squares of a Sorted Array
package Leetcode.StudyPlanAlgorithm;

class Solution {
    public int[] sortedSquares(int[] nums) {
        
        int [] newArr = new int[nums.length];
        int start = 0;
        int end = nums.length - 1;
        
        for (int i = nums.length-1 ; i >= 0 ; i--) {
            if (Math.abs(nums[start]) >= Math.abs(nums[end])) {
                newArr[i] = nums[start]*nums[start];
                start++;
            }
            else {
                newArr[i] = nums[end]*nums[end];
                end--;
            }
        }    
        return newArr;
    }
}