// LeetCode 2021 . 12 . 17
// Study Plan - Algorithm Day 6 3. Longest Substring Without Repeating Characters
package Leetcode.StudyPlanAlgorithm;

import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int ans = 0;
        int i = 0;
        int j = 0;
        int s_length = s.length();
        HashSet<Character> set = new HashSet<Character>();
        
        while(j != s_length) {
            if(!set.contains(s.charAt(j))) {
                set.add(s.charAt(j));
                j++;
                ans = Math.max(ans, j-i);
            }
            else {
                set.remove(s.charAt(i));
                i++;
            }  
        }
        return ans;
    }
}


