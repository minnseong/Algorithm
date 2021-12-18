// LeetCode 2021 . 12 . 18
// Study Plan - Algorithm Day 6 567. Permutation in String
package Leetcode.StudyPlanAlgorithm;

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int [] s1_Array = new int[26];
        int [] s2_Array = new int[26];
        boolean ans = false;
        
        if (s1.length() > s2.length()) {
            return false;
        }
        
        for (int i = 0 ; i < s1.length() ; i++) {
            s1_Array[s1.charAt(i) - 'a']++;
            s2_Array[s2.charAt(i) - 'a']++;
        }
        
        for (int i = 0 ; i < s2.length() - s1.length() ; i++) {
            if(equalArray(s1_Array, s2_Array)) {
                ans = true;
                break;
            }
            s2_Array[s2.charAt(i) - 'a']--;
            s2_Array[s2.charAt(i+s1.length()) - 'a']++;
        }
        
        if(!ans && equalArray(s1_Array, s2_Array)) {
            ans = true;
        }
        
        return ans;
    }
    
    public boolean equalArray(int [] arr1, int [] arr2) {
        for(int i = 0 ; i < 26 ; i++) {
            if(arr1[i] != arr2[i]) {
                return false;
            }
        }
        return true;
    }
}