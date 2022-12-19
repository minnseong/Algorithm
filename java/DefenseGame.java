// Programmers 12/19 2022
// Java 코테 연습 - 디펜스 게임

package java;

import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        
        PriorityQueue<Integer> pQueue = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int i = 0 ; i < enemy.length ; i++) {
            n = n - enemy[i];
            pQueue.add(enemy[i]);
            
            if (n < 0) {
                if (k > 0) {
                    n += pQueue.poll();
                    k -= 1;
                }
                else {
                    break;
                }
            }
            answer += 1;
        }
        
        return answer;
    }
}