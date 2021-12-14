// LeetCode 2021 . 12 . 14
// Study Plan - Algorithm Day 2 189. Rotate Array
package Leetcode.StudyPlanAlgorithm;

class Solution {
    public void rotate(int[] nums, int k) {
        
        int [] newArr = nums.clone();
        k = k % nums.length;
        
        for (int i = 0 ; i < nums.length ; i++) {
            if (i < k) {
                nums[i] = newArr[nums.length-k+i];
            }
            else {
                nums[i] = newArr[i-k];
            }
        }
    }
}