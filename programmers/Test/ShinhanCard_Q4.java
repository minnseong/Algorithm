// 신한카드 코딩테스트 10/13 2022
// Q4

package programmers.Test;

public class ShinhanCard_Q4 {
    class Solution {
        public int[] solution(int[] black_caps) {
    
            int n = black_caps.length;
    
            int[] answer = new int[n];
    
            for (int i = 0 ; i < n ; i++) {
                if (i == 0 && black_caps[i] == 1)
                    answer[1] = 1;
                else if (i== 0 && black_caps[i] == 0)
                    answer[1] = 2;
                else if (i == n-1 && black_caps[i] == 1)
                    answer[n-2] = 1;
                else if (i== n-1 && black_caps[i] == 0)
                    answer[n-2] = 2;
                else if (black_caps[i] == 2) {
                    answer[i-1] = 1;
                    answer[i+1] = 1;
                }
                else if (black_caps[i] == 0) {
                    answer[i-1] = 2;
                    answer[i+1] = 2;
                }
            }
    
            if (black_caps[1] == 2)
                answer[0] = 1;
            if (black_caps[n-2] == 2)
                answer[n-1] = 1;
    
            for (int i = 1 ; i < n-1 ; i++) {
                if (black_caps[i] == 1) {
                    if (answer[i-1] == 2)
                        answer[i+1] = 1;
                    else if (answer[i+1] == 2)
                        answer[i-1] = 1;
                    else if (answer[i-1] == 1)
                        answer[i+1] = 2;
                    else if (answer[i+1] == 1)
                        answer[i-1] = 2;
                }
            }
    
            return answer;
        }
    }    
}
