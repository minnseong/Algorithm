// LeetCode 2021 . 12 . 15
// Study Plan - Algorithm Day 4 557. Reverse Words in a String III
package Leetcode.StudyPlanAlgorithm;

class Solution {
    public String reverseWords(String s) {
        String res = "";
        String tmp = "";
        int idx = 0;
        
        
        while(idx <= s.length()) {
            if (s.charAt(idx) != " ") {
                tmp += s.charAt(idx);
            }
            else {
                res += swap(tmp);
                res += " ";
            }
            idx++;
        }
        
        return res;
    }
    
    public static String swap(String s) {
        int start = 0;
        int end = s.length() - 1;
        String newS = s;
        char tmp;
        
        
        while (start < end) {
            tmp = newS.charAt(start);
            newS.charAt(start) = newS.charAt(end);
            newS.charAt(end) = newS.charAt(start);
            start++;
            end--;
        }
        
        return newS;
    }
}