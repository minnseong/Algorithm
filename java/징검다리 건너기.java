import java.util.*;

class Solution {
    public int solution(int[] stones, int k) {
        
        int answer = 0;
        int start = 0;
        int end = 0;
        
        for (int s : stones)
            if (s > end) end = s;
        
        while (start <= end) {
            int mid = (start + end) / 2; // 3
            
            int cnt = 0;
            boolean flag = true;
            for (int s: stones) {
                if (mid >= s) {
                    cnt += 1;
                }
                else cnt = 0;
                
                if (cnt == k) {
                    flag = false;
                    break;
                }
            }
            
            if (flag) {
                start = mid + 1;
            } else {
                answer = mid;
                end = mid - 1;
            }
        }
        
        return answer;
    }
}
