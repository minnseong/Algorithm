// Programmers 12/14 2022
// Java 코테 연습 - 양궁 대회

package java;

public class ArcheryCompetition {
    class Solution {
        
        int max, ans[], apeach[];
        
        void find(int n, int cur) {
            
            int score = 0;
            int[] state = new int[11];
            
            for (int i = 1; i<= 10; i++) {
                if ((cur & 1<< i) != 0) {
                    state[10-i] = apeach[10-i]+1;
                    n -= state[10-i];
                    if (n < 0)
                        return;
                    score += i;
                }
                else if (apeach[10-i] > 0) 
                    score -= i;
            }
            
            if (score <= 0) return;
            state[10] = n;
            if (max < score) {
                max = score;
                ans = state;
            } 
            else if (max == score) {
                for (int i=10 ; i>=0 ;i--) {
                    if (state[i] > ans[i])
                        ans = state;
                    return;
                }
            }
            
        }

        public int[] solution(int n, int[] info) {
            
            for(int i = 1; i < 1<<11 ; i++) {
                if (Integer.bitCount(i) <= n) {
                    find(n, i);
                }
            }
            
            return max == 0 ? new int[] {-1} : ans;
        }
    }
}