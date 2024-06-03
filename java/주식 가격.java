import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        Stack<Integer[]> stack = new Stack<>();
        
        // [위치, 주식가격]
        for (int i = 0 ; i < prices.length ; i++) {
            
            if (stack.isEmpty()) {
                stack.push(new Integer[] {i, prices[i]});    
            }
            else {
                while(!stack.isEmpty() && stack.peek()[1] > prices[i]) {
                    Integer[] p = stack.pop();
                    answer[p[0]] = i-p[0];
                 }
                stack.push(new Integer[] {i, prices[i]}); 
            }
        }
        
        if (!stack.isEmpty()) {
            int px = stack.peek()[0];
            while (!stack.isEmpty()) {
                Integer[] p = stack.pop();
                answer[p[0]] = px - p[0];
            }
        }
    
        return answer;
    }
}
