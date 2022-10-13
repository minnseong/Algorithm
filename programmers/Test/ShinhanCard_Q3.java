// 신한카드 코딩테스트 10/13 2022
// Q3

package programmers.Test;
import java.util.*;

public class ShinhanCard_Q3 {
    class Solution {
        public ArrayList<Integer> solution(int n, int[][] queries) {
            ArrayList<Integer> answer = new ArrayList<>();
    
            Queue<Integer>[] queues = new LinkedList[n];
    
            for (int i = 0 ; i < queues.length ; i++) {
                queues[i] = new LinkedList<Integer>();
            }
    
            int cur = 0;
            ArrayList<Integer> front = new ArrayList<Integer>();
    
            int emptyCnt = 0;
            for (int[] query : queries) {
                if (query[0] == -1) {
                    for (int i = cur ; i < cur + queues.length ; i++) {
                        if (front.isEmpty() && queues[i%n].isEmpty())
                            emptyCnt += 1;
                        else if (!front.isEmpty() && queues[i%n].isEmpty()) {
                            answer.add(front.remove(0));
                        }   
                        else {
                            int popValue = queues[i%n].poll();
                            if (front.isEmpty()) 
                                front.add(popValue);
                            else {
                                answer.add(front.remove(0));
                                front.add(popValue);
                            }
                            cur = (i+1) % n;
                            emptyCnt = 0;
                            break;
                        }
                    }
                    if (emptyCnt == n)
                        break;
                }
                else {
                    if (front.isEmpty()) {
                        front.add(query[1]);
                    }
                    else {
                        queues[query[0]].add(query[1]);
                    }
                }
            }
            return answer;
        }
    }    
}
