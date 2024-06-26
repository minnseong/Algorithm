// Programmers 12/21 2022
// Java 코테 연습 - 점 찍기

package java;

public class PrintPoint {
    class Solution {
        public long solution(int k, int d) {
            long answer = 0;

            for (long i = 0; i <= d/k; i++) {
                long x = i * k;
                long y = (long) Math.sqrt((long) Math.pow(d, 2) - (long) Math.pow(x, 2)) / k;

                answer += y + 1;
            }
            return answer;
        }
    }
}
