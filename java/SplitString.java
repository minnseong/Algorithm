// Programmers 12/20 2022
// Java 코테 연습 - 문자열 나누기

package java;

public class SplitString {
    class Solution {
        public int solution(String s) {
            int answer = 0;
            
            int n = 0;
            int m = 0;
    
            char x = '-';
            for (int i = 0 ; i < s.length() ; i++) {
                if (n == 0 && m == 0) {
                    x = s.charAt(i);
                    n += 1;
                }          
                else {
                    if (x != s.charAt(i)) {
                        m += 1;
                    } else {
                        n += 1;
                    }
                    
                    if (n == m) {
                        answer += 1;
                        n = 0;
                        m = 0;
                        x = '-';
                    }
                }
            }
            
            if (m != 0 || n != 0) {
                answer += 1;
            }
            
            return answer;
        }
    }
}
