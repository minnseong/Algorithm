// 신한카드 코딩테스트 10/13 2022
// Q2

package programmers.Test;

public class ShinhanCard_Q2 {
    class Solution {
        public int solution(int money, int[] cost) {
            int answer = 0;
    
            int j = 0;
            int paid = cost[j];
    
            if (paid <= money) {
                answer = 1;
            }
            else {
                paid -= cost[j];
                j+= 1;
            }
    
            for (int i = 1 ; i < cost.length ; i++) {
                paid += cost[i];
                if (paid <= money) {
                    answer = Math.max(answer, i-j+1);
                }
                else {
                    paid -= cost[j];
                    j += 1;
                    if (paid <= money) {
                        answer = Math.max(answer, i-j+1);
                    }
                }
            }
    
            return answer;
        }
    }
    
}
