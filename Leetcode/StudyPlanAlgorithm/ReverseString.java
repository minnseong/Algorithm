// LeetCode 2021 . 12 . 14
// Study Plan - Algorithm Day 4 344. Reverse String
package Leetcode.StudyPlanAlgorithm;

class Solution {
    public void reverseString(char[] s) {
        
        int start = 0;
        int end = s.length-1;
        
        while (start < end) {
            swap(s, start, end);
            start++;
            end--;
        }
    }
    
    public static void swap(char[] arr, int idx1, int idx2) {
        char tmp;
        tmp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = tmp;
    }
}