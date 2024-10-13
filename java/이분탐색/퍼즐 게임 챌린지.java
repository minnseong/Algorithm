import java.util.*;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        long answer = (long) 0;
        
        long start = (long) 1;
        long end = (long) 0;
        int count = diffs.length;
        
        for (int diff : diffs) {
            if (end <= diff) {
                end = diff;
            }
        }
        
        while (start <= end) {
            long level = (start + end) / 2;
            long usedTime = (long) 0;
            
            for (int idx = 0 ; idx < count ; idx++) {
                if (level >= diffs[idx]) {
                    usedTime += times[idx];
                } else {
                    long wrongTime = diffs[idx] - level;
                    
                    usedTime += (wrongTime * (times[idx] + times[idx-1]));
                    usedTime += times[idx];
                }
            }
            
            if (usedTime <= limit) {
                end = level - 1;
                answer = level;
            } else {
                start = level + 1;
            }
        }
        
        return (int) answer;
    }
}
