// LeetCode 2021 . 12 . 14
// Study Plan - Algorithm Day 3 167. Two Sum II - Input Array Is Sorted
package Leetcode.StudyPlanAlgorithm;

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int [] res = new int[2];
        int start = 0;
        int end = numbers.length-1;
        
        while(start < end) {
            int sum = numbers[start] + numbers[end];
            if(sum == target) {
                res[0] = start+1;
                res[1] = end+1;
                break;
            }
            else if(sum > target) {
                end--;
            }
            else {
                start++;
            }
        }
        return res;
    }
}
