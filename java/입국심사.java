import java.util.*;

class Solution {

    public long solution(int n, int[] times) {
        long answer = 0;
        
        Arrays.sort(times);
        
        long start = 0;
        long end = times[times.length-1] * (long)n;
        long mid = 0;
        
        while (start <= end) {
            
            mid = (start + end) / 2;
            
            long cnt = 0;
            for (int t : times) {
                cnt += (mid / t);
            }
            
            if (cnt >= n) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        
        return start;
    }
}

// 6
// 7, 10
// s, e, mid
// 1 ~ 60
