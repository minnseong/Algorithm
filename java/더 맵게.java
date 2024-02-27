import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        
        for (int i : scoville) {
            heap.add((Integer) i);
        }        
        
        while (heap.peek() < K) {
            
            if (heap.size() >= 2) {
                Integer num1 = heap.poll();
                Integer num2 = heap.poll();
                heap.add(num1 + num2 * 2);
                answer += 1;
            }
            else {
                return -1;
            }
        }
        
        return answer;
    }
}
