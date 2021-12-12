// LeetCode 2021 . 12 . 13
// Study Plan - Algorithm Day 1 278. First Bad Version
package Leetcode.StudyPlanAlgorithm;

/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        
        int low = 1;
        int high = n;
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            if(isBadVersion(mid)) {
                high = mid;
            }
            else {
                low = mid + 1;
            }
        }
        
        return low;
    }
}