// LeetCode 2021 . 12 . 16
// Study Plan - Algorithm Day 4 557. Reverse Words in a String III
package Leetcode.StudyPlanAlgorithm;

class Solution {
    public String reverseWords(String s) {
        String res = "";
        String tmp = "";
        int idx = 0;
        
        while(idx <= s.length()-1) {
            if (s.charAt(idx) != ' ') {
                tmp += s.charAt(idx);
            }
            else {
                res += swap(tmp);
                res += " ";
                tmp = "";
            }
            
            if (idx == s.length()-1) {
                res += swap(tmp);
                tmp = "";
            }
            idx++;
        }
        return res;
    }
    
     public static String swap(String s) {
        int start = 0;
        int end = s.length() - 1;
        char tmp;
        
        char [] charArray = s.toCharArray();

        while (start < end) {
            tmp = charArray[start];
            charArray[start] = charArray[end];
            charArray[end] = tmp;
            start++;
            end--;
        }
        
        String newString = String.valueOf(charArray);
        return newString;
    }
}